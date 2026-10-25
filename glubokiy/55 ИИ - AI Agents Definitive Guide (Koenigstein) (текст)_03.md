<!-- gpt-oss:120b (Hermes), глубокое чтение, 55 ИИ - AI Agents Definitive Guide (Koenigstein) (текст)_03.txt -->
**ЧАСТЬ 3 из 21 (стр. —) – Конспект по главам для Claude**  

> Эта часть охватывает две большие темы:  
> 1) **Структурированные методы рассуждения** (CoT, ToT, ReAct) и **Human‑in‑the‑Loop (HITL)** с готовыми паттернами и готовыми кусками кода LangGraph.  
> 2) **Многоагентные архитектуры** – супервизор, иерархия, ро́й (swarm) и сравнение их преимуществ/проблем.  
> В конце – начало **Глава 3** о reinforcement learning (RL) для агентов.  

---

## 1. Структурированные методы рассуждения (таблица 2‑3)  
**Главная мысль** – Четко определённые шаблоны — *Chain‑of‑Thought* (CoT), *Tree‑of‑Thoughts* (ToT) и *ReAct* — делают выводы LLM более надёжными, прозрачными и пригодными к интеграции в рабочий цикл агента.  

### Как пользоваться (общий процесс)  
1. **Определите тип задачи** (математика, креативный поиск, работа с инструментами).  
2. **Выберите подходящий паттерн** (CoT → поэтапный вывод; ToT → многовариантный поиск; ReAct → рассуждение + вызов инструмента).  
3. **Встроите выбранный паттерн в ваш LangGraph‑workflow** (см. главы 5‑9).  

### Правила / числа (из таблицы 2‑3)  

| Метод | Когда полезен | Плюсы | Минусы |
|------|----------------|-------|--------|
| **CoT** | Математика, планирование, аналитика | ↑ надёжность, ↑ прозрачность, позволяет использовать небольшие модели | ↓ скорость, verbose‑output, может генерировать правдоподобные, но ошибочные рассуждения |
| **ToT** | Творческое писательство, поиск стратегии | Исследует альтернативы, ↓ «first‑answer bias» | ↑ вычислительные затраты, ветвление растёт без обрезки |
| **ReAct** | Задачи, требующие одновременно рассуждения и вызова инструментов (поиск, код, API) | Интегрирует рассуждение + действие, создаёт audit‑trail, адаптируется к обратной связи | Сложное управление состоянием, риск бесконечного цикла без критериев останова |

### Шаблоны / примеры (из текста)  
- **CoT**: «Step‑by‑step reasoning for math, planning, analysis».  
- **ToT**: «Exploratory tasks with multiple solution paths (creative writing, strategy search)».  
- **ReAct**: «Tasks needing both reasoning and tool use (research, coding, APIs)».  

### Ошибки и предупреждения  
- **CoT** → не доверяйте «правдоподобным, но неверным» выводам.  
- **ToT** → контролируйте глубину ветвления (применяйте pruning).  
- **ReAct** → следите за зацикливанием: требуется чёткое условие остановки.  

### Где пригодится  
> Для построения **прозрачных, проверяемых** цепочек рассуждений в агенте‑помощнике (запросы, проверка кода, планирование).  

---

## 2. Human‑in‑the‑Loop (HITL) – зачем и как  

**Главная мысль** – Внедрение точек контроля, где агент **приостанавливается**, запрашивает подтверждение у человека и только затем продолжает, повышает надёжность, поддаёт процесс аудиту и упрощает внедрение в продакшн.  

### Основные паттерны прерываний (стр. —)  

| Прерывание | Когда используют |
|------------|-------------------|
| **Approve / Reject** | Пауза перед критическим шагом (например, HTTP‑запрос). |
| **Review and Edit** | Пауза для исправления/дополнения состояния графа. |
| **Review Tool Calls** | Инспекция аргументов инструмента, который влияет на внешние системы. |
| **Validate Human Input** | Запрос дополнительного контекста/информации у человека. |

### Как внедрять (пошаговый алгоритм)  

1. **Определите место в графе**, где нужна проверка.  
2. **Вставьте `interrupt(...)`** с нужным `question`, `schema` и текущими данными.  
3. **Получите ответ** (`v = interrupt(...)`).  
4. **По ответу** –  
   * если `approve` → `Command(goto=next_node, update={...})`  
   * если `revise` → обновите состояние и вернитесь к текущему узлу (`goto="b_gate"`).  
5. **Продолжайте исполнение** после получения подтверждения.  

### Правила / числа (из текста)  

