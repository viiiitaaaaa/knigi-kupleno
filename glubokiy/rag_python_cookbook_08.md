<!-- gpt-oss:120b (Hermes), глубокое чтение, rag_python_cookbook_08.txt -->
## 8.6 Building a Sales Negotiation Agent with OpenAI’s Agents SDK and Chroma (стр. 257–258)
- **Главная мысль** – OpenAI Agents SDK — лёгкий фреймворк для создания агентов, поддерживающий ограничители, передачу управления между агентами и пошаговый трасс‑лог. Он позволяет организовать иерархическую делегацию через паттерн «модератор», передающий историю диалога суб‑агентам.
- **Как делать**  
  1. Оформите функции‑инструменты декоратором `@function_tool` (преобразует функцию в вызываемый агентом инструмент).  
  2. Включите трассировку SDK; просматривайте отдельные запуски на **OpenAI Platform Traces**.  
  3. При построении мульти‑агентных взаимодействий используйте «модератор», который:  
     - получает полную историю беседы,  
     - передаёт её каждому суб‑агенту,  
     - получает их ответы как инструменты.  
  4. Оцените необходимость: если важна низкая задержка, избегайте паттерна (каждая передача требует отдельного вызова LLM).  
- **Правила и числа** – каждый «hand‑off» — отдельный вызов LLM, стоимость растёт линейно с количеством ходов (стр. 258).  
- **Шаблоны и примеры** – фигуры 8‑19 и 8‑20 показывают трасс‑лог диалога «покупатель‑продавец».  
- **Ошибки и предупреждения** – Не применяйте модератор, если критична латентность; для простых делегирований лучше прямые вызовы функции.  
- **Где нам пригодится** – запросы типа «переговоры», маршрутизация поддержки, совместное редактирование, когда у ролей разные цели, но нужен общий контекст диалога.

---

## 8.7 Enriching Your Agent’s Capabilities with MCP Tools (стр. 259–264)
- **Главная мысль** – MCP (Model Context Protocol) позволяет аген тям подключать сторонние инструменты (в виде MCP‑серверов) без написания интеграционного кода. Пример: браузерный инструмент Playwright.
- **Как делать**  
  1. Установите SDK: `pip install openai-agents`.  
  2. Найдите нужный MCP‑сервер в NPM: `npm search @modelcontextprotocol`.  
  3. Установите Playwright‑MCP сервер:  
     ```bash
     npm install -g @modelcontextprotocol/server-playwright
     # или
     npm install -g @playwright/mcp@latest
     ```  
  4. Подключите сервер через `MCPServerStdio`:  
     ```python
     params = {"command": "npx", "args": ["@playwright/mcp@latest"]}
     async with MCPServerStdio(params=params, client_session_timeout_seconds=30) as server:
         tools = await server.list_tools()
     ```  
  5. Создайте агент с инструкциями «может просматривать веб и сохранять файлы», передав список серверов (`mcp_servers=[files, browser]`).  
  6. Запустите задачу через `Runner.run`, например поиск рецепта и сохранение в `recipe.md`.  
- **Правила и числа** – таймаут соединения по умолчанию 5 сек, в примерах поднят до **30 сек** (браузер) и **60 сек** (файловая система). На Windows возможны ошибки — рекомендуется Linux/WSL (стр. 259).  
- **Шаблоны и примеры** – код подключения к Playwright, перечисление доступных инструментов (стр. 261‑263), пример исследовательского агента, сохраняющего рецепт (стр. 262‑267).  
- **Ошибки и предупреждения** – Некоторые MCP‑серверы плохо работают в Windows/Jupyter; нужен Node.js + NPM (или Python + pip для Python‑серверов). Убедитесь, что `npx`/`uvx` доступны.  
- **Где нам пригодится** – когда агенту нужен доступ к веб‑браузеру, файловой системе или другим готовым сервисам без собственного кода (поиск рецептов, скачивание отчётов, автоматизация UI).

---

