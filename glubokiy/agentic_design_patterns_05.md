<!-- gpt-oss:120b (Hermes), глубокое чтение, agentic_design_patterns_05.txt -->
**Часть 5 (стр. 122‑155) – Конспект по главам и подглавам**  

---

## 1. Пользовательский агент‑иерархия (стр. 122‑123)  
**Главная мысль** – В ADK можно создавать собственный агент `BaseAgent` с произвольным (не LLM) поведением и включать его в иерархию под‑агентов другого LLM‑агента.  
### Как делать  
1. Наследовать `BaseAgent`, задав `name` и `description`.  
2. Переопределить `async def _run_async_impl(self, context) -> AsyncGenerator[Event, None]`, где реализуется логика и `yield`‑ятся события.  
3. Создать LLM‑агенты (`LlmAgent`) с обязательным параметром `model` и инструкцией.  
4. Инициализировать кастомный агент (`TaskExecutor()`).  
5. Собрать «родительский» агент, указав `sub_agents=[greeter, task_doer]`.  
6. После инициализации ADK автоматически задаёт ссылки `parent_agent` у под‑агентов.  

### Правила и числа  
* `LlmAgent` **требует** указания модели (`model`) и инструкции (`instruction`).  
* Проверка иерархии: `assert greeter.parent_agent == coordinator` и аналогично для `task_doer`.  

### Шаблон кода (коротко)  
```python
class TaskExecutor(BaseAgent):
    name = "TaskExecutor"
    description = "Executes a predefined task."

    async def _run_async_impl(self, ctx):
        yield Event(author=self.name, content="Task finished successfully.")
```

### Ошибки / предупреждения  
* Не указать `model` у `LlmAgent` → исключение при создании.  

### Где пригодится  
* При построении систем, где часть шагов должна выполняться «вручную» (скриптами, API), а остальные – через LLM‑агенты (например, в автоматизированных бизнес‑процессах).

---

## 2. LoopAgent — итеративный рабочий процесс (стр. 123‑124)  
**Главная мысль** – `LoopAgent` позволяет выполнять под‑агенты последовательно в цикле, останавливаясь по условию, задаваемому кастомным агентом‑проверкой.  

### Как делать  
1. Описать кастомный агент‑проверку (`ConditionChecker`) → в `context.session.state` читаем значение `status`.  
2. Если `status == "completed"` → `yield Event(..., actions=EventActions(escalate=True))` (прерывает цикл).  
3. Иначе → `yield Event(..., content="Condition not met…")`.  
4. Создать LLM‑агент‑шаг (`ProcessingStep`) с инструкцией, которая при завершении ставит `status = "completed"`.  
5. Сконструировать `LoopAgent(name="StatusPoller", max_iterations=10, sub_agents=[process_step, ConditionChecker()])`.  

### Правила и числа  
* `max_iterations=10` — ограничитель количества проходов (стр. 124).  
* `EventActions(escalate=True)` — сигнал к завершению цикла.  

### Шаблон кода  
```python
class ConditionChecker(BaseAgent):
    async def _run_async_impl(self, ctx):
        status = ctx.session.state.get("status", "pending")
        if status == "completed":
            yield Event(author=self.name, actions=EventActions(escalate=True))
        else:
            yield Event(author=self.name,
                         content="Condition not met, continuing loop.")
```

### Ошибки / предупреждения  
* Не задать `model` у `LlmAgent` → ошибка (см. комментарий «Correction»).  

### Где пригодится  
* Периодический опрос статуса задачи, мониторинг прогресса, пауза‑проверка в ETL‑процессах.

---

## 3. SequentialAgent — линейный конвейер (стр. 124‑125)  
**Главная мысль** – `SequentialAgent` соединяет несколько агентов в строгой последовательности, передавая данные из `session.state` от одного шага к другому.  

### Как делать  
1. Создать простой `Agent`‑шаг 1 с `output_key="data"` — его ответ автоматически сохраняется в `session.state["data"]`.  
2. Создать `Agent`‑шаг 2 с инструкцией, обращающейся к `state['data']`.  
3. Объединить их в `SequentialAgent(name="MyPipeline", sub_agents=[step1, step2])`.  

### Шаблон кода  
```python
step1 = Agent(name="Step1_Fetch", output_key="data")
step2 = Agent(name="Step2_Process",
             instruction="Analyze state['data'] and provide a summary.")
pipeline = SequentialAgent(name="MyPipeline", sub_agents=[step1, step2])
```

### Ошибки / предупреждения  
* Не указать `output_key` у первого агента → результат не сохранится в `state`.  

### Где пригодится  
* Построение многошаговых аналитических пайплайнов, где каждый шаг обогащает контекст (например, «запрос‑выгрузка‑анализ‑отчёт»).

---

