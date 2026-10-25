<!-- gpt-oss:120b (Hermes), глубокое чтение, build_ai_agent_07.txt -->
## Extending agents with callbacks (стр. 161–162)  
- **Главная мысль** – Для изменения поведения агента без правки его ядра используют два типа обратных вызовов: `before_tool_callback` (вызывается до инструмента) и `after_tool_callback` (вызывается после). Если любой из них возвращает значение ≠ `None`, дальнейшее исполнение инструмента (для `before`) или оригинальный результат (для `after`) заменяется этим значением (паттерн *Early Exit*).  
- **Как делать**  
  1. При создании агента добавить параметры `before_tool_callbacks` и `after_tool_callbacks`‑списки (по умолчанию `[]`).  
  2. В методе `act()` разбить обработку вызовов инструмента на три стадии:  
     1) пройтись по `before_tool_callbacks`; если один из них возвращает не‑`None` – запомнить как `tool_response` и прервать цикл;  
     2) если `tool_response` `None`, выполнить реальный инструмент;  
     3) пройтись по `after_tool_callbacks`; если один из них возвращает не‑`None`, заменить им `ToolResult`.  
- **Правила и числа** – *Early Exit* – выполнение останавливается на первом колбэке, который возвращает значение, отличное от `None` (стр. 161).  
- **Шаблоны и примеры**  
  ```python
  class Agent:
      def __init__(..., before_tool_callbacks=None, after_tool_callbacks=None):
          self.before_tool_callbacks = before_tool_callbacks or []
          self.after_tool_callbacks = after_tool_callbacks or []
  ```  
  ```python
  # в act()
  for cb in self.before_tool_callbacks:
      result = cb(context, tool_call)
      if result is not None:  # Early Exit
          tool_response = result
          break
  ```  
- **Ошибки и предупреждения** – Не проверять список колбэков на `None` → ошибка при итерации; забыть обработать `await`‑able результаты – приложение «зависнет».  
- **Где нам пригодится** – Для реализации HITL‑проверки, кэш‑проверок, валидации входов, пост‑обработки результатов.  

---

## Human‑in‑the‑loop tool‑execution approval (стр. 163–164)  
- **Главная мысль** – Опасные инструменты (удаление файлов, отправка писем, запросы к БД) должны исполняться только после явного подтверждения пользователя. Это реализуется через `before_tool_callback`, который запрашивает согласие и, в случае отказа, возвращает строку‑отказ вместо выполнения инструмента.  
- **Как делать**  
  1. Сформировать список `DANGEROUS_TOOLS` (например, `["delete_file","send_email","execute_sql"]`).  
  2. Написать функцию‑колбэк `approval_callback(context, tool_call)`:  
     - если `tool_call.name` не в списке → вернуть `None` (пропустить проверку);  
     - вывести запрос пользователю, собрать ввод `y/n`;  
     - при `y` → вернуть `None` (разрешить исполнение);  
     - иначе → вернуть строку‑сообщение отказа.  
  3. При создании агента указать `before_tool_callbacks=[approval_callback]`.  
- **Правила и числа** – Список опасных инструментов: `DANGEROUS_TOOLS = ["delete_file", "send_email", "execute_sql"]` (стр. 164).  
- **Шаблоны и примеры**  
  ```python
  def approval_callback(context, tool_call):
      if tool_call.name not in DANGEROUS_TOOLS:
          return None
      print(f"\nDangerous tool execution requested: {tool_call.name}")
      resp = input("Do you want to execute? (y/n): ").lower().strip()
      return None if resp == "y" else f"User denied execution of {tool_call.name}"
  ```  
  ```python
  agent = Agent(..., before_tool_callbacks=[approval_callback])
  ```  
- **Ошибки и предупреждения** – Синхронный `input()` блокирует процесс; в веб‑службах такой подход невозможен (стр. 167).  
- **Где нам пригодится** – Для безопасного выполнения файловых и сетевых операций в интерактивных прототипах.  

---

