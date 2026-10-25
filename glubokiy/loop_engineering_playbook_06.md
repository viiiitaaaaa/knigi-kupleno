<!-- gpt-oss:120b (Hermes), глубокое чтение, loop_engineering_playbook_06.txt -->
## THE PRODUCT‑AGENT FIT TEST (стр. 240)  
- **Главная мысль** – Прежде чем начинать автоматизацию, проверьте, подходит ли задача под агентный продукт.  
- **Как делать**:  
  1. Оцените, повторяется ли задача достаточно часто, чтобы оправдать автоматизацию.  
  2. Определите, приемлема ли стоимость отказа агента.  
  3. Сформулируйте измеримый критерий «успеха».  
  4. Проверьте, будут ли пользователи доверять агенту в этой задаче.  
  5. Если хотя бы один ответ «нет» – пересмотрите область продукта.  
- **Где нам пригодится** – при формулировании первой гипотезы продукта‑агента, планировании MVP.

---

## USER EXPERIENCE PATTERNS FOR AGENT PRODUCTS (стр. 240‑242)  
- **Главная мысль** – UX‑паттерны для агентов должны учитывать недетерминированный вывод и переменный процесс.  
- **Как делать** (по классу `AgentUX`):  
  1. **render_progress** – показывать пользователю текущий шаг, количество завершённых шагов, оценку оставшегося времени, промежуточные результаты и текущие затраты.  
  2. **render_result** – прогрессивное раскрытие: сразу‑же «summary», «confidence», а детали (полный текст, источники, трассировка, стоимость) в раскрывающихся секциях; добавить кнопки‑действия (thumbs‑up/down, retry, export).  
  3. **handle_failure** – никогда не показывать сырые ошибки. Для `timeout` предлагать «Wait», «Get partial results», «Cancel». Для `low_confidence` предлагать «Accept», «Provide more context», «Request human review».  
- **Шаблоны и примеры** – JSON‑структуры, возвращаемые методами `render_progress`, `render_result`, `handle_failure`.  
- **Ошибки и предупреждения** – Показ сырых ошибок (см. анти‑паттерн ниже).  
- **Где пригодится** – построение UI‑интерфейса для любого LLM‑агента (веб‑приложения, чат‑боты).

---

## ANTI‑PATTERN: SHOWING RAW ERRORS TO USERS (стр. 242)  
- **Главная мысль** – Показ стек‑трейса или сообщения типа *“anthropic.APIError: 529 Overloaded”* разрушает доверие.  
- **Как делать** – реализовать глобальный обработчик исключений, который маппит каждый тип ошибки в человекочитаемое сообщение с конкретным «следующим шагом».  
- **Правила и числа** – *Never let a technical error escape the application boundary* (текст).  
- **Где пригодится** – любой продакшн‑агент, где пользователь может столкнуться с ошибками внешних API.

---

## THE FEEDBACK FLYWHEEL (стр. 242‑243)  
- **Главная мысль** – Замкнутый цикл «обратная связь → улучшение агента → удовлетворённые пользователи → больше обратной связи» – главный драйвер роста.  
- **Как делать**:  
  1. **collect_feedback** – сохранять `result_id`, оценку (thumbs up/down), категорию (accuracy, speed, format), комментарий, трассу и timestamp.  
  2. **analyze_weekly** – раз в неделю:  
     - отобрать отрицательную обратную связь за последние 7 дней;  
     - кластеризовать её по типу сбоя;  
     - если кластер ≥ 5 (повторяющаяся проблема) – автоматически создать eval‑тест (input = representative_input, expected = user_correction).  
  3. Возвратить метрики: общее количество обратной связи, satisfaction‑rate, топ‑3 проблемы, число созданных eval‑кейсов.  
- **Шаблоны** – Python‑класс `FeedbackFlywheel` (см. код).  
- **Ошибки** – Не собирать структуру обратной связи → нет возможности построить автотесты.  
- **Где пригодится** – при построении системы метрик и CI‑тестов для агента.

---

## SCORING WALKTHROUGH 18.3: SCALING FROM MVP TO PRODUCT (стр. 243)  
- **Главная мысль** – Чтобы перейти от 50 платных пользователей к 500, нужно работать над надёжностью, масштабированием и ростом.  
- **Три параллельных трека**:  
  1. **Reliability** – поднять success‑rate с 92 % до 98 % (анализировать 8 % провалов, сосредоточиться на 2‑3 типах документов, добавить fallback‑человек).  
  2. **Scale** – перейти от single‑tenant к multi‑tenant, добавить очередь (SQS/RabbitMQ) и кэширование повторяющихся клауз.  
  3. **Growth** – добавить free‑tier (3 док/мес), открыть API, командные функции.  
