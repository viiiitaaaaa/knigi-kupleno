<!-- gemini-3.5-flash-lite (Gemini, 2-й читатель), build_ai_agent_08.txt -->
### Управление сессиями и разработка для разработки · Используйте InMemorySessionManager для сред разработки и тестирования, который хранит сессии в словаре Python (в памяти) и сбрасывает их при завершении программы. · `class InMemorySessionManager(BaseSessionManager): ... self._sessions: dict[str, Session] = {}` · (стр. 189)

### Обеспечение обратной совместимости · Используйте свойства (`@property`) в расширенном классе ExecutionContext для доступа к событиям и состоянию через внутреннюю сессию, что позволяет существующему коду работать без изменений. · `class ExecutionContext: session: Session | None = None ... @property def events(self) -> list[Event]: return self.session.events` · (стр. 190)

### Инициализация агента с менеджером сессий · Настройте конструктор агента так, чтобы он принимал `session_manager`, а при его отсутствии автоматически использовал `InMemorySessionManager`. · `self.session_manager = session_manager or InMemorySessionManager()` · (стр. 191)

### Поддержка многооборотных диалогов через `session_id` · Передавайте одинаковый `session_id` при вызовах `run()`, чтобы агент сохранял контекст предыдущих взаимодействий и помнил информацию о пользователе. · `result1 = await agent.run("...", session_id="alice_session")` · (стр. 193)

### Разделение независимых задач и диалогов · Используйте сессии для диалоговых приложений с множеством сообщений; для одноразовых задач (например, проблем из бенчмарка GAIA) запускайте независимые вызовы `run()` без сессий. · `if session_id: session = await self.session_manager.get_or_create(session_id)` · (стр. 195)

### Сериализация сложных объектов в состояние сессии · Используйте методы Pydantic `model_dump()` и `model_validate()` для сохранения и восстановления сложных объектов (например, ожидающих подтверждения вызовов) в словаре состояния сессии `context.state`. · `context.state["pending_tool_calls"] = [p.model_dump() for p in pending_calls]` · (стр. 195)

### Добавление подтверждения действий пользователя (HITL) · Расширьте класс `BaseTool` атрибутами `requires_confirmation` и `confirmation_message_template`, чтобы агент останавливал выполнение деструктивных операций (например, удаления файлов) до получения одобрения. · `@tool(name="delete_file", requires_confirmation=True, confirmation_message="...")` · (стр. 196)

### Реализация внутренней логики фреймворка вместо колбэков · Обрабатывайте подтверждения инструментов внутри внутреннего метода `_prepare_llm_request()`, а не через пользовательские колбэки, чтобы избежать проблем с порядком выполнения и добавлением событий. · `async def _prepare_llm_request(self, context: ExecutionContext) -> LlmRequest:` · (стр. 198)

### Принцип упреждающего блокирования · Блокируйте выполнение инструментов, требующих подтверждения, ДО их фактического запуска, а не спрашивайте пользователя после того, как действие (например, удаление файла) уже совершено. · `if tool.requires_confirmation: pending_calls.append(pending); continue` · (стр. 199)

### Белый список подтверждений и частичное одобрение · Разрешайте пользователям одобрять только часть запрошенных инструментов (белый список); невыбранные или явно отклоненные инструменты автоматически обрабатываются как ошибки. · `if confirmation and confirmation.approved: ... else: results.append(ToolResult(..., status="error", content=[reason]))` · (стр. 202)

### Изменение аргументов пользователем · Позволяйте пользователям изменять аргументы инструментов при подтверждении (`modified_arguments`), объединяя их с оригинальными параметрами. · `arguments = {**pending.tool_call.arguments, **(confirmation.modified_arguments or {})}` · (стр. 203)

### Структурированное извлечение долгосрочной памяти · Используйте схемы Pydantic (например, `TaskMemory`) и параметр `response_format` в методе LLM `ask()`, чтобы извлекать из истории выполнения структурированные данные вместо неструктурированного текста. `TaskMemory(BaseModel)` · `data = await llm_client.ask(prompt, response_format=GaiaOutput)` · (стр. 208)

### Проверка на дубликаты в долгосрочной памяти · Перед сохранением нового воспоминания проверяйте его на дубликаты с помощью LLM, используя решение ADD (сохранить новое) или SKIP (пропустить, если такое уже есть). · `class DuplicateCheckResult(BaseModel): decision: str = Field(description="ADD or SKIP")` · (стр. 209)

### Использование локальной векторной базы данных ChromaDB · Применяйте легковесную базу данных ChromaDB с функцией эмбеддингов (например, OpenAIEmbeddingFunction) для автоматического преобразования документов в векторы и выполнения семантического поиска. · `client = chromadb.Client()`, `collection = client.get_or_create_collection(...)` · (стр. 210)

### Использование метаданных в векторном хранилище · Сохраняйте вспомогательную информацию (подходы, ответы, успешность) в параметре `metadatas` векторной базы данных вместе с текстовыми документами. · `collection.add(ids=[...], documents=[...], metadatas=[metadata])` · (стр. 214)

### Автоматическая инъекция памяти перед вызовом LLM · Реализуйте метод `process_llm_request()` у инструментов с `tool_definition=None`, чтобы автоматически внедрять релевантные прошлые воспоминания в инструкции для LLM перед каждым запросом без явного вызова инструмента моделью. · `request.append_instructions(f"...\n<PAST_EXPERIENCES>\n{result}\n</PAST_EXPERIENCES>")` · (стр. 217)
