# Сверка английских цитат конспекта NotebookLM с текстом книги: python -I sverka_citat_uchoba.py <конспект.md> <книга.txt>
import re, sys, pathlib
sys.stdout.reconfigure(encoding="utf-8")
norm = lambda s: re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()
B = norm(pathlib.Path(sys.argv[2]).read_text("utf-8", "ignore"))
words = B.split(); sh = set(" ".join(words[i:i+4]) for i in range(len(words)-3))
txt = pathlib.Path(sys.argv[1]).read_text("utf-8")
qs = re.findall(r'["“«]([A-Za-z][^"”»\n]{30,}?)["”»]', txt)
exact, close, net = 0, 0, []
for q in qs:
    parts = [p for p in re.split(r"\.\.\.|…|\[.*?\]", q) if len(norm(p)) > 15]
    if not parts: continue
    if all(norm(p) in B for p in parts): exact += 1; continue
    w = norm(q).split(); s = [" ".join(w[i:i+4]) for i in range(len(w)-3)]
    if s and sum(x in sh for x in s)/len(s) >= 0.5: close += 1
    else: net.append(q)
print(f"цитат {exact+close+len(net)}: дословно {exact}, близко {close}, нет в тексте {len(net)}")
for q in net: print("  НЕТ:", q[:120])