- **Метрики** – NPS, time‑to‑value, expansion‑revenue; таймлайн: 3 мес reliability + scale, потом 3 мес growth.  
- **Где пригодится** – планирование роста уже существующего SaaS‑агента.

---

## SCORING WALKTHROUGH 18.4: PRICING AN AGENT PRODUCT (стр. 244‑245)  
- **Главная мысль** – Цена должна базироваться на стоимости, которую пользователь экономит, а не только на себестоимости LLM.  
- **Пример расчёта**:  
  - LLM‑cost = $0.08/документ, infra = $0.02 → total = $0.10.  
  - Юрист тратит 30 минут × $300/час = $150 → ценность = $150.  
  - Тарифы: Free 5 док/мес (lead‑gen), Pro $49/мес → $0.49/док (50 % margin), Team $199/мес → $0.40/док, Enterprise custom.  
  - При $0.49/док margin = 80 % (прибыль $0.39), 500 Pro‑пользователей → $24 500 MRR.  
- **Где пригодится** – составление бизнес‑модели для любого LLM‑агента.

---

## EXERCISES (стр. 245)  
- **Список** (7 упражнений): Pricing Model, Feedback System, Incident Playbook, Onboarding Flow, Competitive Analysis, UX Prototype, Unit Economics.  
- **Где пригодится** – практические задания для закрепления концепций главы 18.

---

## CHAPTER 18 SUMMARY (стр. 246)  
- **Ключевые пункты**: 5 слоёв (UI, auth, billing, monitoring, feedback); цены — по ценности (gross‑margin > 80 %); цель — ≥ 98 % success‑rate перед масштабированием; feedback‑flywheel – главный ростовой двигатель; UX‑паттерны – показывать прогресс, прогрессивное раскрытие, никогда не показывать сырые ошибки; сначала MVP → проверка product‑agent fit, затем надёжность.  

---

## CHAPTER 19 – THE LOOP ENGINEER CAREER (стр. 247‑252)  

### LOOP ENGINEER CAREER OVERVIEW (стр. 247‑248)  
- **Главная мысль** – Специалисты по «loop engineering» (автономные LLM‑циклы) сейчас самые высокооплачиваемые в софт‑индустрии ($180K‑$400K).  
- **Роли**:  
  1. **L3/L4 Loop Engineer** — $180K‑$250K, реализует отдельные агенты.  
  2. **L5 Senior Loop Engineer** — $250K‑$320K, проектирует архитектуру агентов, отвечает за eval и observability.  
  3. **L6 Staff Loop Engineer** — $320K‑$400K+, задаёт направление платформы, менторит, работает с продуктом.  

### SKILLS ASSESSMENT MATRIX (стр. 248‑249)  
- **Три уровня**: core (LLM‑API, prompt‑engineering, ReAct, tool design, eval), intermediate (multi‑agent, memory, cost‑opt, observability, resilience), advanced (product‑arch, fine‑tuning, custom eval, multimodal, security).  

### PORTFOLIO PROJECT IDEAS (стр. 249‑250)  
- Примеры: Code Review Agent (intermediate, 2‑3 уикенда), Research Report Generator (intermediate, 2 уикенда), Multi‑Agent Content Pipeline (advanced, 3‑4 уикенда).  

### COMPANY TYPE & COMPENSATION (стр. 249‑250)  
- Таблица с типами компаний (AI‑startup, Scale‑up, Big‑tech, Enterprise, Consulting) и диапазонами зарплат.  

### SCORING WALKTHROUGH 19.1: PREPARING FOR A LOOP ENGINEER INTERVIEW (стр. 250‑251)  
- **Пять областей**: System design, Coding, Evaluation, Production, Product thinking.  
- **Подготовка** – практиковать whiteboard‑дизайн, реализовать ReAct за 30 минут, подготовить eval‑suite, знать реальные метрики (success‑rate, P95 latency, cost/run).  

### SCORING WALKTHROUGH 19.2: NEGOTIATING COMPENSATION (стр. 251‑252)  
- **Фреймворк оценки**: сравнить base‑salary с рынком, оценить опционы (strike, vesting, valuation), суммировать total‑comp, использовать леверные пункты (sign‑on, ускоренный vesting, title bump).  

### THE PORTFOLIO BEATS THE RESUME (стр. 252‑253)  
- **Главная мысль** – Демо‑проекты важнее дипломов. Нужно 2‑3 репозитория с ReAct, продакшн‑обработкой ошибок, cost‑optimisation и 5‑минутными видео‑демо.  

