<!-- gpt-oss:120b (Hermes), глубокое чтение, rag_python_cookbook_10.txt -->
## 10.6 Оценка релевантности ответа RAG‑системы (стр. 334–336)

- **Главная мысль** – Релевантность ответа измеряется через «обратную генерацию вопросов»: из ответа генерируются вопросы и сравниваются с оригинальным запросом с помощью косинусного сходства; эв evasive (не‑коммиттальные) ответы полностью снижают оценку.  
- **Как делать**  
  1. Сгенерировать «искусственные» вопросы к ответу (см. предыдущие рецепты).  
  2. Получить эмбеддинги для исходного вопроса пользователя `user_question_embedding = create_embeddings(user_input, client)`.  
  3. Для каждого сгенерированного вопроса:  
     a) Вычислить эмбеддинг `generated_question["embedding"] = create_embeddings(generated_question["question"], client)`.  
     b) Вычислить косинус‑схожесть  

        ```python
        generated_question["cosine_sim"] = np.dot(user_question_embedding,
                                                generated_question["embedding"]) / (
                np.linalg.norm(user_question_embedding) *
                np.linalg.norm(generated_question["embedding"])
        )
        ```  
  4. Вычислить среднее косинус‑сходство по всем вопросам:  

     ```python
     cosine_sim_mean = pd.DataFrame(generated_questions)["cosine_sim"].mean()
     ```  
  5. Проверить, есть ли не‑коммиттальные вопросы:  

     ```python
     has_noncommittal = any(pd.DataFrame(generated_questions)["noncommittal"])
     ```  
  6. Рассчитать итоговый скор:  

     - Жёстко: `response_relevance_score = cosine_sim_mean * int(not has_noncommittal)` (score = 0, если хотя бы один не‑коммиттальный).  
     - Мягко: `response_relevance_score = cosine_sim_mean * (1 - noncommittal_ratio)`, где `noncommittal_ratio` – доля не‑коммиттальных вопросов.  

- **Правила и числа**  
  - Косинус‑схожество ≈ 1 ⇒ вектор‑пары почти идентичны (стр. 334).  
  - При «не‑коммиттальном» ответе скор может стать 0 (стр. 335).  
  - Пример высокого скорa = 0.87 (стр. 335).  

- **Шаблоны и примеры**  
  - Структура объекта вопроса с эмбеддингом и `cosine_sim` (Fig. 10‑19).  
  - Формула «жёсткого» скоринга (стр. 335).  
  - Формула «мягкого» скоринга (стр. 335).  

- **Ошибки и предупреждения**  
  - При использовании только косинус‑схожести система не обнаруживает неполные ответы (только оф‑топик) – необходима комбинация с метрикой точности (стр. 336).  

- **Где нам пригодится** – Оценка, насколько ответ RAG‑системы действительно решает запрос пользователя (для отладки, сравнения разных промтов, контроля качества).

---

## Введение в RAG‑веб‑приложения (стр. 337)

- **Главная мысль** – Быстрое прототипирование RAG‑приложений делается в Streamlit; для масштабных продакшн‑систем лучше использовать Django, Flask или FastAPI.  
- **Как делать** – Не требуется; это лишь обзор.  

- **Правила и числа**  
  - Streamlit перезапускает весь скрипт при каждом взаимодействии, что ограничивает масштаб до «несколько десятков*» одновременных пользователей (≈ 50) (стр. 337).  
  - Для «тысяч‑мл milions*» пользователей выбирайте Django/Flask/FastAPI (стр. 337).  

- **Ошибки и предупреждения** – Streamlit не масштабируется: каждый запрос требует повторный прогон полного скрипта (стр. 337).  

- **Где нам пригодится** – Быстрое создание демо‑версий RAG‑ботов и внутренних инструментов.

---

## 11.1 Создание первого Streamlit‑приложения (стр. 338–340)

