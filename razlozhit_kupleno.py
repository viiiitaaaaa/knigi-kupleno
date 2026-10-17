# Раскладка G:\Мой диск\куплено по темам + копии лекций (рефератов) из папки «Учёба». Журнал — для отката.
import csv, os, shutil, sys, time
from pathlib import Path

K = Path(r"G:\Мой диск\куплено")
U = Path(r"G:\Мой диск\Учёба — маркетплейсы, дропшиппинг, бизнес")
TRASH = Path(r"G:\Мой диск\_Можно удалить (дубли и мусор)")
LOG = K / f"_журнал раскладки {time.strftime('%Y-%m-%d %H-%M')}.csv"

T = {
    "01": "01 Маркетинг — основы и стратегия",
    "02": "02 Реклама, SEO и соцсети",
    "03": "03 Интернет-магазин, дропшиппинг и товар",
    "04": "04 Маркетплейсы (WB, Ozon)",
    "05": "05 Продажи и переговоры",
    "06": "06 Бренд, дизайн и позиционирование",
    "07": "07 Аналитика, данные и мышление",
    "08": "08 Бизнес и стратегия",
    "09": "09 ИИ, агенты и Claude",
    "10": "10 IT и сети",
    "11": "11 Обучение и память",
    "12": "12 Психология, НЛП и личностный рост",
    "13": "13 Личные финансы и жизнь",
    "99": "99 Не по делу",
}

# ключевое слово в имени файла -> тема (первое совпадение)
RULES = [
    ("17.mobi", "01"), ("Marketing 4.0", "01"), ("Marketing 6.0", "01"), ("Marketing 7.0", "01"),
    ("Marketing Management", "01"), ("Marketing Strategy in the Digital Age", "01"), ("Marketing, Eighth", "01"),
    ("=Marketing.7z", "01"), ("=Marketing.epub", "01"), ("Principles of Marketing", "01"), ("ENTREPRENEURIAL", "01"),
    ("CONSUMER BEHAVIOR", "01"), ("ALGEROIS", "01"), ("внукам", "01"),
    ("Advertising", "02"), ("SEO", "02"), ("Social Media Marketing", "02"), ("SaaS Marketing", "02"),
    ("Show Your Work", "02"), ("Seni Penulisan", "02"),
    ("8-Figure", "03"), ("Amazon FBA", "03"), ("Dropshipping", "03"), ("E-Commerce Business", "03"),
    ("Home-Based Business", "03"), ("High-Priced", "03"), ("Sewing to Sell", "03"),
    ("Challenger", "05"), ("SPIN", "05"), ("PITCH ANYTHING", "05"), ("Never_Split", "05"), ("Ask_For_It", "05"),
    ("Persuasion", "05"), ("Продажи B2B", "05"), ("LinkedIn Sales", "05"), ("Million Dollar Consulting", "05"),
    ("Mom Test", "05"),
    ("Graphic Design", "06"), ("Naming Book", "06"), ("Obviously Awesome", "06"), ("Storytelling in Design", "06"),
    ("Design for how People Think", "06"), ("PORTFOLIOS", "06"),
    ("Lean Analytics", "07"), ("Storytelling with Data", "07"), ("Minto", "07"),
    ("International Business", "08"),
    ("Claude Code", "09"), ("Mastering Claude", "09"), ("Agentic Design", "09"), ("AI Engineering", "09"), ("AI_Engineering", "09"),
    ("Build an AI Agent", "09"), ("0→1 Loop", "09"), ("RAG", "09"), ("Co-Intelligence", "09"), ("Prediction Machines", "09"),
    ("OpenVPN", "10"), ("Distributed Systems", "10"),
    ("Make_It_Stick", "11"), ("Ultralearning", "11"), ("Mind_For_Numbers", "11"), ("Peak__", "11"),
    ("Moonwalking", "11"), ("Fluent_Forever", "11"), ("Second_Brain", "11"),
    ("NLP", "12"), ("Bandler", "12"), ("Dilts", "12"), ("Telling Lies", "12"), ("Playing_Big", "12"),
    ("Firearms", "99"), ("Market Garden", "99"), ("Art Market", "99"),
]

LECT = {  # реферат -> тема
    "01 Реферат": "04", "02 Реферат": "04", "03 Реферат": "03", "04 Реферат": "03", "05 Реферат": "02",
    "06 Реферат": "08", "07 Реферат": "09", "08 Реферат": "07", "10 Реферат": "12", "11 Реферат": "12",
    "12 Реферат": "13",
}
LECT_DIRS = {"Курсы DDD": "10", "Схемы": "05"}

dry = "--go" not in sys.argv
rows, unknown = [], []

def do(op, src, dst):
    rows.append((op, str(src), str(dst)))
    if dry:
        return
    dst.parent.mkdir(parents=True, exist_ok=True)
    if dst.exists():
        rows[-1] = ("ПРОПУСК (уже есть)", str(src), str(dst)); return
    if op == "перенос":
        shutil.move(str(src), str(dst))
    elif src.is_dir():
        shutil.copytree(str(src), str(dst))
    else:
        shutil.copy2(str(src), str(dst))

for f in sorted(K.iterdir()):
    n = f.name
    if f.is_dir() or n.startswith("_журнал") or n == "desktop.ini":
        continue
    if n.endswith(".tmp"):
        do("перенос", f, TRASH / "куплено — недокачанные .tmp" / n); continue
    t = next((t for k, t in RULES if (n == k[1:] if k.startswith("=") else k.lower() in n.lower())), None)
    if t is None:
        unknown.append(n); continue
    do("перенос", f, K / T[t] / n)

for f in sorted(U.iterdir()):
    n = f.name
    t = next((t for k, t in LECT.items() if n.startswith(k)), None) or \
        next((t for k, t in LECT_DIRS.items() if n.startswith(k)), None)
    if t:
        do("копия лекции", f, K / T[t] / ("Лекции — " + n if f.is_dir() else n))

for op, s, d in rows:
    print(op, "|", Path(s).name, "->", Path(d).parent.name)
print("НЕ РАЗЛОЖЕНО:", unknown)
if not dry:
    with open(LOG, "w", newline="", encoding="utf-8-sig") as fh:
        w = csv.writer(fh, delimiter=";"); w.writerow(["действие", "откуда", "куда"]); w.writerows(rows)
    print("журнал:", LOG)
