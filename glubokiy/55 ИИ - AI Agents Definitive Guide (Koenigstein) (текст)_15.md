<!-- gpt-oss:120b (Hermes), глубокое чтение, 55 ИИ - AI Agents Definitive Guide (Koenigstein) (текст)_15.txt -->
**Часть 15 из 21 книги «55 ИИ – AI Agents Definitive Guide (Koenigstein)»**  
*Содержание представлено в виде терминов‑разделов, сгруппированных под буквенными заголовками. Ниже – конспект по каждому термину. Если в тексте нет подробных описаний, указано « данные отсутствуют ».  

---

## C  

### cache eviction (стр. —)  
- **Главная мысль** – управление удалением (выбрасыванием) элементов из кэша при инференсе модели.  
- **Как делать** – данных нет.  
- **Правила и числа** – нет.  
- **Шаблоны и примеры** – нет.  
- **Ошибки и предупреждения** – нет.  
- **Где нам пригодится** – оптимизация инференс‑бекендов, уменьшение задержек холодных стартов.  

### cache hit ratio (стр. —)  
- **Главная мысль** – показатель, сколько запросов обслуживается из кэша (отношение «хитов» к общему числу запросов).  
- **Как делать** – данных нет.  
- **Где нам пригодится** – измерение эффективности KV‑кеширования.  

### cache invalidation (стр. —)  
- **Главная мысль** – процесс снятия устаревших данных из кэша, упомянут в контексте KV‑caching и Inference Backends.  
- **Где нам пригодится** – поддержание актуальности кэшей при изменении модели/данных.  

### cache pollution (стр. —)  
- **Главная мысль** – загрязнение кэша недостоверными/ненужными записями; связано с Memoizing Agentic State Transitions.  

### cache time to live (TTL) (стр. —)  
- **Главная мысль** – ограничение времени жизни записи в кэше.  

### cache‑first execution (стр. —)  
- **Главная мысль** – стратегия выполнения, при которой сначала пытаются использовать кэшированные результаты.  

### calls per request (стр. —)  
- **Главная мысль** – количество вызовов, совершённых агентом в рамках одного запроса; упомянуто в Agentic Cost Multiplier.  

### canonical fact keys (стр. —)  
- **Главная мысль** – стандартные (канонические) ключи фактов, используемые при мемоизации состояний агента.  

### canonicalization (стр. —)  
- **Главная мысль** – процесс приведения данных к канонической (универсальной) форме; упомянуто в Runtime Isolation with Docker и The Need for a Fallback Guy.  

### capability escalation (стр. —)  
- **Главная мысль** – повышение возможностей агента (например, через инструменты), рассматривается в Tool Governance.  

### cascading agent failures (стр. —)  
- **Главная мысль** – последовательный сбой нескольких агентов; тема Early Threat Testing.  

### catastrophic forgetting (стр. —)  
- **Главная мысль** – потеря ранее выученных знаний при дообучении; упомянуто в контексте LoRA и Adapters.  

### category caps (стр. —)  
- **Главная мысль** – ограничения (лимиты) по категориям, обсуждаются в System‑Level Defense for Your Agents.  

### causal attention (стр. —)  
- **Главная мысль** – тип внимания в Decoder‑Only Models.  

### chain of thought (CoT) (стр. —)  
- **Главная мысль** – метод «размышления в слух» LLM‑агентов; упомянут в нескольких разделах (Letting Your AI Agents Think Out Loud, Generating a Tree of Possibilities, How to Make Your Agent Take Action and Reflect).  

### checkpointing (стр. —)  
- **Главная мысль** – создание точек восстановления; включено в Hardening the Backbone и Procedural Memory.  

#### as core infrastructure pattern (стр. —)  
- **Главная мысль** – чекпоинтинг как фундаментальная инфраструктурная практика.  

#### encrypted serialization (стр. —)  
- **Главная мысль** – шифрование при сериализации данных (Procedural Memory).  

#### forking and replaying (стр. —)  
- **Главная мысль** – форк и воспроизведение состояний, часть Short‑Term Memory and Time Travel.  

#### history markers in subgraphs (стр. —)  
- **Главная мысль** – метки истории внутри подграфов; используется при Mapping FSM/HSM to Agent Frameworks.  

#### implementation and crash recovery (стр. —)  
- **Главная мысль** – реализация и восстановление после падения, см. Hardening the Backbone.  

