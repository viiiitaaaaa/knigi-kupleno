# Книги 14.10.2026 — что осталось (для новой сессии)

«Готово» = 6 конспектов в `~\.claude\skills\knowledge-library\references\knigi\novye13\<slug>.md` → razlozhit → панель → GitHub → выжимка в kak-uchitsya.

1. Hermes: пересказ `txt13\pereskaz\<slug>_NN.md` для peak_ericsson, moonwalking_einstein, second_brain, fluent_forever,
   ai_engineering, resilient_distributed (лог hermes_14_10c.log). Проверить: `ls txt13/pereskaz/<slug>_*.md` против `txt13/chunks/<slug>_*.txt`.
   Если не доделан (сессия закрыта) — `python hermes_pereskaz.py --only <slug> --par 3` (готовые куски пропускает).
2. Помощники Sonnet по ZADANIE_13_10.md, как 14.10 (промпты — в этой сессии: «Конспект Ultralearning» и др.):
   - 4 книги об обучении → главный скилл `kak-uchitsya`, плюс `dogovorennosti`, `love-scripts`; подзаголовок «### Как ей учиться и запоминать» первым.
     Peak — осознанная практика; Moonwalking — дворец памяти, мнемоника; Second Brain — CODE/PARA для наших скиллов и памяти; Fluent Forever — языки, карточки.
   - ai_engineering (Huyen) и resilient_distributed (Newman) → claude-code-priemy, hermes, kursy-konspekty, writing-for-agents, tg-news, trend-radar, b2b-sbor.
   Названия книг в razlozhit_dop.py BOOK уже добавлены.
3. `python razlozhit_dop.py novye13` → `tg_monitor\build_books.py` → `news.py --build` → `ARTMELLIO_SKILLS\sync_skills.ps1`.
4. Дописать «Главное» в `kak-uchitsya\SKILL.md` по Peak, Moonwalking, Second Brain, Fluent Forever; запись в память kuplennye-knigi.
5. Табло: `agent_status.py done knigi1410b`.

- 14.10: пересказ Hermes по всем 6 книгам ГОТОВ — шаг 1 пропустить.
- 14.10 вечером: ВСЁ СДЕЛАНО (шаги 2–5).
