import pathlib, html, sys
N = pathlib.Path(r"C:\Users\User\knigi_kupleno\notebooklm")
slug, title = sys.argv[1], sys.argv[2]
md = (N / f"{slug}_uchoba.md").read_text("utf-8-sig")
page = """<!doctype html><html lang="ru"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>""" + html.escape(title) + """ — учёба</title>
<style>:root{--bg:#faf8f4;--ink:#1f2328;--line:#e3ded4}
@media (prefers-color-scheme:dark){:root{--bg:#16181b;--ink:#e8e6e1;--line:#33373d}}
body{margin:0;background:var(--bg);color:var(--ink);font:17px/1.6 system-ui,"Segoe UI",sans-serif}
main{max-width:860px;margin:0 auto;padding:24px 16px 60px}h1{font-size:1.6rem}h2,h3{margin-top:28px}
.mermaid{background:#fff;border-radius:10px;padding:10px;overflow-x:auto}table{border-collapse:collapse}td,th{border:1px solid var(--line);padding:6px}</style></head>
<body><main id="m"></main>
<script type="text/plain" id="src">""" + html.escape(md) + """</script>
<script src="https://cdn.jsdelivr.net/npm/marked@12.0.2/marked.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/mermaid@10.9.1/dist/mermaid.min.js"></script>
<script>
const t=document.createElement('textarea');t.innerHTML=document.getElementById('src').textContent;
document.getElementById('m').innerHTML=marked.parse(t.value);
document.querySelectorAll('code.language-mermaid').forEach(c=>{const d=document.createElement('div');d.className='mermaid';d.textContent=c.textContent;c.parentElement.replaceWith(d)});
mermaid.initialize({startOnLoad:false});mermaid.run();
</script></body></html>"""
(N / f"{slug}_uchoba.html").write_text(page, "utf-8")
print("ok", slug)
