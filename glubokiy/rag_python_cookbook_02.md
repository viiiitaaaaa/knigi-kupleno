<!-- gpt-oss:120b (Hermes), глубокое чтение, rag_python_cookbook_02.txt -->
**Часть 2 (стр. 36‑72) – «Foundation Models» и «Loading Data»**  

---

## Обсуждение: Установка зависимостей и виртуальные окружения (стр. 36)  
- **Главная мысль** – Держать зависимости проекта изолированными (по главе) — это уменьшает конфликты версий и делает окружения лёгкими.  
- **Как делать**  
  1. Для каждой главы создайте отдельный файл `requirements_chXX.txt` с нужными библиотеками.  
  2. При работе в Jupyter‑ноутбуке установите их, выполнив команды из файла (или скопируйте их из начала ноутбука).  
  3. Создайте виртуальное окружение (`python -m venv venv && source venv/bin/activate`) и активируйте его каждый раз перед запуском примеров.  
- **Правила и числа** – *Нет* (только рекомендация).  
- **Шаблоны и примеры** – Файлы `requirements_ch01.txt … requirements_ch08.txt` в корне репозитория.  
- **Ошибки и предупреждения** – Не использовать глобальную установку, иначе возможны конфликтующие версии библиотек.  
- **Где пригодится** – При подготовке локального рабочего места для экспериментов с рецептами из книги.  

---

## Chapter 2 : Foundation Models (стр. 37‑38)  
- **Главная мысль** – Фундаментальные модели (LLM и мультимодальные) являются ядром RAG: используют‑ся для подготовки материалов (извлечение, транскрипция, суммирование) и для генерации ответов.  
- **Как делать** – Типичный мультимодальный пайплайн (см. рис. 2‑1):  
  1. Vision‑модель → анализ кадров видео;  
  2. Speech‑to‑text → транскрипция аудио;  
  3. Embedding‑модель → преобразует полученный текст в вектор;  
  4. Retrieval → поиск релевантных контекстов;  
  5. Language model → генерация ответа.  
- **Правила и числа** – *Нет* (только описание этапов).  
- **Шаблоны и примеры** – (см. рис. 2‑1).  
- **Ошибки и предупреждения** – Не использовать один и тот же набор моделей для обеих фаз без проверки качества.  
- **Где пригодится** – При проектировании любой RAG‑системы (видео, аудио, текст).  

---

## 2.1 Defining a Suitable Prompt Template (стр. 38‑40)  
- **Главная мысль** – Эффективный промпт для RAG – это фиксированная структура из четырёх частей: роль, инструкция, контекст, требования к выводу.  
- **Как делать**  
  1. Определите **role** — как должен «вести себя» ассистент.  
  2. Сформулируйте **instruction** — задайте задачу и обязательство использовать только предоставленный контекст.  
  3. Добавьте **[Context]** — в реальном пайплайне сюда подставляются найденные фрагменты.  
  4. Укажите **output requirements** — ограничьте длину, стиль и формат.  
- **Правила и числа** – Вывод ограничен **до 120 слов** (пример).  
- **Шаблоны и примеры**  

```
[Role]
You are a procurement analyst who explains internal policies in a simple and reliable way.

[Instruction]
Read the retrieved context and answer the user's question using only the information from the retrieved context.
If the answer is not covered in the context, say that the information is not available in the provided context.

[Context]
<<context>>

[User Question]
Do our standard supplier contracts include a minimum warranty period?

[Output Requirements]
Short answer. Clear wording. Up to 120 words.
```  

- **Ошибки и предупреждения** – Слишком «свободный» шаблон → модель может «выдумывать» факты; слишком «жёсткий» → модель может отказываться отвечать.  
- **Где пригодится** – При построении чат‑ботов, которые должны давать проверяемые ответы (например, поддержка отдела закупок).  

---

## 2.2 Selecting the Right Language Model for Your Task (стр. 40‑44)  

