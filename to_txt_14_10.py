"""Книги 14.10.2026 (НЛП, переговоры, уверенность) -> txt13\\ с метками страниц, дописываем в svodka_13_10.json.
Повтор «Never Split… (1).pdf» — та же SHA-256, пропущен. Два издания Introducing NLP — оба в текст, берём полное."""
import json, pathlib, warnings
warnings.filterwarnings("ignore")
import pymupdf

W = pathlib.Path(r"C:\Users\User\knigi_kupleno")
SRC = pathlib.Path(r"G:\Мой диск\куплено")
OUT = W / "txt13"
NEW = {
    "introducing_nlp": "Introducing_NLP_-_Joseph_OConnor.pdf",
    "introducing_nlp_b": "Introducing_NLP_-_Joseph_Connor.pdf",
    "sleight_of_mouth": "Sleight_of_Mouth_-_Robert_Dilts.pdf",
    "changing_belief_systems": "Changing_Belief_Systems_With_NLP_-_Robert_Dilts.pdf",
    "using_your_brain": "Using_Your_Brain--For_a_Change_-_Richard_Bandler.pdf",
    "take_charge_bandler": "How_to_Take_Charge_of_Your_Life_The_Users_Guide_to_NLP_-_Richard_Bandler.pdf",
    "never_split_difference": "Never_Split_the_Difference__Negotiating_as_-_Chris_Voss.pdf",
    "ask_for_it": "Ask_For_It_How_Women_Can_Use_the_Power_of_Negotiation_to_Get_What_They_Really_Want_-_Linda_Babcock.pdf",
    "playing_big": "Playing_Big_-_Tara_Mohr.pdf",
}
sv = [r for r in json.loads((W / "svodka_13_10.json").read_text("utf-8")) if r.get("slug") not in NEW]
for slug, name in NEW.items():
    d = pymupdf.open(SRC / name)
    t = "".join(f"\n\n=== стр. {i+1} ===\n" + pg.get_text() for i, pg in enumerate(d))
    (OUT / f"{slug}.txt").write_text(t, "utf-8")
    r = {"slug": slug, "file": name, "units": len(d), "words": len(t.split())}
    sv.append(r); print(r, flush=True)
(W / "svodka_13_10.json").write_text(json.dumps(sv, ensure_ascii=False, indent=1), "utf-8")
