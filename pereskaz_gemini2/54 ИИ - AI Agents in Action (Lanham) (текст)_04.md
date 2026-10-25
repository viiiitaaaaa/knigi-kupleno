<!-- gemini-3.5-flash-lite (Gemini, 2-й читатель), 54 ИИ - AI Agents in Action (Lanham) (текст)_04.txt -->
### Изоляция кода в Docker · Запускайте AutoGen и агентов через Docker для изоляции среды выполнения, предотвращения блокировок интерфейса и защиты операционной системы от потенциально вредоносного кода. · TIP: Executing AutoGen and AutoGen Studio using Docker is recommended, especially when working with code that may affect the operating system. (стр. 96)

### Использование готовых навыков вместо генерации кода · Предпочтительнее предоставлять агентам готовые навыки, действия и инструменты, а не заставлять их писать код для выполнения задач «на лету», так как написанный код быстро устаревает и ломается. · NOTE: Many agentic systems employ the practice of allowing agents to code to solve goals. However, we discovered that code can be easily broken... (стр. 97)

### Кэширование для экономии лимита · Используйте встроенное кэширование AutoGen (включая указание cache_seed), чтобы сохранять прогресс, продолжать прерванные сессии и сокращать расход токенов. · AutoGen uses caching to store progress and reduce token usage. Caching is enabled by default... (стр. 105)

### Контроль затрат и мониторинг через AgentOps · Подключайте платформы наблюдаемости вроде AgentOps для трекинга токенов, времени выполнения и оценки реальной денежной стоимости запросов агентов. · Connecting to AgentOps is as simple as installing the package... (стр. 88)

### Анализ зацикленности агентов · Проверяйте график «Repeat Thoughts» (повторяющиеся мысли) в AgentOps: чрезмерная повторяемость сигнализирует о нерешительности агента, требуя смены паттерна обработки, задач или изменения числа агентов. · The Repeat Thoughts plot from AgentOps is an excellent way to measure the repetition your agent system encounters. (стр. 98)