### Таблица 2‑1 (стр. 41‑42) – классификация моделей по уровням  
| Тир | Примеры моделей | Характеристики |  
|---|---|---|  
| Ultra‑efficient | Gemini 3 Flash, Claude Haiku 4.5, GPT‑5 nano | простые задачи, высока‑пропускная способность, небольшие контексты |  
| Efficient/everyday | Gemini 2.5 Flash, GPT‑5 mini, GPT‑4.1 | генерация текста, суммирование, чат‑боты |  
| Flagship | Gemini 3 Pro, GPT‑5, Claude Sonnet 4.5 | сложные/креативные задачи, глубокий анализ |  
| Reasoning/frontier | GPT‑5, Claude Opus 4.5 | многократные выводы, научные задачи, длинные контексты |  

### Ценообразование (стр. 42‑43)  

- **Ultra‑efficient** ≈ 0,05‑0,20 USD за 1 M входных токенов.  
- **Efficient** ≈ 0,25‑0,60 USD за 1 M входных токенов.  
- **Flagship** ≈ 1‑5 USD за 1 M входных токенов.  
- **Reasoning/frontier** ≈ 2‑30 USD за 1 M входных токенов.  

- **Как делать**  
  1. Оцените требования к **latency** (время ответа).  
  2. Оцените **сложность задачи** (классификация → efficient, глубокий анализ → flagship).  
  3. Сравните **цену** в пределах одного тира у разных провайдеров (например, GPT‑5 vs Gemini 3 Pro).  
  4. Выберите **самую лёгкую** модель, удовлетворяющую требованиям.  
- **Ошибки и предупреждения** – Не ставьте reasoning‑модель на задачи‑классификаторы; не «переплачивайте» за большую модель без измерения выгоды.  
- **Где пригодится** – При выборе LLM для каждой стадии конвейера (retrieval, generation, агенты).  

---

## 2.3 Generating Content with the OpenAI API (стр. 44‑46)  
- **Главная мысль** – OpenAI предоставляет управляемый API; достаточно задать ключ и отправить список сообщений.  
- **Как делать**  
  1. Получите **API‑key** в настройках OpenAI и положите в переменную окружения `OPENAI_API_KEY`.  
  2. Установите зависимости: `pip install openai httpx`.  
  3. Создайте клиент `client = OpenAI()`.  
  4. Сформируйте список `messages` (system + user).  
  5. Вызовите `client.chat.completions.create(model="gpt-5.2", messages=messages)`.  
  6. Возьмите ответ `response.choices[0].message.content`.  
- **Пример кода** (стр. 45‑46)  

```python
from openai import OpenAI
def ask_with_context(context, question):
    client = OpenAI()
    messages = [
        {"role": "system", "content": "Answer based only on the provided context."},
        {"role": "user", "content": f"Context:\n{context}\n\nQuestion:\n{question}"}
    ]
    response = client.chat.completions.create(
        model="gpt-5.2",
        messages=messages
    )
    return response.choices[0].message.content
```  

- **Транскрипция аудио** – `client.audio.transcriptions.create(model="gpt-4o-transcribe", file=audio_file)`.  
- **Ошибки и предупреждения** – Не забывайте про **rate‑limits**; при больших объёмов лучше выбрать провайдера с более высоким лимитом.  
- **Где пригодится** – Быстрое прототипирование RAG‑приложений без собственного инференса.  

---

## 2.4 Generating Content with Google’s Gemini Models (стр. 46‑48)  
- **Главная мысль** – Gemini API совместим с OpenAI‑клиентом; меняется только базовый URL и ключ.  
- **Как делать**  
  1. Получите **API‑key** в Google AI Studio → переменная `GOOGLE_API_KEY`.  
  2. Установите `pip install openai`.  
  3. Создайте клиент:  

```python
client = OpenAI(
    api_key=os.getenv("GOOGLE_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)
```  

  4. Вызывайте `client.chat.completions.create(model="gemini-3-flash", …)`.  
