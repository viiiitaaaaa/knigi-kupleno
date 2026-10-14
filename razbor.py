"""Собрать приёмы из разделов «Что применяем у нас» всех конспектов по скиллам -> knigi_kupleno/po_skillam/<skill>.md"""
import re, glob, pathlib, collections
K = pathlib.Path(r"C:\Users\User\.claude\skills\knowledge-library\references\knigi")
OUT = pathlib.Path(r"C:\Users\User\knigi_kupleno\po_skillam"); OUT.mkdir(exist_ok=True)
by = collections.defaultdict(list)
for f in sorted(K.glob("*.md")):
    if f.name.startswith("00_") or f.name.startswith("seni_"):
        continue
    t = f.read_text("utf-8")
    m = re.search(r"(?im)^#+\s*.*Что применяем.*$", t)
    if not m:
        continue
    sec = t[m.start():]
    e = re.search(r"(?im)^#+\s*.*Чего\s+НЕ\s+брать.*$", sec)
    sec = sec[:e.start()] if e else sec
    # блоки = пункты списка / абзацы
    for blk in re.split(r"\n(?=\s*(?:[-*]|\d+[.)])\s)|\n\s*\n", sec):
        tags = set(re.findall(r"→\s*`?([a-z][a-z0-9\-]+)`?", blk))
        for tg in tags:
            by[tg].append(f"[{f.stem}] " + blk.strip())
for tg, items in by.items():
    (OUT / f"{tg}.md").write_text(f"# Приёмы из книг для скилла {tg} ({len(items)})\n\n" + "\n\n".join(items), "utf-8")
    print(tg, len(items))
