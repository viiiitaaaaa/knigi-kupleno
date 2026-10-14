"""Книги 14.10.2026, вторая пачка (как учиться и запоминать) -> txt13\\ с метками страниц, дописываем в svodka_13_10.json."""
import json, pathlib, warnings
warnings.filterwarnings("ignore")
import pymupdf

W = pathlib.Path(r"C:\Users\User\knigi_kupleno")
SRC = pathlib.Path(r"G:\Мой диск\куплено")
OUT = W / "txt13"
NEW = {
    "a_mind_for_numbers": "A_Mind_For_Numbers_-_Barbara_Oakley.pdf",
    "ultralearning": "Ultralearning_-_Scott_Young.pdf",
    "make_it_stick": "Make_It_Stick_-_Peter_C_Brown_Henry_L_Roediger_III.pdf",
    "peak_ericsson": "Peak__Secrets_from_the_New_Science_of_Expe_-_Anders_Ericsson.pdf",
    "moonwalking_einstein": "Moonwalking_With_Einstein__The_Art_and_Sci_-_Joshua_Foer.pdf",
    "second_brain": "Building_a_Second_Brain_A_Proven_Method_to_Organize_Your_Digital_Life_and_Unlock_Your_Creative_Potential_-_Tiago_Forte.pdf",
    "fluent_forever": "Fluent_Forever_-_Gabriel_Wyner.pdf",
}
sv = [r for r in json.loads((W / "svodka_13_10.json").read_text("utf-8")) if r.get("slug") not in NEW]
for slug, name in NEW.items():
    d = pymupdf.open(SRC / name)
    t = "".join(f"\n\n=== стр. {i+1} ===\n" + pg.get_text() for i, pg in enumerate(d))
    (OUT / f"{slug}.txt").write_text(t, "utf-8")
    r = {"slug": slug, "file": name, "units": len(d), "words": len(t.split())}
    sv.append(r); print(r, flush=True)
(W / "svodka_13_10.json").write_text(json.dumps(sv, ensure_ascii=False, indent=1), "utf-8")