## 4. ParallelAgent — параллельные задачи (стр. 125‑126)  
**Главная мысль** – `ParallelAgent` запускает несколько под‑агентов одновременно, каждый сохраняет свой результат в `session.state` под различными ключами.  

### Как делать  
1. Определить отдельные `Agent`‑подзапросы (`weather_fetcher`, `news_fetcher`) с `output_key` (`weather_data`, `news_data`).  
2. Указать модель и инструкцию для каждого агента.  
3. Объединить в `ParallelAgent(name="data_gatherer", sub_agents=[weather_fetcher, news_fetcher])`.  

### Шаблон кода  
```python
weather_fetcher = Agent(name="weather_fetcher",
                       model="gemini-2.0-flash-exp",
                       instruction="Fetch the weather …",
                       output_key="weather_data")
news_fetcher = Agent(name="news_fetcher",
                     model="gemini-2.0-flash-exp",
                     instruction="Fetch the top news …",
                     output_key="news_data")
data_gatherer = ParallelAgent(name="data_gatherer",
                              sub_agents=[weather_fetcher, news_fetcher])
```

### Ошибки / предупреждения  
* Если забыть задать `output_key`, результат не попадёт в `state`.  

### Где пригодится  
* Одновременный сбор разнородных данных (погода + новости + курсы валют) перед их последующей агрегацией.

---

## 5. Агент‑как‑инструмент (слойный агент) (стр. 126‑129)  
**Главная мысль** – Один агент может вызывать другого агента через `AgentTool`, аналогично функции‑вызову, что позволяет построить иерархию «высоко‑уровневый планировщик → специализированный исполнитель».  

### Как делать  
1. **Создать функцию‑инструмент** (`generate_image(prompt)`) — возвращает словарь с `status`, `image_bytes`, `mime_type`.  
2. **Определить LLM‑агент‑исполнитель** (`image_generator_agent`) с `tools=[generate_image]` и инструкцией использовать этот инструмент.  
3. Обернуть исполнителя в `AgentTool` (`image_tool = AgentTool(agent=image_generator_agent, description=…)`).  
4. **Создать старший агент** (`artist_agent`) с инструкцией сначала придумать промт, затем вызвать `image_tool`.  

### Шаблон кода  
```python
def generate_image(prompt: str) -> dict:
    ...

image_generator_agent = LlmAgent(
    name="ImageGen",
    model="gemini-2.0-flash",
    description="Generates an image …",
    instruction="… use `generate_image` tool …",
    tools=[generate_image]
)

image_tool = agent_tool.AgentTool(
    agent=image_generator_agent,
    description="Use this tool to generate an image."
)

artist_agent = LlmAgent(
    name="Artist",
    model="gemini-2.0-flash",
    instruction="Invent a prompt, then call `ImageGen` tool.",
    tools=[image_tool]
)
```

### Ошибки / предупреждения  
* **Не** передавать входные данные в `generate_image` → инструмент не получит нужный промт.  
* Плохая «separation of concerns»: ставьте логику генерации изображения в инструмент, а формулирование промта — в LLM‑агент.  

### Где пригодится  
* Сложные задачи, где требуется предварительная подготовка данных (prompt engineering) перед вызовом специализированного сервиса (генерация изображений, кода, аудио).

---

## 6. Паттерн **Multi‑Agent Collaboration** (стр. 129‑131)  
**Главная мысль** – При решении сложных, многодоменных задач один агент делегирует подзадачи нескольким специализованным агентам; взаимодействие может быть последовательным, параллельным, иерархическим или дебатным.  

### Ключевые рекомендации (Rule of thumb)  
* Применять, когда задача **не помещается в рамки одного LLM‑агента** и её можно разбить на независимые подпроцессы, требующие разных экспертиз или инструментов (стр. 129).  

### Примерный визуальный шаблон (не код)  
```
          ┌─────────────┐
          │  Coordinator│
          └─────┬───────┘
   ┌─────────┼─────────────┐
   ▼         ▼             ▼
Greeter   TaskExecutor   … (другие специализированные агенты)
```

### Ошибки / предупреждения  
* Отсутствие чёткой инструкции у «координатора» → не будет понятна логика делегирования.  

### Где пригодится  
* Большие исследовательские проекты, разработка программного обеспечения, генерация мультимедийного контента со многими шагами.

---

## 7. Глава 8 — **Memory Management** (стр. 132‑152)

### 7.1 Краткое содержание (стр. 132‑133)  
* **Short‑Term Memory (контекстное)** — окно контекста LLM, хранит последние сообщения, результаты инструментов, рефлексии. Ограничено размером окна; может быть расширено «long‑context» моделями.  
* **Long‑Term Memory (постоянное)** — внешние хранилища (БД, графы, векторные базы). Позволяют семантический поиск, хранение знаний между сессиями.  

### 7.2 Практика в **Google ADK** (стр. 134‑142)  

