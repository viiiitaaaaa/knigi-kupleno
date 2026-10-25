<!-- gpt-oss:120b (Hermes), глубокое чтение, rag_python_cookbook_05.txt -->
**Часть 5 из 11 – “Embeddings” (стр. 153‑159) и начало главы 6 “Vector Databases and Similarity Searches” (стр. 160‑185)**  

---

## 5.6 Performing Text Classification with Embeddings (стр. 153–154)  
- **Главная мысль** – Классификация → обучаем модель (random forest), которая по векторам‑эмбеддингов распределяет запросы в заранее заданные категории, тем самым ускоряя поиск.  
- **Как делать**  
  1. Создать клиент `OpenAI()`.  
  2. Функция `create_embeddings(text_chunk, client)` → вектор size = 1536 (модель *text‑embedding‑3‑small*).  
  3. Применить её к колонке `text` в DataFrame → получить колонку `embedding`.  
  4. Подготовить целевую переменную `y = chunks_df["label"]`.  
  5. Преобразовать каждый вектор в строку‑столбцы (`X = chunks_df["embedding"].apply(lambda x: pd.Series(eval(x)) … )`).  
  6. Обучить `RandomForestClassifier()` → `clf.fit(X, y)`.  
  7. Для нового вопроса → получить эмбеддинг, предсказать класс `clf.predict` и вероятность `clf.predict_proba`.  
- **Правила и числа**  
  - Размерность эмбеддинга = 1 536 (стр. 153).  
  - Пример вероятности: 94 % для *Premier_League* (стр. 153).  
- **Шаблоны и примеры**  
  ```python
  client = OpenAI()
  embedding = client.embeddings.create(input=[text], model="text-embedding-3-small").data[0].embedding
  clf = RandomForestClassifier()
  clf.fit(X, y)
  pred = clf.predict([new_embedding])
  prob = clf.predict_proba([new_embedding])
  ```  
- **Ошибки и предупреждения**  
  - Если в колонке `embedding` хранятся строки, требуется `eval(x)` → может бросать ошибку при некорректных данных.  
- **Где пригодится** – При построении RAG‑конвейера, где необходимо быстро направлять запросы в отдельные домены (спорт, политика, финансы) → сокращение объёма поиска (стр. 154).  

---

## 5.7 Improving Search Results with a Hybrid Search Approach (стр. 155–159)  
- **Главная мысль** – Объединить два независимых ранжира: BM25‑поиск по ключевым словам и семантический поиск по векторам, а затем слить их через Reciprocal Rank Fusion (RRF) для лучшего качества.  
- **Как делать**  
  1. **BM25**:  
     - Установить `pip install openai rank-bm25 sentence-transformers pandas`.  
     - Токенизировать документы, создать `BM25Okapi`, получить `bm25_scores`.  
     - Сформировать список `keyword_ranking_doc_ids` (по убыванию `score`).  
  2. **Семантический поиск**:  
     - Сгенерировать эмбеддинги документов (`create_embedding`).  
     - Сгенерировать эмбеддинг запроса.  
     - Вычислить косинусное сходство (`cos_sim`).  
     - Сформировать `semantic_ranking_doc_ids`.  
  3. **RRF**:  
     - Выбрать параметр `k` (обычно 60; более высокие → меньший вес топ‑рангов).  
     - Построить таблицу с колонками `keyword_rank`, `semantic_rank`.  
     - Вычислить `rrf_score = 1/(k+keyword_rank) + 1/(k+semantic_rank)`.  
     - Отсортировать по `rrf_score` → `final_ranking_doc_ids`.  
- **Правила и числа**  
  - Параметр `k` = 60 (стр. 157).  
  - При выборе `k` = 10‑20 → акцент на совпадениях в верхних позициях; 60‑100 → учитываются более низкие ранги (стр. 159).  
  - Минимум ≈ 100‑200 размеченных фрагментов для надёжной классификации (стр. 154).  
  - Не использовать гибридный поиск, если набор < 10 000 документов (стр. 154).  
