<!-- gpt-oss:120b (Hermes), глубокое чтение, build_ai_agent_08.txt -->
**Часть 6 из 13 книга «Build an AI Agent From Scratch» (Hur, Song)**  
*Содержание ниже — конспект по главам/разделам, которые присутствуют в страницах 189‑219. Всё взято из текста, никаких добавлений.*

---

## 6.3.3 Интеграция сессий в агент (стр. 189‑191)

- **Главная мысль** – Чтобы агент мог вести многошаговые (multiturn) диалоги, в него внедряется *Session* (история событий + состояние) и *SessionManager* (создание/получение/сохранение сессий).  
- **Как делаем**  
  1. Реализуем `BaseSessionManager` с абстрактными `create`, `get`, `save`.  
  2. Пишем `InMemorySessionManager` (словарь `self._sessions`).  
     - При `create` проверяем, нет ли уже `session_id`; если есть → `raise ValueError`.  
     - `get` → `self._sessions.get(session_id)`.  
     - `save` → `self._sessions[session.session_id] = session`.  
  3. Расширяем `ExecutionContext`: добавляем поля `session` и `session_manager`.  
     - Свойства `events` и `state` **прокси** к `session.events` / `session.state`.  
  4. Меняем конструктор `Agent`: параметр `session_manager`; если `None` → `InMemorySessionManager()`.  
  5. В `run()` добавляем три новых шага:  
     - Приём `session_id`.  
     - `session = await self.session_manager.get_or_create(session_id)`.  
     - Создание `ExecutionContext(session=…, session_manager=…)`.  
     - После завершения: `await self.session_manager.save(session)`.  

- **Правила и числа**  
  - `ValueError` при попытке создать сессию с уже существующим `session_id` (стр. 189).  

- **Шаблоны / примеры**  
  ```python
  class InMemorySessionManager(BaseSessionManager):
      def __init__(self):
          self._sessions: dict[str, Session] = {}

      async def create(self, session_id, user_id=None):
          if session_id in self._sessions:
              raise ValueError(f"Session {session_id} already exists")
          session = Session(session_id=session_id, user_id=user_id)
          self._sessions[session_id] = session
          return session
  ```

- **Ошибки и предупреждения**  
  - При использовании `InMemorySessionManager` все сессии **теряются** после завершения программы.  

- **Где пригодится** – При построении чат‑ботов/ассистентов, где пользователи возвращаются в разговор (запросы, проверка памяти, хранение состояния между вызовами).

---

## 6.3.4 Базовый пример – мультитурн‑разговор (стр. 191‑194)

- **Главная мысль** – Показать, как одинаковый `session_id` сохраняет контекст, а отсутствие `session_id` приводит к независимым запускам.  
- **Как делаем**  
  1. Создаём `Agent` с `InMemorySessionManager`.  
  2. Вызываем `agent.run(...)` без `session_id` → каждая итерация имеет пустой `session.events`.  
  3. Вызываем два раза с одинаковым `session_id` → первая вызывает `create`, вторая `get_or_create` возвращает уже существующую сессию, LLM видит предыдущее событие.  

- **Правила и числа**  
  - При одинаковом `session_id` **выполняются** шаги:  
    1. `get_or_create` → создаёт новую сессию (первый вызов).  
    2. Сохраняет `session.events`.  
    3. При следующем вызове `get_or_create` возвращает существующую. (стр. 193)  
  - При разных/отсутствующих `session_id` каждый запуск **создаёт** новую сессию (стр. 194).  

- **Шаблоны / примеры**  
  ```python
  # без session_id
  result1 = await agent.run("Hi! My name is Alice ...")
  result2 = await agent.run("What's my name ...")
  # с тем же session_id
  result1 = await agent.run("Hi! ...", session_id="alice_session")
  result2 = await agent.run("What's my name ...", session_id="alice_session")
  ```

- **Ошибки и предупреждения**  
  - Не забывать указывать один и тот же `session_id`, иначе «память» будет потеряна.  

- **Где пригодится** – При построении приложений с продолжающимися диалогами (поддержка исторических запросов, персонализация).

---

## 6.3.5 Структуры данных для подтверждения инструментов (стр. 194‑196)

- **Главная мысль** – Для Human‑in‑the‑Loop (HITL) нужен способ хранить **ожидающие** вызовы инструментов и **решения пользователя**.  
- **Как делаем**  
  1. `PendingToolCall` хранит оригинальный `ToolCall` и `confirmation_message`.  
  2. `ToolConfirmation` хранит `tool_call_id`, `approved`, `reason` (опционально) и `modified_arguments`.  
  3. Расширяем `AgentResult`: поле `status` (`complete`, `pending_confirmation`, `error`) + `pending_tool_calls`.  

