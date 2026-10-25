# Задание проверяльщику (proverka). Всё по-английски, ответ — по-русски (in Russian).
Goal: check that rules in a draft skill are really supported by its source notes (no invented facts, numbers or steps).
Skill file: C:/Users/User/knigi_kupleno/skill_chernovik_glubokiy/polzer-rag-python-cookbook/SKILL.md
Source notes (the only truth; read what you need): C:/Users/User/knigi_kupleno/glubokiy/rag_python_cookbook_*.md
Check exactly these 12 lines of the skill (line numbers): 21, 22, 26, 29, 40, 75, 80, 86, 117, 123, 136, 166.
For each line: find the supporting text in the source notes (grep for key words/numbers). Verdict: СОВПАЛО (claim and numbers are in the source) / ЧАСТИЧНО (what differs) / НЕТ В ИСТОЧНИКЕ. Result line: "N | verdict | quote ≤15 words from source + file name".
Then total "совпало N из 12" (ЧАСТИЧНО not counted). Also: 1) does the skill have frontmatter with name and description; 2) are there lines with "(заполню сама)" placeholder — only a note.
Do not edit anything. Step ceiling: at most 30 tool calls; stuck -> stop and report what you have.