#### 7.2.1 Session, State, Memory (стр. 135‑139)  
* **Session** – объект, представляющий один чат‑токен, хранит `id`, `app_name`, `user_id`, список `Event`, `state` и `last_update_time`. Управляется `SessionService`.  
* **State** – словарь (`session.state`)‑«scratchpad» для временных данных в текущей сессии. Ключи могут иметь префиксы:  
  * `user:` — общие для данного пользователя во всех сессиях,  
  * `app:` — общие для всех пользователей приложения,  
  * `temp:` — только на текущий ход, не сохраняются.  
* **MemoryService** – сервис долгосрочного хранилища (семантический поиск).  

#### 7.2.2 Выбор реализации `SessionService` (стр. 135‑138)  
| Реализация | Когда использовать | Пример кода |
|------------|--------------------|-------------|
| `InMemorySessionService` | Локальная разработка, тесты | `session_service = InMemorySessionService()` |
| `DatabaseSessionService` | Продакшен, требуется постоянство | `session_service = DatabaseSessionService(db_url="sqlite:///my.db")` |
| `VertexAiSessionService` | GCP‑продакшен, масштабируемость | `session_service = VertexAiSessionService(project, location)` |

#### 7.2.3 Обновление **state**  

* **Способ 1 – `output_key`** (стр. 137‑139) – указываем `output_key` в `LlmAgent`; Runner автоматически сохраняет финальный текст в `session.state[output_key]`.  

* **Способ 2 – `EventActions.state_delta`** (стр. 139‑141) – для сложных изменений (много полей, префиксы). Делать **только** через события, а не прямой доступ к `session.state`.  

#### 7.2.4 Пример Tool‑based обновления состояния (стр. 140‑141)  
```python
def log_user_login(tool_context: ToolContext) -> dict:
    state = tool_context.state
    state["user:login_count"] = state.get("user:login_count", 0) + 1
    state["task_status"] = "active"
    state["user:last_login_ts"] = time.time()
    state["temp:validation_needed"] = True
    return {"status": "success", "message": "..."}
```
*Важное предупреждение* (стр. 141): **не** изменять `session.state` напрямую — это обходит журнал событий, может нарушить согласованность и не сохраняется в выбранном `SessionService`.

#### 7.2.5 Долгосрочная память (`MemoryService`) (стр. 142‑144)  
* `InMemoryMemoryService` – временное хранилище (для тестов).  
* `VertexAiRagMemoryService` – продакшн‑решение, использующее RAG‑корпус Google Cloud. Параметры: `similarity_top_k`, `vector_distance_threshold`.  

#### 7.2.6 Пример использования `VertexAiRagMemoryService` (стр. 142‑144)  
```python
memory_service = VertexAiRagMemoryService(
    rag_corpus=RAG_CORPUS_RESOURCE_NAME,
    similarity_top_k=5,
    vector_distance_threshold=0.7
)
```

### 7.3 Memory Management в **LangChain / LangGraph** (стр. 143‑149)  

| Компонент | Что делает | Пример |
|-----------|------------|--------|
| `ChatMessageHistory` | Ручное хранение списка сообщений | `history.add_user_message("…")` |
| `ConversationBufferMemory` | Автоматически сохраняет диалог в переменную `history` (стр. 145) | `memory = ConversationBufferMemory(memory_key="history")` |
| `ConversationBufferMemory(return_messages=True)` | Возвращает список объектов сообщений, удобно для чат‑моделей (стр. 146) | `memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)` |
| `InMemoryStore` (LangGraph) | Хранит JSON‑документы; поддерживает векторный поиск | `store.put(namespace, "a-memory", {...})` |
| `VertexAiMemoryBankService` | Управляемый сервис Google, автоматически извлекает факты из диалогов и сохраняет их (стр. 150‑151) | `memory_service = VertexAiMemoryBankService(project, location, agent_engine_id)` |

### 7.4 Краткое резюме (стр. 151‑152)  
* **Ключевая мысль** – Нужно два уровня памяти: короткосрочная (контекст окна LLM, `session.state`) и долговременная (векторные/семантические хранилища).  
* **Правило** – Обновляйте `state` только через `output_key` или `EventActions.state_delta`; используйте `MemoryService` для постоянных знаний.  

### 7.5 Где пригодится (для Claude)  
* **Запросы**: «Как сохранить пользовательские предпочтения между сессиями?», «Как собрать историю диалога в контекст LLM?».  
* **Проверка**: убедиться, что `session.state` обновляется корректно, а `MemoryService` настроен под нужный тип данных.  
* **Память**: хранить текущие шаги задачи в `state`, а справочную информацию (техническую документацию, пользовательские профили) в `MemoryService`.  

---

## 8. Глава 9 — **Learning and Adaptation** (стр. 154‑155)