- **Шаблон** – такой же, как у OpenAI (список сообщений).  
- **Особенности** – Gemini 2.5 Pro поддерживает контекст до **≈ 1 млн токенов**, подходит для длинных документов и мультимодальных запросов (текст + изображения).  
- **Ошибки и предупреждения** – Для коротких запросов OpenAI обычно быстрее (меньше «времени до первого токена»).  
- **Где пригодится** – При работе с большими объёмами текста (> 100 k токенов) или с комбинированными модальностями (изображения, аудио).  

---

## 2.5 Generating Content with the Anthropic API (стр. 48‑52)  
- **Главная мысль** – Claude модели от Anthropic ориентированы на точный, консервативный вывод, хороши для правовых и кодовых задач.  
- **Как делать**  
  1. Создайте аккаунт Anthropic → `ANTHROPIC_API_KEY`.  
  2. Установите SDK: `pip install anthropic`.  
  3. Пример запроса:  

```python
from anthropic import Anthropic
client = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
response = client.messages.create(
    model="claude-sonnet-4.5",
    max_tokens=200,
    messages=[{"role":"user","content":"Explain how vector databases work in simple terms."}]
)
print(response.content[0].text)
```  

- **Модели по размерам** – Haiku (ultra‑efficient), Sonnet (efficient), Opus (reasoning).  
- **Ошибки и предупреждения** – Claude медленнее и дороже при высокой пропускной способности; не использовать для простых чат‑ботов с целью скорости.  
- **Где пригодится** – Задачи, где важен **консервативный вывод**, проверка гипотез, сложный код, юридический анализ.  

---

## 2.6 Running Open Source Models Locally with Ollama (стр. 52‑55)  
- **Главная мысль** – Ollama позволяет запускать открытые LLM локально, имитируя OpenAI‑совместимый эндпоинт.  
- **Как делать**  
  1. Установите **Ollama** (macOS/Windows/Linux).  
  2. С помощью `ollama pull <model>` скачайте модель (пример: `llama2`, `mistral`, `codellama`).  
  3. Подключите клиент OpenAI к локальному серверу:  

```python
client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
response = client.chat.completions.create(
    model="qwen3:4b",
    messages=[{"role":"user","content":"What is retrieval augmented generation?"}]
)
```  

  4. При необходимости сравните несколько моделей в цикле.  
- **Таблица 2‑2 (стр. 54)** – список популярных открытых моделей (Llama 2, GPT‑OSS, Mistral, Qwen, Falcon) с датой выпуска, размером параметров и популярностью.  
- **Ограничения** – На ноутбуке без мощного GPU эффективны только модели ≤ 13 B; большие модели (≈ 70 B) требуют ≥ 16 GB VRAM.  
- **Ошибки и предупреждения** – Не запускать тяжёлую модель без достаточного GPU; локальная инференция медленнее облачной, но обеспечивает конфиденциальность.  
- **Где пригодится** – Когда данные строго конфиденциальны (медицина, финансы) или когда объём запросов настолько велик, что стоимость облачных вызовов выше, чем эксплуатация собственного железа.  

---

## 2.7 Creating Structured Outputs with the OpenAI SDK and Pydantic (стр. 55‑58)  
- **Главная мысль** – С помощью **Pydantic** можно задать схему ответа (JSON) и получать сразу типизированный Python‑объект, что упрощает дальнейшую обработку.  
- **Как делать**  
  1. Установите `pip install openai pydantic`.  
  2. Определите схему, наследуясь от `BaseModel`. Пример для счета‑фактуры:  

```python
class LineItem(BaseModel):
    description: str
    quantity: int
    total: float

class Invoice(BaseModel):
    invoice_number: str
    invoice_date: date
    supplier: str
    items: List[LineItem]
    total_due: float
```  

  3. Вызовите `client.responses.parse(..., response_format=Invoice)`.  
  4. Полученный объект уже прошёл валидацию: `invoice: Invoice = result.output_parsed`.  
