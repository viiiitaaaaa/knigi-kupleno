<!-- gemini-3.5-flash-lite (Gemini, 2-й читатель), rag_python_cookbook_03.txt -->
### Защита конфиденциальных данных · Выбирайте локальный запуск Whisper (open source) вместо облачного API для конфиденциальных аудиоданных, которые не должны покидать ваш периметр. · Whisper locally: Use for sensitive audio that cannot leave your environment. · (стр. 74)

### Гибридная маршрутизация документов · Используйте классификатор или анализатор макета для отправки простых текстовых документов в классический OCR, а сложных (с таблицами, диаграммами) — в мультимодальные модели, чтобы сократить расходы. · Route simple text-heavy documents through OCR, and complex documents... to multimodal models. · (стр. 63)

### Трассируемые метаданные · Сохраняйте вместе с каждым текстовым фрагментом исходный путь к файлу, путь к изображению, номер страницы и таймстампы для цитирования, отладки и повторной обработки. · Store traceable metadata alongside every extracted text chunk (PDF path, image path, page number, timestamps). · (стр. 77)

### Структурированное извлечение метаданных · Используйте модели с поддержкой Structured Outputs и Pydantic-схемы для извлечения информации об авторах и контактах из текста документов в чистые поля метаданных. · Define a Pydantic model... and use OpenAI Structured Outputs to extract those fields. · (стр. 86)

### Фильтрация по метаданным · Применяйте ограничения по метаданным в векторной базе до вычисления семантического сходства, чтобы сузить область поиска и избежать ложноположительных результатов. · Vector databases first apply metadata constraints..., then perform semantic search only on the filtered subset. · (стр. 88)

### Замена сокращений и терминов · Заменяйте аббревиатуры и технические термины на их полные формы (и пояснения) перед созданием эмбеддингов, чтобы фрагменты текста были понятны изолированно. · Use regexes and LLMs to expand abbreviations and clarify technical terms before generating embeddings. · (стр. 90)

### Генерация гипотетических вопросов · Создавайте с помощью LLM гипотетические вопросы для текстовых фрагментов на этапе индексации и сохраняйте их эмбеддинги вместо сырых чанков, чтобы преодолеть разрыв между формулировками пользователя и техническим текстом. · Iterate over the chunks and generate at least one hypothetical question per text chunk... store the hypothetical questions and their embeddings. · (стр. 95)
