# Текст книги -> куски по ~6000 слов в chunks_vse\<slug>_NN.txt. python izvlech_knigu.py <файл> <slug>
import sys, re, zipfile, html, pathlib
sys.stdout.reconfigure(encoding="utf-8")
src, slug = sys.argv[1], sys.argv[2]
out = pathlib.Path(r"C:\Users\User\knigi_kupleno\chunks_vse")
low = src.lower()
if low.endswith(".pdf"):
    import fitz
    d = fitz.open(src); text = "\n".join(f"=== стр. {i+1} ===\n" + (p.get_text() or "") for i, p in enumerate(d))
elif low.endswith(".epub"):
    z = zipfile.ZipFile(src); parts = []
    for n in sorted(z.namelist()):
        if n.lower().endswith((".xhtml", ".html", ".htm")):
            t = z.read(n).decode("utf8", "ignore")
            t = re.sub(r"(?is)<(script|style).*?</\1>", "", t); t = re.sub(r"(?i)</(p|div|h\d|li|tr)>|<br\s*/?>", "\n", t)
            parts.append(html.unescape(re.sub(r"<[^>]+>", "", t)))
    text = "\n".join(parts)
else:  # fb2
    t = open(src, encoding="utf8", errors="ignore").read()
    t = re.sub(r"(?is)<binary.*?</binary>", "", t); t = re.sub(r"(?i)</(p|title|section|v)>", "\n", t)
    text = html.unescape(re.sub(r"<[^>]+>", "", t))
text = re.sub(r"\n{3,}", "\n\n", text)
words = text.split(" "); n = 0; cur = []; cnt = 0
for line in text.split("\n"):
    cur.append(line); cnt += len(line.split())
    if cnt >= 6000:
        n += 1; (out / f"{slug}_{n:02d}.txt").write_text("\n".join(cur), "utf-8"); cur = []; cnt = 0
if cur: n += 1; (out / f"{slug}_{n:02d}.txt").write_text("\n".join(cur), "utf-8")
print(slug, "слов", len(text.split()), "кусков", n)
