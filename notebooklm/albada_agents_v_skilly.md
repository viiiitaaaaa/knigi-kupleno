# Albada «Building Applications with AI Agents» (O'Reilly, Fifth Early Release) — итог и новое в скиллы (23.10.2026)

Источник: NotebookLM (Freya, блокнот «Проектирование систем ИИ-агентов»), файл «49 ИИ - … (Albada) (текст).txt».
Оригинал: `G:\Мой диск\куплено\09 ИИ, агенты и Claude\…(Michael Albada).epub`; текст — `knigi_kupleno\txt\Building_Applications_with_AI_Agents_Albada (текст).txt`
(в адресе ниже «стр. txt» = строка этого файла; в epub нет номеров страниц).
Готовы главы 1–8 из 13; главы 9 Measurement and Validation, 10 Monitoring, 11 Protecting, 12 Your New Teammate, 13 Humans and Agent — «unavailable».

## Что сделано
- Учебный конспект: `notebooklm\albada_agents_uchoba.md` / `.html` (список глав, идеи по главам, схема, чек-лист, ошибки, 20 карточек, 5 заданий).
- Пересказ: `pereskaz_vse\albada_agents_01..04.md` (главы 1–2, 3–4, 5–6, 7–8).
- Сверка (`sverka_citat.py`, `sverka_cifr.py`): цитаты 29/29 найдены (27 дословно, 2 близко к тексту); цифры — 0 ошибок.
  14 «ненайденных» в 04 — это сноски NotebookLM вида [10, 275–277], а не цифры книги; $100 в книге — «$100.0».
- Выдуманных глав нет: главы 9–13 NotebookLM честно пометил «недоступна».
- В конце ответов NotebookLM дописывает вопрос «Хотите…?» — это не текст книги.

## Новое в скиллы (проверено по тексту книги)
1. **Правила из опыта: подтвердить / удалить / поправить / добавить** (гл. 7 › Experiential Learning, ExpeL; операции AGREE/REMOVE/EDIT/ADD,
   promote/demote). Список уроков регулярно пересматривают: полезное поднимают, бесполезное опускают, дубли удаляют.
   → claude-code-priemy (`kak-uchit-claude.md`, раздел 7): у «ловушек» и уроков считать, сколько раз правило подтвердилось. Удалять — только с её «да».
2. **Предел длины цепочки шагов** — «errors can compound down the length of the chain» (гл. 5 › Chains, стр. txt 3139).
   → там же: длинную цепочку резать на шаги с проверкой между ними.
3. **Смысловые коллизии навыков** — «multiple skills overlap in functionality», лечится группировкой в иерархию
   (гл. 4 › Skill Hierarchies, стр. txt 2575; гл. 5 › Hierarchical Skill Selection). → там же: у нас ~150 скиллов с похожими триггерами.
4. **Важное — ближе к концу промпта** — «placing it close to the end of the prompt can increase the likelihood that it will be used»
   (гл. 6 › Managing Context Windows, стр. txt 3295). Совпадает с Anthropic (вопрос — внизу) и Lost in the Middle.
5. **Заметки до ответа (Self-Notes):** контекст → заметки по контексту → заметка по вопросу → ответ (гл. 6 › Note Taking; arXiv 2305.00833).
   Близко к нашему «сначала цитаты, потом вывод».
6. **Задача не слишком узкая, широкая или размытая** (гл. 2 › Avoiding Common Pitfalls in Task Definition, стр. txt 1268–1371).
7. **Против слепого доверия (automation bias):** показывать уверенность («Уверенность 70%, рекомендуем проверить»), просить
   подтверждение важного шага (гл. 3 › Communicating Confidence and Uncertainty; Preventing Automation Bias).
   → там же: в ответах ей помечать, в чём не уверена.
8. Бережливость: агента добавлять, только когда нельзя расширить текущего (гл. 8 › Principles for Adding Agents) — у нас уже так.

## Не взято
LangGraph, FAISS, векторные базы, Graph RAG, дообучение моделей — это код для разработчиков, нам сейчас не нужно.
Главы про проверку и защиту (9, 11) ещё не вышли — когда выйдет полное издание, разобрать их.
