# Буфер обмена → файл UTF-8. python sohranit.py <путь> [заголовок-комментарий]
import subprocess, sys, pathlib
t = subprocess.run(["powershell", "-NoProfile", "-Command",
    "[Console]::OutputEncoding=[Text.Encoding]::UTF8; Get-Clipboard -Raw"], capture_output=True).stdout.decode("utf-8")
p = pathlib.Path(sys.argv[1])
head = f"<!-- {sys.argv[2]} -->\n" if len(sys.argv) > 2 else ""
p.write_text(head + t.strip() + "\n", "utf-8")
print("сохранено", p.name, len(t), "знаков")