- **Не помещайте** код, вызывающий side‑effects (API, DB) **в тот же узел**, где происходит `interrupt`.  
- **Всегда** ставьте паузу **перед** выполнением действия, требующего подтверждения.  

### Шаблоны кода (из примеров)  

```python
# 1️⃣ Пример: запрос у LLM план‑запроса → сохраняем в state
def b_propose(state):
    prompt = "Return only JSON with keys url and params ..."
    text = LLM.invoke(prompt).content
    m = re.search(r"\{.*\}", text, re.S)
    data = {"url": "https://httpbin.org/get", "params": {"q":"fallback","limit":1}}
    if m:
        try: data = json.loads(m.group(0))
        except: pass
    return {"proposed_request": data}
```

```python
# 2️⃣ Пример: "Approve or revise" gate
def b_gate(state) -> Command[Literal["b_call","b_propose"]]:
    v = interrupt({
        "question":"Approve or revise request",
        "proposed_request":state["proposed_request"],
        "schema":{...}})
    if v["action"] == "approve":
        return Command(goto="b_call", update={"decision":"approved"})
    # иначе – собрать изменения и вернуться к gate
    new_req = state["proposed_request"].copy()
    upd = v.get("update") or {}
    if "url" in upd: new_req["url"]=upd["url"]
    if isinstance(upd.get("params"), dict):
        new_req.setdefault("params",{}).update(upd["params"])
    return Command(goto="b_gate", update={"proposed_request":new_req,
                                         "decision":"revised"})
```

```python
# 3️⃣ Пример: Выполнение HTTP‑запроса после одобрения
def b_call(state):
    import requests
    r = requests.get(state["proposed_request"]["url"],
                      params=state["proposed_request"]["params"],
                      timeout=10)
    return {"api_result": {"status_code": r.status_code,
                           "url": r.url}}
```

```python
# 4️⃣ Пример: Review‑and‑edit текста
def c_edit(state):
    res = interrupt({
        "task":"Edit the summary text",
        "summary":state["summary"],
        "schema":{"type":"object",
                  "properties":{"edited_text":{"type":"string"}},
                  "required":["edited_text"]}})
    return {"summary": res["edited_text"]}
```

### Ошибки / предупреждения  
- **Не забывайте** возвращать `Command(resume=…)` при повторных запусках, иначе граф зациклится.  
- **Проверяйте** схему JSON‑payload: если она не соответствует, пользователь получит валидационную ошибку.  
- **Избегайте** бесконечного `interrupt → resume` без изменения состояния – будет «залипание».  

### Где пригодится  
> Для **чувствительных операций**: финансовые транзакции, запись в базу, изменения в инфраструктуре, а также для проверки качества генераций (текст, код).  

---

## 3. Параллельные прерывания (множественный ввод)  

**Главная мысль** – Иногда требуется собрать несколько независимых отзывов от разных людей (или от одного человека в разных ролях) одновременно, а потом продолжить, когда все ответы получены.  

### Пошаговый алгоритм (на примере 2‑20 и 2‑21)  

1. **Создайте отдельные узлы** (`d_h1`, `d_h2`) – каждый вызывает `interrupt(...)`.  
2. **Подключите их к `START`** (по обеим ветвям).  
3. **Скомпилируйте граф с `checkpointer`**, чтобы система могла «заморозить» состояние между прерываниями.  
4. При выполнении `stream` получаете список `interrupts` в состоянии.  
5. **Соберите ответы** в функции `wait_for_interrupt_and_prompt`:  
   - Вывести список `interrupt_id` и текущие значения.  
   - Запросить у пользователя новые значения (можно оставить пустым → оставить оригинал).  
   - Попытаться распарсить ввод как JSON (для структурированных правок).  
6. **Вернуть** `Command(resume=resume_map)`, где `resume_map` — словарь `interrupt_id → новое значение`.  

### Шаблоны кода  

```python
def wait_for_interrupt_and_prompt(app,cfg):
    state = app.get_state(cfg)
    ints = getattr(state,"interrupts",[]) or []
    if not ints: return None
    if len(ints)>1:
        print("\nMultiple interrupts pending:")
        for i,it in enumerate(ints,1):
            print(f"[{i}] id={it.interrupt_id} value={jdump(it.value)}")
        resume_map={}
        for it in ints:
            val = input(f"Value for {it.interrupt_id}: ").strip()
            if val:
                try: resume_map[it.interrupt_id]=json.loads(val)
                except: resume_map[it.interrupt_id]=val
            else:
                resume_map[it.interrupt_id]=it.value
        return Command(resume=resume_map)
```

