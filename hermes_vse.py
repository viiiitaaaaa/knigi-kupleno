"""Все купленные книги (14.10.2026): Hermes перечитывает КАЖДУЮ книгу из txt\\ и txt13\\ заново.
Режем текст на куски ~8 тыс. слов, отдаём каждый модели Hermes (gpt-oss:120b через Ollama) прямо в запросе.
Итог: pereskaz_vse\\<slug>_NN.md. Готовые куски пропускает, можно перезапускать после обрыва.
Запуск: python hermes_vse.py [--only slug] [--limit N] [--par 3] [--spisok]"""
import argparse, json, pathlib, re, time, urllib.error, urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed

W = pathlib.Path(r"C:\Users\User\knigi_kupleno")
SRC = [W / "txt", W / "txt13"]
CH = W / "chunks_vse"
OUT = W / "pereskaz_vse"
WORDS = 8000
MIN_BYTES = 20000  # сканы (Consumer Behavior, Экман, Portfolios, Seni): текста нет, пропускаем

TITLES = {
    '17_mobi': 'SEO-книга 2013 (Matthew Davidson)',
    '8-Figure_Ecommerce_Engine_epub': '8-Figure Ecommerce Engine',
    'Advertising_An_Integrated_Marketing_Communication_Perspectiv_pdf': 'Advertising: An Integrated Marketing Communication Perspective 4e (Belch & Belch)',
    'Amazon_FBA_and_E-commerce_With_Shopify_A_Step-by-Step_Beginn_pdf': 'Amazon FBA and E-commerce With Shopify (Mark Miller)',
    'CONSUMER_BEHAVIOR_AND_MARKETING_STRATEGY_EIGHTH_EDITION_J_Pa_pdf': 'Consumer Behavior and Marketing Strategy 8e (Peter & Olson) — СКАН',
    'Claude_Code_Полное_pdf': 'Claude Code: Полное руководство (Мукминов, 2026)',
    'Dropshipping_and_Affiliate_Marketing_A_Beginner_s_Guide_to_G_pdf': 'Dropshipping and Affiliate Marketing (Mark Miller)',
    'E-Commerce_Business__3_Books_in_1__The_Ultimate_Guide_to_Mak_epub': 'E-Commerce Business: 3 Books in 1',
    'ENTREPRENEURIALMARKETING_pdf': 'Entrepreneurial Marketing (Kotler и др., 2023)',
    'Home-Based_Business_University__The_Most_Profitable_Money-Ma_epub': 'Home-Based Business University',
    'How_To_Successfully_Market_High-Priced_Products_epub': 'How To Successfully Market High-Priced Products',
    'How_to_Use_Graphic_Design_to_Sell_Things_Explain_Things_Make_epub': 'How to Use Graphic Design to Sell Things… (Michael Bierut)',
    'International_Business_Competing_in_the_Global_Marketplace_1_pdf': 'International Business 14e (Charles W. L. Hill)',
    'Marketing_4_0__Do_tradicional_ao_digital_pdf': 'Marketing 4.0 (Kotler, португ.)',
    'Marketing_6.0_epub': 'Marketing 6.0 (Kotler)',
    'Marketing_7.0_epub': 'Marketing 7.0 (Kotler)',
    'Marketing_Eighth_Edition_Dhruv_Grewal_Levy_Grewal_pdf': 'Marketing 8e (Grewal & Levy)',
    'Marketing_Management_EBook_Global_Edition_pdf': 'Marketing Management 16e (Kotler, Keller, Chernev)',
    'Marketing_Strategy_in_the_Digital_Age___Applying_Kotler_s_St_pdf': 'Marketing Strategy in the Digital Age (Cao, M. Kotler)',
    'Marketing_epub': 'Marketing (Brian Tracy)',
    'Marketing_pdf': 'Marketing 3e (Grewal, Levy…)',
    'Mastering_Claude_AI_pdf': 'Mastering Claude AI (Dickey, 2025)',
    'More_Demos_Trials_amp_Buyers__SaaS_Marketing_Playbook_2021_epub': 'More Demos, Trials & Buyers: SaaS Marketing Playbook 2021',
    'PORTFOLIOS_pdf': 'Design Matters // Portfolios 01 — КАРТИНКИ',
    'Persuasion__The_Psychology_Of_Selling_-_Proven_Techniques__S_epub': 'Persuasion: The Psychology of Selling',
    'SEO_2025__Learn_search_engine_optimization_with_smart_intern_epub': 'SEO 2025 (Adam Clarke)',
    'Seni_Penulisan_Efektif_untuk_Digital_Marketing_pdf': 'Seni Penulisan Efektif untuk Digital Marketing (индонез.) — КАРТИНКИ',
    'Sewing_to_Sell_The_Beginners_Guide_to_Starting_a_Craft_Busin_pdf': 'Sewing to Sell (Virginia Lindsay)',
    'Social_Media_Marketing_Strategies_of_Facebook_Marketing_Inst_epub': 'Social Media Marketing (Facebook, Instagram, LinkedIn, YouTube)',
    'Storytelling_in_Design_epub': 'Storytelling in Design (Anna Dahlström)',
    'The_Naming_Book_epub': 'The Naming Book',
    'The_Ultimate_LinkedIn_Sales_Guide_How_to_Use_Digital_and_Soc_epub': 'The Ultimate LinkedIn Sales Guide (Daniel Disney)',
    'http___avxhome_se_blogs_ALGEROIS_pdf': 'Французский учебник маркетинга (Vuibert)',
    'Эту_книгу_я_посвящаю_моим_горячо_любимым_внукам__1_pdf': 'Котлер «Десять смертных грехов маркетинга» (рус.)',
    '说谎_揭穿商业_政治与婚姻中的骗局_Telling_Lies_Clues_to_Deceit_in_the_Market_pdf': 'Telling Lies (Paul Ekman, кит.) — СКАН',
    'a_mind_for_numbers': 'A Mind for Numbers (Barbara Oakley)',
    'agentic_design_patterns': 'Agentic Design Patterns (Antonio Gulli)',
    'ai_engineering': 'AI Engineering (Chip Huyen)',
    'ask_for_it': 'Ask For It (Linda Babcock)',
    'build_ai_agent': 'Build an AI Agent From Scratch (Hur, Song)',
    'challenger_sale': 'The Challenger Sale (Dixon, Adamson)',
    'changing_belief_systems': 'Changing Belief Systems With NLP (Robert Dilts)',
    'co_intelligence': 'Co-Intelligence (Ethan Mollick)',
    'design_how_people_think': 'Design for How People Think (John Whalen)',
    'fluent_forever': 'Fluent Forever (Gabriel Wyner)',
    'introducing_nlp': "Introducing NLP (Joseph O'Connor)",
    'lean_analytics': 'Lean Analytics (Croll, Yoskovitz)',
    'loop_engineering_playbook': 'The 0→1 Loop Engineering Playbook (2026)',
    'make_it_stick': 'Make It Stick (Brown, Roediger)',
    'mastering_openvpn': 'Mastering OpenVPN (Crist, Keijser)',
    'million_dollar_consulting': 'Million Dollar Consulting (Alan Weiss)',
    'minto_pyramid': 'The Minto Pyramid Principle (Barbara Minto)',
    'mom_test': 'The Mom Test (Rob Fitzpatrick)',
    'moonwalking_einstein': 'Moonwalking with Einstein (Joshua Foer)',
    'never_split_difference': 'Never Split the Difference (Chris Voss)',
    'obviously_awesome': 'Obviously Awesome (April Dunford)',
    'openvpn_cookbook': 'OpenVPN Cookbook 2e (Keijser)',
    'peak_ericsson': 'Peak (Anders Ericsson)',
    'pitch_anything': 'Pitch Anything (Oren Klaff)',
    'playing_big': 'Playing Big (Tara Mohr)',
    'prediction_machines': 'Prediction Machines (Agrawal, Gans, Goldfarb)',
    'prodazhi_b2b_kolotilov': 'Продажи B2B: 101+ кейс (Евгений Колотилов)',
    'rag_production': 'Hands-On RAG for Production (Mendelevitch и др.)',
    'rag_python_cookbook': 'RAG with Python Cookbook (Dominik Polzer)',
    'resilient_distributed': 'Building Resilient Distributed Systems (Sam Newman)',
    'second_brain': 'Building a Second Brain (Tiago Forte)',
    'show_your_work': 'Show Your Work (Austin Kleon)',
    'sleight_of_mouth': 'Sleight of Mouth (Robert Dilts)',
    'spin_fieldbook': 'The SPIN Selling Fieldbook (Neil Rackham)',
    'storytelling_data_makeovers': 'Storytelling with Data: Before and After (Knaflic)',
    'take_charge_bandler': 'How to Take Charge of Your Life: NLP (Richard Bandler)',
    'ultralearning': 'Ultralearning (Scott Young)',
    'using_your_brain': 'Using Your Brain — For a Change (Richard Bandler)',
}