### THE LOOP ENGINEER INTERVIEW STRUCTURE (стр. 253‑254)  
| Раунд | Длительность | Что проверяется | Как готовиться |
|------|--------------|------------------|----------------|
| System Design | 45‑60 min | End‑to‑end архитектура | Спроектировать 5 разных систем |
| Coding | 45‑60 min | Реализация агента/инструмента | Реализовать ReAct за ≤ 30 мин |
| Evaluation | 30‑45 min | Тестирование и метрики | Знать eval‑framework, rubric |
| Production | 30‑45 min | Стоимость, observability, масштаб | Иметь реальные цифры (cost, latency, failure) |
| Product/Behavioral | 30‑45 min | Продуктовое мышление, коллаборация | 3‑4 STAR‑истории о проектах |  

### EXAMPLE 3: SYSTEM DESIGN INTERVIEW QUESTION (стр. 255‑256)  
- **Требования** (функциональные + нефункциональные) – 80 % Tier‑1 тикетов, эскалация, обучение, latency < 5 сек, cost < $0.10/тикет, accuracy > 95 %, uptime 99.9 %, масштаб 10 k конкр.  
- **Архитектура** – Intent classifier (Haiku), роутер (rule‑based), несколько resolver‑agents (FAQ, account, order, escalation), quality‑check (LLM‑as‑judge), feedback‑loop (thumbs + CSAT).  
- **Cost analysis** – per‑ticket $0.04‑$0.09 → $2‑4.5k/мес против $750k человеческих расходов.  

### PRODUCTION TIP (стр. 256)  
- Упомянуто: в интервью обязательно озвучивать cost‑analysis (пример выше).  

### CAREER PATHS & TRANSITIONS (стр. 257‑259)  
- Таблица переходов из разных ролей (Backend → Loop Engineer 2‑3 мес, ML → 1‑2 мес, Data → 3‑4 мес и т.д.).  

### CHAPTER 19 SUMMARY (стр. 256)  
- **Кратко**: высокая компенсация, 5‑слойный набор навыков, 5‑раундовое интервью, портфолио важнее резюме, быстрый переход из backend (2‑3 мес) и т.д.  

---

## CHAPTER 20 – YOUR 30‑DAY LOOP ENGINEERING PLAN (стр. 257‑272)  

### OVERVIEW (стр. 257‑259)  
- **Главная мысль** – За 30 дней построить минимум три работающих агента, портфолио и готовность к интервью/продукту.  

### WEEK 1 – FOUNDATION (Days 1‑7)  
**Шаги**:  
1. **Day 1** – установить Python 3.11+, создать venv, добавить API‑ключи, инициализировать Git‑репо `loop-engineering-portfolio`, установить `anthropic`, `openai`, `python‑dotenv`.  
2. **Day 2** – написать функцию, вызывающую один LLM‑tool (пример `calculate`). Проверить возврат результата.  
3. **Days 3‑4** – построить чистый ReAct‑агент (без фреймворков), подключить 3 инструмента (web‑search, calculator, file‑reader), протестировать 5 запросов.  
4. **Days 5‑6** – добавить `AgentTracer` (JSON‑trace с input, steps, output, cost, latency). Вывести читабельный вывод и сохранить в `traces/`.  
5. **Day 7** – написать README (описание, diagram, пример трассы, ограничения) и пуш в GitHub.  

### WEEK 2 – PATTERNS (Days 8‑14)  
- **Plan‑and‑Execute**: Добавить планировщик (Claude генерирует 3‑7‑шаговый план), исполнитель – текущий ReAct‑агент, реализовать replanning при конфликте. Тест: сравнение цен 3 облачных провайдеров.  
- **Eval Suite**: 10 тест‑кейсов (4 happy‑path, 3 edge, 2 adversarial, 1 regression). Две оценки – exact match и LLM‑as‑judge. Должно работать < 2 мин на каждый commit.  
- **Error Recovery & Cost Budgets**: декоратор `retry_with_backoff`, трекер бюджета $0.50/run, деградация – при падении поиска использовать знания модели с дисклеймером.  

### WEEK 3 – APPLICATION (Days 15‑21)  
- **Domain‑specific Agent** (выбирать один):  
  - **Option A – Coding Agent** (инструменты: read/write file, search_code, run_tests, git_diff). Тестировать 5 реальных багов, цель – исправить ≥ 3 из 5.  
  - **Option B – Research Agent** (web_search, read_page, calculate, cite_source). 5 вопросов, требующих синтеза из нескольких источников.  
  - **Option C – Data‑Analysis Agent** (query_csv, plot_chart, calculate, summarize). 5 вопросов к реальному набору данных.  
