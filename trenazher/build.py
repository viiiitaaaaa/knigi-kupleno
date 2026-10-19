# Склеивает кусочки из папки src в ОДИН файл trenazher_peregovory.html.
# Запуск: python build.py
from pathlib import Path

here = Path(__file__).parent          # папка, где лежит этот скрипт
src = here / "src"                    # подпапка с кусочками

def read(name):
    return (src / name).read_text(encoding="utf-8")   # открыть файл и прочитать как текст

js = "\n".join(read(n) for n in ["cards.js", "scen.js", "dialogs.js", "app.js"])   # склеить 4 файла в один
html = read("shell.html").replace("/*CSS*/", read("style.css")).replace("/*JS*/", js)  # вставить на места-метки

out = here / "trenazher_peregovory.html"
out.write_text(html, encoding="utf-8")
print("готово:", out, round(out.stat().st_size / 1024), "КБ")