- **Шаблон запроса** (стр. 56‑57) – отправьте массив `input` с `role` = "user", где `content` содержит как текст, так и изображение (`type: "input_image"`).  
- **Ошибки и предупреждения** – Структурированный вывод **увеличивает задержку** и может «зажимать» модель, если схема слишком жёсткая для задачи (например, требующий «depends» ответ). Не использовать для свободного творчества.  
- **Где пригодится** – При построении пайплайнов, где дальнейшие шаги требуют строгих типов: загрузка в БД, триггер бизнес‑правил, цепочки агентов.  

---

## Chapter 3 : Loading Data (стр. 59‑60)  
- **Главная мысль** – Преобразовать разнородные корпоративные данные (текст, PDF, таблицы, медиа) в единый текстовый формат, пригодный для эмбеддингов и поиска.  
- **Как делать** – Последовательность (рис. 3‑2):  
  1. **Индексация** → загрузка и обработка документов → эмбеддинги → векторный store.  
  2. **Рантайм** → поиск релевантных фрагментов → генерация ответа.  
- **Ошибки и предупреждения** – При использовании фреймворков (LangChain, LlamaIndex) фиксируйте версии зависимостей и изолируйте их в небольших адаптерах, иначе часто ломаются из‑за быстроменяющихся API.  
- **Где пригодится** – Планирование архитектуры любой RAG‑системы, выбор библиотек‑основ.  

---

## 3.1 Loading Word Files in Python (стр. 61‑63)  
- **Главная мысль** – Для `.docx` есть два подхода: простое чтение текста (`python-docx`) и структурированное извлечение элементов (`Unstructured`).  
- **Как делать**  
  1. Установите `pip install python-docx unstructured pandas`.  
  2. **Быстрый текст**:  

```python
from docx import Document
doc = Document(file_path)
text = "\n".join(p.text for p in doc.paragraphs)
```  

  3. **Структурированный** (сохраняет типы элементов):  

```python
from unstructured.partition.docx import partition_docx
elements = partition_docx(filename=file_path)
elements_df = pd.DataFrame([{
    "element_id": e.id,
    "file_path": file_path,
    "category": e.category,   # Title, NarrativeText, ListItem, …
    "text": e.text,
    "last_modified": e.metadata.last_modified,
} for e in elements])
```  

- **Ошибки и предупреждения** – Первый метод теряет структуру (заголовки, списки); второй требует больше памяти и времени, но даёт метаданные для фильтрации.  
- **Где пригодится** – Если нужно задавать разные веса для заголовков vs. обычного текста при поиске.  

---

## 3.2 Loading PDF Files (стр. 64‑66)  
- **Главная мысль** – `PyPDF2` удобно извлекать текст и метаданные из *цифровых* PDF‑файлов (не сканированных).  
- **Как делать**  
  1. Установить `pip install PyPDF2 pandas`.  
  2. Открыть файл и пройтись по страницам:  

```python
reader = PyPDF2.PdfReader(file)
pages = []
for i, page in enumerate(reader.pages, 1):
    pages.append({
        "file_name": reader.metadata.get("/Title"),
        "producer": reader.metadata.get("/Producer"),
        "page_number": i,
        "text": page.extract_text(),
        "images": page.images,
    })
pages_df = pd.DataFrame(pages)
```  

- **Ошибки и предупреждения** – Не работает с изображенными (сканированными) PDF; для них нужен OCR (см. рецепт 3.6, не в этой части).  
- **Где пригодится** – Быстрое извлечение текста из больших пакетов PDF‑отчётов, генерация эмбеддингов.  

---