### Ошибки / предупреждения  
- **Не смешивайте** side‑effects с `interrupt` в том же узле – может получиться двойное выполнение.  
- **Убедитесь**, что у всех параллельных прерываний есть уникальные `interrupt_id`.  

### Где пригодится  
> Для **многопользовательской проверки** (юридический + технический аудит), а также для параллельных запросов к разным специалистам внутри одного процесса.  

---

## 4. Многоагентные паттерны: супервайзер, иерархия, ро́й  

**Главная мысль** – Когда задачи растут в сложности, лучше делить их на независимые *специализированные* агенты и регулировать их взаимодействие через **супервизор** (центральный роутер), **иерархию** (супервизоры‑супервизоры) или **ро́й** (peer‑to‑peer hand‑off). Это повышает модульность, масштабируемость и контроль.  

### 4.1 Супервизор (один‑над‑одним)  

#### Алгоритм создания (пример 2‑22)  

1. **Определите список имён‑агентов** (`members`).  
2. **Сформируйте системный промпт**: «Ты — супервизор, выбирай, какой работник действует дальше, либо FINISH».  
3. **Определите тип‑структуру** `Router` с полем `next` (множество `["FINISH", *members]`).  
4. **Внутри узла** собирайте сообщения (`state["messages"]`), вызывайте LLM с `with_structured_output(Router)`.  
5. **Получите `goto`**: если `"FINISH"` → `END`, иначе → имя агента.  
6. **Верните `Command(goto=goto, update={"next":goto})`.**  

```python
def make_supervisor_node(llm,members):
    options=["FINISH"]+members
    system_prompt = (
        "You are a supervisor tasked with managing a conversation ..."
    )
    class Router(TypedDict):
        next: Literal[*options]
    def supervisor_node(state):
        messages=[{"role":"system","content":system_prompt}]+state["messages"]
        response=llm.with_structured_output(Router).invoke(messages)
        goto=response["next"]
        if goto=="FINISH": goto=END
        return Command(goto=goto, update={"next":goto})
    return supervisor_node
```

#### Где пригодится  
> Для **малых команд** с чётко разделёнными ролями (поиск + скрапинг + патентный запрос).  

---

### 4.2 Рабочие узлы‑агенты (пример 2‑23)  

```python
def make_react_worker_node(*, llm, name, tools, prompt=None, goto="supervisor"):
    agent = create_react_agent(llm, tools=tools, prompt=prompt)
    def node(state):
        result = agent.invoke(state)
        msgs = result.get("messages", [])
        content = getattr(msgs[-1],"content","") if msgs else ""
        return Command(
            update={"messages":[HumanMessage(content=content, name=name)]},
            goto=goto)
    return node
```

- **Создаём** `create_react_agent` (из LangGraph) с набором инструментов и роль‑промптом.  
- **Возвращаем** `Command` с обновлённым `messages` и переходом к `supervisor`.  

#### Где пригодится  
> Для **универсального шаблона**: любой специализированный агент (поиск, скрапинг, патентный поиск) может быть быстро подключён к общей схеме.  

---

### 4.3 Пример: Исследовательская команда  

| Агент | Инструмент | Промпт |
|------|------------|--------|
| `search` | `tavily_tool` | Role: Web researcher … |
| `web_scraper` | `scrape_webpages` | Role: Web scraper … |
| `exa_search` | `exa_search_tool` | Role: Research assistant … |
| `patent_research` | `patent_search` | Role: Market researcher … |

Код (пример 2‑25) **динамически** создаёт словарь `nodes` и присваивает каждое имя узлу через `make_react_worker_node`.  

#### Где пригодится  
> Для **быстрого прототипа** исследовательской группы, готовой к дальнейшему объединению в иерархию.  

---

### 4.4 Сборка графа исследования (пример 2‑27)  

1. **Создать `StateGraph(State)`**.  
2. **Добавить узлы**: `supervisor`, `search`, `web_scraper`, `exa_search`, `patent_research`.  
3. **Связать**: `START → supervisor`; каждый worker → `supervisor`; `supervisor` → выбранный worker; `FINISH` → `END`.  
4. **Компилировать** → `research_graph`.  

```python
research_builder = StateGraph(State)
research_builder.add_node("supervisor", research_supervisor_node)
research_builder.add_node("search", search_node)
...
research_builder.add_edge(START, "supervisor")
research_builder.add_edge("search","supervisor")
...
research_graph = research_builder.compile()
```

#### Запуск (пример 2‑28)  

```python
for s in research_graph.stream(
        {"messages":[("user","What are AI agents? …")]},
        {"recursion_limit":100}):
    print(s); print("---")
```

**Вывод** показывает последовательность: `supervisor → search → patent_research → __end__`.  

