"""Все книги из «куплено» и распакованных архивов -> txt с метками страниц/глав + сводка."""
import re, sys, json, pathlib, warnings, html
warnings.filterwarnings("ignore")
import pymupdf, ebooklib
from ebooklib import epub

W = pathlib.Path(r"C:\Users\User\knigi_kupleno")
SRC = [pathlib.Path(r"G:\Мой диск\куплено"), W / "arh"]
OUT = W / "txt"; OUT.mkdir(exist_ok=True)

def strip_html(s):
    s = re.sub(r"(?is)<(script|style).*?</\1>", "", s)
    s = re.sub(r"(?i)<br\s*/?>|</p>|</h\d>|</div>|</li>", "\n", s)
    s = re.sub(r"<[^>]+>", "", s)
    return re.sub(r"\n{3,}", "\n\n", html.unescape(s))

def pdf(p):
    d = pymupdf.open(p)
    return "".join(f"\n\n=== стр. {i+1} ===\n" + pg.get_text() for i, pg in enumerate(d)), len(d)

def ep(p):
    b = epub.read_epub(str(p), options={"ignore_ncx": True})
    parts = [strip_html(it.get_content().decode("utf-8", "ignore")) for it in b.get_items_of_type(ebooklib.ITEM_DOCUMENT)]
    return "".join(f"\n\n=== часть {i+1} ===\n{t}" for i, t in enumerate(parts)), len(parts)

def mobi_(p):
    import mobi, shutil
    tmp, f = mobi.extract(str(p))
    s = pathlib.Path(f).read_text("utf-8", "ignore")
    shutil.rmtree(tmp, ignore_errors=True)
    if f.endswith(".epub"):
        return ep(pathlib.Path(f))
    return strip_html(s), 1

res = []
seen = set()
for src in SRC:
    for p in sorted(src.rglob("*")):
        if p.name in seen: continue
        seen.add(p.name)
        ext = p.suffix.lower()
        if ext not in (".pdf", ".epub", ".mobi"):
            continue
        try:
            t, n = {".pdf": pdf, ".epub": ep, ".mobi": mobi_}[ext](p)
        except Exception as e:
            res.append({"file": p.name, "error": repr(e)}); continue
        name = re.sub(r"[^\w\-]+", "_", p.stem)[:60].strip("_") + "_" + ext[1:] + ".txt"
        (OUT / name).write_text(t, "utf-8")
        words = len(t.split())
        head = re.sub(r"\s+", " ", t[:3000])[:700]
        res.append({"file": p.name, "txt": name, "units": n, "words": words, "head": head})
(W / "svodka.json").write_text(json.dumps(res, ensure_ascii=False, indent=1), "utf-8")
for r in res:
    print(json.dumps(r, ensure_ascii=False)[:900], "\n")
