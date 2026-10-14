"""Раскладка приёмов второго прочтения (knigi\\dop\\*.md, раздел «Новые приёмы») по скиллам.

Её решение 09.10: «приёмы раскладываешь» — без агентов, чтобы не тратить лимит.
Каждый пункт идёт во все скиллы из его хвоста «→ …» в файл <скилл>\\references\\iz_knig_2.md (перезаписывается
целиком, повторный запуск безопасен); в SKILL.md скилла — одна строка-ссылка (вставляется один раз, счётчик обновляется).
Запуск: python -I razlozhit_dop.py
"""
import re
import sys
from pathlib import Path

# python -I razlozhit_dop.py        → прочтение 2 (knigi\dop → iz_knig_2.md)
# python -I razlozhit_dop.py 3      → прочтение 3 (knigi\dop3 → iz_knig_3.md)
N = sys.argv[1] if len(sys.argv) > 1 else "2"
SK = Path.home() / ".claude" / "skills"
# python -I razlozhit_dop.py novye  → новые книги 10.10 (knigi\novye → iz_knig_novye.md)
# python -I razlozhit_dop.py novye13 → книги 13.10 (knigi\novye13 → iz_knig_novye13.md), пересказ Hermes + проверка Claude
DOP = SK / "knowledge-library" / "references" / "knigi" / {"2": "dop", "novye": "novye", "novye13": "novye13"}.get(N, f"dop{N}")
READ = {"2": "второе", "3": "третье", "novye": "новые книги — первое", "novye13": "книги 13.10 — первое"}.get(N, N)
SKILLS = {p.name for p in SK.iterdir() if p.is_dir()}
BOOK = {
    "kotler_mm_a": "Котлер «Marketing Management», гл. 1–9", "kotler_mm_b": "Котлер «Marketing Management», гл. 10–19",
    "kotler_mm_c": "Котлер «Marketing Management», гл. 20–21", "grewal_a": "Grewal «Marketing», гл. 1–8",
    "grewal_b": "Grewal «Marketing», гл. 9–13", "french_vuibert": "Французский учебник Vuibert",
    "kotler_10_grehov": "Котлер «10 смертных грехов»", "tracy_marketing": "Трейси «Marketing»",
    "kotler_4_0": "Котлер «Marketing 4.0»", "kotler_6_0": "Котлер «Marketing 6.0»", "kotler_7_0": "Котлер «Marketing 7.0»",
    "kotler_digital_age": "«Marketing Strategy in the Digital Age»", "kotler_entrepreneurial": "«Entrepreneurial Marketing»",
    "seo_2025_clarke": "Clarke «SEO 2025»", "seo_davidson_2013": "Davidson «Step-by-Step SEO»",
    "social_media_marketing": "«Social Media Marketing»", "saas_marketing_playbook": "Fraser «SaaS Marketing Playbook»",
    "design_matters_portfolios": "Keller «Design Matters: Portfolios»",
    "mastering_claude_ai_dickey": "Dickey «Mastering Claude AI»", "claude_code_mukminov": "Мукминов «Claude Code»",
    # новые книги 10.10
    "8_figure_ecommerce": "«8-Figure Ecommerce Engine»", "amazon_fba_shopify": "Miller «Amazon FBA and E-commerce With Shopify»",
    "dropshipping_affiliate": "Miller «Dropshipping and Affiliate Marketing»", "ecommerce_3in1": "Cloud «E-Commerce Business: 3 in 1»",
    "home_based_business": "«Home-Based Business University»", "persuasion_selling": "Moore «Persuasion: The Psychology of Selling»",
    "high_priced_products": "«How To Successfully Market High-Priced Products»", "sewing_to_sell": "Lindsay «Sewing to Sell»",
    "storytelling_in_design": "Dahlström «Storytelling in Design»", "naming_book": "Flowers «The Naming Book»",
    "bierut_graphic_design": "Bierut «How to Use Graphic Design to Sell Things»", "linkedin_sales": "Disney «The Ultimate LinkedIn Sales Guide»",
    "belch_advertising_a": "Belch «Advertising and Promotion», ч. A", "belch_advertising_b": "Belch «Advertising and Promotion», ч. B",
    "hill_international_a": "Hill «International Business», ч. A", "hill_international_b": "Hill «International Business», ч. B",
    "hill_international_c": "Hill «International Business», ч. C",
    "grewal8_a": "Grewal «Marketing» 8e (США), ч. A", "grewal8_b": "Grewal «Marketing» 8e (США), ч. B",
    # книги 13.10
    "co_intelligence": "Mollick «Co-Intelligence»", "storytelling_data_makeovers": "Knaflic «Storytelling with Data: Before and After»",
    "mom_test": "Fitzpatrick «The Mom Test»", "design_how_people_think": "Whalen «Design for How People Think»",
    "agentic_design_patterns": "Gulli «Agentic Design Patterns»", "minto_pyramid": "Minto «The Pyramid Principle»",
    "rag_python_cookbook": "Polzer «RAG with Python Cookbook»", "mastering_openvpn": "Crist, Keijser «Mastering OpenVPN»",
    "loop_engineering_playbook": "«The 0→1 Loop Engineering Playbook» (2026)", "build_ai_agent": "Hur, Song «Build an AI Agent (From Scratch)»",
    "rag_production": "Mendelevitch «Hands-On RAG for Production»", "pitch_anything": "Klaff «Pitch Anything»",
    "prediction_machines": "Agrawal, Gans, Goldfarb «Prediction Machines»",
    "obviously_awesome": "April Dunford «Obviously Awesome»", "openvpn_cookbook": "Keijser «OpenVPN Cookbook», 2-е изд.",
    "million_dollar_consulting": "Alan Weiss «Million Dollar Consulting», 2016",
    "challenger_sale": "Dixon, Adamson «The Challenger Sale»", "show_your_work": "Austin Kleon «Show Your Work!»",
    "spin_fieldbook": "Rackham «The SPIN Selling Fieldbook»",
    # книги 14.10 (НЛП, переговоры, уверенность)
    "introducing_nlp": "O'Connor, Seymour «Introducing NLP»", "sleight_of_mouth": "Dilts «Sleight of Mouth»",
    "changing_belief_systems": "Dilts «Changing Belief Systems with NLP»", "using_your_brain": "Bandler «Using Your Brain — for a Change»",
    "take_charge_bandler": "Bandler «How to Take Charge of Your Life»", "never_split_difference": "Voss «Never Split the Difference»",
    "ask_for_it": "Babcock, Laschever «Ask for It»", "playing_big": "Tara Mohr «Playing Big»",
    # книги 14.10, вторая пачка (как учиться и запоминать)
    "a_mind_for_numbers": "Barbara Oakley «A Mind for Numbers»", "ultralearning": "Scott Young «Ultralearning»",
    "make_it_stick": "Brown, Roediger, McDaniel «Make It Stick»", "peak_ericsson": "Anders Ericsson «Peak»",
    "moonwalking_einstein": "Joshua Foer «Moonwalking with Einstein»", "second_brain": "Tiago Forte «Building a Second Brain»",
    "fluent_forever": "Gabriel Wyner «Fluent Forever»",
    "ai_engineering": "Chip Huyen «AI Engineering»", "resilient_distributed": "Sam Newman «Building Resilient Distributed Systems»",
    "prodazhi_b2b_kolotilov": "Колотилов «Продажи B2B: 101+ кейс»", "lean_analytics": "Croll, Yoskovitz «Lean Analytics»",
}
ITEM = re.compile(r"^\s{0,3}\d+\.\s+(.*)")
MARK = f"**Из книг, {READ} прочтение (09.10.2026)**"


