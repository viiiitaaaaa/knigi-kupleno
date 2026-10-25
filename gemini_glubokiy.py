r"""Глубокое чтение книг блоков 1, 3, 4 (25.10.2026, её «только техника»): по каждому куску — конспект по главам «как делать».
Пишет в glubokiy\<кусок>.md, готовые пропускает, при дневном лимите останавливается (остаток — завтра тем же запуском).
Запуск: python gemini_glubokiy.py [--limit N] [--model M] [--slugs regex]
Что делает целиком: берёт каждый кусок книги, просит Gemini разложить главы на идеи, шаги, шаблоны, ошибки и числа со страницами, и сохраняет."""
import argparse, re, time
import gemini_vse as g
import hermes_vse as h

OUT = h.W / "glubokiy"; OUT.mkdir(exist_ok=True)
SLUGS = re.compile(r"ai_engineering|agentic_design|build_ai_agent|Albada|Lanham|\b54 |Koenigstein|^55|rag_production|rag_python|loop_engineering|"
                   r"co_intelligence|prediction_machines|lean_analytics|minto|storytelling_data|make_it_stick|ultralearning|peak|a_mind|second_brain|moonwalking", re.I)
PROMPT = """Ниже — часть {n} из {m} книги «{title}», между <<<ТЕКСТ и ТЕКСТ>>>. Метки «=== стр. N ===» — номера страниц.
Ты глубокий читатель. Сделай ПО-РУССКИ подробный конспект ПО ГЛАВАМ этой части для ИИ-помощника Claude, который работает с одним человеком (предприниматель-одиночка, данные, свои скрипты, агенты, учёба). Простыми словами, термины расшифровывай.
Для каждой главы или раздела (с номерами страниц):
## Название (стр. A–B)
- Главная мысль — 1–2 предложения.
- Как делать — пронумерованные шаги, если в тексте есть процесс.
- Правила и числа — только те, что есть в тексте (с (стр. N)).
- Шаблоны и примеры — короткие, из текста.
- Ошибки и предупреждения.
- Где нам пригодится — одной строкой (для запросов, проверки, памяти, помощников, данных или учёбы).
Не пропускай главы. Если в части нет содержательного текста (оглавление, указатель, литература) — напиши «содержания нет». СТРОГО из текста, ничего не придумывай; чего нет в тексте — не пиши.

<<<ТЕКСТ
{text}
ТЕКСТ>>>"""
ap = argparse.ArgumentParser(); ap.add_argument("--limit", type=int); ap.add_argument("--slugs"); ap.add_argument("--model", default="gemini-flash-lite-latest"); a = ap.parse_args()
if a.slugs: SLUGS = re.compile(a.slugs, re.I)
jobs = []
for f in h.books():
    if not SLUGS.search(f.stem): continue
    fs = h.split(f)
    jobs += [(c, len(fs), f.stem) for c in fs if not ((OUT / (c.stem + ".md")).exists() and (OUT / (c.stem + ".md")).stat().st_size > 500)]
if a.limit: jobs = jobs[:a.limit]
print(f"осталось кусков: {len(jobs)}", flush=True)
k = g.key(); bad = 0
for i, (c, m, slug) in enumerate(jobs, 1):
    n = int(c.stem.rsplit("_", 1)[1]); t = time.time(); st = None
    prompt = PROMPT.format(n=n, m=m, title=h.TITLES.get(slug, slug), text=c.read_text("utf-8"))
    for att in range(3):
        try:
            txt, ver = g.ask(a.model, k, prompt)
            if len(txt) > 300:
                (OUT / (c.stem + ".md")).write_text(f"<!-- {ver}, глубокое чтение, {c.name} -->\n{txt}\n", "utf-8"); st = "ок"; break
            st = f"короткий ответ {len(txt)}"
        except g.urllib.error.HTTPError as e:
            body = e.read().decode("utf-8", "replace")
            if e.code == 429 and "PerDay" in body:
                print(f"ДНЕВНОЙ ЛИМИТ — остановилась на {i} из {len(jobs)}, не собрано {len(jobs)-i+1}", flush=True); raise SystemExit
            st = f"HTTP {e.code}"
            if e.code not in (429, 500, 503): break
        except Exception as e:
            st = repr(e)[:120]
        time.sleep(30 * (att + 1))
    if st != "ок":
        bad += 1; (OUT / (c.stem + ".err")).write_text(str(st), "utf-8")
    print(f"{i} из {len(jobs)} | {c.stem} | {st} | {int(time.time()-t)} с", flush=True)
print(f"ГОТОВО. не собрано: {bad} из {len(jobs)}", flush=True)
