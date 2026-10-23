# Кодовая проверка ответов (быстрая, без модели-судьи): ловит формальные нарушения.
# Запуск: python sverka.py   -> читает otvety/<книга>.md, пишет sverka_itog.md
import re, glob, os

here = os.path.dirname(os.path.abspath(__file__))
# Главная строчка: каждое правило — «шаблон -> что это значит»
BAD = [
    (r"\b8[- ]?800\b|\b112\b|\b\+?7[\d\s\-()]{9,}", "номер телефона"),
    (r"\bстр\.?\s*\d+|\bстраниц[аеы]\s*\d+", "номер страницы"),
    (r"\b\d{2,}\s?(₽|руб|%|\$)", "голая цифра/ставка (должно быть __)"),
]
NET = re.compile(r"в (этой )?(книге|источнике|конспекте|карточках)[^.\n]{0,40}\bнет\b|этого нет в", re.I)

out = []
for f in sorted(glob.glob(os.path.join(here, "otvety", "*.md"))):
    book = os.path.basename(f)[:-3]
    txt = open(f, encoding="utf-8").read()
    parts = re.split(r"^##\s*(T-\d+)", txt, flags=re.M)
    for i in range(1, len(parts), 2):
        tid, body = parts[i], parts[i + 1]
        flags = [name for pat, name in BAD if re.search(pat, body)]
        q = body.count("?")
        if tid in ("T-5", "T-6") and not NET.search(body):
            flags.append("нет метки «в книге нет» (тест на «не знаю»)")
        out.append(f"| {book} | {tid} | {q} | {'; '.join(flags) or '—'} |")

with open(os.path.join(here, "sverka_itog.md"), "w", encoding="utf-8") as g:
    g.write("| книга | тест | знаков «?» | нарушения кодом |\n|---|---|---|---|\n" + "\n".join(out) + "\n")
    bad = sum(1 for r in out if not r.endswith("| — |"))
    g.write(f"\nС нарушениями: {bad} из {len(out)}\n")
print("готово:", len(out), "ответов")