- **Шаблоны и примеры**  
  ```python
  # BM25
  bm25 = BM25Okapi([c.split() for c in text_chunks])
  bm25_scores = bm25.get_scores(user_query.split())
  # Semantic
  query_emb = create_embedding(user_query)
  embeddings_df["similarity"] = cos_sim(embeddings_df["embedding"], query_emb)
  # RRF
  k = 60
  rrf_df["rrf_score"] = 1/(k+rrf_df["keyword_rank"]) + 1/(k+rrf_df["semantic_rank"])
  final_ids = rrf_df.sort_values("rrf_score", ascending=False)["doc_id"].tolist()
  ```  
- **Ошибки и предупреждения**  
  - Не применять гибрид, если запросы чисто «натуральные», без технических терминов (стр. 159).  
  - При сильно перекрывающихся доменах лучше использовать метаданные‑фильтрацию, а не принудительное одно‑категориальное классифицирование (стр. 154).  
- **Где пригодится** – При поиске в коллекциях, где есть точные идентификаторы (SKU, ICD‑10, URL‑пути) вместе с естественными формулировками запросов (стр. 158‑159).  

---

## 6.1 Choosing the Right Vector Database (стр. 162–163)  
- **Главная мысль** – Выберите векторное хранилище, исходя из сценария (offline vs live), наличия бизнес‑данных рядом, масштаба и ограничений инфраструктуры.  
- **Как делать**  
  1. **Шаг 1**: Определить, нужен ли векторный поиск в живом сервисе.  
     - Если только offline → FAISS/Annoy (либо Chroma для локального прототипа).  
  2. **Шаг 2**: Если live, решить, должны ли векторы жить рядом с бизнес‑данными.  
     - Да → использовать уже имеющуюся СУБД (PostgreSQL + pgvector, MongoDB, Redis, Cassandra).  
  3. **Шаг 3**: Оценить масштаб и требования к фильтрации/контролю доступа.  
     - Миллионы‑десятки миллионов → цель‑специфичные или управляемые векторные БД (Weaviate, Qdrant, Milvus, Pinecone).  
  4. **Шаг 4**: Сопоставить практические вопросы (Таблица 6‑1) – например, разрешено ли отправлять данные в облако? – и выбрать кандидатов.  
  5. Сравнить оставшиеся варианты (Таблица 6‑2) по *pros* и *cons*.  
- **Правила и числа**  
  - < 10 000 документов → не стоит тратить ресурсы на классификатор (стр. 154).  
  - При классификации нужен минимум 100–200 размеченных фрагментов на категорию (стр. 154).  
- **Шаблоны и примеры**  
  - Таблица 6‑1 «Практические вопросы»:  
    | Вопрос | Если да → lean toward |
    |--------|-----------------------|
    | Можно отправлять данные в облако? | Pinecone или cloud‑managed PostgreSQL |
    | Уже работает PostgreSQL/MongoDB? | pgvector или MongoDB vector search |
    | Нужно комбинировать keyword‑search с векторами? | Elasticsearch, OpenSearch, Weaviate |
    | Нужен минимум настройки? | Chroma или управляемый Pinecone |
  - Таблица 6‑2 *Pros/Cons* для FAISS, Chroma, PostgreSQL, Weaviate.  
- **Ошибки и предупреждения**  
  - Не выбирать по «бенчмаркам», а ориентироваться на рабочий процесс (стр. 164).  
  - Не использовать тяжёлый векторный сервис, если требуется лишь несколько тысяч векторов в прототипе (стр. 164).  
- **Где пригодится** – При планировании RAG‑архитектуры: быстро подобрать подходящее хранилище под свои ограничения (стр. 162‑165).  

---