#### nested subgraph modes (стр. —)  
- **Главная мысль** – вложенные режимы подграфов; относится к Memory Topology в Multi‑Agent Systems.  

#### restoring prior messages per turn (стр. —)  
- **Главная мысль** – восстановление предыдущих сообщений в каждом разговорном обороте; связано с Giving the LLM a State.  

#### short‑term state persistence (стр. —) – то же, что выше.  

#### at state boundaries in FSMs (стр. —) – важность границ состояний в конечных автоматах.  

### checks (стр. —) – набор проверок в разных контекстах.  

#### agent alignment (стр. —) – проверка соответствия целей агента (System‑Level Defense).  

#### deterministic (стр. —) – детерминированные проверки (From Production Traces to Custom Benchmarks).  

#### LLM‑based (стр. —) – проверки, основанные на LLM (из того же раздела).  

#### rule (стр. —) – правило в Behavioral Stress Testing: Role Playing with Your Agents.  

#### trace‑level (стр. —) – проверка на уровне трасс (From Production Traces to Custom Benchmarks).  

### chunked prefill (стр. —) – предзаполнение кэша кусками, важный аспект KV‑caching.  

### CIA (confidentiality, integrity, and availability) (стр. —) – базовая модель безопасности (Extending Threat Modeling to Agent Systems, Red Teaming Your Agents).  

### circuit breakers (стр. —) – «прерыватели цепи», применяются в Deploying Agents in Real Products и Hardening the Backbone.  

### Clarke, Arthur C. (стр. —) – упомянут в контексте Advanced Planning, Reasoning, and Scalable Execution in Agents.  

### classical IT security (стр. —) – традиционная ИТ‑безопасность в модели угроз агентных систем.  

### closed models versus open source models (стр. —) – сравнение закрытых и открытых моделей (Open Versus Closed Models).  

### cloud‑based coding sandboxes (стр. —) – изолированные среды разработки в облаке.  

### code agents (стр. —) – агенты, генерирующие/исполняющие код; упомянуты в гибридных наградах.  

### code execution (стр. —) – запуск кода, требуется sandboxing (Safeguarding Programmatic Tool Calling).  

### code mode (стр. —) – режим работы с кодом (Safeguarding Programmatic Tool Calling).  

### CodeModeToolset (стр. —) – набор инструментов для режима кода.  

### CodeShield (стр. —) – система защиты кода (System‑Level Defense).  

### coding sandboxes in cloud (стр. —) – повторение темы облачных песочниц.  

### coding‑agent benchmarks (стр. —) – Bench‑бенчмарк для репозитория (Turn Your Repo into a Benchmarkable Environment).  

### cold starts (стр. —) – «холодный старт» в инференс‑бекендах; важен для быстрого отклика.  

### Command objects (стр. —) – объекты‑команды, используемые в Giving the LLM a State и Designing Human‑in‑the‑Loop Workflows.  

### compaction of semantic memory (стр. —) – сжатие семантической памяти (Memory Hygiene).  

### compliance (стр. —) – соответствие требованиям (Open Versus Closed Models).  

### Composio (стр. —) – инструмент для обнаружения MCP‑серверов агентами.  

### compositional risk (стр. —) – риск, связанный с составными компонентами (System‑Level Defense).  

### compression of memory entries (стр. —) – сжатие записей памяти (Memory Hygiene).  

### concurrency safety for MCP tool calls (стр. —) – безопасность параллельных вызовов MCP‑инструментов.  

### concurrency (стр. —) – управление конкуренцией, упомянуто в контексте семафоров (Behavioral Stress Testing).  

### conditional computation (стр. —) – условные вычисления в Mixture‑of‑Experts Models.  

### confidentiality, integrity, and availability (CIA) (стр. —) – дублирование модели безопасности.  

### conflicting evidence (стр. —) – конфликтные данные в синтезе (Memoizing Agentic State Transitions).  

### constrained decoding (стр. —) – ограниченный декодинг, рассматривается в The Need for a Fallback Guy.  

### CONT nodes (стр. —) – узлы CONT в Adaptive Branching Monte Carlo Tree Search (AB‑MCTS).  

### contained agents (стр. —) – агенты, работающие в ограниченной среде (Early Threat Testing).  

### containment (стр. —) – изоляция выполнения и управления инструментами (Safeguarding Programmatic Tool Calling).  

### context bloat (стр. —) – «разрастание» контекста, проблема в Deep Agents и Memory Topology.  

