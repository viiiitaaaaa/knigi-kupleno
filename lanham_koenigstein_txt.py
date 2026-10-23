"""Lanham (pdf) и Koenigstein (epub) -> txt в папку Freya для NotebookLM (23.10.2026)."""
import pathlib, re, html, warnings
warnings.filterwarnings("ignore")
import pymupdf, ebooklib
from ebooklib import epub

SRC = pathlib.Path(r"G:\Мой диск\куплено")
FREYA = pathlib.Path(r"G:\Мой диск\Для NotebookLM (Freya) - загрузить 17.10")
TXT = pathlib.Path(r"C:\Users\User\knigi_kupleno\txt")

def strip_html(s):
    s = re.sub(r"(?is)<(script|style).*?</\1>", "", s)
    s = re.sub(r"(?i)<br\s*/?>|</p>|</h\d>|</div>|</li>", "\n", s)
    s = re.sub(r"<[^>]+>", "", s)
    return re.sub(r"\n{3,}", "\n\n", html.unescape(s))

# Lanham: метки страниц, чтобы у каждого вывода был адрес
doc = pymupdf.open(SRC / "AI Agents in Action (Micheal Lanham).pdf")
lan = "".join(f"\n\n=== стр. {i+1} ===\n{p.get_text()}" for i, p in enumerate(doc))
print("Lanham стр.", len(doc), "знаков", len(lan))

book = epub.read_epub(str(SRC / "AI Agents the Definitive Guide - Design, Deployment, and Evaluation (Nicole Koenigstein).epub"), options={"ignore_ncx": True})
parts = [strip_html(it.get_content().decode("utf-8", "ignore")) for it in book.get_items_of_type(ebooklib.ITEM_DOCUMENT)]
koe = "".join(f"\n\n=== часть {i+1} ===\n{t}" for i, t in enumerate(parts))
print("Koenigstein частей", len(parts), "знаков", len(koe))

for name, text in [("54 ИИ - AI Agents in Action (Lanham) (текст).txt", lan),
                   ("55 ИИ - AI Agents Definitive Guide (Koenigstein) (текст).txt", koe)]:
    (TXT / name).write_text(text, encoding="utf-8")
    (FREYA / name).write_text(text, encoding="utf-8")