- **Правила и числа**  
  - `AgentResult.status` — стр. 176.  
  - `pending_tool_calls` – пустой список по умолчанию (стр. 176).  

- **Шаблоны / примеры**  
  ```python
  class PendingToolCall(BaseModel):
      tool_call: ToolCall
      confirmation_message: str

  class ToolConfirmation(BaseModel):
      tool_call_id: str
      reason: str | None = None
      approved: bool
      modified_arguments: dict | None = None
  ```

- **Ошибки и предупреждения**  
  - При сохранении в `Session.state` нельзя хранить Pydantic‑модели напрямую – нужно сериализовать их `model_dump()` / `model_validate()`.  

- **Где пригодится** – При построении воркфлоу, где требуется одобрение (удаление файлов, платежи, изменение настроек).

---

## 6.3.6 Расширение инструментов для подтверждения (стр. 196‑197)

- **Главная мысль** – Инструмент сам сообщает, нужен ли он верификации, и формирует сообщение для пользователя.  
- **Как делаем**  
  1. В `BaseTool` добавляем атрибуты:  
     - `requires_confirmation: bool = False`  
     - `confirmation_message_template: str` (с placeholders `{name}` и `{arguments}`)  
  2. Метод `get_confirmation_message(arguments)` подставляет значения.  
  3. Декоратор `@tool` получает новые параметры `requires_confirmation` и `confirmation_message`.  

- **Правила и числа**  
  - Шаблон по‑умолчанию: `"The agent wants to execute '{name}' with arguments: {arguments}. Do you approve?"` (стр. 196).  

- **Шаблоны / примеры**  
  ```python
  @tool(
      name="delete_file",
      description="Delete a file from the filesystem",
      requires_confirmation=True,
      confirmation_message="
          The agent wants to delete '{arguments[filename]}'. "
          "This action cannot be undone. Do you approve?"
  )
  def delete_file(filename: str) -> str: ...
  ```

- **Ошибки и предупреждения**  
  - Если `requires_confirmation=True` и `confirmation_message` не задано, будет использован шаблон по‑умолчанию.  

- **Где пригодится** – Любой инструмент, который может нанести вред или изменить существенное состояние (файлы, платежи, конфигурация).

---

## 6.3.7 Реализация паузы и возобновления в агенте (стр. 197‑203)

### Основные идеи
- **Внутреннее vs. внешнее расширение** – подтверждение — внутреннее ядро фреймворка, реализуется в `_prepare_llm_request()`, а не в пользовательском колбэке.  
- **Принципы дизайна**  
  1. **Pre‑execution blocking** – инструмент с `requires_confirmation=True` не может выполниться без одобрения.  
  2. **Whitelist approval** – пользователь может одобрить отдельные вызовы, остальные считаются отклонёнными.  

### Как делаем (пошагово)

1. **`act()`**  
   - Итерируем `tool_calls`.  
   - Если `tool.requires_confirmation` → `PendingToolCall` → добавить в `pending_calls`.  
   - Не выполнять инструмент, а **не создавать** `ToolResult`.  
   - По окончании сохраняем в `context.state["pending_tool_calls"]` сериализованные объекты (`model_dump()`).  

2. **`run()`** (новые параметры)  
   ```python
   async def run(...,
                 tool_confirmations: List[ToolConfirmation] | None = None,
                 session_id: str | None = None,
                 user_input: str | None = None,
                 context: ExecutionContext | None = None) -> AgentResult:
   ```
   - Если `tool_confirmations` переданы → сохраняем в `context.state["tool_confirmations"]`.  
   - Внутренний цикл `while not context.final_result …`  
   - После `step(context)` проверяем `context.state.get("pending_tool_calls")`.  
   - При наличии → возвращаем `AgentResult(status="pending_confirmation", pending_tool_calls=…)`.  

3. **`_prepare_llm_request()`**  
   - Если в `context.state` есть и `pending_tool_calls`, и `tool_confirmations` → вызываем `_process_confirmations(context)`.  
   - Добавляем полученные `ToolResult` как событие, очищаем оба ключа из `state`.  

4. **`_process_confirmations()`**  
   - Формируем словари `pending_map` и `confirmation_map`.  
   - Для каждого `tool_call_id`:  
     - Если подтверждено → **слияем** оригинальные аргументы с `modified_arguments` (если есть).  
     - Выполняем инструмент (await).  
     - При успехе → `ToolResult(status="success")`; при исключении → `ToolResult(status="error")`.  
     - Если не подтверждено → `ToolResult(status="error")` с объяснением (`reason` либо стандартный текст).  