- **Главная мысль** – Streamlit позволяет построить полностью рабочее веб‑приложение из одного Python‑скрипта за несколько строк кода.  
- **Как делать**  
  1. Установить Streamlit: `pip install streamlit` (стр. 338).  
  2. Создать файл `streamlit_app.py` со следующим содержимым:  

     ```python
     import streamlit as st
     st.title("Simple Chatbot")
     user_input = st.text_input("You:")
     if user_input:
         st.write(f"Bot: You said '{user_input}'!")
     ```  
  3. Запустить: `streamlit run streamlit_app.py` (стр. 339).  
  4. Открыть в браузере `http://localhost:8501` (по умолчанию Streamlit использует порт 8501) (стр. 339).  

- **Правила и числа**  
  - По умолчанию Streamlit слушает порт 8501 (стр. 339).  

- **Шаблоны и примеры** – Минимальный код выше (стр. 339).  

- **Ошибки и предупреждения** – Никаких специфических ошибок; однако помните о ограничениях масштабируемости (см. вводную часть).  

- **Где нам пригодится** – Быстрый прототип UI для RAG‑бота, проверка идеи, демонстрации клиентам.

---

## 11.2 Создание чат‑бота в Streamlit (стр. 340–345)

- **Главная мысль** – В Streamlit можно собрать RAG‑чатбот с полноценной историей диалога, управлением сессией и интеграцией внешних API (пример – погода).  
- **Как делать**  
  1. Установить зависимости:  

     ```bash
     pip install streamlit openai requests geopy
     ```  
     (стр. 341).  
  2. (Опционально) Создать виртуальное окружение `python -m venv venv` (стр. 341).  
  3. Создать базовый UI с `st.chat_message` и `st.chat_input`:  

     ```python
     import streamlit as st
     with st.chat_message("user"):
         st.write("Hello, I am a user message.")
     with st.chat_message("assistant"):
         st.write("Hello, I am an assistant message.")
     ```  
     (стр. 341).  
  4. Инициализировать `st.session_state["messages"] = []`, если ещё не существует (стр. 342).  
  5. Реализовать простую функцию‑заглушку `simple_rag(query)` с `if/elif/else` (стр. 342).  
  6. Добавить цикл выводa истории:  

     ```python
     for message in st.session_state.messages:
         with st.chat_message(message["role"]):
             st.markdown(message["content"])
     ```  
     (стр. 343).  
  7. При получении нового ввода (`prompt := st.chat_input("Ask a question")`) –  
     a) Сохранить пользовательский запрос в `messages`.  
     b) Вызвать `simple_rag(prompt)` (или реальную RAG‑логiku).  
     c) Сохранить ответ и отобразить. (стр. 343‑344).  
  8. **Реальная RAG‑логика** (погода):  
     - **Извлечение места** через LLM, запрос JSON (стр. 343‑345).  
     - **Geopy Nominatim** → координаты (стр. 344).  
     - **Open‑Meteo API** → текущая погода (стр. 345).  
     - **Создание промта** – включить вопрос пользователя и JSON‑данные о погоде (стр. 346‑347).  
     - **Отправка промта** в LLM и получение ответа (стр. 347).  
  9. Вынести вспомогательные функции в отдельный модуль (`app_helper_functions.py`) и добавить функцию `perform_rag(user_query)` (стр. 347).  
  10. Интегрировать `perform_rag` в главный Streamlit‑скрипт (стр. 348).  

- **Правила и числа**  
  - Streamlit перезапускает скрипт полностью при каждой интеракции → требуется хранить состояние в `st.session_state` (стр. 349).  
  - При тестировании «один‑таб» могут не проявиться баги с утечкой состояния между пользователями; проверять в двух браузерах (стр. 349).  
  - Рекомендовано держать Streamlit‑скрипт < 100 строк, а тяжёлую логику выносить в отдельные модули (стр. 349).  

- **Шаблоны и примеры**  
  - Минимальный UI‑код (стр. 341).  
  - Функция `extract_the_city_and_country` с `response_format={"type":"json_object"}` (стр. 344).  
  - Запрос к Open‑Meteo (стр. 345).  
  - Пример промта `create_weather_prompt` (стр. 346).  
  - Полный чат‑бот (стр. 348).  

