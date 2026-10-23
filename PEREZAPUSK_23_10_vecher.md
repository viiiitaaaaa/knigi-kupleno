# Где остановились (23.10.2026 поздно вечером, перезапуск вкладки «Тесты книг: продолжение»)
Читать после PEREZAPUSK_23_10.md. Память: perplexity-knigi-stop-na-hall, mom-test-/voss-/klaff-/weiss-/hall-30-situacij-perplexity, ne-dublirovat-platnyy-zapros.

## Сделано (всё закоммичено, последний коммит ac402cb)
- Perplexity (глубокое исследование) по 5 книгам, по 30 ситуаций: perplexity_knigi\01_mom_test … 05_hall.md. Серия ОСТАНОВЛЕНА её словом на Hall.
- Порядок работы: ответ → `razlozhit_perplexity.py` → 3 проверяющих сверяют ключ с книгой + ищут дыры карточки → дополнить карточку → 3 исполнителя вслепую → судья → правило → повтор.
- Папки: retest_23_10_p (Mom Test), _v (Voss), _k (Klaff), _w (Weiss), _h (Hall); внутри vhod/otvety/otvety_r2/sud (ключ сверенный klyuch_*_sverennyy.md, ITOG_*.md, ITOG_*_r2.md).
- Счёт (по сверенному ключу): первый прогон Mom Test 25, Voss 25, Klaff 28, Weiss 29, Hall 27; повтор правил 29–34: 29, 26, 29, 28, 29. Хвост старых тестов (retest_23_10\sud3\ITOG_hvost.md): Voss 6/6, Weiss 4/6, Co-Intelligence 5/6 = 15/18.
- Правила: dogovorennosti\references\retest_2310_pravila.md (25–41), love-scripts\references\retest_2310_pravila.md (34–35). Карточки дополнены: karty\voss, klaff, weiss (dogovorennosti), karty\hall_nlp (love-scripts). Бэкапы старых карточек в retest_23_10_<код>\02_priyomy.md.bak.
- Расход: вкладка ≈ 3,8% недельного расхода на 18:43 (Sonnet), ещё +2–3% после; отдельно 5 запросов Perplexity.

## Не сделано / по её слову
- Perplexity-книги дальше (Challenger, SPIN, Колотилов, Obviously Awesome, Co-Intelligence) — ТОЛЬКО по её новому слову.
- Предложены судьи Gemini (нужен API-ключ в .env или через сайт) и Hermes (бесплатный; лёгкие формальные проверки): сравнить с Sonnet «совпало N из 30», расхождения — проверяльщику по тексту книги. Её ответ про ключ Gemini не получен.
- Правила 35–41 полным набором не перепроверены; нужны СВЕЖИЕ ситуации (те же 30 уже «знают» правила).
- Voss самый слабый (26/30): ложные «в книге нет» и схема Аккермана.
- Приёмник текста Perplexity: scratchpad\recv.py (порт 8765; старый процесс убивать перед новым). Ответ Perplexity дорисовывается долго после «Завершено» — ждать, пока длина текста перестанет расти, прокручивать страницу.
