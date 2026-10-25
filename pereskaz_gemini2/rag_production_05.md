<!-- gemini-3.5-flash-lite (Gemini, 2-й читатель), rag_production_05.txt -->
### Инкрементальные обновления · что делать (1–2 предложения) · Обновляйте только измененные документы (новые, обновленные или удаленные), а не переиндексируйте весь датасет целиком. · «Instead of re-indexing the entire dataset every time a change occurs, incremental updates involve identifying only the modified documents...» · (стр. 99–100)

### Двухэтапная поисковая архитектура (Two-Stage Retrieval) · что делать (1–2 предложения) · Разделите поиск на генерацию кандидатов (быстро, с высоким охватом) и ранжирование (точно, с помощью трансформеров) для баланса скорости и точности. · «It breaks down the retrieval process into two distinct phases to optimize both speed and accuracy.» · (стр. 75)

### Гибридный поиск (Hybrid Search) · что делать (1–2 предложения) · Объединяйте семантический поиск по векторам и лексический поиск по ключевым словам (например, через BM25), чтобы находить и концептуально близкие, и точные термины. · «Hybrid search combines the strengths of vector search with that of lexical (keyword-based) search...» · (стр. 76)

### Объединение результатов поиска через RRF · что делать (1–2 предложения) · Используйте Reciprocal Rank Fusion для объединения списков семантического и лексического поиска по их позициям (рангам), избегая проблемы нормализации разных шкал оценок. · «RRF has the advantage that it doesn’t require score normalization between the two different search systems...» · (стр. 78)

### Ранжирование с помощью кросс-энкодеров · что делать (1–2 предложения) · Применяйте модели-реранкеры на базе кросс-энкодеров для глубокой оценки релевантности найденных кандидатов запросу. · «...cross-encoders—as they can capture subtle semantic relationships between the query and the chunks.» · (стр. 72, 79)

### Цепочка реранкеров (Chained Reranking) · что делать (1–2 предложения) · Комбинируйте несколько видов ранжирования последовательно (например: релевантность -> MMR для разнообразия -> кастомная бизнес-логика). · «In practice, it is quite common to include multiple forms of reranking as a chained reranking pipeline.» · (стр. 83, 89)

### Защитные барьеры (Guardrails) на выходе · что делать (1–2 предложения) · Проверяйте сгенерированный ответ с помощью промпт-инструкций или специализированных моделей-аудиторов (например, ShieldGemma, Llama Guard) перед показом пользователю. · «Guardrails can also operate after the initial response has been generated, but before it’s shown to the user.» · (стр. 84)

### Защита промпт-инъекций (Instruction Defense) · что делать (1–2 предложения) · Разделяйте системные инструкции, контекст и запрос пользователя с помощью четких разделителей (например, XML-тегов), приказывая ИИ трактовать ввод пользователя строго как данные, а не как команды. · «...construct your RAG prompt with clear delimiters (like XML tags or special markers) to distinctly separate system instructions...» · (стр. 87)

### Детекция галлюцинаций через LLM-судью или HHEM · что делать (1–2 предложения) · Оценивайте фактическую согласованность ответа с исходным текстом с помощью отдельного мощного LLM-судьи или специализированной модели классификации (например, HHEM). · «There are two techniques commonly used for hallucination detection—LLM-as-a-judge and using a dedicated model like the Hughes Hallucination Evaluation Model, HHEM.» · (стр. 92)
