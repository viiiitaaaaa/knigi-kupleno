r"""Gemini как ВТОРОЙ читатель технических книг (25.10.2026). Берёт те же куски (chunks_vse), просит ПРИЁМЫ для работы
Claude-агента, пишет в pereskaz_gemini2\<кусок>.md (старые пересказы не трогает). Готовые пропускает.
Запуск: python gemini_vtoroy.py [--limit N]"""
import argparse, re, time
import gemini_vse as g
import hermes_vse as h

OUT2 = h.W / "pereskaz_gemini2"
SLUGS = re.compile(r"Claude_Code|Mastering_Claude|agentic_design|ai_engineering|build_ai_agent|loop_engineering|rag_production|"
                   r"rag_python|resilient|prediction_machines|co_intelligence|Albada|Lanham|Koenigstein|Newman|mastering_openvpn|openvpn_cookbook", re.I)
PROMPT = """Ниже — часть {n} из {m} книги «{title}», между <<<ТЕКСТ и ТЕКСТ>>>. Метки «=== стр. N ===» — номера страниц.
Ты второй читатель. Выпиши ПО-РУССКИ только ПРИЁМЫ, которые помогут ИИ-агенту (Claude Code) лучше работать для одного человека (предпринимателя-одиночки, продаёт товары и услуги, учится сама, работает с данными):
{focus}
Для каждого приёма: ### короткое название · что делать (1–2 предложения) · пример из текста · (стр. N).
Выпиши ВСЕ приёмы, правила, советы, шаблоны промптов и предупреждения об ошибках, которые есть в тексте (обычно 3–15 на часть). «Приёмов нет» пиши только если часть — одно оглавление, указатель или список литературы. СТРОГО только из текста, ничего не придумывай. Без вступлений.

<<<ТЕКСТ
{text}
ТЕКСТ>>>"""

FOCUS = {'ai': 'планирование, проверка результата, память, контекст, помощники, ошибки, безопасность, экономия лимита.', 'x': 'как учить и проверять знания, как анализировать данные и доносить выводы, как вести переговоры и продавать.'}
ap = argparse.ArgumentParser(); ap.add_argument("--limit", type=int); ap.add_argument("--slugs"); a = ap.parse_args()
if a.slugs: SLUGS = re.compile(a.slugs, re.I)
jobs = []
for f in h.books():
    if not SLUGS.search(f.stem):
        continue
    fs = h.split(f)
    jobs += [(c, len(fs), f.stem) for c in fs if not ((OUT2 / (c.stem + ".md")).exists() and (OUT2 / (c.stem + ".md")).stat().st_size > 300)]
if a.limit:
    jobs = jobs[:a.limit]
print(f"осталось кусков: {len(jobs)}", flush=True)
k = g.key(); bad = 0
for i, (c, m, slug) in enumerate(jobs, 1):
    n = int(c.stem.rsplit("_", 1)[1]); t = time.time()
    prompt = PROMPT.format(n=n, m=m, title=h.TITLES.get(slug, slug), text=c.read_text("utf-8"), focus=FOCUS['x' if a.slugs else 'ai'])
    st = None
    for att in range(3):
        try:
            txt, ver = g.ask("gemini-flash-lite-latest", k, prompt)
            if txt.strip():
                (OUT2 / (c.stem + ".md")).write_text(f"<!-- {ver} (Gemini, 2-й читатель), {c.name} -->\n{txt}\n", "utf-8"); st = "ок"; break
        except g.urllib.error.HTTPError as e:
            body = e.read().decode("utf-8", "replace")
            if e.code == 429 and "PerDay" in body:
                print(f"дневной лимит — остановилась на {i} из {len(jobs)}, не собрано {len(jobs)-i+1}", flush=True); raise SystemExit
            st = f"HTTP {e.code}"
            if e.code not in (429, 500, 503): break
        except Exception as e:
            st = repr(e)[:120]
        time.sleep(30 * (att + 1))
    if st != "ок":
        bad += 1; (OUT2 / (c.stem + ".err")).write_text(str(st), "utf-8")
    print(f"{i} из {len(jobs)} | {c.stem} | {st} | {int(time.time()-t)} с", flush=True)
print(f"ГОТОВО. не собрано: {bad} из {len(jobs)}", flush=True)