## 8.8 Building an Agentic System with LangGraph (стр. 264–272)
- **Главная мысль** – LangGraph моделирует агентскую логику как граф состояний: **State** (общие данные), **Nodes** (функции‑действия) и **Edges** (правила переходов). Позволяет строить циклы, вызывать инструменты и явно управлять потоком.
- **Как делать**  
  1. Установите зависимости:  
     ```bash
     pip install langgraph geopy requests langchain_openai langchain-core pydantic
     ```  
  2. Описание **State** — `TypedDict` с полем `messages` (редуктор `add_messages`) и счётчиком шагов.  
  3. Определите схемы ввода для инструментов через Pydantic (`SearchInput`, `AudioInput`).  
  4. Оформите функции‑инструменты декоратором `@tool` (`get_weather_forecast`, `transcribe_audio`).  
  5. Свяжите инструменты с LLM:  
     ```python
     llm = ChatOpenAI(model="gpt-5.2", temperature=1.0, max_retries=2)
     model = llm.bind_tools([get_weather_forecast])
     ```  
  6. Реализуйте узлы:  
     - `call_model(state, config)` — вызывает LLM, возвращает новые сообщения.  
     - `call_tool(state)` — перебирает `tool_calls` последнего сообщения, вызывает соответствующий инструмент, формирует `ToolMessage`.  
  7. Определите условный переход `should_continue(state)`: если в последнем сообщении есть `tool_calls` — возвращаем `"continue"`, иначе `"end"`.  
  8. Постройте граф:  
     ```python
     workflow = StateGraph(AgentState)
     workflow.add_node("llm", call_model)
     workflow.add_node("tools", call_tool)
     workflow.set_entry_point("llm")
     workflow.add_conditional_edges("llm", should_continue,
         {"continue": "tools", "end": END})
     workflow.add_edge("tools", "llm")
     graph = workflow.compile()
     ```  
  9. Визуализируйте (`graph.get_graph().draw_mermaid_png()`).  
  10. Запустите с потоковой печатью шагов, при необходимости добавляйте новые сообщения в `state["messages"]` для продолжения.  
- **Правила и числа** – `client_session_timeout_seconds` = 30/60 сек, `max_retries` = 2, `temperature` = 1.0, векторные индексы используют `END` как финальный узел.  
- **Шаблоны и примеры** – полные куски кода для состояния, инструментов, узлов, графа и примера запуска (стр. 265‑270).  
- **Ошибки и предупреждения** – Не используйте LangGraph для простых линейных цепочек (стр. 272); иначе добавляется лишняя сложность. Следите, чтобы условные переходы не образовывали бесконечных циклов. Фреймворк сильно связывает код с графовой моделью, миграция будет дорогостоящей.  
- **Где нам пригодится** – сложные мультишаговые задачи, где нужен контроль над циклом (планирование, вызов внешних сервисов, «ReAct»‑парадигма), а также отладка пути выполнения и совместное состояние нескольких агентов.

---

## 9.1 Creating Your First Neo4j Knowledge Graph and Feeding It with Text from Documents (стр. 277–284)
- **Главная мысль** – Построить граф знаний SLA‑контрактов в Neo4j: узлы — `Company`, `SLA`, `Clause`, `ClauseType`; ребра — `HAS_CLAUSE`, `NEXT`, `OF_TYPE`. Сохраняет порядок текста и типы пунктов.
- **Как делать**  
  1. Установите Neo4j (Desktop или Aura) и Python‑клиент: `pip install neo4j python-dotenv`.  
  2. Поместите параметры соединения в `.env` (`NEO4J_URI`, `NEO4J_USERNAME`, `NEO4J_PASSWORD`).  
  3. Реализуйте `get_driver()` → `GraphDatabase.driver(...)`.  
  4. Создайте уникальные ограничения:  
     ```cypher
     CREATE CONSTRAINT sla_id IF NOT EXISTS FOR (s:SLA) REQUIRE s.id IS UNIQUE;
     CREATE CONSTRAINT clause_id IF NOT EXISTS FOR (c:Clause) REQUIRE c.id IS UNIQUE;
     CREATE CONSTRAINT type_name IF NOT EXISTS FOR (t:ClauseType) REQUIRE t.name IS UNIQUE;
     ```  
  5. Парсите SLA‑файл: разбейте по заголовкам `##` → список объектов `Clause(id, title, text, order)`.  
  6. Запишите в граф:  
     - `MERGE (s:SLA {id:$id}) SET s.title=$title`.  
     - `MERGE (cl:Clause {id:$id}) SET cl.title=$title, cl.text=$text, cl.order=$order`.  
     - `MERGE (s)-[:HAS_CLAUSE]->(cl)`.  
     - `MERGE (a)-[:NEXT]->(b)` для последовательных пунктов.  
  7. Определите тип пункта по ключевым словам (`infer_clause_type`).  
  8. Создайте узлы `ClauseType` и ребра `OF_TYPE`.  
  9. Проверьте граф простым запросом `MATCH (s:SLA)-[:HAS_CLAUSE]->(cl:Clause) RETURN … ORDER BY cl.order`.  
