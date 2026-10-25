<!-- gemini-3.5-flash-lite (Gemini, 2-й читатель), Building_Applications_with_AI_Agents_Albada (текст)_07.txt -->
### Планирование · Что делать: Использовать динамические граф-структуры и пошаговые блокноты (whiteboards/scratchpads) для решения сложных задач по шагам. · Пример из текста: «Just as for humans, it is not always possible to solve problems directly. Sometimes, we need to work through a problem step by step, and save our notes as we go. This is exactly what a “whiteboard” is for a foundation model...» · (стр. 7)

### Проверка результата · Что делать: Применять механизмы рефлексии (Reflexion) и проверки данных для анализа ошибок и корректировки поведения агента на основе языковой обратной связи. · Пример из текста: «In this approach, agents adapt based on linguistic feedback. Specifically, they take actions, receive feedback, and maintain their own text in which they regularly reflect on their performance in a memory buffer...» · (стр. 12)

### Память · Что делать: Хранить прошлый опыт (примеры успешных задач и взаимодействий) в банке памяти и динамически извлекать релевантные кейсы для промптов. · Пример из текста: «This typically involves building a memory bank where details of each interaction, such as the context, actions taken, outcomes, and any feedback received, are stored.» · (стр. 12)

### Контекст · Что делать: Использовать графовые базы данных (Graph RAG и Knowledge Graphs) и метод заметок (self-notes), чтобы обогащать контекст задачи связанной информацией и структурированными правилами. · Пример из текста: «With the self-note approach, the model generates notes on multiple parts of the context, and then generates a note on the question, before finally moving to generate the final answer.» · (стр. 7)

### Помощники · Приёмов нет.

### Ошибки · Что делать: Регулярно переоценивать и обновлять накопленные инсайты/правила (добавлять, удалять, редактировать, повышать или понижать их приоритет через ExpeL), чтобы избегать повторения прошлых неудач. · Пример из текста: «As the agent extracts insights from its experience bank, it maintains this list of insights over time, and dynamically modifies these insights, promoting the most valuable insights, downvoting the least useful ones...» · (стр. 12)

### Безопасность · Что делать: Применять строгие меры безопасности (шифрование, контроль доступа, анонимизацию) при работе с динамическими базами знаний, содержащими пользовательские данные. · Пример из текста: «Strong security measures, including encryption, access controls, and anonymization techniques, are crucial to ensure that all data inputs and integrations comply with current security and privacy regulations.» · (стр. 7)

### Экономия лимита · Что делать: Динамически отбирать и подставлять в промпт только самые релевантные примеры или инсайты вместо того, чтобы раздувать контекст всеми доступными данными. · Пример из текста: «A common way to address this is to dynamically select the most relevant examples to include tin the prompt...» · (стр. 12)
