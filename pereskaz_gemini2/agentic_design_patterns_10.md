<!-- gemini-3.5-flash-lite (Gemini, 2-й читатель), agentic_design_patterns_10.txt -->
### Валидация и фильтрация входящих данных · Фильтрация входящих данных до их обработки агентом с помощью API модерации контента и схем валидации (например, Pydantic) для блокировки вредоносного контента и конфиденциальных тем. · `...utilizing content moderation APIs to detect inappropriate prompts and schema validation tools like Pydantic to ensure structured inputs adhere to predefined rules...` · (стр. 287)

### Мониторинг и логирование · Непрерывное отслеживание поведения агента путем логирования всех действий, использования инструментов, входных и выходных данных для последующей отладки и аудита. · `This involves logging all actions, tool usage, inputs, and outputs for debugging and auditing, as well as gathering metrics on latency, success rates, and errors.` · (стр. 287)

### Обработка ошибок и отказоустойчивость · Использование блоков try-except и логики повторных попыток с экспоненциальной задержкой для преодоления временных сбоев. · `...includes using try-except blocks and implementing retry logic with exponential backoff for transient issues.` · (стр. 287)

### Экономия лимита и производительность · Использование менее мощных, быстрых и экономичных моделей (например, Gemini Flash) в качестве предварительного фильтра для проверки входных и выходных данных. · `...a less computationally intensive model can be employed as a rapid, additional safeguard to pre-screen inputs or double-check the outputs...` · (стр. 286)

### Безопасность и контроль инструментов · Проверка параметров инструментов через callback-функции перед их выполнением для ограничения прав и сопоставления идентификаторов пользователей со стандартным состоянием сессии. · `validate_tool_params function is a callback designed to be executed before a tool is called by the agent.` · (стр. 298)

### Принцип наименьших привилегий · Предоставление агенту минимально необходимого набора разрешений и инструментов для выполнения конкретной задачи, чтобы ограничить радиус поражения при ошибках. · `An agent should be granted the absolute minimum set of permissions required to perform its task.` · (стр. 303)

### Проверка результата через LLM-Судью · Оценка качества ответов или промежуточных шагов агента с помощью специализированного промпта-рубрики и отдельного LLM-судьи для масштабируемого качественного анализа. · `A potential framework involves using an LLM as an evaluator. This LLM-as-a-Judge approach assesses another AI agent's output...` · (стр. 310)

### Мониторинг задержек (Latency) · Измерение и сохранение в постоянное хранилище (БД, time-series, файлы) времени, затрачиваемого агентом на обработку запросов, для контроля производительности. · `Logging this information to a persistent storage system is recommended. Options include structured log files... time-series databases...` · (стр. 309)

### Экономия токенов · Интеграция систем мониторинга и подсчета токенов для управления расходами на вызовы LLM и оптимизации работы с промптами. · `For LLM-powered agents, tracking token usage is crucial for managing costs and optimizing resource allocation.` · (стр. 309)
