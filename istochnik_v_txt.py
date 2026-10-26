"""Ссылка или файл -> один txt для загрузки в NotebookLM (26.10.2026; наш вариант вместо чужого qiaomu-anything-to-notebooklm).
Что делает целиком: берёт открытую страницу сайта (http/https) или файл pdf/epub/docx/html/md/txt, достаёт текст,
ставит метки «=== стр. N ===» / «=== часть N ===» и кладёт txt в папку notebooklm_txt. Никуда не входит, ключей не просит,
paywall не обходит (закрытая страница = честное «не открылась»), в NotebookLM сам не грузит — это делает помощник.
Запуск: python istochnik_v_txt.py <ссылка_или_путь> [папка_вывода]"""
import html
import pathlib
import re
import sys
import urllib.request
import warnings

warnings.filterwarnings("ignore")
OUT = pathlib.Path(r"C:\Users\User\knigi_kupleno\notebooklm_txt")


def strip_html(s):  # убираем теги, оставляем абзацы
    s = re.sub(r"(?is)<(script|style|nav|footer|header).*?</\1>", "", s)
    s = re.sub(r"(?i)<br\s*/?>|</p>|</h\d>|</div>|</li>|</tr>", "\n", s)
    s = re.sub(r"<[^>]+>", "", s)
    return re.sub(r"\n{3,}", "\n\n", html.unescape(s)).strip()


def from_url(u):
    req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0) VitaReader/1.0"})
    with urllib.request.urlopen(req, timeout=30) as r:  # 401/402/403 -> исключение, не повторяем и не обходим
        raw = r.read(8_000_000)
        enc = r.headers.get_content_charset() or "utf-8"
    return strip_html(raw.decode(enc, "ignore"))


def from_file(p):
    ext = p.suffix.lower()
    if ext == ".pdf":
        from pypdf import PdfReader
        return "".join(f"\n\n=== стр. {i+1} ===\n{pg.extract_text() or ''}" for i, pg in enumerate(PdfReader(str(p)).pages))
    if ext == ".epub":
        import ebooklib
        from ebooklib import epub
        book = epub.read_epub(str(p), options={"ignore_ncx": True})
        parts = [strip_html(it.get_content().decode("utf-8", "ignore")) for it in book.get_items_of_type(ebooklib.ITEM_DOCUMENT)]
        return "".join(f"\n\n=== часть {i+1} ===\n{t}" for i, t in enumerate(parts))
    if ext == ".docx":
        import docx
        return "\n".join(par.text for par in docx.Document(str(p)).paragraphs)
    if ext in (".html", ".htm"):
        return strip_html(p.read_text(encoding="utf-8", errors="ignore"))
    return p.read_text(encoding="utf-8", errors="ignore")  # md, txt


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    src = sys.argv[1]
    out_dir = pathlib.Path(sys.argv[2]) if len(sys.argv) > 2 else OUT
    out_dir.mkdir(parents=True, exist_ok=True)
    try:
        if re.match(r"https?://", src):
            text = from_url(src)
            name = re.sub(r"[^\w.-]+", "_", re.sub(r"^https?://", "", src))[:80]
        else:
            p = pathlib.Path(src)
            text = from_file(p)
            name = p.stem
    except Exception as e:  # молчаливых ошибок нет: что случилось + что делать
        sys.exit(f"НЕ СОБРАНО: {src}\nПричина: {e}\nЗакрытые страницы (403/401/подписка) не обходим — пришли файл или другой источник.")
    if len(text.strip()) < 200:
        sys.exit(f"НЕ СОБРАНО: {src}\nТекста почти нет ({len(text.strip())} знаков): скан без текста или страница грузится скриптами.")
    out = out_dir / f"{name}.txt"
    out.write_text(text, encoding="utf-8")
    print(f"Готово: {len(text)} знаков -> {out}")


if __name__ == "__main__":
    main()
# Что скрипт делает целиком: берёт ссылку или файл, вытаскивает текст, кладёт в txt с метками страниц —
# дальше этот txt загружает в NotebookLM помощник.