#### Где пригодится  
> Для **полноценного исследования** (поиск, скрапинг, патентный анализ) в рамках одного рабочего цикла.  

---

### 4.5 Иерархическая архитектура  

#### Шаг 1 – Создать «суперграф» (пример 2‑29)  

```python
super_builder = StateGraph(State)
super_builder.add_node("supervisor", teams_supervisor_node)
super_builder.add_node("research_team", call_research_team)
super_builder.add_node("writing_team", call_paper_writing_team)
super_builder.add_edge(START, "supervisor")
super_graph = super_builder.compile()
```

#### Шаг 2 – Запуск (пример 2‑30)  

```python
TASK_MSG = """Write an 800‑word whitepaper on semiconductor development…
               Use write_document tool, file_name="semiconductor_whitepaper.txt"."""
for step in super_graph.stream({"messages":[("user",TASK_MSG.strip())]}, {"recursion_limit":150}):
    print(step); print("---")
```

- **Супервизор** решает, какой под‑граф (исследовательский или писательский) активировать.  
- **Финальный результат** – автоматически сохранённый `.txt`‑файл.  

#### Где пригодится  
> Для **мульти‑командных пайплайнов** (исследование → написание → визуализация) с полной отделённостью уровней.  

---

### 4.6 Róй (swarm) – динамический hand‑off  

**Главная мысль** – Вместо жёсткой иерархии агенты обмениваются контролем через *handoff‑tool*, позволяя «передавать» задачу другому агенту по мере необходимости.  

#### Шаг 1 – Создать hand‑off‑инструменты (пример 2‑31)  

```python
to_writer = create_handoff_tool(
    agent_name="writer_assistant",
    description="Transfer to the writing assistant …")
to_research = create_handoff_tool(
    agent_name="research_assistant",
    description="Return to the research assistant …")
```

#### Шаг 2 – Определить роли (пример 2‑32)  

```python
research_assistant = create_react_agent(
    model=llm,
    tools=[tavily_tool, scrape_webpages, to_writer],
    prompt="You are a research assistant … hand off to writer when ready.")
writer_assistant = create_react_agent(
    model=llm,
    tools=[to_research],
    prompt="You are a writing assistant … hand back if more sources needed.")
```

#### Шаг 3 – Собрать ро́й (пример 2‑33)  

```python
swarm = create_swarm(
    agents=[research_assistant, writer_assistant],
    default_active_agent="research_assistant").compile()
```

#### Шаг 4 – Запуск (пример 2‑34)  

```python
user_request = {"messages":[{"role":"user","content":"""Find the current Swiss fintech licensing options…"""}]}
for chunk in swarm.stream(user_request):
    print(chunk); print()
```

- **Работает**: исследователь собирает источники → handoff → писатель синтезирует → (по необходимости) handoff обратно.  
- **Время выполнения** ~ 30 сек.  

#### Где пригодится  
> Для **гибкой коллаборации** между агентами, когда порядок действий неизвестен заранее (например, исследование ↔ письмо ↔ визуализация).  

---

## 5. Таблица 2‑4 – сравнение мульти‑агентных стратегий  

| Архитектура | Когда применять | Плюсы | Минусы |
|------------|----------------|-------|--------|
| **Supervisor** | Маленькие команды с чёткими границами задач | Простая настройка, сильный контроль, отсутствие deadlock‑ов | Узкое место, одна точка отказа |
| **Hierarchical** | Большие, многокомандные процессы, требующие масштабируемости | Модульность, масштабируемость, отражает оргструктуру | Труднее отлаживать, требует продуманного дизайна |
| **Swarm** | Динамичное совместное взаимодействие (исследователь ↔ писатель) | Гибкая обратная связь, естественный «back‑and‑forth» поток | Менее предсказуемо, нужен надёжный hand‑off‑механизм |

**Где пригодится** – Выбирайте **Supervisor** для простых пайплайнов, **Hierarchical** – когда хотите соединять целые под‑команды, **Swarm** – если порядок шагов может менятьcя «на лету».  

---

## 6. Начало **Глава 3** – reinforcement learning (RL) для агентов  

### Главная мысль  
RL обеспечивает **циклическую обратную связь**: агент → действие → наблюдение → награда → обновление политики. Для LLM‑агентов «действие», «наблюдение» и «награда» происходят в **языковом пространстве** (текст, вызов инструментов, промежуточные сообщения).  

### Ключевые определения (Таблица 3‑1)  