## 6.2 Storing and Searching Embeddings with FAISS (стр. 165–168)  
- **Главная мысль** – FAISS — лёгкая библиотека для быстрых векторных поисков без постоянного хранилища и без метаданных. Идеальна для одноразовых/пакетных задач.  
- **Как делать**  
  1. Установить: `pip install faiss-cpu openai numpy`.  
  2. Сгенерировать эмбеддинги (OpenAI model `text-embedding-3-small`).  
  3. Преобразовать массив в `float32`.  
  4. Создать индекс `faiss.IndexFlatL2(dimension)`.  
  5. Добавить эмбеддинги: `index.add(document_embeddings)`.  
  6. Для запроса: генерировать embedding, вызвать `index.search(query_embedding, k)` → получить расстояния и индексы.  
- **Правила и числа**  
  - Размерность = 1536 (стр. 166).  
  - Индекс = `IndexFlatL2` (L2‑расстояние) – один из самых простых.  
- **Шаблоны и примеры**  
  ```python
  index = faiss.IndexFlatL2(document_embeddings.shape[1])
  index.add(document_embeddings)               # add N vectors
  distances, indices = index.search(query_emb.reshape(1, -1), k=5)
  retrieved = [text_chunks[i] for i in indices[0]]
  ```  
- **Ошибки и предупреждения**  
  - FAISS хранит всё в памяти; при больших объёмов может не хватить RAM (стр. 168).  
  - Нет поддержки фильтрации метаданных и контроля доступа (стр. 168).  
- **Где пригодится** – Временный анализ (например, обработка одного контракта, исследовательские скрипты) → быстрый векторный поиск без необходимости постоянного хранилища (стр. 168).  

---

## 6.3 Storing and Working with Embeddings in a Chroma Vector Database (стр. 169–172)  
- **Главная мысль** – Chroma — лёгкая, встроенная в файл векторная БД с простой установкой, поддержкой постоянства и базовым метаданным‑фильтром, подходящая для прототипов и небольших проектов.  
- **Как делать**  
  1. Установить: `pip install chromadb openai`.  
  2. Создать клиент `chromadb.PersistentClient(path=VECTOR_STORE_PATH)`.  
  3. Получить/создать коллекцию `collection = client.get_or_create_collection(name=COLLECTION_NAME)`.  
  4. Сгенерировать эмбеддинги (OpenAI model `text-embedding-3-small`).  
  5. Добавить данные:  
     ```python
     collection.add(
         embeddings=embeddings_list,
         documents=text_chunks,
         ids=[str(i) for i in range(len(text_chunks))]
     )
     ```  
  6. Запрос:  
     ```python
     query_emb = get_embedding(query)
     results = collection.query(query_embeddings=[query_emb], n_results=3)
     ```  
- **Правила и числа**  
  - Доступен два режима: *Ephemeral* (в памяти) и *Persistent* (на диск).  
  - По умолчанию Chroma использует Sentence‑Transformer `all‑MiniLM‑L6‑v2`, но допускает внешние эмбеддинги (стр. 171).  
- **Шаблоны и примеры**  
  ```python
  chroma_client = chromadb.PersistentClient(path="../02_Data/00_Vector_Store")
  coll = chroma_client.get_or_create_collection(name="my_collection")
  coll.add(embeddings=emb_list, documents=texts, ids=["0","1",...])
  res = coll.query(query_embeddings=[query_emb], n_results=3)
  ```  
- **Ошибки и предупреждения**  
  - Не подходит, если набор > ≈ 300 000 векторов, нужен контроль доступа или суб‑миллисекундные задержки (стр. 172).  
  - При масштабировании может потребоваться миграция в PostgreSQL + pgvector или управляемую БД (стр. 172).  
- **Где пригодится** – Быстрый прототип RAG‑агента с небольшим набором (до нескольких сотен тысяч) векторов, где требуется сохранённость между запусками (стр. 170‑172).  

---

