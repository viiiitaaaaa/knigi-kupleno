# Достаёт из 04_testy.md ТОЛЬКО реплики (без критериев и без пометок типа) для слепого теста.
# У четырёх файлов форматы разные, поэтому для каждого — своё правило (regex = шаблон поиска в тексте).
import re
from pathlib import Path

def bold_line(t):      # "- **A1 [У]** текст" -> текст   (dilts_som, bandler_take_charge)
    return re.findall(r"^- \*\*([AB]\d)[^*]*\*\*\s*(.+)$", t, re.M)

def reply_line(t):     # "### A1 ...\n**Реплика Виты:** текст"   (oconnor_nlp)
    return re.findall(r"### ([AB]\d)[^\n]*\n\*\*Реплика Виты:\*\*\s*(.+)", t)

def table_row(t):      # "| A1 | текст | тип | ..."   (bandler_uyb)
    return re.findall(r"^\| ([AB]\d) \| (.+?) \|", t, re.M)

def cbs(t):            # "### A1 — ..\nРеплика: «..»\n- **Обяз."   (dilts_cbs)
    out = []
    for b in re.split(r"\n(?=### )", t):
        m = re.match(r"### ([AB]\d)", b)
        r = re.search(r"Реплика:\s*(.+?)\n- \*\*", b, re.S)
        if m and r:
            out.append((m.group(1), r.group(1).strip()))
    return out

RULES = {"dilts_cbs": cbs, "dilts_som": bold_line, "oconnor_nlp": reply_line,
         "bandler_uyb": table_row, "bandler_take_charge": bold_line}

for d, fn in RULES.items():
    items = fn(Path(d, "04_testy.md").read_text(encoding="utf-8"))
    for blk in "AB":
        lines = [f"# {d}: реплики блока {blk}\n"]
        for tid, rep in items:
            if tid[0] == blk:
                lines.append(f"## {tid}\n{rep}\n")
        Path(d, f"_replici_{blk}.md").write_text("\n".join(lines), encoding="utf-8")
    print(d, sum(1 for i in items if i[0][0] == "A"), sum(1 for i in items if i[0][0] == "B"))