### context engineering (стр. —) – инженерия контекста, важна для KV‑caching.  

### context guards (стр. —) – «охранники» контекста (Memoizing Agentic State Transitions).  

### context isolation (стр. —) – изоляция контекста в памяти многопользовательских систем.  

### context janitor (стр. —) – «уборщик» контекста, упомянут в Hardening the Backbone.  

### context poisoning (стр. —) – «отравление» контекста, рассматривается в Early Threat Testing.  

### context pruning (стр. —) – удаление лишнего контекста, тоже в Hardening the Backbone.  

### continuous batching (стр. —) – непрерывная пакетная обработка, относится к KV‑caching и расчёту памяти.  

### continuous improvement loop (стр. —) – цикл постоянного улучшения (Customized and Advanced Evaluation of Agentic Systems).  

### continuous multi‑adapter batching (стр. —) – пакетирование с несколькими адаптерами (LoRA и Adapters).  

### contracts (стр. —) – контракты, управляющие данными и инструментами.  

#### in agent lifecycle (стр. —) – контракты в жизненном цикле агента (From Prototypes to Production).  

#### Instructor library (стр. —) – библиотека Instructor (Thinking at the Failure Level).  

#### need for (стр. —) – необходимость контракта для правильного управления данными/выводом LLM.  

#### as organizational analogy (стр. —) – сравнение контрактов с организационными аналогиями.  

#### Pydantic (стр. —) – валидация данных и handoff'ов (Keeping Costs in Check).  

#### satisfied yet system compromised (стр. —) – ситуация, когда система кажется удовлетворённой, но уже скомпрометирована (Understanding the AI Agent Threat Landscape).  

#### typed tool contracts in MCP (стр. —) – типизированные контракты для MCP‑инструментов.  

#### validating data and handoffs (стр. —) – проверка данных и переадресаций (Pydantic).  

### contradiction control in memory (стр. —) – контроль противоречий в памяти (Memory Hygiene).  

### control flow (стр. —) – управление потоками в агентных системах.  

#### in agentic systems (стр. —) – базовый контроль в динамических агентах (Foundations).  

#### combined in Command objects (стр. —) – объединение управления в объектах‑командах.  

#### encoded by graph edges (стр. —) – кодирование потока через ребра графа (How to Make Your Agent Take Action and Reflect).  

#### in generated programs (стр. —) – контроль в сгенерированных программах (Safeguarding Programmatic Tool Calling).  

#### in LangGraph primitives (стр. —) – управление в примитивах LangGraph (Giving the LLM a State).  

#### state‑machine patterns explaining (стр. —) – паттерны конечных автоматов (Finite and Hierarchical State Machines).  

### conversation compaction (стр. —) – сжатие диалогов (Hardening the Backbone).  

### conversation history (стр. —) – история беседы, важна в инференс‑бекендах и памяти.  

### correction loops (стр. —) – петли корректировки (Instructor: Thinking at the Failure Level).  

### cost (стр. —) – стоимость систем и её управление.  

#### agentic cost multiplier (стр. —) – коэффициент увеличения стоимости при многократных вызовах (Agentic Cost Multiplier).  

##### infrastructure importance (стр. —)  

- **calculating memory footprint** – расчёт потребления памяти конкретной модели (Calculating the Memory Footprint for a Specific Model).  
- **FlashAttention** – технология ускорения внимания (FlashAttention: Designing for Asymmetric Hardware Scaling).  

#### managing (стр. —) – управление затратами через валидацию Pydantic.  

#### memoizing agentic state transitions (стр. —) – мемоизация переходов агента (Progress‑Aware Synthesis).  

#### of open and closed models (стр. —) – сравнение открытых и закрытых моделей (Open Versus Closed Models).  

#### overview of (стр. —) – обзор от вычислений к затратам (Designing Efficient Agentic Systems).  

#### single‑call estimates (стр. —) – оценка стоимости одного вызова (Agentic Cost Multiplier).  

### CoT (chain of thought) (стр. —) – см. chain of thought выше.  

### countdown tasks (стр. —) – задачи со счётчиком.  

#### hybrid‑reward training example (стр. —) – пример обучения гибридным вознаграждением (The ART of Learning from Experience).  

#### programmatic reward suitability (стр. —) – пригодность программных вознаграждений (Beyond Isolation).  

### crash recovery (стр. —) – восстановление после падения (Hardening the Backbone).  

