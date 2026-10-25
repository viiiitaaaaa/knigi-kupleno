<!-- gpt-oss:120b (Hermes), глубокое чтение, build_ai_agent_05.txt -->
## 86 chapter 4 «Implementing a basic ReAct agent» (стр. 105‑107)

### 4.3 Типы данных и ExecutionContext (стр. 105‑107)  
- **Главная мысль** – Для отладки и анализа необходимо фиксировать каждый шаг агента как объект *Event*, а внутри *Event* хранить сообщения, вызовы инструментов и их результаты.  
- **Как делать**  
  1. Описать три класса‑модели `Message`, `ToolCall`, `ToolResult` (Listing 4.2).  
  2. Обернуть любой из этих объектов в класс `Event` с полями `execution_id`, `author`, `timestamp`, `content` (Listing 4.3).  
  3. Реализовать `ExecutionContext` – центральное хранилище (Listing 4.4):  
     - `execution_id` – уникальный UUID выполнения,  
     - `events` – список всех `Event` в хронологическом порядке,  
     - `current_step` – счётчик шагов,  
     - `state` – произвольный словарь для данных инструментов,  
     - `final_result` – результат после завершения.  
  4. При каждом действии агента создавать новый `Event` и добавлять его через `add_event`.  
- **Правила и числа** – `current_step` используется как защита от бесконечного цикла (максимум `max_steps` задаётся в агенте).  
- **Шаблоны / примеры** – Пример события с вызовом `search_web` (стр. 105).  
- **Ошибки и предупреждения** – Не забывать привязывать `ToolResult` к соответствующему `ToolCall` через `tool_call_id`.  
- **Где пригодится** – Для логирования, отладки и построения трасс исполнения в запросах к агенту.  

---

### 4.4 Абстракция инструментов (стр. 108‑112)

#### 4.4.1 Зачем нужен единый интерфейс (стр. 108)  
- **Главная мысль** – Иметь единый объект‑инструмент, чтобы LLM получал описание и агент мог вызвать его без ручного сопоставления имён.  

#### 4.4.2 `BaseTool` – фундамент (стр. 108‑109)  
- **Как делать** – Наследовать все инструменты от абстрактного класса `BaseTool`:  
  ```python
  class BaseTool(ABC):
      def __init__(self, name=None, description=None, tool_definition=None):
          self.name = name or self.__class__.__name__
          self.description = description or self.__doc__ or ""
          self._tool_definition = tool_definition

      @property
      def tool_definition(self) -> Dict[str, Any] | None: …
      @abstractmethod
      async def execute(self, context: ExecutionContext, **kwargs) -> Any: …
      async def __call__(self, context, **kwargs): return await self.execute(context, **kwargs)
  ```
- **Правила** – `execute` всегда получает `ExecutionContext` первым параметром; если инструмент его не использует – просто игнорировать.  

#### 4.4.3 `FunctionTool` – адаптер для обычных функций (стр. 109‑110)  
- **Как делать** –  
  1. При инициализации проверять сигнатуру функции: есть ли параметр `context`.  
  2. При исполнении передавать `context` только если инструмент ожидает его.  
  3. Генерировать `tool_definition` автоматически через `function_to_input_schema` (Listing 4.6).  
- **Шаблоны** – Оборачиваем простую функцию `calculator` → `calc_tool = FunctionTool(calculator)`.  
- **Декоратор `@tool`** – Сокращает запись:  

  ```python
  @tool
  def calculator(expression: str) -> float: …
  ```
- **Ошибки** – Не учитывать асинхронность функции: `FunctionTool` проверяет `inspect.iscoroutine` и `await`‑ит, если нужно.  

#### 4.4.4 Интеграция MCP‑инструментов (стр. 111‑112)  
- **Главная мысль** – Внешние инструменты MCP (работающие через сетевой сеанс) тоже преобразуются в `BaseTool`.  
- **Как делать**  
  1. `load_mcp_tools(connection)` открывает **stdio**‑клиент, получает список инструментов и для каждого создаёт обёртку `call_mcp`.  
  2. Обрезать `tool_definition` из схемы MCP (`mcp_tool.inputSchema`).  
  3. Обернуть `call_mcp` в `FunctionTool`.  
- **Шаблон** – `await load_mcp_tools(connection)` → список `BaseTool`.  
- **Предупреждение** – Каждый вызов создаёт новое соединение; в продакшене лучше держать постоянный сеанс (стр. 112).  

---

### 4.5 Слой коммуникации с LLM (стр. 113‑118)

