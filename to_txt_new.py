"""Только новые книги (10.10.2026) -> txt\\ с метками страниц, сводка в svodka_new.json.
Пропущены по решению 10.10: оружие (Home Workshop Prototype Firearms), Operation Market Garden, Art Market Gold List;
Principles of Marketing 18e — битый (0 МБ)."""
import json, pathlib, re, sys, warnings
warnings.filterwarnings("ignore")
sys.argv = [sys.argv[0]]
import pymupdf, ebooklib
from ebooklib import epub

W = pathlib.Path(r"C:\Users\User\knigi_kupleno")
SRC = pathlib.Path(r"G:\Мой диск\куплено")
OUT = W / "txt"
SKIP = ("Firearms", "Market Garden", "Art Market", "Principles of Marketing", "clean_pdfs_log")
OLD = {"Marketing.epub", "Marketing 6.0.epub", "Marketing 7.0.epub", "Mastering Claude AI.pdf", "17.mobi",
       "Marketing 4.0_ Do tradicional ao digital.pdf", "http___avxhome.se_blogs_ALGEROIS.pdf", "ENTREPRENEURIALMARKETING.pdf",
       "Claude Code Полное.pdf"}


def strip_html(s):
    import html
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


res = []
for p in sorted(SRC.iterdir()):
    if p.suffix.lower() not in (".pdf", ".epub") or any(s in p.name for s in SKIP) or p.name in OLD \
            or p.name.startswith(("SEO 2025", "Social Media Marketing", "More Demos", "Эту книгу")):
        continue
    try:
        t, n = (pdf if p.suffix.lower() == ".pdf" else ep)(p)
    except Exception as e:
        res.append({"file": p.name, "error": repr(e)}); continue
    name = re.sub(r"[^\w\-]+", "_", p.stem)[:60].strip("_") + "_" + p.suffix[1:].lower() + ".txt"
    (OUT / name).write_text(t, "utf-8")
    res.append({"file": p.name, "txt": name, "units": n, "words": len(t.split()), "lines": t.count("\n")})
(W / "svodka_new.json").write_text(json.dumps(res, ensure_ascii=False, indent=1), "utf-8")
for r in res:
    print(r.get("words", "ERR"), r.get("lines", ""), r.get("units", ""), r.get("txt", r.get("error")), sep=" | ")
