# Сверка русских цитат и чисел пересказа с текстом книги. python -I sverka_ru.py <slug>
import re, sys, pathlib
sys.stdout.reconfigure(encoding="utf-8")
K = pathlib.Path(r"C:\Users\User\knigi_kupleno"); slug = sys.argv[1]
norm = lambda s: re.sub(r"[^a-zа-я0-9]+", " ", s.lower().replace("ё", "е")).strip()
B = norm(" ".join(p.read_text("utf-8", "ignore") for p in sorted((K/"chunks_vse").glob(f"{slug}_*.txt"))))
tot = ok = near = 0; bad = []
for f in sorted((K/"pereskaz_vse").glob(f"{slug}_[0-9]*.md")):
    t = f.read_text("utf-8")
    for q in re.findall(r'[«"“]([^»"”\n]{40,400})[»"”]', t):
        parts = [p for p in re.split(r"\.\.\.|…|\[.*?\]", q) if len(norm(p)) > 25]
        if not parts: continue
        tot += 1
        if all(norm(p) in B for p in parts): ok += 1
        elif all(norm(p)[:50] in B for p in parts): near += 1
        else: bad.append((f.name, q[:160]))
print(f"цитат {tot}: дословно {ok}, близко (начало совпало) {near}, нет в тексте {len(bad)}")
for b in bad: print(" ⚠", *b)
