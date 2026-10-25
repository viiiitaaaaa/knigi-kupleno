<!-- gemini-3.5-flash-lite (Gemini, 2-й читатель), loop_engineering_playbook_06.txt -->
### Проверка результата · Всегда оценивать качество агента по метрикам и тестовым наборам, создавая eval-сьюты перед масштабированием · «An agent you cannot measure is an agent you cannot improve. Before Day 11, you must have a 10-case eval suite that runs in under 2 minutes on every code change.» (стр. 259–260).

### Ошибки · Избегать показа сырых технических ошибок пользователю и всегда заменять их понятным интерфейсом с вариантами дальнейших действий · «Never show a raw error. Always provide a next step... Every failure mode must have a user-facing message with a specific next step.» (стр. 241–242).

### Память · Распределять контекстное окно с помощью строгого бюджета памяти под разные типы данных · «Context budget: 50K tokens max... 30% for the bug report... 25% for import graph... 20% for grep results... 15% for test files... 10% for project structure.» (стр. 254).

### Экономия лимита · Использовать экономные модели для рутинных задач классификации и более мощные только для рассуждений · «Model routing: Haiku for search/classification, Sonnet for planning and code generation.» (стр. 254).

### Безопасность · Устанавливать финансовые лимиты и бюджеты на выполнение задач агентом для защиты от перерасхода средств · «Cost controls: $2 budget per bug.» (стр. 254).