### create_handoff_tool (стр. —) – создание инструмента передачи (Developing a Swarm of Agents).  

### create_react_agent (стр. —) – создание реактивного агента (Building a Hierarchical Research Team).  

### create_swarm function (стр. —) – функция создания роя (Developing a Swarm of Agents).  

### CrewAI (стр. —) – агентский фреймворк, использующий конечные автоматы (Finite and Hierarchical State Machines).  

### critic models (стр. —) – модели‑критики (GRPO).  

### cross‑session continuity (стр. —) – сохранение контекста между сессиями (Short‑Term Memory and Time Travel).  

### curated subsets of benchmark datasets (стр. —) – подмножества наборов данных для бенчмарков (Turn Your Repo into a Benchmarkable Environment).  

### customer support agents (стр. —) – агенты поддержки клиентов (Hardening the Backbone).  

### customization of models (стр. —) – настройка моделей (Open Versus Closed Models).  

### CyberSecEval 4 (стр. —) – набор для красного тестирования (Red Teaming Your Agents).  

### cybersecurity benchmarks for LLMs (стр. —) – бенчмарки кибер‑безопасности LLM (Red Teaming Your Agents).  

---

## D  

### data analysis agents (стр. —) – агенты, анализирующие данные (Letting Your AI Agents Think Out Loud).  

### data exfiltration (стр. —) – кража данных; рассматривается в Understanding the AI Agent Threat Landscape.  

#### data flow management (стр. —) – управление потоком данных.  

- **Instructor library** – библиотека для обработки ошибок на уровне данных (Instructor).  
- **need for** – необходимость правильного контракта (Giving Your Agents the Right Contract).  
- **Pydantic** – валидатор данных (Keeping Costs in Check).  

### data movement (стр. —) – перемещение данных (Calculating the Memory Footprint).  

### data ownership (стр. —) – право собственности на данные (Open Versus Closed Models).  

### data security (стр. —) – безопасность данных (Open Versus Closed Models).  

### data sovereignty (стр. —) – суверенитет данных (Calculating the Memory Footprint).  

#### data validation with Pydantic (стр. —)  

- **bounded retries with explicit routing** – ограниченные попытки с явным роутингом (Keeping Costs in Check).  
- **catching failures at boundary** – отлов ошибок на границе (Keeping Costs in Check).  
- **factory pattern for contracts** – фабричный паттерн создания контрактов (Keeping Costs in Check).  
- **governance modes via OmegaConf** – режимы управления (Keeping Costs in Check).  
- **pinning policy against mid‑run drift** – фиксирование политики против дрейфа во время выполнения.  
- **reliability decay in agent chains** – снижение надёжности цепочек агентов (Giving Your Agents the Right Contract).  
- **resuming without rerunning nodes** – возобновление без повторного выполнения узлов.  
- **semantic feedback over raw traces** – семантическая обратная связь вместо сырых трасс.  

### datasets of benchmarks (стр. —) – наборы данных для бенчмарков (Turn Your Repo into a Benchmarkable Environment).  

### decoder‑only models (стр. —) – модели, использующие только декодер (KV‑caching).  

### decoding, constrained (стр. —) – ограниченный декодинг (The Need for a Fallback Guy).  

### Deep Agents (стр. —) – агенты с предварительным планированием (Deep Agents: Planning Before Execution).  

### DeepEval (стр. —) – оценка на основе продакшн‑трасс (From Production Traces to Custom Benchmarks).  

### DeepTeam (стр. —) – команда глубоких агентов; применяется в Early Threat Testing и автоматизации Red Teaming.  

### Defending Code reference harness (стр. —) – защита инфраструктуры для выполнения кода (Red Teaming).  

#### defenses across lifecycle (стр. —)  

- **red teaming of agents** – красное тестирование (Red Teaming Your Agents).  
- **system‑level defense for agents** – защита на уровне системы (System‑Level Defense).  

### degraded mode (стр. —) – режим деградации (The Need for a Fallback Guy).  

### deny‑by‑default execution (стр. —) – отказ по умолчанию при выполнении (Tool Governance).  

#### deployment (стр. —) – развертывание агентов.  

- **evaluation after** – оценка после запуска (Observing Agents in the Wild).  
- **evaluation before** – оценка перед запуском:  
  - *behavioral stress testing* – стресс‑тестирование поведения.  
  - *early threat testing* – раннее тестирование угроз.  
  - *overview of* – общий обзор процесса.  