5. **Поток выполнения (см. Fig 6.7)** – два вызова `run()`:  
   - Первый → обнаруживает требуемый подтверждения → `pending_confirmation`.  
   - Второй → получает `tool_confirmations` → `_process_confirmations` → создаёт `ToolResult` → LLM видит результаты → завершает разговор (`status="complete"`).  

### Правила и числа
- Сериализация в `context.state["pending_tool_calls"]` и `["tool_confirmations"]` используется `model_dump()` / `model_validate()` (стр. 196‑197).  
- При объединении аргументов: `**original, **modified` → изменённые перезаписывают оригинальные (стр. 203).  

### Шаблоны / примеры
```python
# act() snippet
if tool.requires_confirmation:
    pending = PendingToolCall(
        tool_call=tool_call,
        confirmation_message=tool.get_confirmation_message(tool_call.arguments)
    )
    pending_calls.append(pending)
    continue
# after loop
if pending_calls:
    context.state["pending_tool_calls"] = [
        p.model_dump() for p in pending_calls
    ]
```

```python
# run() snippet (пауза)
if context.state.get("pending_tool_calls"):
    pending_calls = [
        PendingToolCall.model_validate(p)
        for p in context.state["pending_tool_calls"]
    ]
    return AgentResult(
        status="pending_confirmation",
        context=context,
        pending_tool_calls=pending_calls,
    )
```

### Ошибки и предупреждения
- **Не забыть** добавить `tool_confirmations` в `run()` при возобновлении, иначе агент будет опять ждать подтверждения.  
- При неправильном `tool_call_id` в `ToolConfirmation` подтверждение будет проигнорировано → считается отклонённым.  

### Где пригодится
- При построении систем, где пользователь должен одобрять действия (удаление файлов, отправка денег, изменения инфраструктуры).

---

## 6.3.8 Полный пример – HITL‑воркфлоу (стр. 204‑205)

- **Главная мысль** – Демонстрировать весь цикл: запрос → пауза → пользователь одобряет → возобновление → окончательный ответ.  
- **Шаги**  
  1. Определяем `delete_file` (нужен `requires_confirmation=True`).  
  2. Создаём `Agent` с `InMemorySessionManager`.  
  3. `run(..., session_id="file_session")` → получаем `AgentResult.status="pending_confirmation"` и список `pending_tool_calls`.  
  4. Формируем `ToolConfirmation(approved=True)` с `tool_call_id` из предыдущего ответа.  
  5. `run(session_id="file_session", tool_confirmations=[conf])` → получаем `status="complete"` и финальный `output`.  

- **Шаблон вывода**  
  ```
  Status: pending_confirmation
  Pending tools: 1
  Tool: delete_file
  Arguments: {'filename': 'temp.txt'}
  Message: 
   Delete 'temp.txt'? This cannot be undone.

  # после подтверждения
  Status: complete
  Output: I've deleted the file temp.txt as requested.
  ```

- **Где пригодится** – Пример готов к использованию в UI‑приложениях (кнопки «Approve/Reject», чат‑боты с критическими действиями).

---

## 6.4 Долговременная память: накопление знаний между сессиями (стр. 206‑219)

### 6.4.1 Структура долговременной памяти (стр. 206‑207)

- **Главная мысль** – `SessionManager` обеспечивает **горизонтальную** непрерывность внутри одной сессии, а `MemoryManager` – **вертикальную** накопление знаний после завершения сессий.  
- **Ключевые операции** – *Write* (сохраняем важную информацию в внешнее хранилище) и *Retrieval* (ищем релевантные записи в новых сессиях).  
- **Правила** – В примере реализованы только операции **ADD** (новая запись) и **SKIP** (дубликат).  

### 6.4.2 Извлечение информации: структурированный вывод (стр. 207‑209)

- **Главная мысль** – Для сложных данных (например, GAIA‑задач) требуется **структурировать** их в схему Pydantic (`TaskMemory`).  
- **Новые методы LlmClient**  
  - `ask(prompt, response_format=YourModel)` – возвращает объект модели либо простой текст.  
- **Схема `TaskMemory`**  
  ```python
  class TaskMemory(BaseModel):
      task_summary: str
      approach: str
      final_answer: str
      is_correct: bool
      error_analysis: str | None = None
      def to_embedding_text(self) -> str:
          return f"Task: {self.task_summary}"
  ```
- **Промпт для извлечения** – `TASK_MEMORY_EXTRACTION_PROMPT` (стр. 208).  
- **Промпт проверки дубликата** – `DUPLICATE_CHECK_PROMPT` + схема `DuplicateCheckResult` (стр. 209‑210).  

### 6.4.3 Векторный стор с ChromaDB (стр. 210‑211)