- **Multi‑Agent Pipeline** – собрать 2‑агентную цепочку (исследователь → писатель) и сравнить стоимость/качество с одиночным агентом.  
- **Cost Optimization** – внедрить роутинг моделей (Haiku для классификации, Sonnet для рассуждения), добавить `SemanticCache`; измерить снижение стоимости ≥ 40 % при падении качества < 5 %.  

### WEEK 4 – LAUNCH (Days 22‑30)  
- **Portfolio Polish** – улучшить README (diagrams, setup, eval table, cost analysis, demo‑link), убрать хард‑коды, исправить lint‑warnings, добавить type‑hints.  
- **Deploy Web App** – два варианта:  
  1. **Streamlit** (30 мин): `st.title`, `st.text_input`, `st.spinner`, `st.expander`, `st.metric`.  
  2. **FastAPI** (более «продакшн»).  
- **Publish Article** – 5‑пунктный пост (проблема, архитектурные решения, что сработало/не сработало, метрики, дальнейшие шаги).  
- **Network** – 10 контактов в агентных сообществах, 3 «глубоких» беседы.  
- **Launch** – отправка заявок (5 ролей) или внутренний питч с демо‑видео (5 мин), eval‑результат (85 % accuracy) и планом продакшна.  

### THIRTY‑DAY TRACKER (стр. 264)  
```json
{
  "week_1": ["ReAct agent", "3 tools", "Tracing", "README"],
  "week_2": ["Plan‑and‑Execute", "10‑case eval", "Error recovery", "Publish lib"],
  "week_3": ["Domain agent", "Multi‑agent pipeline", "Cost opt.", "Demo video"],
  "week_4": ["Polished portfolio", "Deployed app", "Article", "5 apps"]
}
```  

### SCORING WALKTHROUGH 20.1: PRIORITIZING THE 30‑DAY PLAN (стр. 265‑266)  
- **Если есть только 10 ч/нед** – оставить неизменные ядро: ReAct‑агент (Week 1) + eval‑suite (Week 2) + один доменный агент + демо‑видео (Week 3). Пропустить блог‑пост, Plan‑and‑Execute, multi‑agent, deployed web‑app.  

### SCORING WALKTHROUGH 20.2: CHOOSING YOUR DOMAIN AGENT (стр. 266‑267)  
- **Лучший выбор** – Coding Agent (универсален, демонстрирует весь стек навыков). Второй – Research Agent. Не выбирать творческие или бизнес‑процессы‑агенты без доступа к корпоративным данным.  

### BEYOND DAY 30 – GOING PRO (Weeks 5‑8) (стр. 267‑272)  
- **Week 5** – Production hardening: logging (`AgentTracer`), retry/fallback, budget guard, health‑check endpoint (uptime, success‑rate, avg‑cost, runs/24h). Deploy FastAPI.  
- **Week 6** – Multi‑Agent Architecture: supervisor‑worker, четкое разделение границ, синхронизация.  
- **Week 7** – Comprehensive eval (≥ 50 кейсов, 5 категорий). CI/CD запускает eval после каждого коммита, поддерживается leaderboard. Требование: агент должен быть минимум в 2× лучше baseline.  
- **Week 8** – Ship real‑world product (Slack‑bot, PR‑review CLI, отчетный веб‑app, браузер‑расширение). Протестировать на ≥ 5 реальных пользователях, собрать обратную связь.  

### CHAPTER 20 SUMMARY (стр. 272)  
- **Кратко** – План из 4 недель (ReAct‑agent, eval‑suite, доменный агент, демо‑видео, полировка) + 4‑недельный «Going Pro»‑этап (hardening, multi‑agent, полный eval, реальный продукт). Пять обязательных портфолио‑элементов (custom ReAct, eval > 50, продакшн‑деплой, cost‑analysis, 5‑мин видео). При нехватке времени – приоритет построения, а не чтения, и coding‑agent над другими доменами.

---

## APPENDIX A – FIVE FRAMEWORKS (стр. 273‑276)  

| Фреймворк | Краткое описание | Лучшее применение |
|-----------|------------------|-------------------|
| **LOOP** | Listen → Orchestrate → Observe → Perfect – цикл качества, подходит для одиночных задач (исследование, написание, анализ). | Одноагентные задачи, требующие высокой точности. |
| **AGENT** | Assess → Navigate → Generate → Execute → Track – ориентирован на реальное действие и измерения. | Многошаговые бизнес‑процессы, автоматизация, деплой. |
| **CHAIN** | Chunk → Hypothesize → Act → Inspect → Next – разбиение на части, проверка каждой. | Сложные задачи, требующие декомпозиции (debug, data‑analysis). |
| **REFINE** | Review → Evaluate → Fix → Iterate → Narrow → Export – цикл улучшения качества. | Редактирование, code‑review, оптимизация. |
| **SCALE** | Separate → Cache → Async → Log → Evaluate – инфраструктурный слой для продакшна. | Масштабирование агентных систем, DevOps, платформенный уровень. |

