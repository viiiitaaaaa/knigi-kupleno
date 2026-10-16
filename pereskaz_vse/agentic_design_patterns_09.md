<!-- NotebookLM (аккаунт Freya), Agentic Design Patterns (Gulli), приложения D–G и заключение; 16.10.2026; сверено — см. notebooklm/agentic_design_patterns_v_skilly.md -->
Ниже представлен подробный конспект приложений D, E, F и G, а также Заключения (Conclusion) книги Антонио Гулли **«Agentic Design Patterns»**.



## Appendix D. Building an Agent with AgentSpace / Приложение D. Создание агента с помощью AgentSpace



#### Главная мысль автора



AgentSpace представляет собой корпоративную платформу управления на базе ИИ («agent-driven enterprise»), которая объединяет разобщенные цифровые данные организации через граф знаний (Enterprise Knowledge Graph) и предоставляет графический no-code интерфейс (Agent Designer) для конструирования специализированных, контекстно-ориентированных ИИ-агентов.



#### Ключевые формулировки автора



1. *"AgentSpace is a platform designed to facilitate an 'agent-driven enterprise' by integrating artificial intelligence into daily workflows."* — «AgentSpace — это платформа, созданная для обеспечения "предприятия под управлением агентов" за счет интеграции искусственного интеллекта в ежедневные рабочие процессы.»

2. *"These agents are not merely chatbots; they can reason, plan, and execute multi-step actions autonomously."* — «Эти агенты — не просто чат-боты; они способны рассуждать, планировать и автономно выполнять многошаговые действия.»

3. *"This approach abstracts the underlying technical complexity, enabling the construction of specialized multi-agent systems without requiring deep programming expertise."* — «Этот подход абстрагирует базовую техническую сложность, позволяя создавать специализированные многоагентные системы без необходимости глубоких познаний в программировании.»



#### Overview / Обзор



##### Мысли автора по порядку



* AgentSpace обеспечивает единый семантический поиск по всему цифровому следствию организации (документы, emails, базы данных).

* Платформа использует продвинутые языковые модели (в частности, Google Gemini) для глубокого анализа и синтеза информации.

* Агенты системы способны проводить самостоятельные исследования, формировать отчеты с источниками и цитатами, а также генерировать аудио-резюме.

* В основе лежит выстраивание Enterprise Knowledge Graph для картирования связей между сотрудниками, документами и процессами.

* Конструктор Agent Designer позволяет создавать кастомных агентов без написания кода.



#### How to build an Agent with AgentSpace UI / Как создать агента через интерфейс AgentSpace UI



##### Мысли автора по порядку



* Доступ к AgentSpace осуществляется через панель Google Cloud Console во вкладке «AI Applications» (Fig. 1).

* Разработчик выбирает тип создаваемого приложения: «Search and assistant» (корпоративный поиск и ассистент на базе Gemini) или «Custom search (general)».

* **Подключение корпоративных сервисов:** агент может напрямую подключаться к Google Calendar, Google Mail, Workday, Jira, Outlook и ServiceNow (Fig. 2).

* **Галерея готовых промптов (Prompt Gallery / Fig. 3):**

  * goog_analyze_data (Analyze Data)

  * goog_book_time_off (Book Time Off)

  * goog_chat_with_content (Chat with Content)

  * goog_chat_with_documents (Chat with Documents)

  * goog_create_jira_ticket (Create Jira Ticket)

  * goog_deep_research (Deep Research)

  * goog_draft_email (Draft Email)

  * goog_explain_technical_documentation (Explain Technical Documentation)

  * goog_find_information (Find Information)

  * goog_generate_code (Generate Code)

  * goog_generate_image (Generate Image)

  * goog_generate_marketing_copy (Generate Marketing Copy)

  * goog_help_me_analyze (Analyze/Visualize Data)