- **Правила и числа** – ID пунктов формируются как `"{sla_id}_C{idx}"`. Ограничения `IF NOT EXISTS`. Список ключевых слов для типизации (стр. 268).  
- **Шаблоны и примеры** – код функций `create_constraints`, `parse_sla_file`, `write_sla_and_clauses`, `infer_clause_type`, `add_clause_types`.  
- **Ошибки и предупреждения** – Без ограничений могут появиться дубликаты; не храните `.env` в репозитории; корректно обрабатывайте отсутствие заголовков.  
- **Где нам пригодится** – когда нужны точные извлечения из контрактов, сравнение пунктов, навигация по порядку и типу (комплаенс, аудит, юридический поиск).

---

## 9.2 Extending the Knowledge Graph with Structured Data (стр. 285–288)
- **Главная мысль** – Обогащаем граф бизнес‑данными (компании, адреса, расходы, метаданные SLA), чтобы делать запросы, учитывающие контекст предприятия.
- **Как делать**  
  1. **Компании**: `UNWIND $rows AS row MERGE (c:Company {supplier_id:row.supplier_id}) ON CREATE SET c.name=row.name, c.country=row.country, c.industry=row.industry`.  
  2. **Адреса**: аналогично, `MERGE (a:Address {id:row.id})` с полями `street, city, postal_code, country`.  
  3. **Связь Company‑Address**: `MATCH (c:Company {supplier_id:row.supplier_id}) MATCH (a:Address {id:row.address_id}) MERGE (c)-[:LOCATED_AT]->(a)`.  
  4. **Расходы**: `MATCH (c:Company {supplier_id:row.supplier_id}) SET c.spend_2024=toFloat(row.spend_eur), c.spend_category=row.spend_category`.  
  5. **SLA‑метаданные**: `MERGE (s:SLA {id:row.sla_id}) ON CREATE SET s.title=row.title, s.service_name=row.service_name, s.governing_law=row.governing_law, s.effective_date=CASE WHEN row.effective_date IS NOT NULL THEN date(row.effective_date) ELSE NULL END MERGE (c)-[:HAS_SLA]->(s)`.  
- **Правила и числа** – `UNWIND $rows AS row` шаблон, `toFloat` для расходов, обработка `"N/A"` в датах (`replace` → `None`).  
- **Шаблоны и примеры** – функции `load_companies`, `load_addresses`, `connect_company_addresses`, `load_spend`, `load_slas`.  
- **Ошибки и предупреждения** – Совпадение столбцов CSV с полями в запросе; обновляйте данные при изменениях в источниках, иначе получаются ошибочные фильтры.  
- **Где нам пригодится** – запросы типа «какие крупные поставщики без пункта прекращения контракта?», «какие немецкие компании имеют обязательства по защите данных?», объединяющие текстовые и бизнес‑атрибуты.

---