- **Ошибки и предупреждения**  
  - Не проверять наличие `"messages"` в `st.session_state` → `KeyError`.  
  - Состояние может «перетекать» между пользователями, если тестировать только в одном окне.  
  - `print`‑вывод в Streamlit‑приложении может появляться в неверном порядке – используйте VS Code debugger (стр. 349).  

- **Где нам пригодится** – Быстрая сборка интерактивного RAG‑чатбота с историей диалога, прототипирование интеграций (погода, поиск и т.п.).

---

## 11.3 Добавление анализа PDF‑файлов в чат‑бот (стр. 350–354)

- **Главная мысль** – Для документов, где важны таблицы, изображения и разметка, лучше использовать мультимодальные модели (Vision‑LLM) вместо традиционного OCR; процесс: PDF → страницы‑изображения → мультимодальная модель → текст → экстракция сущностей.  
- **Как делать**  
  1. Установить зависимости:  

     ```bash
     pip install streamlit openai pdf2image pillow pydantic
     ```  
     (стр. 351).  
  2. Реализовать функцию `convert_pdf_to_images(pdf_file)` (стр. 351‑352):  

     ```python
     from pdf2image import convert_from_bytes
     images = convert_from_bytes(pdf_file.read())
     for idx, img in enumerate(images):
         path = f"images/temp_page_{idx}.png"
         img.save(path, "PNG")
         image_paths.append(path)
     return image_paths
     ```  
  3. Реализовать OCR‑функцию `perform_ocr_and_extract_entities(image_paths)`:  

     - Прочитать каждый PNG, base64‑закодировать, отправить в модель `gpt-5.2` с ролью `system: "You are an OCR assistant..."` (стр. 352‑353).  
     - Собрать ответы `full_text` в список `extracted_text`.  

  4. Экстрактировать сущности из полного текста через функцию `extract_entities_from_text(extracted_text)`:  

     ```python
     system_message = ("Extract all people entities from the text as a JSON array ..."
                        "fields: ID (int), Name (str), Age (int), City (str).")
     response = client.chat.completions.create(
         model="gpt-5.2",
         messages=[{"role":"system","content":system_message},
                   {"role":"user","content": "\n".join(extracted_text)}],
         max_tokens=1024,
     )
     return response.choices[0].message.content
     ```  
     (стр. 353).  

  5. Интегрировать в Streamlit‑чат:  

     ```python
     uploaded_pdf = st.file_uploader("Upload a PDF (optional)", type=["pdf"])
     prompt = st.chat_input("Ask a question about the uploaded PDF")
     if prompt and prompt.files:
         with st.spinner("Processing PDF..."):
             for uploaded_file in prompt.files:
                 if uploaded_file.type == "application/pdf":
                     images = convert_pdf_to_images(uploaded_file)
                     extracted_text = perform_ocr_and_extract_entities(images)
                     # выводим текст по страницам
                     # ...
                     extracted_data = extract_entities_from_text(extracted_text)
                     st.write("Extracted Entities:", extracted_data)
     ```  
     (стр. 353‑354).  

- **Правила и числа**  
  - Стоимость мультимодального OCR ≈ 10‑100 × дороже, чем обычный PyMuPDF‑extraction (стр. 354).  
  - Применимо, когда документ содержит смешанные типы контента (таблицы, изображения, формы) (стр. 354).  
  - Не рекомендуется для чисто текстовых PDF (стр. 355).  
  - Для 100‑страничного документа обычный OCR ≈ $0.05, мультимодальный ≈ $0.50‑$2.00 (стр. 354).  

- **Шаблоны и примеры**  
  - `convert_pdf_to_images` (стр. 351).  
  - Промт для OCR‑ассистента (стр. 352).  
  - Промт для извлечения людей (стр. 353).  