* **Создание кастомного промпта (Customizing the Agent's Prompt / Fig. 4):**

  * Пользователь задаёт Name (write), Display name (writing assistant), Title (My personal writing assistant), Description (Help me to write concise sentences), Prompt type (User query) и базовый промпт: *"You are a writing assistant who helps me to write concise sentences"*.



##### Цифры, примеры и истории



* **Пример создания ассистента по письму:** Пользователь настраивает кастомный промпт с типом User query -> система сохраняет параметры -> агент автоматически активируется при старте нового сеанса для редактирования текста.



##### Номера рисунков и таблиц



* *Fig. 1:* How to use Google Cloud Console to access AgentSpace.

* *Fig. 2:* Connected services (Calendar, Mail, Workday, Jira, Outlook, ServiceNow).

* *Fig. 3:* Google's Gallery of Pre-assembled prompts.

* *Fig. 4:* Customizing the Agent's Prompt.



#### Advanced features & UI / Расширенные возможности и интерфейс пользователя



##### Мысли автора по порядку



* Подключение пользовательских хранилищ данных (Connected Data Stores).

* Интеграция с Google Cloud Knowledge Graph и Private Knowledge Graph (Fig. 5).

  * *Ограничение по времени:* Повторная генерация и индексация данных при включении Private Knowledge Graph может занимать до **24** часов.

* Предоставление веб-интерфейса для публикации агента в сети и встроенный модуль аналитики (Analytics).

* Итоговый диалоговый интерфейс Google AgentSpace (Fig. 6) с возможностью загрузки файлов и приветствием *"Hello, student"*.

* Для практического освоения доступен учебный модуль на Google Cloud Skills Boost: *"Build a Gen AI Agent with Agentspace"*.



##### Цифры, примеры и истории



* **24 часа** — время, необходимое для генерации данных в Private Knowledge Graph после его активации.



##### Номера рисунков и таблиц



* *Fig. 5:* AgentSpace advanced capabilities (Knowledge Graph configuration).

* *Fig. 6:* The AgentSpace User Interface for initiating a chat with your Agent.



#### Summary / Резюме приложения D



Приложение D посвящено платформе **AgentSpace** от Google. Автор описывает процесс создания ИИ-агентов без кода (no-code), интеграцию с корпоративными сервисами (Jira, Workday, Outlook), использование готовой галереи промптов, работу с графами знаний (Private Knowledge Graph с обновлением до 24 часов) и интерфейс взаимодействия с пользователем.



## Appendix E. AI Agents on the CLI / Приложение E. ИИ-агенты в CLI (командной строке)



#### Главная мысль автора



Командная строка разработчика трансформируется из простого шелла в интерактивное пространство совместной разработки с помощью автономных CLI-агентов, обладающих ментальной моделью репозитория, пониманием естественного языка и способностью выполнять многошаговые инженерные задачи.



#### Ключевые формулировки автора



1. *"The developer's command line, long a bastion of precise, imperative commands, is undergoing a profound transformation."* — «Командная строка разработчика, долгое время бывшая оплотом точных императивных команд, переживает глубокую трансформацию.»

2. *"These agents move beyond merely executing commands; they understand natural language, maintain context about your entire codebase, and can perform complex, multi-step tasks..."* — «Эти агенты выходят за рамки простого выполнения команд; они понимают естественный язык, удерживают контекст всей вашей кодовой базы и способны выполнять сложные многошаговые задачи...»

3. *"Proficiency in leveraging them will become an essential skill, fundamentally changing how developers build, debug, and manage software."* — «Мастерство в использовании этих инструментов станет ключевым навыком, фундаментально меняющим то, как разработчики создают, отлаживают и управляют программным обеспечением.»



#### Introduction / Введение



##### Мысли автора по порядку



* CLI-агенты выходят за рамки однострочных команд, формируя целостный контекст проекта.

* Главные различия между CLI-инструментами заключаются в точности, скорости и качестве выполнения сложных инженерных задач.



#### Claude CLI (Claude Code) / Claude CLI (Claude Code)



##### Мысли автора по порядку



* Высокоуровневый кодинг-агент от Anthropic с глубоким пониманием архитектуры проекта.

* Взаимодействует в стиле диалогового парного программирования, объясняя свои планы перед внесением правок.

* Содержит встроенные инструменты анализа структуры кода и интегрирован с системой Git.

* Поддерживает расширение через протокол MCP (Multi-tool Control Protocol) для обращения к приватным API и базам данных.



##### Цифры, примеры и истории



* **Пример 1 (Крупномасштабный рефакторинг):** Команда *"Refactor the entire codebase to use stateless JWTs..."* -> Claude вычитывает файлы репозитория, обновляет эндпоинты входа/выхода, мидлвары и логику обработки токенов на фронтенде.

* **Пример 2 (Интеграция API):** Подача OpenAPI-спецификации погодного сервиса -> Claude создает модуль обращения к API, UI-компонент и встраивает его в главный дашборд.

* **Пример 3 (Генерация документации):** Запрос *"Analyze the ./src/utils/data_processing.js file. Generate comprehensive TSDoc comments..."* -> Claude генерирует документацию TSDoc для каждой функции.



#### Gemini CLI / Gemini CLI



##### Мысли автора по порядку



* Универсальный открытый (open-source) CLI-агент от Google на базе модели Gemini 2.5 Pro с гигантским контекстным окном и мультимодальностью.

* Использует цикл "Reason and Act" (ReAct) и нативно интегрирован с Google Cloud.



##### Цифры, примеры и истории



* **Пример 1 (Мультимодальная разработка):** Вызов gemini describe component.png со скриншотом макета -> инструкция *"Write the HTML and CSS code to build a React component..."* -> Gemini генерирует адаптивный код компонента.

* **Пример 2 (Управление облаком):** Команда *"Find all GKE clusters in the production project that are running versions older than 1.28 and generate a gcloud command to upgrade them..."* -> Gemini находит кластеры старее версии **1.28** и формирует скрипт обновления через gcloud.

* **Пример 3 (Корпоративный MCP-инструмент):** Использование кастомного инструмента get-employee-details -id=E90210 -> извлечение данных сотрудника -> заполнение файла welcome_template.md.

* **Пример 4 (Масштабный рефакторинг Java):** Замена библиотеки org.apache.log4j на org.slf4j.Logger и LoggerFactory во всех .java файлах директории src/main/java с переписыванием вызовов .info(), .debug(), .error().



#### Aider / Aider



##### Мысли автора по порядку



* Открытый ассистент, работающий непосредственно в файлах проекта и создающий автоматические Git-комиты после успешного изменения.

* Не привязан к конкретной модели (model-agnostic) и идеален для разработки через тестирование (TDD).



##### Цифры, примеры и истории



* **Пример 1 (TDD):** Разработчик просит написать падающий тест для функции факториала -> Aider создает тест -> тест падает -> промпт *"Now, write the code to make the test pass"* -> Aider пишет код и подтверждает прохождение теста.

* **Пример 2 (Точное исправление багов):** Баг-репорт по ошибке функции calculate_total в billing.py в високосный год -> Aider добавляет файл в контекст, исправляет баг и прогоняет тесты.

* **Пример 3 (Обновление зависимостей):** Запрос на замену устаревших вызовов библиотеки requests -> Aider обновляет импорты во всех Python-файлах и актуализирует requirements.txt.



#### GitHub Copilot CLI / GitHub Copilot CLI



##### Мысли автора по порядку



* Расширение Copilot для терминала с глубокой интеграцией в инфраструктуру GitHub (автоматическое решение Issues и отправка Pull Request).



##### Цифры, примеры и истории



* **Пример 1 (Автоматическое решение тикетов):** Назначение тикета *"Issue #123: Fix off-by-one error in pagination"* -> Copilot создает ветку, пишет фикс и выставляет Pull Request без участия человека.

* **Пример 2 (Q&A по репозиторию):** Вопрос *"Where in this repository is the database connection logic defined...?"* -> Copilot выдает точные пути к файлам и переменным среды.

* **Пример 3 (Помощник CLI):** Запрос gh? find all files larger than 50MB, compress them, and place them in an archive folder -> генерация точной шелл-команды для файлов крупнее **50MB**.



#### Terminal-Bench: A Benchmark for AI Agents in Command-Line Interfaces / Terminal-Bench: Бенчмарк для ИИ-агентов в командной строке



##### Мысли автора по порядку



* Terminal-Bench — фреймворк оценки работы ИИ-агентов в текстовой изолированной среде CLI.

* Версия **Terminal-Bench-Core-v0** содержит **80** отобранных вручную задач из области науки и анализа данных.

* Для объективного тестирования языковых моделей создан стандартизированный тестовый агент Terminus.



##### Цифры, примеры и истории



* **80 задач** входят в начальный тестовый набор Terminal-Bench-Core-v0.



#### Summary / Резюме приложения E



Приложение E посвящено ИИ-агентам в командной строке (CLI). Автор сравнивает 4 ведущих инструмента: Claude CLI (архитектурный рефакторинг и MCP), Gemini CLI (мультимодальность, Gemini 2.5 Pro и Google Cloud), Aider (TDD и автоматические Git-комиты) и GitHub Copilot CLI (авто-создание PR по тикетам GitHub), а также описывает бенчмарк Terminal-Bench из 80 задач.



## Appendix F. Under the Hood / Приложение F. Под капотом — РАЗДЕЛ УДАЛЁН ПРИ СВЕРКЕ

> В нашем PDF приложения F нет: в оглавлении оно помечено как онлайн-материал, между E (стр. 399) и G (стр. 404) его страниц нет. NotebookLM сочинил весь раздел вместе с «дословными цитатами» (ни одной нет в книге). Удалено 16.10.2026, 4474 знаков.

## Appendix G. Coding Agents / Приложение G. Кодинг-агенты



#### Главная мысль автора



Переход от простого фрагментарного генератора кода («vibe coding») к структурированной гибридной команде из разработчика-оркестратора и специализированных ИИ-агентов (Scaffolder, Test Engineer, Documenter, Optimizer, Process Supervisor) позволяет кардинально повысить скорость и качество разработки в корпоративных условиях.



#### Ключевые формулировки автора



1. *"Vibe coding excels at brainstorming, but developing robust, scalable, and maintainable software demands a more structured approach..."* — «Vibe coding отлично подходит для мозгового штурма, но создание надежного, масштабируемого и сопровождаемого ПО требует более структурированного подхода...»

2. *"Over 30% of new code is now assisted or generated by our Gemini models, fundamentally changing our development velocity."* — «Более 30% нового кода в Google теперь создается с помощью или при содействии наших моделей Gemini, фундаментально меняя скорость разработки.»

3. *"The fundamental relationship has been redefined; it is no longer a contest of human versus machine, but a partnership between human ingenuity and AI..."* — «Фундаментальные отношения были переопределены; это больше не соперничество человека и машины, а партнерство человеческой изобретательности и ИИ...»



#### Vibe Coding: A Starting Point / Vibe Coding: Стартовая точка



##### Мысли автора по порядку



* **Vibe coding:** практика использования LLM для быстрого прототипирования, преодоления проблемы «чистого листа» и исследования незнакомых API.

* Подходит для идей и драфтов, но не обеспечивает архитектурную надежность и сопровождаемость кода без человеческого контроля.



#### Agents as Team Members & Foundational Principles / Агенты как члены команды и базовые принципы



##### Мысли автора по порядку



* Заявления лидеров индустрии: Сундар Пичаи (Alphabet/Google) и Сатья Наделла (Microsoft) заявили в начале **2025 года**, что **более 30%** нового кода в их компаниях генерируется или ассистируется ИИ-моделями (Gemini и Copilot).

* **3 базовых принципа человеко-агентной команды:**

  1. *Human-Led Orchestration (Человеческое оркестрование):* Разработчик выступает главным архитектором и тимлидом, принимающим итоговые решения.

  2. *The Primacy of Context (Приоритет контекста):* Тщательная подготовка полного брифа для агента (кодовая база, внешняя документация, спецификация задачи).

  3. *Direct Model Access (Прямой доступ к флагманским моделям):* Прямое использование сильнейших моделей (Gemini 2.5 Pro, Claude 4 Opus, OpenAI, DeepSeek) без урезания контекста.



##### Цифры, примеры и истории



* **30%** нового кода в Google и Microsoft создается ИИ-моделями в **2025 году** (заявления Сундара Пичаи и Сатьи Наделлы).



#### Core Components & Specialist Agents / Основные компоненты и специализированные агенты



##### Мысли автора по порядку



* **The Orchestrator (Human Developer):** человек-архитектор.

* **Context Staging Area:** временная директория (task-context/) с файлами целей (01_BRIEF.md), кодом (02_CODE/) и документацией.

* **Специализированные агенты (Specialist Agents / Fig. 1):**

  1. *The Scaffolder Agent (Implementer):* пишет новый код и фичи по брифу.

    * *Промпт:* *"You are a senior software engineer. Based on the requirements in 01_BRIEF.md and the existing patterns in 02_CODE/, implement the feature..."*

  2. *The Test Engineer Agent (Quality Guard):* пишет юнит- и интеграционные тесты (например, на pytest).

    * *Промпт:* *"You are a quality assurance engineer. For the code provided in 02_CODE/, write a full suite of unit tests using pytest..."*

  3. *The Documenter Agent (Scribe):* создает Markdown-документацию к API и классам.

    * *Промпт:* *"You are a technical writer. Generate markdown documentation for the API endpoints defined in the provided code..."*

  4. *The Optimizer Agent (Refactoring Partner):* находит узкие места производительности и проводит рефакторинг.

    * *Промпт:* *"Analyze the provided code for performance bottlenecks or areas that could be refactored for clarity..."*

  5. *The Process Agent (Code Supervisor):* выполняет двухэтапный анализ: *Critique* (поиск багов и нарушений стиля) -> *Reflection* (синтез и приоритезация самых критических замечаний).

    * *Промпт:* *"You are a principal engineer conducting a code review. First, perform a detailed critique... Second, reflect on your critique to provide a concise, prioritized summary..."*



##### Номера рисунков и таблиц



* *Fig. 1:* Coding Specialist Examples (Agent Scaffolder, Agent Test, Agent Documenter, Agent Optimizer, Agent Supervisor -> Human Developer -> Project Codebase -> Merge into Mainline).



#### Practical Implementation & Principles for Leading / Практическая реализация и принципы управления



##### Мысли автора по порядку



* **Чек-лист настройки (Setup Checklist):**

  1. Доступ к API минимум 2 флагманских моделей (Gemini 2.5 Pro и Claude 4 Opus).

  2. Инструмент оркестровки локального контекста (context.toml).

  3. Версионируемая библиотека промптов в Git (/prompts/ с файлами reviewer.md, tester.md и др.).

  4. Автоматизация через Git Hooks (например, pre-commit hook запускает Reviewer Agent перед комитом).

* **Принципы управления:** сохранение архитектурного владения, мастерство составления брифа, роль окончательного гейткипера качества и итеративный диалог с агентами.



#### Summary / Резюме приложения G



Приложение G посвящено кодинг-агентам. Автор противопоставляет хаотичный «vibe coding» структурированной концепции команды специализированных агентов (Scaffolder, Test Engineer, Documenter, Optimizer, Process Supervisor) под управлением человека-архитектора. Приводятся статистические данные Google и Microsoft (более 30% кода создается ИИ в 2025 г.) и детальный чек-лист внедрения Git-хуков и библиотеки промптов.



## Conclusion / Заключение



#### Главная мысль автора



Создание автономных ИИ-систем — это искусство построения сложной архитектуры на техническом холсте («technical canvas»), где 21 паттерн проектирования выступают в роли базовых кирпичиков, комбинирование которых позволяет переходить от реактивных чат-ботов к надёжным, целеориентированным и проактивным мультиагентным экосистемам будущего.



#### Ключевые формулировки автора



1. *"Building intelligent agents is akin to creating a complex work of art on a technical canvas..."* — «Создание интеллектуальных агентов подобно созданию сложного произведения искусства на техническом холсте...»

2. *"The true craft lies not in mastering a single pattern but in understanding their interplay—in seeing the canvas as a whole..."* — «Настоящее мастерство заключается не в освоении одного паттерна, а в понимании их взаимодействия — в видении холста как единого целого...»

3. *"The canvas is before you, the patterns are in your hands. Now, it is time to build."* — «Холст перед вами, паттерны в ваших руках. Теперь пришло время строить.»



#### Review of key agentic principles / Обзор ключевых агентских принципов



##### Мысли автора по порядку



* Все **21 паттерн** книги обобщаются в **4 фундаментальные категории** способности агентов:

  1. *Core Execution and Task Decomposition (Базовое исполнение и декомпозиция задач):* Prompt Chaining (последовательные шаги), Routing (условные ветвления), Parallelization (параллельное исполнение), Planning (многошаговая стратегия).

  2. *Interaction with the External Environment (Взаимодействие с внешней средой):* Tool Use / Function Calling (вызов внешних API и кода), Knowledge Retrieval / RAG (заземление на внешние базы знаний).

  3. *State, Learning, and Self-Improvement (Состояние, обучение и самоулучшение):* Memory Management (кратковременная и долговременная память), Reflection / Self-Correction (самокритика и исправление ошибок), Learning and Adaptation (эволюция поведения на основе опыта).

  4. *Collaboration and Communication (Взаимодействие и коммуникация):* Multi-Agent Collaboration (кооперация специализированных агентов), стандарты A2A и MCP (унификация обмена сообщениями и контекстом).



#### Combining Patterns for Complex Systems / Комбинирование паттернов для сложных систем



##### Мысли автора по порядку



* Настоящая сила агентского проектирования проявляется при объединении нескольких паттернов в единой системе.

* **Пример комбинирования 5 паттернов в ИИ-ассистенте исследований (Autonomous AI Research Assistant):**

  1. *Planning:* Агент-планировщик декомпозирует запрос *"Analyze the impact of quantum computing on cybersecurity"* на 4 шага (концепции квантовых вычислений, шифрование, угрозы, итоговый отчет).

  2. *Tool Use:* Каждый шаг запускает вызов инструментов поиска (Google Search, Vertex AI Search, ArXiv API).

  3. *Multi-Agent Collaboration:* Разделение труда между агентом-исследователем (сбор данных) и агентом-писателем (синтез отчета).

  4. *Reflection / Self-Correction:* Агент-критик проверяет черновик на логические ошибки и фактические неточности, отправляя его на доработку агенту-писателю.

  5. *Memory Management:* Система памяти хранит план, собранные факты, черновики и замечания на протяжении всего многошагового процесса.



##### Цифры, примеры и истории



* **Пример комбинации 5 паттернов:** ИИ-исследователь квантовой кибербезопасности (Planning + Tool Use + Multi-Agent Collaboration + Reflection + Memory Management).



#### Looking to the Future & Final Thoughts / Взгляд в будущее и заключительные мысли



##### Мысли автора по порядку



* **Тренды будущего:**

  * Переход от систем «Human-in-the-loop» (человек как пилот) к «Human-on-the-loop» (человек как супервайзер, задающий вектор автономным долгим задачам).

  * Стандартизация агентских экосистем и маркетплейсов на базе открытых протоколов MCP и A2A.

  * Появление каталогов открытых агентов (например, репозиторий Awesome Agents на GitHub).

  * Повышенные требования к паттернам безопасности (Safety Patterns), этическому выравниванию и устойчивости к джейлбрейкам.

* **Заключительный призыв:** Паттерны проектирования — это грамматика нового языка создания систем. Пришло время переходить от теории к практике и строить будущее под управлением агентов.



#### Summary / Резюме заключения



Заключение объединяет все **21 паттерн** книги в **4 категории** (исполнение, взаимодействие со средой, память/самоулучшение и коммуникация). Автор на примере ИИ-исследователя демонстрирует синергию комбинации 5 паттернов (Planning, Tool Use, Multi-Agent Collaboration, Reflection, Memory Management) и прогнозирует переход к экосистемам «Human-on-the-loop» на базе стандартов MCP и A2A.