## Compressing search results (стр. 165–166)  
- **Главная мысль** – Результаты веб‑поиска часто огромны (десятки тысяч токенов). После выполнения инструмента `search_web`‑колбэк `after_tool_callback` автоматически сокращает их, оставляя только самое релевантное (топ‑3 чанка) через векторный поиск.  
- **Как делать**  
  1. В `after_tool_callback` проверить, что `tool_result.name == "search_web"`.  
  2. Если длина `content[0]` < 2000 символов → вернуть `None` (не сжимать).  
  3. Иначе из `ExecutionContext` извлечь оригинальный запрос (`_extract_search_query`).  
  4. Разбить результат на чанки (`fixed_length_chunking`), получить эмбеддинги (`get_embeddings`), выполнить векторный поиск (`vector_search`, `top_k=3`).  
  5. Сконструировать новый `ToolResult` с объединёнными топ‑3 чанками и вернуть его.  
- **Правила и числа** – Длинный результат > 2000 символов → сжатие (стр. 165). Топ‑3 чанка (стр. 165).  
- **Шаблоны и примеры**  
  ```python
  def search_compressor(context, tool_result):
      if tool_result.name != "search_web": return None
      original = tool_result.content[0]
      if len(original) < 2000: return None
      query = _extract_search_query(context, tool_result.tool_call_id)
      chunks = fixed_length_chunking(original, chunk_size=500, overlap=50)
      results = vector_search(query, chunks, get_embeddings(chunks), top_k=3)
      compressed = "\n\n".join([r['chunk'] for r in results])
      return ToolResult(..., content=[compressed])
  ```  
- **Ошибки и предупреждения** – Не сопоставить `tool_call_id` → могут сжать результаты другого запроса; при отсутствии запроса в контексте (`_extract_search_query` возвращает `""`) колбэк должен вернуть `None`.  
- **Где нам пригодится** – Для экономии токенов при длительных веб‑исследованиях в автоматических агентных воркфлоу.  

---

## Summary of callback pattern (стр. 167–168)  
- **Главная мысль** – Паттерн *callback* позволяет расширять поведение агента без изменения его ядра: `before_tool_callback` — может отменять/заменять вызов (HITL, кеш, валидация); `after_tool_callback` — может менять результат (сжатие, маскирование, форматирование). Комбинирование нескольких колбэков дает чистый, «однозначный» код.  
- **Как делать** – 1) Реализовать отдельный колбэк с одной ответственностью; 2) Добавить его в соответствующий список при инициализации агента; 3) При необходимости комбинировать несколько колбэков, порядок их регистрации определяет приоритет (первый «Early Exit»).  
- **Правила и числа** – Синхронный HITL работает только в локальном тесте; асинхронный‑HITL будет реализован в главе 6 (стр. 167).  
- **Шаблоны и примеры** – см. разделы 5.5.3 и 5.5.4 (approval + search compressor).  
- **Ошибки и предупреждения** – Не забывать, что каждый колбэк получает **только** копию результата; изменение `request.contents` в `before_llm_callback` не меняет `ExecutionContext.events`.  
- **Где нам пригодится** – Для построения модульных, легко тестируемых агентных систем (пользователь‑контроль, пост‑обработка, снижение токенов).  

---

## Adding memory to your agent – introduction (стр. 168–169)  
- **Главная мысль** – Память отличает «инструмент без состояния» от «интеллектуального помощника»: без неё агент не хранит предшествующие шаги, не продолжает диалог и не учится.  
- **Как делать** – Подготовка: понять, что будем вводить три паттерна управления контекстом (Reduction, Write, Retrieval) и три типа памяти (краткосрочная, сессия, долгосрочная).  
- **Правила и числа** – Никаких чисел, только концептуальное разделение.  
- **Шаблоны и примеры** – Схема «Agent ↔ Memory ↔ Planning ↔ Tools» (рис. 6.1).  
- **Ошибки и предупреждения** – Не вводить память сразу – сначала изучить ограничения текущего `ExecutionContext`.  
- **Где нам пригодится** – Для построения длительных, контекстно‑зависимых диалогов и персонализированного опыта.  

---