---

## APPENDIX B – 100 AGENT DESIGN PATTERNS (стр. 277‑281)  

### Категория 1: Loop Control (паттерны 1‑15)  
- **Примеры**: Bounded Loop (контроль стоимости), Early Exit (прекращение при достижении цели), Cost Circuit Breaker (лимит расходов), Convergence Check (остановка при убывающем возврате), Oscillation Detector (избегает зацикливания), Backoff Loop (смягчение ошибок), Priority Loop (максимизирует эффект), Checkpoint Loop (восстановление после сбоя), Timeout Guard (ограничение wall‑clock), Nested Loop (изолирует бюджеты подзадач), Parallel Loop (параллельные подзадачи, ускорение 60‑80 %), Conditional Loop (оптимизация стоимости по сложности), Warmup Loop (калибровка модели), Cooldown Loop (поймать последние ошибки), Adaptive Step Limit (подгонка длины цикла).  

### Категория 2: Tool Use (паттерны 16‑30)  
- **Ключевые**: Tool Router (экономит 50‑70 % при выборе инструмента), Tool Fallback (обработка падений), Tool Composition (уменьшает LLM‑шаги), Tool Validation (раннее отлов 80 % ошибок), Tool Caching (сокращает 15‑30 % повторов), Rate Limiter (избегает бана), Sandboxing (изоляция риска), Discovery (масштаб к сотням инструментов), Doc Injection (уменьшает prompt 40‑60 %), Read‑Only First (защита от перезаписи), Idempotent Tools (безопасные повторы), Versioning, Health Check, Result Summarization, Confirmation Tool.  

### Категория 3: Memory (паттерны 31‑45)  
- **Кратко**: Sliding Window (простая контекст‑управляемость), Landmark Memory (ключевые решения), Semantic Recall (поиск релевантного контекста), Memory Compression (экономия 60‑80 % при превышении лимита), Episodic Memory (использование прошлых траекторий), Working Memory Buffer (изолирует промежуточные расчёты), Preference Store (персонализация), Fact Cache (избегает повторной верификации фактов), Context Budget (баланс источников), Memory Eviction (оставляет ценные записи), Shared Memory (координация агентов), Memory Versioning (отладка через воспроизведение), Structured State (избавление от интерпретаций), State Validation (защита от коррумпирования), Rollback State (восстановление после ошибок).  

### Категория 4: Multi‑Agent (паттерны 46‑60)  
- **Ключевые**: Supervisor (централизованная делегия), Pipeline (последовательный поток), Debate (снижение предвзятости), Ensemble (голосование), Specialist Routing (подбор лучшего агента), Reviewer‑Writer (итеративное улучшение), Hierarchical Delegation (многоуровневая декомпозиция), Blackboard (асинхронный совместный доступ), Auction (распределение ресурсов), Consensus (предотвращение одиночных ошибок), Agent Pool (эластичное масштабирование), Lifecycle (контроль «зомби‑агентов»), Message Bus (декуплинг), Role Rotation (тест robustness).  

### Категория 5: Quality & Safety (паттерны 61‑75)  
- **Кратко**: Self‑Critique (ловит 10‑20 % ошибок), Rubric Scoring (квантитативный порог), Adversarial Check (поиск уязвимостей), Citation Verification (удаляет неподтверждённые утверждения), Output Validation (схема‑контроль JSON), Guardrails (политика), Consistency Check (противоречия), Confidence Scoring (маршрутизация низко‑уверенных ответов).  

- **Где пригодится** – При проектировании любого LLM‑агента: выбирайте паттерн из соответствующей категории, ориентируясь на «When to Use» (стр. 277‑281).  

--- 

**Итого для Claude** – Эта часть книги предоставляет практический набор инструментов и методик: проверка product‑agent fit, UX‑паттерны, обратная связь, сценарии масштабирования и ценообразования, карьерный путь Loop Engineer, подробный 30‑дневный план построения портфолио, а также готовый набор 5 фреймворков и более 100 конкретных паттернов. Всё это можно сразу применять в работе единственного предпринимателя‑разработчика: от быстрой прототипизации (Day 1‑2) до построения продакшн‑сервиса, оценки стоимости и подготовки к интервью.