- **Ошибки и предупреждения**  
  - Мультимодальные модели могут «галлюцинировать» поля или пропускать страницы при плохом качестве (стр. 355).  
  - Нужно валидировать результат через Pydantic‑схемы (стр. 355).  
  - Высокая вычислительная стоимость – не использовать для массовой обработки тысяч страниц (стр. 354).  

- **Где нам пригодится** – Анализ загруженных PDF‑документов (инвойсы, формы, исследования) внутри RAG‑чатбота, когда важна структура и расположение элементов.

---

## 11.4 Подключение RAG‑приложения к SQL‑базе (стр. 355–360)

- **Главная мысль** – Текст‑в‑SQL (через Vanna AI) позволяет пользователям задавать естественноязыковые запросы к базе; система использует векторное хранилище (Chroma) для поиска релевантных частей схемы и генерирует SQL‑запрос, который затем исполняется.  
- **Как делать**  
  1. Установить зависимости:  

     ```bash
     pip install streamlit openai vanna chromadb sqlite3
     ```  
     (стр. 356).  
  2. Создать SQLite‑файл `bookstore.db` (скрипт в репозитории) с таблицами — жанры, клиенты, книги, продажи и т.д. (стр. 357).  
  3. Определить класс‑обёртку для Vanna:  

     ```python
     class MyVanna(ChromaDB_VectorStore, OpenAI_Chat):
         def __init__(self, config=None):
             ChromaDB_VectorStore.__init__(self, config=config)
             OpenAI_Chat.__init__(self, config=config)
     ```  
     (стр. 357).  
  4. Инициализировать Vanna и подключить к SQLite:  

     ```python
     if "vn" not in st.session_state:
         st.session_state.vn = MyVanna({
             "api_key": os.environ.get("OPENAI_API_KEY"),
             "model": "gpt-5.2",
             "path": "./chroma_db",
         })
         st.session_state.vn.connect_to_sqlite("bookstore.db")
     ```  
     (стр. 357‑358).  
  5. Обучить Vanna на схеме (DDL) и/или дополнительной документации:  

     ```python
     ddl_df = st.session_state.vn.run_sql(
         "SELECT sql FROM sqlite_master WHERE sql IS NOT NULL"
     )
     for ddl in ddl_df["sql"]:
         st.session_state.vn.train(ddl=ddl)
     ```  
     (стр. 358‑359).  
  6. Пример генерации и выполнения запроса:  

     ```python
     user_input = "What are the top 5 best-selling books?"
     sql_query = vn.generate_sql(user_input)
     result = vn.run_sql(sql_query)
     ```  
     (стр. 359).  
  7. Интегрировать в Streamlit‑чат:  

     ```python
     if prompt := st.chat_input("Ask about the bookstore"):
         sql = st.session_state.vn.generate_sql(prompt)
         result = st.session_state.vn.run_sql(sql)
         answer = OpenAI().chat.completions.create(
             model="gpt-5-mini",
             messages=[{
                 "role":"user",
                 "content": f"Answer based on this data: {result}\nQuestion: {prompt}"
             }]
         ).choices[0].message.content
         # выводим в чат + expand с результатом SQL
     ```  
     (стр. 359‑360).  

- **Правила и числа**  
  - Vanna AI использует Chroma‑vectorstore (стр. 357).  
  - При генерации SQL‑запросов рекомендуется сначала показывать запрос пользователю (стр. 360).  
  - Тренировать можно четырьмя типами данных (DDL, documentation‑strings, SQL‑запросы, парные (question, SQL)) (таблица 11‑1, стр. 358).  

- **Шаблоны и примеры**  
  - Пример `MyVanna` (стр. 357).  
  - Тренировка DDL (стр. 358).  
  - Генерация SQL для топ‑5 книг (стр. 359).  
  - Полный Streamlit‑чат с текст‑в‑SQL (стр. 360).  

- **Ошибки и предупреждения**  
  - Модели могут «галлюцинировать» имена столбцов, если документация неполна (стр. 360).  
  - Сложные запросы (> 5 таблиц) могут тайм‑аутиться или возвращать неверные результаты (стр. 360).  
  - Не использовать, если пользователи не могут проверять сгенерированный SQL (стр. 360).  
  - Для детерминированного поведения лучше агентный подход с шаблонами запросов (стр. 360‑361).  