- **fallback model** – запасная (fallback) модель (The Need for a Fallback Guy).  
- **inference backends** – бекенды инференса (Cold Starts, Caching, Deployment Physics).  
- **maturity model** – модель зрелости (Deploying Agents in Real Products).  
- **from MVP to production‑setup** – путь от минимального продукта к продакшен‑настройке:  
  1. *building diagnostic lab* – создать диагностическую лабораторию.  
  2. *hardening of architecture* – укрепление архитектуры.  
  3. *monitoring of agents* – мониторинг агентов.  
- **open versus closed models** – выбор модели (см. выше).  
- **overview of** – общие сведения о развертывании.  
- **physics** – физика инференса (Cold Starts, Caching).  
- **tiers** – уровни (расчёт памяти).  
- **topology** – топология стоимости (Agentic Cost Multiplier).  

### deterministic checks (стр. —) – детерминированные проверки (From Production Traces to Custom Benchmarks).  

### deterministic reconciliation (стр. —) – согласование детерминированных данных (Memory Hygiene).  

### deus ex machina (стр. —) – «дэвис экс мачина» – возможностей, доступных в текущий момент (What Is Possible Right Now?).  

### development loop (стр. —) – цикл разработки (Behavioral Stress Testing).  

### development, hardening agents during (стр. —) – развитие с усилением защиты (Early Threat Testing).  

### diagnostic lab (стр. —) – диагностическая лаборатория (Building a Diagnostic Lab).  

### direct preference optimization (DPO) (стр. —) – метод оптимизации предпочтений (GRPO).  

### disaggregated KV transfer (стр. —) – раздельный перенос KV‑данных (KV‑caching).  

### discovery and execution, separating (стр. —) – раздельное обнаружение и исполнение (Tool Governance).  

### distributed tracing (стр. —) – распределённое трассирование (Observing Agents in the Wild).  

### Docker (стр. —) – изоляция выполнения (Runtime Isolation with Docker); также упомянут Firecracker, gVisor.  

- **benchmark repository isolation** – изоляция репозитория бенчмарков (Turn Your Repo into a Benchmarkable Environment).  
- **as MCP server source** – использование Docker как источника MCP‑сервера (Letting Your Agents Discover MCP Servers).  

### Docker MCP (стр. —) – Docker‑версия MCP‑сервера.  

### docstrings (стр. —) – документирующие строки в коде (Foundations).  

### domain experts (стр. —) – эксперты‑домены в продвинутых парадигмах (Supervisor and Hierarchical Agents).  

### downstream risks (стр. —) – риски, возникающие после внедрения (Understanding the AI Agent Threat Landscape).  

### DPO (direct preference optimization) (стр. —) – см. выше (GRPO).  

#### drift (стр. —) – дрейф в разных уровнях.  

- **agent** – дрейф в агенте (Memory Topology).  
- **behavioral** – поведенческий дрейф (Building a Diagnostic Lab).  
- **mid‑run** – дрейф во время исполнения (Pydantic).  
- **model** – дрейф модели (The Need for a Fallback Guy).  
- **semantic** – семантический дрейф (The Need for a Fallback Guy).  

### duplicate suppression (стр. —) – подавление дублирования (Long‑Term Memory, Memory Hygiene).  

### durable infrastructure (стр. —) – надёжная инфраструктура, в частности для чекпоинтов (Short‑Term Memory and Time Travel).  

### dynamic adapter loading (стр. —) – динамическая загрузка адаптеров (LoRA and Adapters).  

### dynamic agents (стр. —) – **данные отсутствуют** (раздел объявлен, но подробностей нет).  

---  

**Как использовать конспект**  
- **Запросы** – ищите нужные термины в списке, чтобы быстро понять, где искать детали в полной книге.  
- **Проверка и валидация** – смотрите разделы о Pydantic, контрактах и проверках, когда требуется надёжный ввод/вывод.  
- **Память и кэш** – главы о KV‑caching, Memory Hygiene и checkpointing пригодятся при построении эффективных агентных систем.  
- **Защита и тестирование** – темы Red Teaming, Early Threat Testing, System‑Level Defense позволяют построить безопасный продакшн.  
- **Обучение и оценка** – разделы о CoT, Tree of Possibilities, Continuous Improvement Loop полезны для исследования и улучшения агентов.  

*Если в тексте нет конкретного описания процесса, шагов или шаблонов – они не включаются в конспект.*