#### 4.5.1 Зачем отдельный слой (стр. 113)  
- **Главная мысль** – Преобразовать внутренние объекты (`Event`, `ContentItem`) в формат, ожидаемый API LLM, и обратно, скрыв провайдер‑специфику.  

#### 4.5.2 `LlmRequest` – что отправляем (стр. 113‑114)  
- Поля: `instructions` (список строк), `contents` (список `ContentItem`), `tools` (список `BaseTool`), `tool_choice` (`"auto"`/`"required"`).  

#### 4.5.3 `LlmResponse` – что получаем (стр. 115‑117)  
- Поля: `content` (список `ContentItem`), `error_message`, `usage_metadata` (токены).  

#### 4.5.4 `LlmClient` – адаптер к провайдерам (стр. 115‑119)  
- **Как делать**  
  1. Инициализировать `LlmClient(model, **config)`.  
  2. `generate(request)` →  
      - собрать сообщения (`_build_messages`),  
      - собрать схемы инструментов,  
      - вызвать `liteLLM.acompletion`,  
      - разобрать ответ (`_parse_response`).  
- **Шаблоны** – Пример использования (Listing 4.14):  
  ```python
  client = LlmClient(model="gpt-5-mini")
  request = LlmRequest(instructions=["You are a helpful assistant."],
                        contents=[Message(role="user", content="What is 2 + 2?")])
  response = await client.generate(request)
  ```  
- **Ошибки** – Если API падает, возвращается `LlmResponse(error_message=…)` вместо исключения.  

#### 4.5.5 Сборка запросов и парсинг (стр. 116‑117)  
- **Message → {"role":…, "content":…}**  
- **ToolCall → в массив `tool_calls` предыдущего сообщения‑ассистента**  
- **ToolResult → {"role":"tool", "tool_call_id":…, "content":…}`**  

---

## 86 chapter 4 «Implementing a basic ReAct agent» (стр. 119‑124)

### 4.6 Реализация класса Agent (стр. 119‑124)

- **Главная мысль** – Агент управляет циклом *think → act*, используя `ExecutionContext`, `BaseTool` и `LlmClient`.  

#### 4.6.1 Структура `Agent` (стр. 119‑120)  
- **Конструктор** принимает: `model` (`LlmClient`), `tools` (`List[BaseTool]`), `instructions` (строка), `max_steps` (по умолчанию 10), `name` (по‑умолчанию "agent").  
- `_setup_tools()` пока лишь возвращает список, но служит точкой расширения.  

#### 4.6.2 Метод `run` (стр. 121‑123)  
- **Шаги**  
  1. При отсутствии `ExecutionContext` создать новый.  
  2. Обернуть пользовательский запрос в `Event(author="user")` и добавить в контекст.  
  3. Цикл `while not context.final_result and context.current_step < max_steps:` → `await step(context)`.  
  4. После каждого шага проверять `_is_final_response` и, если да, извлекать результат в `context.final_result`.  
- **Помощник** – `AgentResult(output, context)` возвращает как итоговый ответ, так и полный журнал выполнения.  

#### 4.6.3 Метод `step` (стр. 124‑125)  
- **Шаги**  
  1. Сформировать `LlmRequest` через `_prepare_llm_request`.  
  2. Получить `LlmResponse` от `think`.  
  3. Записать ответ в `Event`.  
  4. Если есть `ToolCall`‑ы → вызвать `act`, записать их `ToolResult` в отдельный `Event`.  
  5. `context.increment_step()`.  

#### 4.6.4 `think` и `act` (стр. 124‑125)  
- `think` – просто `return await self.model.generate(request)`.  
- `act` –  
  1. Создать словарь `{tool.name: tool}`.  
  2. Для каждого `ToolCall` искать инструмент, вызывать `await tool(context, **args)`.  
  3. При ошибке вернуть `ToolResult(status="error", content=[str(e)])`.  

#### 4.6.5 Вспомогательные методы  
- `_is_final_response` – проверяет отсутствие `ToolCall` и `ToolResult`.  
- `_extract_final_result` – берёт текст из сообщения‑ассистента.  

- **Где пригодится** – Для построения запросов пользователя, отладки шагов, ограничения количества итераций.  

---

## 86 chapter 4 «Implementing a basic ReAct agent» (стр. 125‑129)

### 4.7 Добавление структурированного вывода (стр. 125‑129)

- **Главная мысль** – Вместо свободного текста агент может вернуть строго типизированный Pydantic‑модель, используя механизм вызова инструмента `final_answer`.  

#### 4.7.1 Инструменты‑форматтеры (стр. 125‑126)  
- Создаём динамический инструмент `final_answer` с сигнатурой `(output: <output_type>) -> <output_type>`.  
- Декоратор `@tool` автоматически генерирует схему и проверку входных данных.  

#### 4.7.2 Изменения в `Agent` (стр. 126‑129)  

| Метод | Что меняем | Кратко |
|------|-------------|--------|
| `__init__` | Добавляем `output_type: Optional[Type[BaseModel]]` и `output_tool_name` | Храним тип ожидаемого результата |
| `_setup_tools` | Если `output_type` задан, объявляем `final_answer`‑инструмент и сохраняем его имя | Динамический инструмент |
| `_prepare_llm_request` | При наличии `output_tool_name` ставим `tool_choice="required"` | Принудительный вызов инструмента |
| `_is_final_response` | Ищем успешный `ToolResult` от `final_answer` | Определяем завершённость |
| `_extract_final_result` | Возвращаем `item.content[0]` из успешного `ToolResult` | Возвращаем уже валидированный Pydantic‑объект |

#### 4.7.3 Пример использования (стр. 128‑129)  

```python
class SentimentAnalysis(BaseModel):
    sentiment: Literal["positive","negative","neutral"]
    confidence: float
    key_phrases: List[str]