## 6.4 Storing Embeddings in PostgreSQL with the pgvector Extension (стр. 173–176)  
- **Главная мысль** – pgvector добавляет тип `vector` и операторы сравнения в PostgreSQL, позволяя хранить эмбеддинги рядом с бизнес‑данными и выполнять векторный поиск через привычный SQL.  
- **Как делать**  
  1. **Установить** PostgreSQL + pgvector (Docker `ankane/pgvector` или локальная установка).  
  2. Запустить контейнер (docker‑compose.yml, пример в тексте).  
  3. Установить Python‑зависимости: `pip install psycopg2-binary openai`.  
  4. Подключиться к БД через `psycopg2`.  
  5. Создать расширение и таблицу:  
     ```sql
     CREATE EXTENSION IF NOT EXISTS vector;
     CREATE TABLE embeddings (
         id SERIAL PRIMARY KEY,
         chunk TEXT NOT NULL,
         embedding vector(1536) NOT NULL
     );
     ```  
  6. Сгенерировать эмбеддинги (OpenAI model `text-embedding-3-small`) и INSERT‑ить их в таблицу.  
- **Правила и числа**  
  - Размерность вектора = 1536 (стр. 176).  
  - При использовании Docker‑compose задаются переменные `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_DB`.  
- **Шаблоны и примеры**  
  ```python
  cur.execute("""
      INSERT INTO embeddings (id, chunk, embedding)
      VALUES (%s, %s, %s)
  """, (idx, text_chunk, embedding))
  ```  
- **Ошибки и предупреждения**  
  - Без установки pgvector тип `vector` недоступен – запросы падут.  
  - При больших объёмах (млрд‑векторов) PostgreSQL может быть медленнее специализированных векторных баз (стр. 176).  
- **Где пригодится** – Когда приложение уже использует PostgreSQL, нужны объединённые запросы с метаданными и транзакционными гарантиями (ACID) (стр. 176‑177).  

---

## 6.5 Performing Similarity Search in PostgreSQL (стр. 177–180)  
- **Главная мысль** – Векторный поиск в PostgreSQL реализуется через операторы `<=>`, `<->`, `<#>`, `<+>` для косинусного, евклидового, внутреннего произведения и манхэттенского расстояний, позволяя выполнять поиск непосредственно в SQL‑запросах.  
- **Как делать**  
  1. Убедиться, что таблица с колонкой `embedding vector(1536)` существует (см. 6.4).  
  2. Сгенерировать эмбеддинг запроса (`client.embeddings.create`).  
  3. Выполнить запрос:  
     ```sql
     SELECT 1 - (embedding <=> '{query_emb}') AS cosine_similarity, *
     FROM embeddings
     ORDER BY 1 - (embedding <=> '{query_emb}') DESC
     LIMIT 20;
     ```  
     - Для евклида: `<->`; для inner product: `<#>`; для Manhattan: `<+>`.  
- **Правила и числа**  
  - Cosine‑similarity вычисляется как `1 - (embedding <=> query)`.  
  - Пример: запрос «Sweets are delicious» → топ‑2 совпадения «Ice cream is delicious», «I love chocolate» (стр. 180).  
- **Шаблоны и примеры**  
  ```python
  cur.execute(f"""
      SELECT 1 - (embedding <=> '{embedded_query}') AS cosine_similarity, *
      FROM embeddings
      ORDER BY cosine_similarity DESC
      LIMIT 20;
  """)
  rows = cur.fetchall()
  ```  
- **Ошибки и предупреждения**  
  - Если не построен векторный индекс, PostgreSQL будет сканировать всю таблицу → медленно (стр. 181).  
  - Не использовать сложные многотабличные JOIN‑ы вместе с `<=>` без предварительной фильтрации, иначе тормозит (стр. 181).  
- **Где пригодится** – Когда нужны гибкие фильтры (`WHERE user_id = …`, `WHERE created_at > …`) вместе с семантическим поиском (стр. 181‑182).  

---