DIRECT = """Ниже — часть {n} из {m} книги «{title}», между строками <<<ТЕКСТ и ТЕКСТ>>>. Метки «=== стр. N ===» — номера страниц.
Напиши ПО-РУССКИ подробный пересказ этой части в Markdown:
- для каждой главы/раздела, который встретился, — подзаголовок ### с названием (англ. + перевод);
- под ним: главные мысли автора, модели и схемы, правила, цифры и факты, примеры и кейсы (кто → что сделал → результат);
- чек-листы, шаблоны писем/скриптов/промптов, формулы и списки шагов — ПОЛНОСТЬЮ, дословно (англ.) + перевод;
- у каждой мысли в скобках страница по ближайшей метке выше: (стр. N).
СТРОГО только то, что написано в тексте. Ничего не добавляй от себя, не придумывай правил, шаблонов и цифр, которых нет в тексте.
Пропусти оглавление, благодарности, рекламу, указатель, списки источников. В ответе — только пересказ, без вступлений.

<<<ТЕКСТ
{text}
ТЕКСТ>>>"""


def books():
    for d in SRC:
        for f in sorted(d.glob("*.txt")):
            if f.stat().st_size >= MIN_BYTES:
                yield f


def split(f):
    slug = f.stem
    text = f.read_text("utf-8", errors="replace")
    pages = re.split(r"(?=\n\n=== (?:стр|часть)\. ?\d+ ===)", text)
    chunks, cur, n = [], [], 0
    for p in pages:
        w = len(p.split())
        if cur and n + w > WORDS:
            chunks.append("".join(cur)); cur, n = [], 0
        if w > WORDS * 1.5:  # огромная «часть» epub — режем по словам
            ws = p.split(" ")
            for i in range(0, len(ws), WORDS):
                chunks.append(" ".join(ws[i:i + WORDS]))
            continue
        cur.append(p); n += w
    if cur:
        chunks.append("".join(cur))
    chunks = [c for c in chunks if len(c.split()) > 150]
    files = []
    for i, c in enumerate(chunks, 1):
        cf = CH / f"{slug}_{i:02d}.txt"
        if not cf.exists():
            cf.write_text(c, "utf-8")
        files.append(cf)
    return files