- **Где нам пригодится** – Позволяет конечным пользователям (не‑программистам) задавать вопросы к базе данных через естественный язык, быстро прототипировать аналитические чат‑боты.

---

## 11.5 Деплой Streamlit‑приложения с Docker и AWS (стр. 361–365)

- **Главная мысль** – Контейнеризация (Docker) + облачная оркестрация (AWS ECR + ECS Fargate) обеспечивают воспроизводимый, масштабируемый и безопасный запуск RAG‑приложений.  
- **Как делать**  
  1. **Подготовка**: установить Docker Desktop, иметь облачный аккаунт (стр. 362).  
  2. **Структура проекта**:  

     ```
     ├─ Dockerfile
     ├─ requirements.txt
     ├─ streamlit_app.py
     └─ entrypoint.sh
     ```  
     (стр. 362).  
  3. **Dockerfile** (пример):  

     ```Dockerfile
     FROM python:3.9-slim
     WORKDIR /app
     COPY requirements.txt .
     RUN pip install --no-cache-dir -r requirements.txt
     COPY . .
     EXPOSE 8501
     ENTRYPOINT ["bash", "entrypoint.sh"]
     ```  
     (стр. 363).  
  4. **Сборка образа**:  

     ```bash
     docker build -t rag-streamlit-app:latest .
     ```  
     (стр. 363).  
  5. **Локальная проверка**:  

     ```bash
     docker run -p 8501:8501 rag-streamlit-app:latest
     ```  
     Откройте `http://localhost:8501` (стр. 363).  
  6. **Деплой в AWS**:  
     - Установить AWS CLI.  
     - Создать репозиторий ECR: `aws ecr create-repository --repository-name rag-streamlit-app` (стр. 363).  
     - Авторизоваться, пушить образ (инструкции в консоли ECR).  
     - Создать задачу ECS, указать образ из ECR, выбрать Fargate (стр. 363‑364).  
  7. **Альтернативы**: Google Cloud Run, Azure Container Apps (стр. 363).  
  8. **Оценка стоимости**: Fargate ≈ $30‑$40 / мес за 1 vCPU + 2 ГБ RAM (стр. 364).  
  9. **Дополнительные прод‑уровни**:  
     - **IaC** (Terraform/CDK) – описывают инфраструктуру кодом (стр. 364‑365).  
     - **CI/CD** (GitHub Actions, GitLab CI) – автоматический тест, сбор, пуш и деплой (стр. 364‑365).  
     - **Управление секретами** – AWS Secrets Manager или переменные окружения, а не хардкод в образе (стр. 364‑365).  

- **Правила и числа**  
  - Порт 8501 (по умолчанию Streamlit) (стр. 363).  
  - Fargate ≈ $30‑$40 / мес за 1 vCPU + 2 ГБ RAM (стр. 364).  
  - Рекомендация: ограничить максимальное количество задач в ECS, чтобы избежать неожиданного роста расходов (стр. 364).  

- **Шаблоны и примеры**  
  - Dockerfile (стр. 363).  
  - Команды `docker build`, `docker run` (стр. 363).  
  - Команда создания репозитория ECR (стр. 363).  

- **Ошибки и предупреждения**  
  - Хардкод API‑ключей в образе → утечка в реестре (стр. 364).  
  - Без IaC и CI/CD конфигурация «дрейфует», трудно отлаживать (стр. 364‑365).  
  - Не ограничивайте масштабирование в Fargate – может привести к неожиданным счетам (стр. 364).  

- **Где нам пригодится** – Перенос готового RAG‑приложения (Streamlit) в продакшн‑окружение с гарантией воспроизводимости и масштабируемости, а также для организации CI/CD и управления секретами.

---

## Индекс (стр. 366–368)

**Содержания нет** – это только указатель по темам книги, без дополнительного текста.
