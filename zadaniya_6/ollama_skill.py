r"""Скилл по книге через Ollama (gpt-oss:120b-cloud): сперва выжимка каждого конспекта, потом сборка SKILL.md по заданию.
Запуск: python ollama_skill.py <ключ: lean|minto|story|stick|peak|mind>
Что делает целиком: читает файл-задание книги, просит Ollama выжать правила из каждого конспекта (со страницами), потом собрать из выжимок один скилл-черновик."""
import sys, re, json, time, urllib.request, urllib.error
from pathlib import Path
Z = Path("C:/Users/User/knigi_kupleno/zadaniya_6"); key = sys.argv[1]
task = (Z / (key + ".md")).read_text("utf-8")
files = re.search(r"Файлы \(читать только их\): (.*?)\nДругие", task, re.S).group(1).split("; ")
out = Path(re.search(r"Куда писать: (.*?) \(", task).group(1)); out.parent.mkdir(parents=True, exist_ok=True)
def ask(p):
    body = json.dumps({"model": "gpt-oss:120b-cloud", "stream": False, "messages": [{"role": "user", "content": p}]}).encode()
    for a in range(3):
        try:
            r = urllib.request.urlopen(urllib.request.Request("http://127.0.0.1:11434/api/chat", body, {"Content-Type": "application/json"}), timeout=900)
            return json.loads(r.read())["message"]["content"].strip()
        except urllib.error.HTTPError as e:
            if e.code in (401, 403, 429): sys.exit(f"СТОП: Ollama {e.code} (лимит/доступ), не повторяю")
            time.sleep(30 * (a + 1))
        except Exception: time.sleep(30 * (a + 1))
    sys.exit("СТОП: не ответил 3 раза")
EXT = """Ты помогаешь собрать скилл из конспекта книги. Ниже конспект одной части. Выпиши по-русски ВСЕ конкретные правила, шаги, числа, пороги, списки, «когда НЕ применять» — каждое отдельной строкой «- правило (стр. N)». Страницу бери ТОЛЬКО из конспекта; нет — «стр. нет в конспекте». Ничего от себя не добавляй, воду убирай. Только список, без вступления.

Конспект:
"""
ex = []
for i, f in enumerate(files, 1):
    p = Path(f); t = ask(EXT + p.read_text("utf-8"))
    (Z / "ollama" / f"{key}_vyzhimka_{i:02d}.md").write_text(t, "utf-8"); ex.append(f"### {p.name}\n{t}")
    print(f"выжимка {i} из {len(files)}", flush=True)
FIN = task.split("Файлы (читать")[0] + "\n" + "Формат и правила — из задания выше (frontmatter, разделы «Если хочу X — шаги — (стр. N)», внизу «Не дочитано / неясно» с пометкой что конспекты писали открытые модели и с книгой не сверены; «Как применять с Витой» = «(заполню сама)»). Вместо файлов конспектов используй ВЫЖИМКИ ниже (они уже со страницами). Не добавляй фактов, которых нет в выжимках. Верни только текст SKILL.md, начиная со строки ---.\n\nВЫЖИМКИ:\n" + "\n\n".join(ex)
res = ask(FIN)
res = res[res.find("---"):] if "---" in res else res
out.write_text(res, "utf-8"); print("ГОТОВО", out, len(res.splitlines()), "строк")