- **Главная мысль** – Храним записи в виде **текст + вектор**; ChromaDB автоматически генерирует эмбеддинги через `OpenAIEmbeddingFunction`.  
- **Создание клиента**  
  ```python
  client = chromadb.Client()
  embedding_fn = OpenAIEmbeddingFunction(model_name="text-embedding-3-small")
  collection = client.get_or_create_collection(
      name="my_memories", embedding_function=embedding_fn)
  ```
- **Пример `add` / `query`** – строки 215‑219.  

### 6.4.4 Реализация `TaskMemoryManager` (стр. 211‑215)

| Метод | Описание (стр.) |
|------|-----------------|
| `__init__` | Инициализирует `llm_client`, `chromadb.Client`, создаёт коллекцию с эмбеддинг‑функцией (стр. 212). |
| `_format_execution_history` | Преобразует список `Event` в строку, форматируя сообщения, вызовы инструментов, результаты (стр. 213). |
| `_extract_memory` | Вызывает `llm_client.ask` с `response_format=TaskMemory`; возвращает `TaskMemory` или `None` (стр. 212‑213). |
| `_is_duplicate` | Запрашивает LLM с `DuplicateCheckResult`; возвращает `True` если решение = `SKIP` (стр. 214‑215). |
| `save` | **4‑шаговый** процесс (стр. 215‑219): 1) форматировать историю, 2) извлечь память, 3) поиск похожих записей, 4) если не дубликат – добавить в ChromaDB (`metadata = memory.model_dump()`). |
| `search` | Запрос к коллекции, преобразование метаданных в объекты `TaskMemory` (стр. 219‑220). |

- **Шаблоны** – `save()` возвращает `memory_id` или `None`.  

### 6.4.5 Получение памяти (стр. 216‑219)

- **Подход 1 – инструмент** (`MemoryTool`)  
  - `execute(context, query)` → `await context.memory_manager.search(query, top_k=3)` → форматирует записи (`_format_memories`).  
- **Подход 2 – автоматическое внедрение**  
  - Переопределяем `process_llm_request(context, request)` в `MemoryTool`.  
  - На каждом запросе LLM извлекаем **последнее пользовательское сообщение**, ищем похожие записи, добавляем их в `request.append_instructions(...)`.  
  - Чтобы инструмент **не отображался в списке LLM**, задаём `tool_definition=None` в `__init__`.  

- **Изменения в агенте** (`_prepare_llm_request`) – фильтруем `self.tools` по наличию `tool_definition` и вызываем `await tool.process_llm_request(context, request)` (стр. 218‑219).  

- **Шаблоны**  
  ```python
  class MemoryTool(BaseTool):
      def __init__(self):
          super().__init__(
              name="recall_memory",
              description="...",
              tool_definition=None,   # скрыт от LLM
          )

      async def process_llm_request(self, context, request):
          user_msgs = [c for c in request.contents if isinstance(c, Message) and c.role=="user"]
          if not user_msgs: return
          result = await self.execute(context, user_msgs[-1].content)
          if result:
              request.append_instructions(
                  f"The following are records from similar problems:\n<PAST_EXPERIENCES>{result}</PAST_EXPERIENCES>"
              )
  ```

### Ошибки и предупреждения

- При использовании `MemoryTool` с `tool_definition=None` **инструмент не будет предлагаться LLM**, но всё равно будет выполнен (важно помнить, если нужен лишь автодобавление).  
- При отсутствии совпадений `search()` возвращает пустой список – тогда `process_llm_request` ничего не добавляет.  

### Где пригодится

- Профиль пользователя (имя, предпочтения) – автодобавление в начало диалога.  
- Поиск прошлых решений проблем (GAIA, технические задачи) – как отдельный инструмент **recall_memory** или как автоматический контекст.  

---

## Итоги (стр. 219‑200)

- **Session/SessionManager** → мульти‑шаговые беседы, паузы для HITL.  
- **TaskMemoryManager + ChromaDB** → долговременная память, доступная между сессиями.  
- **Три паттерна использования памяти**:  
  1. Одна‑выходная (память в `ExecutionContext`).  
  2. Непрерывная (сессии).  
  3. Долговременная (векторный стор, извлечение, дубликаты).  
- **Стратегия управления токенами** – сначала измеряем, потом сжимаем (компрессия результатов инструментов), в крайнем случае summarise.  
- **Разделяем хранение и представление** – `ExecutionContext` *не изменяется*, а `LlmRequest` формируется заново для каждого вызова.  

--- 

**Для Claude**: используйте эти конспекты как «шпаргалки» при построении собственного агента‑одиночки. Каждый пункт можно превратить в задачу, а шаблоны кода – в быстрые вставки в ваши скрипты. Если понадобится уточнить детали (например, точный код `act()`), просто откройте соответствующую страницу из оригинального текста.