## Anatomy of agent memory (стр. 169–171)  
- **Главная мысль** – Отсутствие памяти приводит к двум классическим проблемам: *контекст‑эксплозия* (слишком много токенов в одной сессии) и *потеря истории* (между сессиями). Решением являются три уровня: **краткосрочная память** (внутри `ExecutionContext`), **сессия** (накопление событий across runs) и **долгосрочная память** (выборочная сохранённость через векторный поиск).  
- **Как делать** – 1) Определить `Session` — объединяет события и произвольный `state`; 2) При каждом `run()` сохранять текущий `ExecutionContext` в `Session`; 3) При старте нового `run()` загружать `Session` по `session_id`.  
- **Правила и числа** – *Challenge 1*: контекст‑эксплозия; *Challenge 2*: отсутствие непрерывного диалога; *Challenge 3*: отсутствие постоянных знаний (стр. 169‑172).  
- **Шаблоны и примеры** – Таблица 6.1 (стратегии контекст‑инжиниринга) и Таблица 6.2 (соответствие паттернов); рисунки 6.2 / 6.3 показывают разницу между «независимыми» и «сессионными» вызовами.  
- **Ошибки и предупреждения** – Не путать **сессию** (один чат) и **долгосрочную память** (информация, общая для всех сессий).  
- **Где нам пригодится** – При построении чат‑бота с сохранением пользовательских данных и при решении сложных задач, требующих многократных вызовов инструментов.  

---

## Context engineering and memory (стр. 172–173)  
- **Главная мысль** – Три паттерна управления контекстом (1 — внутри‑выполнения, 2 — мульти‑запуск в сессии, 3 — долгосрочное хранение) соответствуют стратегиям из главы 1: **Reduce** + **Write** для паттернов 1 и 2, **Write** + **Retrieval** для паттерна 3.  
- **Как делать** – Сопоставить каждый паттерн с техникой:  
  - Паттерн 1 → Sliding‑window, компакцию, суммаризацию;  
  - Паттерн 2 → Session + State (Write);  
  - Паттерн 3 → Извлечение фактов → векторный поиск (Retrieval).  
- **Правила и числа** – Таблица 6.2, где «Pattern 1, 2 – Reduce + Write», «Pattern 3 – Write + Retrieval» (стр. 172).  
- **Шаблоны и примеры** – Нет кода, только концептуальные таблицы.  
- **Ошибки и предупреждения** – Смешивание стратегий без учёта их назначения может привести к избыточному токен‑использованию.  
- **Где нам пригодится** – При проектировании общего подхода к управлению контекстом в разных сценариях.  

---

## Managing context during execution (стр. 174–176)  
- **Главная мысль** – Контекст‑менеджмент реализуется через разделение *хранилища* (`ExecutionContext.events`, неизменяемое) и *представления* (`LlmRequest.contents`, модифицируемое перед отправкой LLM). `before_llm_callback` позволяет менять запрос без изменения истиных событий.  
- **Как делать**  
  1. Реализовать `before_llm_callback(context, request)`. Должен вернуть `None` (продолжить) или `LlmResponse` (пропустить LLM).  
  2. Для гибкости использовать фабрику `create_optimizer_callback(apply_optimization, threshold)`, которая генерирует такой колбэк, вызывая `apply_optimization` только если токен‑счёт превышает `threshold`.  
- **Правила и числа** – Порог по умолчанию = 50 000 токенов (стр. 174).  
- **Шаблоны и примеры**  
  ```python
  def create_optimizer_callback(apply_optimization, threshold=50000):
      async def callback(context, request):
          if count_tokens(request) < threshold:
              return None
          await apply_optimization(context, request)
          return None
      return callback
  ```  
- **Ошибки и предупреждения** – Не менять `context.events` внутри колбэка – потеряется возможность отладки.  
- **Где нам пригодится** – Для внедрения любой стратегии снижения контекста (окно, компакция, суммаризация) без изменения ядра агента.  

---

## Token counting (стр. 176–177)  
- **Главная мысль** – Для точного контроля размера контекста нужно измерять количество токенов, а не количество сообщений. Библиотека **tiktoken** (OpenAI) позволяет посчитать токены, учитывая сообщения, инструменты и их аргументы.  
- **Как делать**  
  1. Выбрать кодек модели (`tiktoken.encoding_for_model`).  
  2. Преобразовать `LlmRequest` в список сообщений через `build_messages`.  
  3. Суммировать токены: 4 пер‑сообщение + токены контента + токены `tool_calls` + токены определений инструментов.  
- **Правила и числа** – Пер‑сообщение = 4 токена (стр. 177). Пороговое значение ≈ 20 000 токенов в примерах (стр. 177).  
- **Шаблоны и примеры**  
  ```python
  def count_tokens(request):
      encoding = tiktoken.encoding_for_model(request.model_id or "gpt-5")
      messages = build_messages(request)
      total = 0
      for m in messages:
          total += 4
          total += len(encoding.encode(m.get("content","")))
          # tool_calls handling omitted for brevity
      return total
  ```  