LIMIT = False  # лимит Ollama кончился (429) — остальные куски не трогаем, планировщик запустит позже


def probe():
    """Пробный запрос: False, если Ollama отвечает 429 (лимит)."""
    body = json.dumps({"model": "gpt-oss:120b-cloud", "stream": False,
                       "messages": [{"role": "user", "content": "ok"}]}).encode()
    try:
        urllib.request.urlopen(urllib.request.Request("http://127.0.0.1:11434/api/chat", body,
                                                      {"Content-Type": "application/json"}), timeout=300).read()
    except urllib.error.HTTPError as e:
        return e.code != 429
    return True


def run(f, m):
    global LIMIT
    out = OUT / (f.stem + ".md")
    if out.exists() and out.stat().st_size > 1500:
        return f.stem, "уже есть", 0
    if LIMIT:
        return f.stem, "пропуск: лимит", 0
    slug, n = f.stem.rsplit("_", 1)
    body = json.dumps({"model": "gpt-oss:120b-cloud", "stream": False, "messages": [{"role": "user", "content": DIRECT.format(
        n=int(n), m=m, title=TITLES.get(slug, slug), text=f.read_text("utf-8"))}]}).encode()
    t, err = time.time(), ""
    for attempt in range(4):
        try:
            req = urllib.request.Request("http://127.0.0.1:11434/api/chat", body, {"Content-Type": "application/json"})
            txt = json.loads(urllib.request.urlopen(req, timeout=900).read())["message"]["content"].strip()
            if len(txt) > 1500:
                out.write_text(f"<!-- gpt-oss:120b (модель Hermes), {f.name} -->\n" + txt + "\n", "utf-8")
                return f.stem, f"ок {len(txt)} симв.", int(time.time() - t)
            err = f"короткий ответ {len(txt)}"
        except urllib.error.HTTPError as e:
            if e.code == 429:
                LIMIT = True
                return f.stem, "ЛИМИТ 429, попробуем позже", int(time.time() - t)
            err = repr(e)[:300]
        except Exception as e:
            err = repr(e)[:300]
        time.sleep(30 * (attempt + 1))
    (OUT / (f.stem + ".err")).write_text(err, "utf-8")
    return f.stem, "ОШИБКА " + err, int(time.time() - t)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only"); ap.add_argument("--limit", type=int); ap.add_argument("--par", type=int, default=3)
    ap.add_argument("--spisok", action="store_true", help="только показать книги и число кусков")
    a = ap.parse_args()
    CH.mkdir(exist_ok=True); OUT.mkdir(exist_ok=True)
    jobs = []
    for f in books():
        if a.only and f.stem != a.only:
            continue
        fs = split(f)
        if a.spisok:
            print(f"{len(fs):3} кусков | {TITLES.get(f.stem, f.stem)}")
        jobs += [(c, len(fs)) for c in fs]
    # книги из pervymi.txt — в начало очереди, в их порядке (15.10.2026, ТОП-10 от Perplexity)
    pf = pathlib.Path(__file__).with_name("pervymi.txt")
    if pf.exists():
        pr = [l.strip() for l in pf.read_text("utf-8").splitlines() if l.strip() and not l.startswith("#")]
        jobs.sort(key=lambda j: pr.index(j[0].stem.rsplit("_", 1)[0]) if j[0].stem.rsplit("_", 1)[0] in pr else len(pr))
    if a.limit:
        jobs = jobs[:a.limit]
    print(f"кусков всего: {len(jobs)}", flush=True)
    if a.spisok:
        return
    if not probe():
        print(time.strftime("%d.%m %H:%M") + " | лимит Ollama (429) — выхожу, следующая попытка по планировщику", flush=True)
        return
    done = 0
    with ThreadPoolExecutor(a.par) as ex:
        for fut in as_completed([ex.submit(run, c, m) for c, m in jobs]):
            done += 1
            name, st, sec = fut.result()
            if st != "пропуск: лимит":
                print(f"{done} из {len(jobs)} | {name} | {st} | {sec} с", flush=True)
    if LIMIT:
        print(time.strftime("%d.%m %H:%M") + " | лимит Ollama (429) — остановилась, следующая попытка по планировщику", flush=True)
        return
    bad = sorted(p.stem for p in OUT.glob("*.err") if not (OUT / (p.stem + ".md")).exists())
    print("ГОТОВО." + (f" С ошибкой (запусти скрипт ещё раз): {', '.join(bad)}" if bad else " Все куски пересказаны."))


if __name__ == "__main__":
    main()
