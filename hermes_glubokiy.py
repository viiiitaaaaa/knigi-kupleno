r"""Глубокое чтение блоков 1, 3, 4 через Hermes (gpt-oss:120b, Ollama) — те же куски и то же задание, что в gemini_glubokiy.py.
Пишет в glubokiy\<кусок>.md, готовые пропускает; на лимит 429 выходит (остаток доберёт Gemini или завтрашний запуск).
Запуск: python hermes_glubokiy.py [--par 3] [--limit N] [--slugs regex]
Что делает целиком: отдаёт Hermes каждый ещё не прочитанный кусок книги и сохраняет его конспект по главам."""
import argparse, json, re, sys, time, urllib.error, urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
sys.argv_saved = sys.argv; sys.argv = [sys.argv[0]]          # gemini_glubokiy разбирает свои аргументы сам
import hermes_vse as h
src = (h.W / "gemini_glubokiy.py").read_text("utf-8")
PROMPT = re.search(r'PROMPT = """(.*?)"""', src, re.S).group(1)
SL = re.search(r'SLUGS = re\.compile\((.*?), re\.I\)', src, re.S)
SLUGS = re.compile(eval('(' + SL.group(1) + ')'), re.I)
sys.argv = sys.argv_saved
OUT = h.W / "glubokiy"
ap = argparse.ArgumentParser(); ap.add_argument("--cloud", action="store_true", help="идти напрямую в ollama.com по ключу из .env"); ap.add_argument("--rev", action="store_true", help="с конца списка"); ap.add_argument("--model", help="модель Ollama вместо gpt-oss:120b"); ap.add_argument("--keyvar", default="OLLAMA_API_KEY"); ap.add_argument("--par", type=int, default=3); ap.add_argument("--limit", type=int); ap.add_argument("--slugs"); a = ap.parse_args()
if a.slugs: SLUGS = re.compile(a.slugs, re.I)
LIMIT = False
URL, HDR = "http://127.0.0.1:11434/api/chat", {"Content-Type": "application/json"}
if a.cloud:
    _k = [l.split("=", 1)[1].strip() for l in (h.W / ".env").read_text("utf-8").splitlines() if l.startswith(a.keyvar + "=")][0]
    URL, HDR = "https://ollama.com/api/chat", {"Content-Type": "application/json", "Authorization": "Bearer " + _k}

def run(c, m, slug):
    global LIMIT
    out = OUT / (c.stem + ".md")
    if out.exists() and out.stat().st_size > 500: return c.stem, "уже есть"
    if LIMIT: return c.stem, "пропуск: лимит"
    n = int(c.stem.rsplit("_", 1)[1])
    body = json.dumps({"model": a.model or ("gpt-oss:120b" if a.cloud else "gpt-oss:120b-cloud"), "stream": False, "messages": [{"role": "user", "content": PROMPT.format(
        n=n, m=m, title=h.TITLES.get(slug, slug), text=c.read_text("utf-8"))}]}).encode()
    err = ""
    for att in range(3):
        try:
            req = urllib.request.Request(URL, body, HDR)
            txt = json.loads(urllib.request.urlopen(req, timeout=900).read())["message"]["content"].strip()
            if len(txt) > 500:
                out.write_text(f"<!-- gpt-oss:120b (Hermes), глубокое чтение, {c.name} -->\n{txt}\n", "utf-8"); return c.stem, "ок"
            err = f"короткий ответ {len(txt)}"
        except urllib.error.HTTPError as e:
            if e.code == 429: LIMIT = True; return c.stem, "ЛИМИТ 429"
            err = repr(e)[:200]
        except Exception as e:
            err = repr(e)[:200]
        time.sleep(30 * (att + 1))
    (OUT / (c.stem + ".err")).write_text(err, "utf-8"); return c.stem, "ОШИБКА " + err

jobs = []
for f in h.books():
    if not SLUGS.search(f.stem): continue
    fs = h.split(f); jobs += [(c, len(fs), f.stem) for c in fs if not ((OUT / (c.stem + ".md")).exists() and (OUT / (c.stem + ".md")).stat().st_size > 500)]
if a.rev: jobs.reverse()
if a.limit: jobs = jobs[:a.limit]
print(f"осталось кусков: {len(jobs)}", flush=True)
done = 0
with ThreadPoolExecutor(a.par) as ex:
    for fu in as_completed([ex.submit(run, *j) for j in jobs]):
        done += 1; print(f"{done} из {len(jobs)} | {fu.result()[0]} | {fu.result()[1]}", flush=True)
print("ГОТОВО", flush=True)
