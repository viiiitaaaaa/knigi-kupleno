import json, pathlib, re, zipfile, posixpath
W = pathlib.Path(r"C:\Users\User\knigi_kupleno")
src = (W / "to_txt_13_10.py").read_text("utf-8").split("res = []")[0]
exec(src)

def ep_zip(p):
    """epub без toc.ncx/части файлов — главы по порядку spine прямо из zip."""
    z = zipfile.ZipFile(p)
    opf = next(n for n in z.namelist() if n.endswith(".opf"))
    o = z.read(opf).decode("utf-8", "ignore"); base = posixpath.dirname(opf)
    man = dict(re.findall(r'<item[^>]*?id="([^"]+)"[^>]*?href="([^"]+)"', o))
    man.update({i: h for h, i in re.findall(r'<item[^>]*?href="([^"]+)"[^>]*?id="([^"]+)"', o)})
    names, parts, missing = set(z.namelist()), [], []
    for idref in re.findall(r'<itemref[^>]*idref="([^"]+)"', o):
        f = posixpath.join(base, man.get(idref, ""))
        if f in names: parts.append(strip_html(z.read(f).decode("utf-8", "ignore")))
        else: missing.append(f)
    return "".join(f"\n\n=== часть {i+1} ===\n{t}" for i, t in enumerate(parts)), len(parts), missing

NEW2 = {"obviously_awesome": "Obviously Awesome (April Dunford).epub", "openvpn_cookbook": "OpenVPN Cookbook"}
sv = [r for r in json.loads((W / "svodka_13_10.json").read_text("utf-8")) if r.get("slug") not in NEW2]
for slug, start in NEW2.items():
    p = next(f for f in SRC.iterdir() if f.name.startswith(start) and f.suffix == ".epub")
    t, n, miss = ep_zip(p)
    (OUT / f"{slug}.txt").write_text(t, "utf-8")
    r = {"slug": slug, "file": p.name, "units": n, "words": len(t.split()), "missing": miss}
    sv.append(r); print(r)
(W / "svodka_13_10.json").write_text(json.dumps(sv, ensure_ascii=False, indent=1), "utf-8")
