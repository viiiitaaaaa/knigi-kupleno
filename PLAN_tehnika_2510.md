# План «Учим Claude — только техника» (25.10.2026, её уточнение)

Её слова: «Пока что только техническая часть — без лекций по ОКР, по любви, по психологии. То, что касается полностью только меня, отбрасываешь. Рассматриваешь только материалы, которые касаются и тебя, и меня. Про работу тоже не надо» + «работа» = поиск работы/вакансии (резюме, отклики, найм, скиллы про вакансии). Продажи/переговоры не исключены — решать по смыслу: техническое и общее для обеих берём.

Готово = по каждой книге: прочитана ЦЕЛИКОМ (по главам, не выжимкой), «как делать» стоит в скилле/CLAUDE.md с триггером, независимая проверка (агент proverka), в таблице «книга · глав прочитано N из M · где стоит · тест N из M · что не дочитано».

## БЕРЁМ (порядок)
1. 09 ИИ/агенты/Claude — 14 шт: Huyen «AI Engineering», Gulli «Agentic Design Patterns», Hur–Song «Build an AI Agent», Albada, Lanham, Koenigstein, Mendelevitch «Hands-On RAG», Polzer «RAG Cookbook», «0→1 Loop Playbook», Mollick «Co-Intelligence», Prediction Machines, реферат «ИИ-агенты». (Мукминов, Dickey — уже целиком, скиллы стоят.)
2. 10 IT — 3 шт: Newman «Resilient Distributed Systems», OpenVPN Cookbook, Mastering OpenVPN (нужны к «свой VPN»).
3. 07 Аналитика — 6 шт: Lean Analytics, Minto Pyramid, Storytelling with Data, реферат А/Б-тестов (как проверять и излагать цифры).
4. 11 Обучение/память — 7 шт: Make It Stick, Ultralearning, Peak, Mind for Numbers, Second Brain, Moonwalking, Fluent Forever — только «как мне учить её и как вести память/заметки»; Fluent Forever (языки) — позже вместе с английским.
5. 05 Продажи/переговоры — Voss, Challenger, Mom Test, SPIN, Klaff, Weiss, Persuasion, Колотилов B2B — общее для нас (переговоры по её делам и клиентам). LinkedIn Sales — по смыслу (если про поиск работы — отложить).

## ОТЛОЖЕНО (по её слову, не открывать)
- 12 Психология/НЛП/ОКР/привязанность (в т.ч. Эkman, NLP-книги) и корневые книги про отношения (папка «Загрузки»-подборка Gibson, Levine, Johnson и т.д.).
- Всё про поиск работы: скилл vakansii-ssha, резюме, отклики, английский для собеседований.
- 13 Финансы, 14 Английский, 15 Тело — личное.
- 01–04, 06, 08 (маркетинг, магазин, бренд, бизнес) — не техника; по её слову позже. Shopify/дропшиппинг — не трогаем и так.

## Метод
Книги — NotebookLM/Gemini-ключ (🟡 разрешено 25.10) по главам с номерами страниц; помощники Sonnet/Haiku; проверяльщик отдельно. Перед стартом — назвать ей числа (страницы × слова × 1,3; для русского ×2–2,5; время ×3) и ждать «да».

## Правило 25.10: Ollama/Hermes сама не вызываю, ТОЛЬКО по её вызову. В этой вкладке она САМА вызвала (сказала «Hermes есть» и дала ключ в .env) — чтение через hermes_glubokiy.py разрешено ею; остановила я по ошибке, возобновлено.
## Её слово 25.10 (по скрину Рабочего стола, ollama launch claude): модели GLM, Kimi, DeepSeek заняты её кредитами/планом — НЕ рассматривать и не вызывать. Брать из остальных: gemma4:31b, gpt-oss, nemotron. Kimi по ключам Free закрыта (402).

## Состояние на «споки» 25.10.2026 ночью
- Конспекты по главам (блоки 1, 3, 4): glubokiy\ — 266 из 266 содержательных кусков (Gemini 18, gpt-oss/Hermes ~140, gemma4:31b остальное); moonwalking_einstein_13 — указатель, пропущен. Сверка: sverka.py «266 из 266».
- Установлены скиллы (7, все проверены proverka, с книгой НЕ сверены): lanham-ai-agents, ultralearning, agentic-design-patterns, hur-song-build-ai-agent, albada-ai-agents, second-brain, huyen-ai-engineering. Черновики — skill_chernovik_glubokiy\.
- Осталось 11 книг без скилла (конспекты готовы): Koenigstein, rag_production, rag_python_cookbook, co_intelligence, prediction_machines, loop_engineering_playbook, lean_analytics, minto_pyramid, storytelling_data_makeovers, make_it_stick, peak_ericsson, a_mind_for_numbers, moonwalking_einstein. Ждёт её «давай» (расход лимита Claude ~120–200 тыс. токенов на книгу; /usage — смотрит она).
- Ключи Ollama (2 шт.) — в .env (вне git). Kimi/GLM/DeepSeek — её слово: не использовать; Kimi по ключам Free закрыта (402).
- Задания помощникам — ZADANIE_skill_*.md, ZADANIE_huyen_part*.md. Скрипты: gemini_glubokiy.py, hermes_glubokiy.py (--cloud --model --keyvar --rev).
