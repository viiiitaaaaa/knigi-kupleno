import os
G="C:/Users/User/knigi_kupleno/glubokiy/"
O="C:/Users/User/knigi_kupleno/skill_chernovik_glubokiy/"
T="""# Задание: скилл-«как делать» по книге {book} (25.10.2026){part}
Цель: из готовых конспектов по главам собрать скилл-черновик на русском для Claude: {goal}
Файлы (читать только их): {files}
Другие файлы не трогать, ничего не удалять.
Куда писать: {out} (только этот файл; папку создать).
Формат: {fm}Разделы: «Если хочу X — шаги — (стр. N)». Каждый шаг/правило/число с (стр. N) ИЗ конспекта; нет страницы — «стр. нет в конспекте»; убывающие диапазоны вроде «80–61» — «номер сомнителен». Внизу раздел «Не дочитано / неясно». Раздел «Как применять с Витой» НЕ придумывать — оставить «(заполню сама)».
Правила: ТОЛЬКО то, что есть в конспектах; не добавлять от себя; мелкая добавка — «(не из конспекта)». Простой русский, термины расшифровывать в скобках. Конспекты написаны разными открытыми моделями (первая строка файла — какая) и с книгой не сверены — напиши это в «Не дочитано». Длина до ~{n} строк: сохраняй числа, пороги, шаги, списки «когда НЕ применять»; воду убирай.
Образец строки: `- Агент проверяет результат инструмента до ответа — шаги: 1) … 2) … (стр. 118)`
Потолок: не больше 25 действий; застрял — стоп и доложи. Итог ответом (по-русски): путь, файлов прочитано N из M, что не вошло.
"""
def fm(name,desc): return "frontmatter `name: %s`, `description` (что даёт + триггеры в кавычках: %s); "%(name,desc)
K=G+"55 ИИ - AI Agents Definitive Guide (Koenigstein) (текст)_%02d.md"
def kk(a,b): return [K%i for i in range(a,b+1)]
KA=G+"55a ИИ - AI Agents Definitive Guide (Koenigstein) гл. 4–6 (текст)_%02d.md"
KB=G+"55b ИИ - AI Agents Definitive Guide (Koenigstein) гл. 7–9 (текст)_%02d.md"
KC=G+"55c ИИ - AI Agents Definitive Guide (Koenigstein) гл. 10–12 (текст)_%02d.md"
kg="проектирование и запуск ИИ-агентов (Koenigstein «AI Agents: The Definitive Guide»): модели, инструменты, память, оценка и наблюдение, планирование и кэш, безопасность."
tasks=[
("k1","Koenigstein «AI Agents: The Definitive Guide»"," — часть 1 из 3 (вводные главы и гл. 4–6)",kg,kk(1,7)+[KA%i for i in (1,2,3)],"koenigstein-ai-agents/part1.md","name: koenigstein-ai-agents; description пока не пиши (её соберу сама) — только разделы по главам. ",300),
("k2","Koenigstein «AI Agents: The Definitive Guide»"," — часть 2 из 3 (гл. 7–9)",kg,kk(8,11)+[KB%i for i in (1,2,3,4)],"koenigstein-ai-agents/part2.md","без frontmatter, только разделы по главам. ",300),
("k3","Koenigstein «AI Agents: The Definitive Guide»"," — часть 3 из 3 (гл. 10–12, безопасность, итоги)",kg,kk(12,21)+[KC%i for i in (1,2,3,4)],"koenigstein-ai-agents/part3.md","без frontmatter, только разделы по главам. ",300),
("rag1","Mendelevitch и др. «Hands-On RAG for Production»",""," как строить RAG (поиск + ответ модели) для рабочего применения: данные, нарезка, поиск, оценка, запуск.",[G+"rag_production_%02d.md"%i for i in range(1,16)],"mendelevitch-rag-production/SKILL.md",fm("mendelevitch-rag-production","«RAG», «поиск по документам», «эмбеддинги», «векторная база», «нарезка текста», «оценка RAG», «reranking», «галлюцинации»"),350),
("rag2","Polzer «RAG Python Cookbook»",""," рецепты RAG на Python: загрузка, нарезка, эмбеддинги, векторные базы, цепочки, оценка, типичные ошибки.",[G+"rag_python_cookbook_%02d.md"%i for i in range(1,12)],"polzer-rag-python-cookbook/SKILL.md",fm("polzer-rag-python-cookbook","«RAG на Python», «рецепт RAG», «эмбеддинги», «векторная база», «chunking», «LangChain», «поиск по документам»"),350),
("co","Mollick «Co-Intelligence»",""," как работать с ИИ как с партнёром: правила, когда ИИ помогает, когда вредит, роли, проверка, обучение, примеры из работы.",[G+"co_intelligence_%02d.md"%i for i in range(1,9)],"mollick-co-intelligence/SKILL.md",fm("mollick-co-intelligence","«ИИ как партнёр», «правила работы с ИИ», «галлюцинации», «когда ИИ вредит», «промпт-роль», «Mollick»"),300),
("pm","Agrawal, Gans, Goldfarb «Prediction Machines»",""," как смотреть на ИИ экономически: предсказание, суждение, данные, риск, когда ИИ окупается; для решений предпринимателя-одиночки.",[G+"prediction_machines_%02d.md"%i for i in range(1,12)],"prediction-machines/SKILL.md",fm("prediction-machines","«окупится ли ИИ», «предсказание и суждение», «данные для ИИ», «риск ИИ», «автоматизировать или нет», «prediction machines»"),300),
("loop","«The 0→1 Loop Engineering Playbook» (2026)",""," как строить рабочие циклы агентов (loop engineering): цикл, проверки, остановка, память, журнал, ошибки, запуск с нуля.",[G+"loop_engineering_playbook_%02d.md"%i for i in range(1,9)],"loop-engineering-playbook/SKILL.md",fm("loop-engineering-playbook","«цикл агента», «loop», «остановка агента», «проверка шага», «зацикливание», «с нуля до рабочего агента»"),350),
]
for key,book,part,goal,files,out,f,n in tasks:
    s=T.format(book=book,part=part,goal=goal,files="; ".join(files),out=O+out,fm=f,n=n)
    open("C:/Users/User/knigi_kupleno/zadaniya_6/%s.md"%key,"w",encoding="utf-8").write(s)
    print(key,len(files),all(os.path.exists(x) for x in files))