## 3.3 Loading and Handling Tabular Data from Excel and CSV Files (стр. 66‑70)  
- **Главная мысль** – Существует три стратегии работы с таблицами в RAG:  
  1. **Row‑to‑text** – каждая строка превращается в одно предложение.  
  2. **Embedding whole table** – помещаем всю таблицу в запрос (Markdown), подходит лишь для небольших таблиц.  
  3. **Text‑to‑SQL** – хранить таблицу в СУБД, а LLM генерирует SQL‑запросы.  

- **Как делать**  
  1. **Row‑to‑text** (пример с Census Income):  

```python
pip install openpyxl pandas
df = pd.read_excel("census-income.xlsx")
def create_text_description_of_row(row):
    return f"The candidate {row['age']} years old is working in the {row['workclass']} sector ..."
df["text_description"] = df.apply(create_text_description_of_row, axis=1)
```  

  2. **Embedding whole table** – вставьте таблицу в запрос в Markdown‑формате (см. рис. 3‑10).  
  3. **Text‑to‑SQL** – загрузите CSV/Excel в СУБД, затем используйте LLM для генерирования запросов (см. рецепт 3.4).  

- **Таблица 3‑1 (стр. 70)** – сравнение подходов (best‑for, ограничения).  
- **Ошибки и предупреждения** – Row‑to‑text не умеет агрегацию; embedding‑в‑prompt ограничен контекстом и дорогой; Text‑to‑SQL требует настройки БД и обработки SQL‑результатов.  
- **Где пригодится** – Выбор подхода зависит от размера таблицы и типа запросов (lookup vs. агрегаты).  

---

## 3.4 Loading Structured Data from a PostgreSQL Database (стр. 71‑72)  
- **Главная мысль** – PostgreSQL может служить как обычной реляционной СУБД, так и векторным хранилищем (через `pgvector`).  
- **Как делать**  
  1. Установить PostgreSQL + pgAdmin (или облачный сервис).  
  2. Установить Python‑библиотеки: `pip install SQLAlchemy psycopg2-binary pandas python-dotenv`.  
  3. Создать движок:  

```python
from sqlalchemy import create_engine
engine = create_engine(
    f"postgresql+psycopg2://{user}:{pwd}@{host}:{port}/{db}"
)
with engine.connect() as conn:
    df = pd.read_sql("SELECT * FROM categories ORDER BY category_id ASC", conn)
```  

- **Ошибки и предупреждения** – Большие LLM‑модели требуют отдельного векторного хранилища (Pinecone, Qdrant) для высокой производительности; PostgreSQL подходит, когда нужны **реляционные фильтры + векторный поиск**.  
- **Где пригодится** – Когда RAG‑приложение уже использует PostgreSQL (логин‑сессии, транзакции) и нужно добавить поиск по эмбеддингам без отдельного кластера.  

---  

### Краткое сведение, где каждый материал пригодится  
| Раздел | Практическое применение для предпринимателя‑одиночки |
|--------|------------------------------------------------------|
| Установка зависимостей | Создание изолированных окружений для разных экспериментов |
| Prompt‑template | Построение чат‑бота, отвечающего только на проверяемый контент |
| Выбор модели | Оптимизация стоимости и скорости ответов в собственных сервисах |
| OpenAI API | Быстрый доступ к мощным LLM без собственного инференса |
| Gemini | Длинные документы, мультимодальные запросы (текст + изображения) |
| Anthropic | Юридический, финансовый контент, где нужен консервативный вывод |
| Ollama | Локальная работа с чувствительными данными (медицинские записи) |
| Pydantic‑output | Структурирование результатов (счета, контракты) для дальнейшего анализа |
| Загрузка Word/PDF | Интеграция корпоративных документов в RAG‑трубопровод |
| Таблицы (Excel/CSV) | Поиск по справочникам, быстрый lookup vs. аналитика через Text‑to‑SQL |
| PostgreSQL | Хранение и совместный поиск (реляционный + векторный) клиентских данных |

Эти конспекты позволяют быстро находить нужные рецепты, понять, какие шаги выполнять, какие ограничения учитывать и где каждый подход будет наиболее полезен в ваших проектах.