## 9.3 Building Your First Cypher Query (стр. 289–291)
- **Главная мысль** – Пример базовых и чуть более продвинутых запросов Cypher для извлечения пунктов SLA, фильтрации по типу и бизнес‑правилам.
- **Как делать**  
  1. **Все пункты одного SLA** (упорядочено):  
     ```cypher
     MATCH (s:SLA {id:$sla_id})-[:HAS_CLAUSE]->(cl:Clause)
     RETURN cl.order AS order, cl.title AS title, cl.text AS text
     ORDER BY order
     ```  
  2. **Пункты конкретного типа** по всем компаниям:  
     ```cypher
     MATCH (c:Company)-[:HAS_SLA]->(s:SLA)-[:HAS_CLAUSE]->(cl:Clause)
     MATCH (cl)-[:OF_TYPE]->(t:ClauseType {name:$clause_type})
     RETURN c.name, s.id, cl.order, cl.title, cl.text
     ORDER BY c.name, s.id, cl.order
     ```  
  3. **Высокие расходы + отсутствие пункта прекращения**:  
     ```cypher
     MATCH (c:Company)-[:HAS_SLA]->(s:SLA)
     WHERE c.spend_2024 > $min_spend
     OPTIONAL MATCH (s)-[:HAS_CLAUSE]->(cl:Clause)-[:OF_TYPE]->(t:ClauseType {name:"Termination"})
     WITH c, s, count(cl) AS num_termination
     WHERE num_termination = 0
     RETURN c.name, c.spend_2024, s.id
     ORDER BY c.spend_2024 DESC
     ```  
  4. **Поиск фраз в пунктах доступности**:  
     ```cypher
     MATCH (c:Company)-[:HAS_SLA]->(s:SLA)-[:HAS_CLAUSE]->(cl:Clause)
     MATCH (cl)-[:OF_TYPE]->(t:ClauseType {name:"Availability"})
     WHERE toLower(cl.text) CONTAINS toLower($phrase)
     RETURN c.name, s.id, cl.order, cl.text
     ORDER BY c.name, s.id, cl.order
     ```  
  5. **Клаузы защиты данных для компаний в EU‑странах**:  
     ```cypher
     MATCH (c:Company)-[:LOCATED_AT]->(a:Address)
     WHERE a.country IN $countries
     MATCH (c)-[:HAS_SLA]->(s:SLA)-[:HAS_CLAUSE]->(cl:Clause)
     MATCH (cl)-[:OF_TYPE]->(t:ClauseType {name:"DataProtection"})
     RETURN c.name, a.country, s.id, cl.order, cl.text
     ORDER BY a.country, c.name, s.id, cl.order
     ```  
- **Правила и числа** – В запросах используется `WHERE c.spend_2024 > $min_spend`; `OPTIONAL MATCH` для отсутствующих пунктов.  
- **Шаблоны и примеры** – полностью приведённый код функций Python `list_clauses_for_sla`, `clauses_of_type`, `high_spend_missing_termination`, `availability_clauses`, `eu_data_protection_clauses`.  
- **Ошибки и предупреждения** – Убедитесь, что указанные свойства (`spend_2024`, `country`) действительно существуют; иначе запрос вернёт пустой набор.  
- **Где нам пригодится** – быстрые точечные запросы к графу для комплаенса, сравнения пунктов, предварительная фильтрация перед семантическим поиском.

---

## 9.4 Enabling Semantic Search on a Neo4j Knowledge Graph (стр. 292–295)
- **Главная мысль** – Комбинировать векторные эмбеддинги (OpenAI `text-embedding-3-small`) с графовыми фильтрами, создавая гибридный поиск: сначала семантическое сходство, затем ограничение по бизнес‑атрибутам.
- **Как делать**  
  1. **Генерация эмбеддингов**:  
     ```python
     def create_embedding(text):
         return client.embeddings.create(
                 model="text-embedding-3-small", input=text
             ).data[0].embedding
     ```  
  2. **Запись эмбеддингов в узлы Clause**:  
     ```python
     for row in clauses:
         emb = create_embedding(row["text"])
         session.run(
             "MATCH (cl:Clause {id:$id}) SET cl.embedding=$emb",
             id=row["id"], emb=emb)
     ```  
  3. **Создание векторного индекса**:  
     ```cypher
     CREATE VECTOR INDEX clause_embeddings IF NOT EXISTS
     FOR (c:Clause) ON c.embedding
     OPTIONS {
         indexConfig: {
             `vector.dimensions`: 1536,
             `vector.similarity_function`: "cosine"
         }
     }
     ```  
  4. **Семантический поиск**:  
     ```cypher
     CALL db.index.vector.queryNodes(
         "clause_embeddings", $top_k, $embedding
     ) YIELD node, score
     RETURN node.title AS title, node.text AS text, score
     ORDER BY score DESC
     ```  
  5. **Гибридный поиск с фильтром отрасли**: добавьте `MATCH (node)<-[:HAS_CLAUSE]-(s:SLA)<-[:HAS_SLA]-(c:Company) WHERE c.industry = $industry`.  
