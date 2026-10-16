# Сверка английских цитат пересказа с текстом книги. python -I sverka_citat.py <книга_slug>
import re, sys, pathlib
sys.stdout.reconfigure(encoding="utf-8")
K = pathlib.Path(r"C:\Users\User\knigi_kupleno"); slug = sys.argv[1]
norm = lambda s: re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()
B = norm(" ".join(p.read_text("utf-8", "ignore") for p in sorted((K/"chunks_vse").glob(f"{slug}_*.txt"))))
for f in sorted((K/"pereskaz_vse").glob(f"{slug}_*.md")):
    qs = re.findall(r'[*"“]"?([A-Z][^"”\n]{40,}?)["”]', f.read_text("utf-8"))
    bad = []
    for q in qs:
        parts = [p for p in re.split(r"\.\.\.|…|\[.*?\]", q) if len(norm(p)) > 20]
        if not all(norm(p)[:100] in B for p in parts): bad.append(q)
    print(f"{f.name}: цитат {len(qs)}, найдено {len(qs)-len(bad)}")
    for q in bad: print("   НЕТ:", q[:110])