agent = Agent(
    model=LlmClient(model="gpt-5-mini"),
    tools=[],
    instructions="Analyze sentiment.",
    output_type=SentimentAnalysis
)

result = await agent.run("This product exceeded my expectations!")
print(result.output.sentiment)   # "positive"
```

- **Ошибки/предупреждения** – Если LLM не вернёт `final_answer`, агент будет продолжать цикл до ограничения `max_steps`.  

- **Где пригодится** – При интеграции со сторонними системами, требующими строгих JSON‑схем (отчёты, API‑ответы, дальнейшая автоматизация).  

---

## 86 chapter 4 «Implementing a basic ReAct agent» (стр. 130‑132)

### 4.8 Тестирование на GAIA‑бенчмарке (стр. 130‑132)

- **Главная мысль** – Оценка эффективности ReAct‑агента с веб‑поиском (MCP‑инструменты) против базовой модели без инструментов.  

#### 4.8.1 От LLM к агенту (стр. 130‑131)  
- **Шаги**  
  1. Загрузить MCP‑инструменты (`load_mcp_tools`).  
  2. Создать `Agent` с `output_type=GaiaOutput`, `max_steps=15`.  
  3. В функции `solve_problem` заменить прямой вызов LLM на `await agent.run(question)`.  
  4. Ограничить параллелизм семафором `SEMAPHORE = asyncio.Semaphore(3)`.  

#### 4.8.2 Результаты (стр. 131‑132)  
| Условие | Правильных | Стоимость |
|--------|------------|-----------|
| С веб‑поиском | 7/10 | $1.89 |
| Без веб‑поиска | 2/10 | $0.26 |

- **Ключевой вывод** – Инструмент `search_web` повышает точность на 50 % и позволяет отвечать на вопросы, требующие актуальной информации.  

- **Ошибки/предупреждения** – Агент без доступа к файлам (PDF, изображения) не решит задачи, где требуется обработка вложений; такие возможности добавляются в главе 5.  

- **Где пригодится** – При построении пайплайна автоматической верификации агентов, при отладке через `display_trace(context)` (стр. 131).  

---

## Введение в часть 2 (стр. 132‑133)

- **Главная мысль** – Первая часть дала базовый ReAct‑агент; в части 2 добавляются:  
  1. Поиск внешних знаний (RAG) и работа с файлами (гл 5),  
  2. Память в трёх слоях и HITL‑проверка (гл 6),  
  3. Планирование и самопроверка (гл 7),  
  4. Выполнение Python‑кода в песочнице и система навыков (гл 8),  
  5. Мульти‑агентные оркестрации (гл 9),  
  6. Систематическая оценка агентов (гл 10).  

- **Где пригодится** – При построении продакшн‑агентов, требующих обновляемой информации, долгосрочной памяти и масштабируемости.  

---

## 5 chapter 5 «Building knowledge bases with RAG» (стр. 134‑135)

- **Содержания нет** – В данном фрагменте только перечислен план главы (ключевые темы: поиск по ключевым словам, векторный поиск, графовый поиск, построение структуры файловой системы, паттерн callback). Подробный код и алгоритмы находятся в следующих страницах книги.  

- **Где пригодится** – При необходимости добавить в агент внешние индексы (векторные, графовые) и подключать RAG‑подсистемы для актуального извлечения информации.
