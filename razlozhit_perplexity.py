# Раскладывает сырой ответ Perplexity (30 ситуаций MESSAGE/CORRECT ANSWER/NOT COVERED/TYPICAL WRONG ANSWER)
# на: perplexity_knigi/NN_книга.md, retest_23_10_<код>/vhod/<книга>_A|B|C.md и sud/klyuch_<книга>.md
# Запуск: python razlozhit_perplexity.py <сырой.txt> <NN_книга> <код_папки> <имя_в_файлах> <URL чата> <книга>
import re, os, sys
raw, nn, code, name, url, book = sys.argv[1:7]
base = os.path.dirname(os.path.abspath(__file__))
t = open(raw, encoding="utf-8").read()
pos = [m.start() for m in re.finditer("MESSAGE:", t)]
assert len(pos) == 30, len(pos)
junk = re.compile(r"^(\+\d+|[a-z0-9\.\-]+\.[a-z]{2,}[a-z0-9\.\-/]*|[a-z]{1,12})$", re.I)
cases = []
for k, p in enumerate(pos):
    pre = t[(pos[k - 1] if k else 0):p]
    lines = [l.strip() for l in pre.split("\n") if l.strip()]
    title = lines[-1] if lines else ""
    end = pos[k + 1] if k + 1 < len(pos) else len(t)
    sl = t[p:end].split("\n")
    if k + 1 < len(pos):
        idx = max(i for i, l in enumerate(sl) if l.strip()); sl = sl[:idx]
    seg = "\n".join(l for l in sl if not (junk.match(l.strip()) and l.strip())).strip()
    seg = re.sub(r"\s*(CORRECT ANSWER|NOT COVERED:|TYPICAL WRONG ANSWER:)", r"\n\n\1", seg)
    cases.append((title, seg))
hdr = f"Источник: Perplexity, глубокое исследование, 23.10.2026, чат {url} ; книга {book}. Запрос — шаблон _prompt.md. Ключ НЕ сверен с текстом книги.\nПоля: MESSAGE / CORRECT ANSWER / NOT COVERED / TYPICAL WRONG ANSWER.\n\n"
body = "\n\n".join(f"{i}. {ti}\n\n{sg}" for i, (ti, sg) in enumerate(cases, 1)) + "\n"
open(os.path.join(base, "perplexity_knigi", nn + ".md"), "w", encoding="utf-8").write(hdr + body)
msgs = {}
for i, (ti, sg) in enumerate(cases, 1):
    m = re.search(r"MESSAGE:\s*(.+?)\s*CORRECT ANSWER", sg, re.S); msgs[i] = m.group(1).strip()
d = os.path.join(base, "retest_23_10_" + code)
for s in ("vhod", "sud", "otvety"): os.makedirs(os.path.join(d, s), exist_ok=True)
for g, (a, b) in zip("ABC", [(1, 10), (11, 20), (21, 30)]):
    open(os.path.join(d, "vhod", f"{name}_{g}.md"), "w", encoding="utf-8").write("\n\n".join(f"## S-{i}\n{msgs[i]}" for i in range(a, b + 1)) + "\n")
open(os.path.join(d, "sud", f"klyuch_{name}.md"), "w", encoding="utf-8").write("# Ключ (Perplexity), НЕ сверен\n\n" + "\n\n".join(f"## S-{i}\n{i}. {ti}\n\n{sg}" for i, (ti, sg) in enumerate(cases, 1)) + "\n")
print("ok", len(cases), [all(k in sg for k in ("CORRECT ANSWER", "NOT COVERED", "TYPICAL WRONG")) for _, sg in cases].count(True))
