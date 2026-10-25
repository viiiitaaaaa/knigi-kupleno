import sys,random,re
name,skill,*src=sys.argv[1:]
lines=open(skill,encoding='utf-8').read().split('\n')
cand=[i+1 for i,l in enumerate(lines) if l.startswith('- ') and len(l)>60]
random.seed(7); pick=sorted(random.sample(cand,min(12,len(cand))))
t=f"""# Задание проверяльщику (proverka). Всё по-английски, ответ — по-русски (in Russian).
Goal: check that rules in a draft skill are really supported by its source notes (no invented facts, numbers or steps).
Skill file: {skill}
Source notes (the only truth; read what you need): {'; '.join(src)}
Check exactly these {len(pick)} lines of the skill (line numbers): {', '.join(map(str,pick))}.
For each line: find the supporting text in the source notes (grep for key words/numbers). Verdict: СОВПАЛО (claim and numbers are in the source) / ЧАСТИЧНО (what differs) / НЕТ В ИСТОЧНИКЕ. Result line: "N | verdict | quote ≤15 words from source + file name".
Then total "совпало N из {len(pick)}" (ЧАСТИЧНО not counted). Also: 1) does the skill have frontmatter with name and description; 2) are there lines with "(заполню сама)" placeholder — only a note.
Do not edit anything. Step ceiling: at most 30 tool calls; stuck -> stop and report what you have.
"""
open(f"check_{name}.md","w",encoding='utf-8').write(t); print(len(pick))
