"""Книги через Gemini (15.10.2026), пока у Ollama кончился бесплатный лимит.
Те же куски и то же задание, что в hermes_vse.py; итог в ту же папку pereskaz_vse\\<slug>_NN.md, готовые пропускает.
Ключ — в .env (GEMINI_API_KEY=...), файл в git не попадает.
Бесплатный тариф: по одному запросу, на 503 (перегрузка) и 429 (лимит в минуту) ждёт и повторяет;
если лимит за день — выходит, завтра запустить ещё раз.
Запуск: python gemini_vse.py [--only slug] [--limit N] [--model gemini-flash-lite-latest]"""
import argparse, json, time, urllib.error, urllib.request
from hermes_vse import CH, DIRECT, OUT, TITLES, W, books, split

URL = "https://generativelanguage.googleapis.com/v1beta/models/{}:generateContent"


def key():
    for line in (W / ".env").read_text("utf-8").splitlines():
        if line.startswith("GEMINI_API_KEY="):
            return line.split("=", 1)[1].strip()
    raise SystemExit("нет GEMINI_API_KEY в .env")


def ask(model, k, prompt):
    body = json.dumps({"contents": [{"parts": [{"text": prompt}]}]}).encode()
    req = urllib.request.Request(URL.format(model), body, {"Content-Type": "application/json", "X-goog-api-key": k})
    r = json.loads(urllib.request.urlopen(req, timeout=600).read())
    return "".join(p.get("text", "") for p in r["candidates"][0]["content"]["parts"]).strip(), r.get("modelVersion", model)


def run(f, m, model, k):
    """Возвращает (статус, секунды); статус 'ДЕНЬ' — дневной лимит кончился."""
    slug, n = f.stem.rsplit("_", 1)
    prompt = DIRECT.format(n=int(n), m=m, title=TITLES.get(slug, slug), text=f.read_text("utf-8"))
    t, err = time.time(), ""
    for attempt in range(6):
        try:
            txt, ver = ask(model, k, prompt)
            if len(txt) > 1500:
                (OUT / (f.stem + ".md")).write_text(f"<!-- {ver} (Gemini), {f.name} -->\n" + txt + "\n", "utf-8")
                return f"ок {len(txt)} симв.", int(time.time() - t)
            err = f"короткий ответ {len(txt)}"
        except urllib.error.HTTPError as e:
            msg = e.read().decode("utf-8", "replace")
            if e.code == 429 and "PerDay" in msg:
                return "ДЕНЬ", int(time.time() - t)
            err = f"HTTP {e.code}: {msg[:200]}"
            if e.code not in (429, 500, 503):
                break
        except Exception as e:
            err = repr(e)[:300]
        time.sleep(30 * (attempt + 1))
    (OUT / (f.stem + ".err")).write_text(err, "utf-8")
    return "ОШИБКА " + err, int(time.time() - t)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only"); ap.add_argument("--limit", type=int)
    ap.add_argument("--model", default="gemini-flash-lite-latest")
    a = ap.parse_args()
    CH.mkdir(exist_ok=True); OUT.mkdir(exist_ok=True)
    jobs = []
    for f in books():
        if a.only and f.stem != a.only:
            continue
        fs = split(f)
        jobs += [(c, len(fs)) for c in fs
                 if not ((OUT / (c.stem + ".md")).exists() and (OUT / (c.stem + ".md")).stat().st_size > 1500)]
    if a.limit:
        jobs = jobs[:a.limit]
    print(f"осталось кусков: {len(jobs)}", flush=True)
    k = key()
    for i, (c, m) in enumerate(jobs, 1):
        st, sec = run(c, m, a.model, k)
        if st == "ДЕНЬ":
            print(time.strftime("%d.%m %H:%M") + f" | дневной лимит Gemini — остановилась на {i} из {len(jobs)}, запусти завтра", flush=True)
            return
        print(f"{i} из {len(jobs)} | {c.stem} | {st} | {sec} с", flush=True)
    print("ГОТОВО.")


if __name__ == "__main__":
    main()