- **Ошибки и предупреждения** – Точность ниже 100 % на разных моделях, но достаточна для пороговых проверок.  
- **Где нам пригодится** – Для динамического выбора стратегии оптимизации (скользящее окно, компакция, суммаризация).  

---

## Compaction strategy (стр. 178–180)  
- **Главная мысль** – Компрессия заменяет уже обработанные большие блоки (например, содержимое файла, результат веб‑поиска) лёгкими ссылками‑заполнителями, экономя токены, но позволяя при необходимости восстановить данные повторным вызовом инструмента.  
- **Как делать**  
  1. Задать правила: `TOOLCALL_COMPACTION_RULES` (для аргументов `create_file`) и `TOOLRESULT_COMPACTION_RULES` (для `read_file`, `search_web`, `tavily_search`).  
  2. В функции `apply_compaction(context, request)` пройтись по `request.contents`.  
     - При `ToolCall` — если имя в `TOOLCALL_COMPACTION_RULES`, заменить соответствующий аргумент (обычно `content`) фиксированным текстом типа `"[Content saved to file]"`.  
     - При `ToolResult` — если имя в `TOOLRESULT_COMPACTION_RULES`, сформировать шаблон с подстановкой пути файла или запроса.  
  3. Вернуть изменённый список `request.contents`.  
- **Правила и числа** – Пример правила: `"create_file": "[Content saved to file]"` (стр. 178). Шаблоны для `read_file`/`search_web` включают placeholder‑подстановки (стр. 179).  
- **Шаблоны и примеры**  
  ```python
  TOOLCALL_COMPACTION_RULES = {"create_file": "[Content saved to file]"}
  TOOLRESULT_COMPACTION_RULES = {
      "read_file": "File content from {file_path}. Re-read if needed.",
      "search_web": "Search results processed. Query: {query}. Re-search if needed."
  }
  ```  
- **Ошибки и предупреждения** – При компактации меняются сообщения в середине контекста, что разрушает **prompt‑caching** (стр. 180). Нужно применять только когда токен‑порог превышен.  
- **Где нам пригодится** – Для снижения токенов при работе с большими файлами и длинными результатами веб‑поиска.  

---

## Summarization strategy (стр. 181–184)  
- **Главная мысль** – Если компакция не устраняет рост контекста, применяется семантическая суммаризация: старые сообщения заменяются структурированным резюме, которое добавляется в инструкцию LLM. Суммаризация теряет оригинальные данные, поэтому её используют как «последний» способ.  
- **Как делать**  
  1. Определить позицию пользовательского сообщения (`user_idx`).  
  2. Сохранить `keep_recent` последних сообщений (по умолчанию 5).  
  3. Вычислить диапазон для суммирования (`summary_start … summary_end`).  
  4. Сформировать текст истории (`format_history_for_summary`).  
  5. С помощью отдельного LLM (можно более дешёвый) спросить резюмировать по шаблону `SUMMARIZATION_PROMPT`.  
  6. Добавить полученное резюме в `request.instructions`; удалить суммированные сообщения из `request.contents`.  
- **Правила и числа** – `keep_recent = 5` (стр. 182). Порог для применения суммирования задаётся в `ContextOptimizer` (стр. 184).  
- **Шаблоны и примеры**  
  ```python
  SUMMARIZATION_PROMPT = """You are summarizing an AI agent's work progress.
  ... (см. текст) ...
  Execution History:
  {history}
  Provide a structured summary."""
  ```  
  ```python
  async def apply_summarization(..., keep_recent=5):
      # … находим user_idx, формируем to_summarize …
      summary = await generate_summary(llm_client, history_text)
      request.append_instructions(f"[Previous work summary]\n{summary}")
  ```  
- **Ошибки и предупреждения** – Суммаризация необратима: потерянные детали невозможно восстановить без нового вызова инструмента.  
- **Где нам пригодится** – Для длительных диалогов, где после нескольких сотен сообщений требуется «закрыть» часть истории, сохранив смысл.  

---

