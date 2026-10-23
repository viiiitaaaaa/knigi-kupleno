"""Building Applications with AI Agents (Albada, 5th Early Release, epub) -> txt с метками частей (23.10.2026)."""
import pathlib, re, html, shutil, warnings
warnings.filterwarnings("ignore")
import ebooklib
from ebooklib import epub

SRC = pathlib.Path(r"G:\Мой диск\куплено\09 ИИ, агенты и Claude\Building Applications with AI Agents (Fifth Early Release) (Michael Albada).epub")
OUT = pathlib.Path(r"C:\Users\User\knigi_kupleno\txt\Building_Applications_with_AI_Agents_Albada (текст).txt")


def strip_html(s):
    s = re.sub(r"(?is)<(script|style).*?</\1>", "", s)
    s = re.sub(r"(?i)<br\s*/?>|</p>|</h\d>|</div>|</li>", "\n", s)
    s = re.sub(r"<[^>]+>", "", s)
    return re.sub(r"\n{3,}", "\n\n", html.unescape(s))


book = epub.read_epub(str(SRC), options={"ignore_ncx": True})
parts = [strip_html(it.get_content().decode("utf-8", "ignore")) for it in book.get_items_of_type(ebooklib.ITEM_DOCUMENT)]
text = "".join(f"\n\n=== часть {i+1} ===\n{t}" for i, t in enumerate(parts))
OUT.write_text(text, encoding="utf-8")
shutil.copy(OUT, pathlib.Path(r"C:\Users\User\Desktop") / OUT.name)
print(len(parts), "частей,", len(text), "знаков ->", OUT)
