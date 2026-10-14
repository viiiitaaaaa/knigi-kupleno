"""Книги 13.10.2026: режем txt13\\<slug>.txt на куски ~8 тыс. слов и отдаём каждый Hermes (лёгкая часть —
подробный пересказ). Итог: txt13\\pereskaz\\<slug>_NN.md. Готовые куски пропускает (можно перезапускать).
Запуск: python hermes_pereskaz.py [--only slug] [--limit N] [--par 3]"""
import argparse, json, os, pathlib, re, subprocess, sys, time
from concurrent.futures import ThreadPoolExecutor, as_completed

W = pathlib.Path(r"C:\Users\User\knigi_kupleno")
TXT = W / "txt13"
CH = TXT / "chunks"
OUT = TXT / "pereskaz"
HERMES = pathlib.Path(os.environ["LOCALAPPDATA"]) / "hermes" / "bin" / "hermes.exe"
WORDS = 8000
TITLES = {r["slug"]: r["file"] for r in json.loads((W / "svodka_13_10.json").read_text("utf-8")) if "file" in r}

PROMPT = """Прочитай файл {path} ЦЕЛИКОМ, от первой до последней строки (читай частями, ничего не пропуская). Ничего не меняй и не создавай.
Это часть {n} из {m} книги «{title}». Метки «=== стр. N ===» — номера страниц.
Напиши ПО-РУССКИ подробный пересказ этой части в Markdown:
- для каждой главы/раздела, который встретился, — подзаголовок ### с названием (англ. + перевод);
- под ним: главные мысли автора, модели и схемы, правила, цифры и факты, примеры и кейсы (кто → что сделал → результат);
- чек-листы, шаблоны писем/скриптов/промптов, формулы и списки шагов — ПОЛНОСТЬЮ, не сокращая;
- у каждой мысли в скобках страница: (стр. N).
Только то, что написано в книге, без своих советов и оценок. Пропусти оглавление, благодарности, рекламу, указатель.
В ответе — только сам пересказ, без вступлений."""


def split(slug):
    text = (TXT / f"{slug}.txt").read_text("utf-8")
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
        f = CH / f"{slug}_{i:02d}.txt"
        f.write_text(c, "utf-8")
        files.append(f)
    return files


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


def run_direct(f, m):
    """13.10: Hermes читал файл своим инструментом не целиком и выдумывал — даём модели Hermes текст прямо в запросе."""
    import urllib.request
    out = OUT / (f.stem + ".md")
    if out.exists() and out.stat().st_size > 1500:
        return f.stem, "уже есть", 0
    slug, n = f.stem.rsplit("_", 1)
    body = json.dumps({"model": "gpt-oss:120b-cloud", "stream": False, "messages": [{"role": "user", "content": DIRECT.format(
        n=int(n), m=m, title=TITLES.get(slug, slug), text=f.read_text("utf-8"))}]}).encode()
    t, err = time.time(), ""
    for attempt in range(4):
        try:
            req = urllib.request.Request("http://127.0.0.1:11434/api/chat", body, {"Content-Type": "application/json"})
            txt = json.loads(urllib.request.urlopen(req, timeout=900).read())["message"]["content"].strip()
            if len(txt) > 1500:
                out.write_text(f"<!-- gpt-oss:120b (модель Hermes), текст в запросе, {f.name} -->\n" + txt + "\n", "utf-8")
                return f.stem, f"ок {len(txt)} симв.", int(time.time() - t)
            err = f"короткий ответ {len(txt)}"
        except Exception as e:
            err = repr(e)[:300]
        time.sleep(30 * (attempt + 1))
    (OUT / (f.stem + ".err")).write_text(err, "utf-8")
    return f.stem, "ОШИБКА " + err, int(time.time() - t)


def run(f, m):
    out = OUT / (f.stem + ".md")
    if out.exists() and out.stat().st_size > 1500:
        return f.stem, "уже есть", 0
    slug, n = f.stem.rsplit("_", 1)
    prompt = PROMPT.format(path=f, n=int(n), m=m, title=TITLES.get(slug, slug))
    t = time.time()
    for attempt in range(3):
        r = subprocess.run([str(HERMES), "-z", prompt, "--in", str(CH)], capture_output=True, text=True,
                           encoding="utf-8", errors="replace", timeout=1200)
        txt = (r.stdout or "").strip()
        if r.returncode == 0 and len(txt) > 1500:
            out.write_text(f"<!-- Hermes gpt-oss:120b, {f.name} -->\n" + txt + "\n", "utf-8")
            return f.stem, f"ок {len(txt)} симв.", int(time.time() - t)
        time.sleep(20 * (attempt + 1))
    (OUT / (f.stem + ".err")).write_text(f"code {r.returncode}\n{r.stdout[-3000:]}\n{r.stderr[-3000:]}", "utf-8")
    return f.stem, f"ОШИБКА код {r.returncode}", int(time.time() - t)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only"); ap.add_argument("--limit", type=int); ap.add_argument("--par", type=int, default=2)
    ap.add_argument("--agent", action="store_true", help="старый способ: агент Hermes сам читает файл")
    a = ap.parse_args()
    worker = run if a.agent else run_direct
    CH.mkdir(exist_ok=True); OUT.mkdir(exist_ok=True)
    jobs = []
    for slug in TITLES:
        if a.only and slug != a.only:
            continue
        fs = split(slug)
        jobs += [(f, len(fs)) for f in fs]
    if a.limit:
        jobs = jobs[:a.limit]
    print(f"кусков: {len(jobs)}", flush=True)
    done = 0
    with ThreadPoolExecutor(a.par) as ex:
        for fut in as_completed([ex.submit(worker, f, m) for f, m in jobs]):
            done += 1
            name, st, sec = fut.result()
            print(f"{done} из {len(jobs)} | {name} | {st} | {sec} с", flush=True)


if __name__ == "__main__":
    main()