## Hierarchical Context Optimizer (стр. 184–186)  
- **Главная мысль** – Оптимизация контекста применяется последовательно: сначала проверка токен‑порога, затем компакция, затем (при необходимости) суммаризация. Класс `ContextOptimizer` реализует эту иерархию и регистрируется как `before_llm_callback`.  
- **Как делать**  
  1. Инициализировать `ContextOptimizer` со смарт‑параметрами: `llm_client` (для суммирования), `token_threshold` (по умолчанию 50000), флаги `enable_compaction`, `enable_summarization`, `keep_recent`.  
  2. В методе `__call__` последовательно: измерить токены → если ниже порога → `None`; иначе → `apply_compaction`; пересчитать токены → если ниже порога → `None`; иначе → `await apply_summarization`.  
  3. Добавить экземпляр в `before_llm_callbacks` при создании агента.  
- **Правила и числа** – Токен‑порог = 50 000 (стр. 185). `keep_recent` = 5 (стр. 184).  
- **Шаблоны и примеры**  
  ```python
  optimizer = ContextOptimizer(
      llm_client=LlmClient(model="gpt-5-mini"),
      token_threshold=50000,
      enable_compaction=True,
      enable_summarization=True
  )
  agent = Agent(..., before_llm_callbacks=[optimizer])
  ```  
- **Ошибки и предупреждения** – Не забывать, что `apply_compaction` меняет сообщения, что может разрушить кэш; использовать порог, чтобы компрессировать только при необходимости (стр. 180‑181).  
- **Где нам пригодится** – Для автоматического контроля размера запросов к LLM в продуктивных сервисах.  

---

## Session class (стр. 186–187)  
- **Главная мысль** – `Session` хранит всё, что должно пережить несколько вызовов `run()`: кумулятивный список `events`, произвольный словарь `state`, метаданные (`created_at`, `updated_at`) и идентификаторы (`session_id`, `user_id`).  
- **Как делать**  
  1. Определить `BaseModel`‑класс с полями: `session_id: str`, `user_id: str|None`, `events: list[Event] = Field(default_factory=list)`, `state: dict[str, Any] = Field(default_factory=dict)`, `created_at`, `updated_at`.  
  2. При каждом завершении `run()` сохранять текущие события и состояние в объект `Session`.  
  3. При новом `run()` по тому же `session_id` загружать `Session` и восстанавливать `ExecutionContext`.  
- **Правила и числа** – `created_at` и `updated_at` заполняются `datetime.now()` (стр. 186).  
- **Шаблоны и примеры**  
  ```python
  class Session(BaseModel):
      session_id: str
      user_id: str | None = None
      events: list[Event] = Field(default_factory=list)
      state: dict[str, Any] = Field(default_factory=dict)
      created_at: datetime = Field(default_factory=datetime.now)
      updated_at: datetime = Field(default_factory=datetime.now)
  ```  
- **Ошибки и предупреждения** – Не хранить в `state` большие бинарные данные – они лучше сохранять в внешних хранилищах.  
- **Где нам пригодится** – Для поддержания диалогов в чат‑боте, где пользователь возвращается спустя часы/дни.  

---

## SessionManager abstract class (стр. 188)  
- **Главная мысль** – `SessionManager` отвечает за создание, поиск, получение/создание и сохранение `Session`. Это абстрактный интерфейс, позволяющий менять реализацию (in‑memory, база данных, облачное хранилище) без изменения кода агента.  
- **Как делать**  
  1. Наследовать от `ABC`.  
  2. Объявить асинхронные абстрактные методы: `create(session_id, user_id=None) -> Session` и `get(session_id) -> Session`.  
  3. Реализовать обычный метод `get_or_create(session_id, user_id=None)`, который пытается `get`, а при неуспехе вызывает `create`.  
  4. Все операции делают `async`, чтобы легко заменить на I/O‑операции (БД, API).  
- **Правила и числа** – Все методы объявлены `async` (стр. 188).  
- **Шаблоны и примеры**  
  ```python
  class BaseSessionManager(ABC):
      @abstractmethod
      async def create(self, session_id: str, user_id: str|None = None) -> Session: ...
  
      @abstractmethod
      async def get(self, session_id: str) -> Session: ...
  
      async def get_or_create(self, session_id, user_id=None):
          try: return await self.get(session_id)
          except NotFound: return await self.create(session_id, user_id)
  ```  
- **Ошибки и предупреждения** – Не реализовать `save` в подклассе – потеря данных между перезапусками сервиса.  
- **Где нам пригодится** – При построении сервисов, где сессии хранятся в Redis, PostgreSQL или другом долговременном хранилище.