| Термин | Что означает |
|--------|---------------|
| **Online RL** | Агент генерирует новые rollout‑ы *во время обучения* и сразу же их использует для обновления. |
| **Offline RL** | Обучение происходит только на фиксальном наборе ранее собранных траекторий. |
| **On‑policy** | Обновление базируется на траекториях, полученных текущей (обновляемой) политикой. |
| **Off‑policy** | Траектории могут быть получены старой политикой, логами, демонстрациями человека и т.п. |
| **Model‑free RL** | Обучение без явной модели переходов среды; агент learns from reward feedback only. |
| **Model‑based RL** | Агент использует (или обучает) модель среды, чтобы планировать/симулировать перед действием. |

### Основные концепты (Таблица 3‑2)  

| Концепт | Что означает | Почему важно |
|---------|--------------|--------------|
| **Reward** | Сигнал «хорошо/плохо» | Замыкает цикл, без него агент не знает прогресса. |
| **Trajectory** | Полный порядок шагов (промпты, tool‑calls, ответы) от начала до результата | Позволяет инспектировать процесс, а не только итог. |
| **Rollout** | Полный прогоны одной задачи (может содержать несколько траекторий) | Сравнивать, оценивать, использовать для обучения. |
| **Policy** | Правило, которое сопоставляет контекст с очередным действием | Обновляется в процессе RL, делает агент «умнее». |
| **Reward / judge model** | Модуль, оценивающий траекторию (LLM‑as‑judge, программный скрипт, человек) | Превращает качественную оценку в числовой сигнал. |
| **Relative evaluation** | Сравнение нескольких rollout‑ов, чтобы определить лучший | Позволяет обучаться без ручных метрик, только через сравнение. |

### Где пригодится (напр.)  
> Для **само‑улучшения** агентов‑помощников: генерация нескольких вариантов ответа, оценка их «качества», автоматическое усиление лучшего пути.  

---

## 7. Обзор дальнейших тем (в начале главы 3)  

| Тема | Кратко |
|------|--------|
| **RL‑цикл** (рис. 3‑1, 3‑2) | От действия → награды → улучшение политики. |
| **Групповая относительная оптимизация** (GRPO, GSPO) | Вместо абсолютных наград используют **относительные ранги** внутри группы генераций. |
| **KL‑дивергенция** | Ограничивает «слишком быстрый» отступ от исходной политики (leash‑on‑curiosity). |
| **PPO vs DPO vs GRPO vs GSPO** (Таблица 3‑3) | Показана, какие методы требуют отдельной модели награды, критика и где применяется KL‑penalty. |

### Краткие цифры из Таблицы 3‑3  

| Метод | Reference policy | Reward / judge | Critic? | Уровень оптимизации |
|-------|------------------|----------------|--------|----------------------|
| **PPO (RLHF)** | Замороженная supervised‑модель | Обученная reward‑модель Rϕ | Да (value‑head) | Токен‑уровень |
| **DPO** | Замороженная πref | Нет (pairwise human prefs) | Нет | Секвенс‑уровень |
| **GRPO** | πref = πold (или другая) | LLM‑as‑judge / программа, per‑sample | Нет | Токен‑уровень, group‑normalized |
| **GSPO** | πold (или другая) | LLM‑as‑judge, per‑sample | Нет | Секвенс‑уровень, group‑normalized |

> Эти сведения помогут **выбрать** подходящий метод обучения, когда вы хотите улучшать **политику** вашего агента без полного пере‑обучения модели.  

---  

### Как использовать этот конспект в работе с Claude  

| Сценарий | Как применить из конспекта |
|----------|----------------------------|
| **Построить надёжный агент‑помощник** | Включить **CoT**/`ReAct`, добавить **HITL**‑gate перед внешними API (пример 2‑15/2‑16). |
| **Собрать несколько вариантов ответа и выбрать лучший** | Генерировать **GRPO‑style** группу ответов, использовать **relative evaluation** (таблица 3‑3). |
| **Разделить крупный проект на под‑задачи** | Создать **супервизор** (пример 2‑22) + **worker‑nodes** (пример 2‑23) → собрать **исследовательскую команду** (пример 2‑27). |
| **Добавить возможность «обратной связи» от коллег** | Использовать **параллельные прерывания** (пример 2‑20/2‑21). |
| **Создать гибкую коллаборацию исследователь ↔ писатель** | Построить **swarm** с **handoff‑tools** (пример 2‑31/2‑33). |
| **Обучать агента без доступа к весам модели** | Применять **он‑лайн RL** → генерировать **rollout‑ы**, оценивать их **LLM‑as‑judge**, обновлять **prompt‑pipeline** (раздел RL). |

---  

*Конспект построен строго из представленного текста; никаких добавлений и домыслов не включено.*
