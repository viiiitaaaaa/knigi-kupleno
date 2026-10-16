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
    words = B.split(); sh = set(" ".join(words[i:i+4]) for i in range(len(words)-3))
    blizko, net = [], []
    for q in bad:
        w = norm(q).split(); s = [" ".join(w[i:i+4]) for i in range(len(w)-3)]
        (blizko if s and sum(x in sh for x in s)/len(s) >= 0.5 else net).append(q)
    print(f"{f.name}: цитат {len(qs)}, дословно {len(qs)-len(bad)}, близко к тексту {len(blizko)}, нет в тексте {len(net)}")
    for q in net: print("   НЕТ:", q[:110])