## 6.6 Accelerating Vector Searches in PostgreSQL with Indexing Techniques (стр. 181–185)  
- **Главная мысль** – При больших датасетах (≥ 100 000 векторов) ускорить поиск можно индексами IVFFlat и HNSW, задавая соответствующие гиперпараметры (`lists`, `m`, `ef_construction`, `ef_search`).  
- **Как делать**  
  1. Подготовить таблицу (`job_description_table`) с колонкой `embedding vector(1536)`.  
  2. **Полный скан**: выполнить `SELECT … ORDER BY embedding <=> query LIMIT …` и замерить время (пример ≈ 85 ms, стр. 183).  
  3. **IVFFlat**:  
     - Создать копию таблицы `test_embedding_table`.  
     - `CREATE INDEX ON test_embedding_table USING ivfflat (embedding vector_cosine_ops) WITH (lists = 30);`  
     - Установить `SET ivfflat.probes = 3;` (контролирует количество проверяемых кластеров).  
  4. **HNSW**:  
     - `CREATE INDEX ON test_embedding_table USING hnsw (embedding vector_cosine_ops) WITH (m = 16, ef_construction = 200);`  
     - Установить `SET hnsw.ef_search = 50;`.  
  5. Сравнить план и время через `EXPLAIN ANALYZE`. Пример: HNSW ≈ 13 ms vs полный скан ≈ 85 ms (стр. 184).  
- **Правила и числа**  
  - `lists` = 30 в IVFFlat (стр. 183).  
  - Параметры HNSW: `m` ≈ 16‑64, `ef_construction` ≈ 200, `ef_search` ≈ 10‑50 (стр. 184‑185).  
  - При < 100 k строк индексы часто не дают выигрыша (стр. 185).  
- **Шаблоны и примеры**  
  ```sql
  CREATE INDEX ON test_embedding_table USING ivfflat (embedding vector_cosine_ops) WITH (lists = 30);
  SET ivfflat.probes = 3;
  CREATE INDEX ON test_embedding_table USING hnsw (embedding vector_cosine_ops) WITH (m = 16, ef_construction = 200);
  SET hnsw.ef_search = 50;
  ```  
- **Ошибки и предупреждения**  
  - Не забыть отключить sequential scan (`SET enable_seqscan = off;`) чтобы убедиться, что план использует индекс (стр. 183).  
  - При малом объёме данных индексы добавляют только накладные расходы.  
  - HNSW требует достаточного объёма RAM, так как хранит граф в памяти (стр. 185).  
- **Где пригодится** – В продакшн‑RAG‑системах с сотнями тысяч‑миллионами векторов, где нужен быстрый поиск и возможность комбинировать его с SQL‑фильтрацией (стр. 185).  

---

### Краткое сопоставление применимости к вашему случаю  
| Технология | Когда стоит использовать | Ограничения |
|------------|--------------------------|-------------|
| **Random‑Forest классификатор** (5.6) | Для чёткого роутинга запросов по доменам, когда есть минимум 100‑200 размеченных фрагментов. | Ошибки классификации могут полностью потерять релевантные документы. |
| **Гибридный поиск (BM25 + вектор + RRF)** (5.7) | При наличии точных идентификаторов (SKU, коды, URL) вместе с естественными запросами. | Добавляет вычислительные затраты и сложность; не нужен для чисто «knowledge‑base» запросов. |
| **FAISS** (6.2) | Одноразовые аналитические задачи, прототипы, скрипты без необходимости постоянного хранилища. | Нет поддержки метаданных, контроля доступа, персистентности. |
| **Chroma** (6.3) | Прототипы и небольшие проекты (< 300 k векторов) с требованием сохранения данных между запусками. | Плохая масштабируемость, ограниченный контроль доступа. |
| **PostgreSQL + pgvector** (6.4‑6.5) | Когда уже используется PostgreSQL, нужны сложные фильтры, транзакции, объединение с другими таблицами. | При миллиардах векторов может быть медленнее специализированных векторных БД. |
| **IVFFlat / HNSW индексы** (6.6) | Данные > ≈ 100 k, требуется ускорение (10‑×‑меньше latency). | Требуют настройки памяти и гиперпараметров; HNSW –‑> более RAM‑затратен. |

Эти конспекты позволят быстро ориентироваться в рецептах книги, выбрать нужный инструмент и избежать типичных ошибок при построении собственного RAG‑конвейера.
