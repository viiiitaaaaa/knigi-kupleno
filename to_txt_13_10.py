"""Новые книги 13.10.2026 -> txt13\\ с метками страниц, сводка в svodka_13_10.json.
Пропущены: недокачанные *.tmp (Chip Huyen, Sam Newman, Obviously Awesome, Lean Analytics, Bierut-повтор);
«Storytelling in Design (Dahlström)…epub» — повтор уже обработанной 10.10 книги."""
import json, pathlib, re, sys, warnings
warnings.filterwarnings("ignore")
import pymupdf, ebooklib
from ebooklib import epub

W = pathlib.Path(r"C:\Users\User\knigi_kupleno")
SRC = pathlib.Path(r"G:\Мой диск\куплено")
OUT = W / "txt13"
OUT.mkdir(exist_ok=True)
NEW = {  # slug: начало имени файла
    "co_intelligence": "Co-Intelligence", "storytelling_data_makeovers": "Storytelling with Data Before",
    "mom_test": "The Mom Test", "design_how_people_think": "Design for how People Think",
    "agentic_design_patterns": "Agentic Design Patterns", "minto_pyramid": "The Minto Pyramid",
    "rag_python_cookbook": "RAG with Python Cookbook", "mastering_openvpn": "Mastering OpenVPN",
    "loop_engineering_playbook": "The 0", "build_ai_agent": "Build an AI Agent",
    "rag_production": "Hands-On RAG for Production", "pitch_anything": "PITCH ANYTHING",
    "prediction_machines": "Prediction Machines",
}


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
files = [p for p in SRC.iterdir() if p.suffix.lower() in (".pdf", ".epub")]
for slug, start in NEW.items():
    p = next((f for f in files if f.name.startswith(start)), None)
    if not p:
        res.append({"slug": slug, "error": "файл не найден"}); continue
    try:
        t, n = (pdf if p.suffix.lower() == ".pdf" else ep)(p)
    except Exception as e:
        res.append({"slug": slug, "file": p.name, "error": repr(e)}); continue
    (OUT / f"{slug}.txt").write_text(t, "utf-8")
    res.append({"slug": slug, "file": p.name, "units": n, "words": len(t.split()), "lines": t.count("\n")})
(W / "svodka_13_10.json").write_text(json.dumps(res, ensure_ascii=False, indent=1), "utf-8")
for r in res:
    print(r["slug"], r.get("words", "ERR"), r.get("units", ""), r.get("error", ""), sep=" | ")