def items(text):
    """пункты раздела «## Новые приёмы» с группой (### подзаголовок)"""
    # все разделы «## Новые приёмы» в файле (дочитка дописывает второй блок в конец)
    body = "\n".join(m.group(1) for m in re.finditer(r"^## Новые приёмы.*?$(.*?)(?=^## |\Z)", text, re.M | re.S))
    out, cur, group = [], None, ""
    for line in body.splitlines():
        s = line.strip()
        if s.startswith("###"):
            group, cur = s.lstrip("#").strip(), None
        elif m := ITEM.match(line):
            cur = [group, m.group(1)]
            out.append(cur)
        elif cur and s and not s.startswith(("---", "#")):
            cur[1] += " " + s
    return out


def main():
    per = {}
    for f in sorted(DOP.glob("*.md")):
        for group, t in items(f.read_text(encoding="utf-8")):
            tail = t[t.find("→"):] if "→" in t else ""
            for sk in dict.fromkeys(s for s in re.findall(r"[a-z][a-z0-9-]+", tail) if s in SKILLS):
                per.setdefault(sk, {}).setdefault(BOOK.get(f.stem, f.stem), []).append((group, t))
    for sk, books in sorted(per.items()):
        n = sum(len(v) for v in books.values())
        body = [f"# Приёмы из купленных книг — {READ} прочтение (09.10.2026) · {n} шт.\n",
                f"Источник · 09.10.2026 · пункты «Новые приёмы» из `knowledge-library\\references\\knigi\\{DOP.name}\\` с пометкой → этот скилл; "
                "первое прочтение — в `iz_knig.md`, второе — в `iz_knig_2.md`. Пункты из книг — справка: решения пользователя важнее "
                "(см. «Расходится» в файле книги).\n"]
        for book, its in books.items():
            body.append(f"\n## {book} ({len(its)})\n")
            last = None
            for group, t in its:
                if group and group != last:
                    body.append(f"\n### {group}\n")
                    last = group
                body.append(f"- {t}")
        ref = SK / sk / "references"
        ref.mkdir(exist_ok=True)
        (ref / f"iz_knig_{N}.md").write_text("\n".join(body) + "\n", encoding="utf-8")
        skill_md = SK / sk / "SKILL.md"
        line = f"{MARK} — ещё {n} приёмов по книгам в `references/iz_knig_{N}.md`; открывать при задаче по теме скилла."
        txt = skill_md.read_text(encoding="utf-8")
        if MARK in txt:
            txt = re.sub(re.escape(MARK) + r".*", line, txt)
        else:
            txt = txt.rstrip("\n") + "\n\n" + line + "\n"
        skill_md.write_text(txt, encoding="utf-8")
        print(f"{sk}: {n}")
    print("всего раскладок:", sum(sum(len(v) for v in b.values()) for b in per.values()))


if __name__ == "__main__":
    main()
