<!-- gemini-3.5-flash-lite (Gemini, 2-й читатель), agentic_design_patterns_15.txt -->
### Приём · Шаблон промпта для индексации документов · Использовать детальный промпт с указанием прочитать исходный документ, извлечь заголовки глав и построить полный алфавитный указатель (не менее 100 терминов) с указанием локаций. · Пример из текста: «do you read https://.../edit?tab=t.0 and all the related documents... Please extract all the titles for each chapter... I want the full index, with 100 index terms». · (стр. 445)

### Приём · Пошаговое планирование агента (Reasoning Steps) · Делать рассуждения прозрачными: фиксировать намерение пользователя, разбивать задачу на шаги, пакетно обрабатывать запросы (batching) для избежания лимитов и проверять артефакты. · Пример из текста: «1. Establish user intent: I've determined the user wants a chapter title list... Orchestrating Chapter Retrieval: batching the calls to prevent any rate-limiting issues». · (стр. 445)

### Приём · Ограничение контекстного окна (Context Window) · Учитывать максимальный объем токенов (вход + выход), помня, что информация вне окна игнорируется. · Пример из текста: «Context Window: The context window is the maximum number of tokens an AI model can process at once... information outside the window is ignored». · (стр. 450)

### Приём · Контекстное обучение (In-Context Learning) · Обучать модель новому заданию прямо в промпте на примерах без необходимости дообучения (retraining). · Пример из текста: «In-Context Learning is an AI's ability to learn a new task from examples provided directly in the prompt, without requiring any retraining». · (стр. 450)

### Приём · Примеры (Zero-Shot, One-Shot & Few-Shot Prompting) · Повышать точность и понимание намерений агента, передавая ему ноль, один или несколько примеров выполнения задачи. · Пример из текста: «Providing more examples generally helps the model better understand the user's intent and improves its accuracy for the specific task». · (стр. 451)

### Приём · Заземление (Grounding) · Подключать внешние источники (например, RAG) для проверки фактов на достоверность и снижения галлюцинаций. · Пример из текста: «Grounding is the process of connecting a model's outputs to verifiable, real-world information sources to ensure factual accuracy and reduce hallucinations. This is often achieved with techniques like RAG». · (стр. 452)

### Приём · Цепочка рассуждений (Chain of Thought, CoT) · Заставлять модель «думать вслух» и объяснять свое решение по шагам перед выдачей финального ответа для улучшения точности. · Пример из текста: «Chain of Thought: This prompting technique encourages a model to explain its reasoning step-by-step before giving a final answer». · (стр. 461)

### Приём · Дерево мыслей (Tree of Thoughts, ToT) · Исследовать несколько путей рассуждения одновременно (как ветки дерева) с возможностью самооценки и выбора лучшего направления. · Пример из текста: «Tree of Thoughts is an advanced reasoning framework where an agent explores multiple reasoning paths simultaneously... allows the agent to self-evaluate different lines of thought». · (стр. 462)

### Приём · Цикл «Рассуждение и действие» (ReAct) · Объединять мышление и действия в единый цикл, где агент думает, использует внешний инструмент, а затем анализирует полученное наблюдение. · Пример из текста: «ReAct is an agent framework that combines reasoning and acting in a loop. The agent first 'thinks' about what to do, then takes an 'action' using a tool...». · (стр. 463)

### Приём · Автономное планирование (Planning) · Декомпозировать глобальную цель на последовательность небольших подзадач для решения сложных многошаговых заданий. · Пример из текста: «Planning: This is an agent's ability to break down a high-level goal into a sequence of smaller, manageable sub-tasks... allows it to handle complex, multi-step assignments». · (стр. 463)

### Приём · Глубокие исследования (Deep Research) · Поручать агенту автономно исследовать тему итеративным поиском, синтезом результатов и генерацией новых вопросов. · Пример из текста: «Deep research refers to an agent's capability to autonomously explore a topic in-depth by iteratively searching for information, synthesizing findings, and identifying new questions». · (стр. 464)

### Приём · Критическая модель (Critique Model) · Использовать специализированную вспомогательную модель для проверки, оценки и рецензирования результатов работы основной модели. · Пример из текста: «A critique model is a specialized AI model trained to review, evaluate, and provide feedback on the output of another AI model... helping to identify errors, improve reasoning». · (стр. 464)