### 8.1 Главная мысль  
Агенты могут улучшать свои способности, меняя **политику действий**, **модели знаний** или **цели** на основе нового опыта: от классических методов RL до быстрых few‑shot‑адаптаций LLM‑агентов.  

### 8.2 Краткое перечисление подходов (стр. 154)  

| Тип обучения | Что делает | Пример применения |
|--------------|------------|-------------------|
| **Reinforcement Learning (RL)** | Агент получает награды/штрафы, формирует оптимальную политику | Управление роботами, игровые боты |
| **Supervised Learning** | Обучается на размеченных примерах | Классификация писем, прогнозирование трендов |
| **Unsupervised Learning** | Выявляет скрытые паттерны в неразмеченных данных | Кластеризация данных, построение карт знаний |
| **Few‑Shot / Zero‑Shot (LLM)** | Быстрая адаптация к новой задаче по нескольким примерам | Быстрый переход от чат‑бота к помощнику по коду |
| **Online Learning** | Постоянное обновление модели при поступлении новых данных | Потоковая обработка новостных лент |
| **Memory‑Based Learning** | Использует прошлый опыт из памяти для текущих решений | Рекомендательные системы, контекст‑aware ответы |

### 8.3 Алгоритм **PPO** (стр. 155)  
1. **Сбор данных** – агент генерирует траектории (state, action, reward).  
2. **Оценка целевой функции** – «surrogate»‑цель с «clipped»‑объективом, ограничивающим отклонения от текущей политики.  
3. **Обновление** – небольшие шаги в «доверительном» диапазоне, чтобы избежать катастрофических ухудшений.  

### 8.4 Алгоритм **DPO** (Direct Preference Optimization) (стр. 155)  
* Альтернатива PPO для согласования LLM с пользовательскими предпочтениями.  
* В традиционном подходе PPO используется два шага:  
  1. **Reward Model** — обучается на сравнениях ответов, полученных от людей.  
  2. **Fine‑tune** — LLM дорабатывается с помощью PPO, стремясь максимизировать предсказанные награды.  

* DPO — упрощённый способ, обходящий отдельную модель награды и PPO‑итерации (детали дальше в книге).  

### 8.5 Где пригодится (для Claude)  
* **Запросы**: «Как добавить он‑лайн обучение в мой агент‑скрипт?», «Как реализовать PPO‑тренинг для управления процессом?»  
* **Проверка**: наличие механизма сбора награды и корректного обновления политики.  
* **Обучение**: запланировать интеграцию DPO вместо сложного PPO, если нужна быстрая калибровка LLM под пользовательские предпочтения.

---  

### Итоги для Claude  

| Раздел | Что запомнить | Как использовать в ваших проектах |
|--------|----------------|-----------------------------------|
| **Custom Agent Hierarchy** | Наследование `BaseAgent`, построение дерева `parent_agent` | Делегировать простые скриптовые задачи в отдельный агент, оставив LLM‑агенту только диалог. |
| **LoopAgent** | Циклическое выполнение до `max_iterations` или `escalate` | Периодический мониторинг статуса длительных процессов (ETL, обучение). |
| **SequentialAgent** | Последовательный конвейер, обмен данными через `output_key` → `state` | Пайплайн «запрос → обработка → резюме». |
| **ParallelAgent** | Параллельный сбор данных, каждый агент пишет в отдельный `state`‑ключ | Одновременный сбор погоды, новостей, цены валют. |
| **Agent as a Tool** | Один агент вызывает другой через `AgentTool` | Высоко‑уровневый планировщик (artist) → специализированный генератор (image). |
| **Multi‑Agent Collaboration** | Делегирование задачи нескольким специализированным агентам (иерархия, параллель, последовательность) | Сложные бизнес‑процессы, где нужны разные экспертизы. |
| **Memory Management (ADK)** | `Session` + `State` (краткосрочная) ↔ `MemoryService` (долгосрочная); обновления только через `output_key` или `EventActions.state_delta`. | Хранить текущий статус задачи в `state`, а профиль пользователя в внешнем векторном хранилище. |
| **Memory Management (LangChain/Graph)** | `ConversationBufferMemory`, `InMemoryStore`, `VertexAiMemoryBankService`. | Быстро интегрировать память в цепочки LangChain, использовать Vertex Memory Bank для хранения фактов. |
| **Learning & Adaptation** | PPO — мягкое обновление политики; DPO — прямое согласование LLM с предпочтениями. | При необходимости адаптировать агента к новым сценариям (например, персонализировать ответы) использовать DPO, а для сложных управляющих задач – PPO. |

Эти конспекты позволяют быстро находить нужные конструкции ADK и связанные паттерны, а также помнить ключевые правила работы с памятью и обучением, что особенно ценно для одиночного предпринимателя, разрабатывающего свои скрипты и агентные системы.
