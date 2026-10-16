# Числа из пересказа (%, $, ≥3 цифр, дробные) — есть ли в тексте книги. python -I sverka_cifr.py <slug>
import re, sys, pathlib
sys.stdout.reconfigure(encoding="utf-8")
K = pathlib.Path(r"C:\Users\User\knigi_kupleno"); slug = sys.argv[1]
book = " ".join(p.read_text("utf-8", "ignore") for p in sorted((K/"chunks_vse").glob(f"{slug}_*.txt")))
bn = set(re.findall(r"\d+(?:\.\d+)?", book.replace(",", "")))
for f in sorted((K/"pereskaz_vse").glob(f"{slug}_*.md")):
    t = f.read_text("utf-8").split("\n", 1)[1]
    nums = set(re.findall(r"\d+(?:[.,]\d+)?(?=\s?%)|\$\s?\d[\d,.]*|\b\d+\.\d+\b|\b\d{3,}(?:[ ,]\d{3})*\b", t))
    norm = lambda n: re.sub(r"[ $]", "", n).replace(",", "." if re.fullmatch(r"\$?\d+,\d{1,2}", n) else "")
    bad = sorted(n for n in nums if norm(n) not in bn and not re.fullmatch(r"20[12]\d", n))
    print(f"{f.name}: чисел {len(nums)}, не найдено {len(bad)}: {', '.join(bad[:15])}")