- **Правила и числа** – Размерность эмбеддинга = **1536**, функция схожести = **cosine**. Параметр `top_k` задаёт количество возвращаемых результатов.  
- **Шаблоны и примеры** – функции `create_clause_embeddings`, `create_vector_index`, `semantic_search`, `hybrid_search_by_industry`.  
- **Ошибки и предупреждения** – Эмбеддинги необходимо генерировать один раз и поддерживать актуальность при добавлении новых пунктов; векторный индекс создаётся один раз.  
- **Где нам пригодится** – запросы, где нужен смысловой поиск (например «клауза о гарантии uptime > 99.9 %») одновременно с бизнес‑ограничениями (отрасль, регион, уровень расходов).

---

## 9.5 Optimizing the Knowledge Graph for RAG Systems (стр. 295–296)
- **Главная мысль** – Улучшить граф дополнительными атрибутами (резюме, агрегаты, риск‑оценки) и индексами, чтобы ускорить и уточнить извлечение.
- **Как делать**  
  1. **Суммирование пунктов**:  
     ```python
     def summarize_clause(text):
         prompt = f"Summarize this SLA clause:\n\n{text}"
         return client.chat.completions.create(
                 model="gpt-4o-mini",
                 messages=[{"role":"user","content":prompt}],
                 max_tokens=120).choices[0].message.content
     ```  
  2. **Добавление резюме в граф**:  
     ```python
     def add_clause_summaries():
         driver = get_driver()
         result = driver.session().run(
             "MATCH (cl:Clause) WHERE cl.summary IS NULL RETURN cl.id AS id, cl.text AS text")
         for row in result:
             s = summarize_clause(row["text"])
             driver.session().run(
                 "MATCH (cl:Clause {id:$id}) SET cl.summary=$s", id=row["id"], s=s)
     ```  
     (печать прогресса каждые 5 пунктов).  
  3. **(Опционально) Создать векторный индекс для полей `summary`** – аналогично пункту 4.2.  
  4. **Агрегаты** – пример подсчёта количества пунктов каждого типа на компанию:  
     ```cypher
     MATCH (c:Company)-[:HAS_SLA]->(s:SLA)-[:HAS_CLAUSE]->(cl:Clause)-[:OF_TYPE]->(t:ClauseType)
     WITH c, t.name AS type, count(cl) AS cnt
     MERGE (c)-[r:TYPE_COUNT]->(t)
     SET r.count = cnt
     ```  
- **Правила и числа** – LLM — `gpt-4o-mini`, `max_tokens=120`; выводится каждые **5** пунктов.  
- **Шаблоны и примеры** – функции `summarize_clause`, `add_clause_summaries`, пример Cypher‑агрегации.  
- **Ошибки и предупреждения** – Не пересчитывайте резюме, уже существующие (`WHERE cl.summary IS NULL`). Учтите стоимость LLM‑вызовов. При добавлении агрегатов следите за актуальностью данных.  
- **Где нам пригодится** – ускоренный поиск по резюме вместо полного текста, предварительный отбор для RAG, аналитика (сколько пунктов определённого типа у каждого поставщика).

---

## Страницы 274–275
**содержания нет** (в этой части только оглавление/первая строка главы).
