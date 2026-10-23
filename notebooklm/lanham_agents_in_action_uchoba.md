# AI Agents in Action (Lanham) · NotebookLM · 2026-10-23 · 8 of 8 questions answered

(Ответы NotebookLM скопированы текстом; номера-сноски источников убраны; хвостовые предложения «Хотите…?» опущены.)

## Q1. Оглавление и пустые главы

Полное оглавление книги Майкла Лэнхэма «AI Agents in Action» («ИИ-агенты в действии»).

- Глава 1: Introduction to agents and their world — Введение в агентов и их мир. Раздел: Brief contents (стр. 8) / Contents (стр. 9). Цитата: "1 ■ Introduction to agents and their world 1" (стр. 8)
- Глава 2: Harnessing the power of large language models — Использование возможностей больших языковых моделей. (стр. 8 / стр. 9). Цитата: "2 ■ Harnessing the power of large language models 14" (стр. 8)
- Глава 3: Engaging GPT assistants — Работа с GPT-ассистентами. (стр. 8 / стр. 10). Цитата: "3 ■ Engaging GPT assistants 39" (стр. 8)
- Глава 4: Exploring multi-agent systems — Исследование многоагентных систем. (стр. 8 / стр. 10). Цитата: "4 ■ Exploring multi-agent systems 68" (стр. 8)
- Глава 5: Empowering agents with actions — Наделение агентов действиями. (стр. 8 / стр. 11). Цитата: "5 ■ Empowering agents with actions 98" (стр. 8)
- Глава 6: Building autonomous assistants — Создание автономных ассистентов. (стр. 8 / стр. 11). Цитата: "6 ■ Building autonomous assistants 129" (стр. 8)
- Глава 7: Assembling and using an agent platform — Сборка и использование платформы агентов. (стр. 8 / стр. 12). Цитата: "7 ■ Assembling and using an agent platform 160" (стр. 8)
- Глава 8: Understanding agent memory and knowledge — Понимание памяти и знаний агента. (стр. 8 / стр. 12). Цитата: "8 ■ Understanding agent memory and knowledge 180" (стр. 8)
- Глава 9: Mastering agent prompts with prompt flow — Освоение промптов агента с помощью Prompt Flow. (стр. 8 / стр. 13). Цитата: "9 ■ Mastering agent prompts with prompt flow 212" (стр. 8)
- Глава 10: Agent reasoning and evaluation — Рассуждение и оценка агентов. (стр. 8 / стр. 13). Цитата: "10 ■ Agent reasoning and evaluation 244" (стр. 8)
- Глава 11: Agent planning and feedback — Планирование и обратная связь агентов. (стр. 8 / стр. 13). Цитата: "11 ■ Agent planning and feedback 272" (стр. 8)

Приложения:
- Appendix A: Accessing OpenAI large language models — Доступ к большим языковым моделям OpenAI. Contents (стр. 14). Цитата: "appendix A Accessing OpenAI large language models 299" (стр. 14)
- Appendix B: Python development environment — Среда разработки Python. Contents (стр. 14). Цитата: "appendix B Python development environment 305" (стр. 14)

Пустые или недоступные главы: в книге нет пустых или недоступных глав. Все 11 глав и 2 приложения полностью присутствуют и содержат подробный материал. Раздел: About this book / How this book is organized: A road map (стр. 20). Цитата: "This book has 11 chapters." (стр. 20)


## Q2. Главные идеи по главам (5–10 на главу)

Глава 1: Introduction to agents and their world (Введение в агентов и их мир)
Понятие ИИ-агента: Агент — это разумный цифровой помощник, который выполняет задачи от имени человека и может самостоятельно принимать решения в рамках заданных правил
Адрес: Глава 1 › Раздел 1.1
Цитата: "A proxy agent is an everyday use case to assist users with unfamiliar tasks or models." (стр. 26)
Модели, цифры и пример: Модель DALL-E 3 в ChatGPT выступает прокси-агентом: когда пользователь просит нарисовать картинку, нейросеть сама переформулирует простой запрос в подробную инструкцию для генератора изображений
Четыре режима взаимодействия с ИИ: Книга разделяет работу с языковыми моделями на 4 уровня: прямое общение, прокси-агент, ассистент с функциями и автономный агент
Адрес: Глава 1 › Раздел 1.1
Цитата: "Figure 1.1 shows four cases where a user may interact with a large language model" (стр. 26)
Модели, цифры и пример: 4 режима общения — от обычного чата с ChatGPT до автономного ИИ, который сам читает и сортирует почту по важности
Многоагентные системы: Командная работа нескольких специализированных ИИ-агентов позволяет параллельно решать сложные задачи и проверять работу друг друга
Адрес: Глава 1 › Раздел 1.1
Цитата: "Where a single agent typically specializes in a single task, multi-agent systems can tackle multiple tasks in parallel." (стр. 28)
Модели, цифры и пример: Фреймворк Microsoft AutoGen; пример команды из 2 агентов: первый агент пишет код программы, а второй агент-тестировщик сразу создает к нему проверочные тесты
Пять базовых блоков агента: Архитектура любого одиночного ИИ-агента строится из 5 ключевых компонентов
Адрес: Глава 1 › Раздел 1.2
Цитата: "Figure 1.3 The five main components of a single-agent system" (стр. 29)
Модели, цифры и пример: 5 компонентов: профиль/персона, действия, память/знания, рассуждения/оценка и планирование/обратная связь
Профиль и персона ИИ: Профиль определяет «личность», роль, правила поведения и доступные инструменты агента
Адрес: Глава 1 › Раздел 1.2
Цитата: "The agent or assistant profile is composed of elements, including the persona." (стр. 30)
Модели, цифры и пример: Задание персоны опытного программиста или строгого тестировщика для генерации качественного кода
Память и базы знаний: Агенты используют кратковременную память для хранения текущего контекста и внешние базы знаний для поиска точных фактов
Адрес: Глава 1 › Раздел 1.2
Цитата: "Figure 1.6 Exploring the role and use of agent memory and knowledge" (стр. 31)
Модели, цифры и пример: Поиск информации в загруженных PDF-документах с помощью векторных эмбеддингов для экономии токенов
Урок проекта AutoGPT: Проект AutoGPT показал силу автономного планирования, но вскрыл проблему бесконечных циклов без контроля
Адрес: Глава 1 › Раздел 1.3
Цитата: "AutoGPT became the first example to demonstrate the power of using task planning and iteration with LLM models." (стр. 33)
Модели, цифры и пример: Модель GPT-4 и система AutoGPT, которая пошагово составляет и уточняет план действий для достижения цели
Сдвиг парадигмы интерфейсов ПО: Программы будущего избавятся от загроможденных меню и кнопок в пользу разговорного ИИ-посредника
Адрес: Глава 1 › Раздел 1.4
Цитата: "Instead, they will be designed to be interfaced using natural language." (стр. 35)
Модели, цифры и пример: Запрос отчета по продажам за прошлый год обычными словами вместо составления сложных SQL-запросов к базе данных
Глава 2: Harnessing the power of large language models (Использование возможностей больших языковых моделей)
Генеративные модели против предиктивных: Современные LLM обучены создавать новый текст и контент, а не просто классифицировать данные
Адрес: Глава 2 › Раздел 2.1
Цитата: "LLMs and GPTs are generative models, which means they are trained to generate rather than predict or classify content." (стр. 38)
Модели, цифры и пример: Архитектура GPT (Generative Pretrained Transformer), масштабируемая до миллиардов параметров
Работа с OpenAI API и Chat Completions: Для взаимодействия с нейросетями используется эндпоинт диалоговых завершений (Chat Completions)
Адрес: Глава 2 › Раздел 2.1
Цитата: "This chapter will look at connecting to an LLM model using the OpenAI Python SDK/package." (стр. 40)
Модели, цифры и пример: Подключение к модели gpt-4-1106-preview (GPT-4 Turbo) через библиотеку openai
Три роли в сообщениях API: Запросы делятся на 3 роли: system (правила/персона), user (запрос пользователя) и assistant (история ответов ИИ)
Адрес: Глава 2 › Раздел 2.1
Цитата: "Within the request, the messages block describes a set of messages and roles used in a request." (стр. 42)
Модели, цифры и пример: 3 роли; пример системной роли: "You are a helpful assistant."
Локальный запуск открытых моделей через LM Studio: Программа LM Studio позволяет бесплатно запускать нейросети прямо на своем компьютере без отправки данных в облако
Адрес: Глава 2 › Раздел 2.2
Цитата: "Here is a quick summary of steps to download and set up LM Studio" (стр. 44)
Модели, цифры и пример: Локальный сервер LM Studio на порту 1234, полностью эмулирующий API OpenAI
Промпт-инжиниринг: Четкие инструкции: Качество ответа ИИ напрямую зависит от точности и детализации сформулированного запроса
Адрес: Глава 2 › Раздел 2.3
Цитата: "Each strategy in figure 2.8 unfolds into tactics that can further refine the specific method of prompt engineering." (стр. 49)
Модели, цифры и пример: Стратегия «Write Clear Instructions»
Тактика роли (Adopting Personas): Задание нейросети конкретной роли существенно меняет стиль и глубину ответов
Адрес: Глава 2 › Раздел 2.3
Цитата: "Adopting personas grants the ability to define an overarching context or set of rules to the LLM." (стр. 53)
Модели, цифры и пример: Сравнение ответов 20-летней студентки-программиста и 38-летнего медбрата на вопрос о выборе предмета для изучения
Использование разделителей и лимитов длины: Спецсимволы отделяют данные от команд, а лимиты помогают получать краткие ответы без «воды»
Адрес: Глава 2 › Раздел 2.3
Цитата: "Delimiters are a useful way of isolating and getting the LLM to focus on some part of a message." (стр. 54)
Модели, цифры и пример: Использование тройных кавычек ''' или XML-тегов <statement>; ограничение ответа строго 3 маркированными пунктами
Восемь критериев выбора моделей: Выбор нейросети зависит от параметров размера, стоимости, скорости и объема контекста
Адрес: Глава 2 › Раздел 2.4
Цитата: "Figure 2.11 The important criteria to consider when consuming an LLM" (стр. 58)
Модели, цифры и пример: 8 критериев выбора модели; сравнение коммерческой GPT-4 Turbo с локальными open-source нейросетями
Глава 3: Engaging GPT assistants (Работа с GPT-ассистентами)
Магазин кастомных ассистентов GPT Store: Платформа OpenAI позволяет без программирования создавать специализированных ИИ-помощников
Адрес: Глава 3 › Раздел 3.1
Цитата: "Figure 3.1 shows the page for the GPT Store within ChatGPT" (стр. 64)
Модели, цифры и пример: Подписка ChatGPT Plus и конструктор GPT Builder
Кулинарный помощник "Culinary Companion": Пример кастомного GPT с жесткими правилами оформления ответа
Адрес: Глава 3 › Раздел 3.1
Цитата: "Culinary Companion assists users with a friendly, engaging tone, reminiscent of the famous chef Julia Child." (стр. 66)
Модели, цифры и пример: Персона шеф-повара Джулии Чайлд; правила сгенерировать картинку блюда через DALL-E 3, рассчитать калории и составить список покупок
Интерпретатор кода (Code Interpreter) для анализа данных: Встроенная песочница Python позволяет ассистенту проводить дата-сайнс исследования
Адрес: Глава 3 › Раздел 3.2
Цитата: "When you enable code interpretation, the assistant will allow file uploads by default." (стр. 68)
Модели, цифры и пример: Ассистент "Data Scout", самостоятельно читающий CSV-файл с фильмами Netflix и строящий графики через библиотеку pandas
Пользовательские действия (Custom Actions): Расширение возможностей GPT путем подключения внешних веб-сервисов по API
Адрес: Глава 3 › Раздел 3.3
Цитата: "Custom actions are a great way to add dynamic functionality to an assistant, whether for personal or commercial use." (стр. 79)
Модели, цифры и пример: Создание REST API на FastAPI, описание в формате OpenAPI/Swagger и проброс туннеля через ngrok на порт 8000
Ассистент-организатор задач "Task Organizer": Пример использования действия для управления ежедневными делами
Адрес: Глава 3 › Раздел 3.3
Цитата: "Task Organizer is designed to help the user prioritize their daily tasks based on urgency and time availability" (стр. 77)
Модели, цифры и пример: Персона Тима Феррисса, обращающаяся к локальному API за списком задач и строящая график расписания на день
Загрузка файлов и расширение знаний: Загрузка документов расширяет знания ассистента до 512 МБ статичного контекста
Адрес: Глава 3 › Раздел 3.4
Цитата: "The GPT Assistants platform provides a knowledge capability called file uploads, which allows you to populate the GPT with a static knowledge base" (стр. 80)
Модели, цифры и пример: Лимит 512 МБ; ассистент по учебнику математики Silvanus P. Thompson «Calculus Made Easy»
Поисковый ассистент по библиотеке книг: Загрузка нескольких файлов превращает GPT в диалоговую поисковую систему
Адрес: Глава 3 › Раздел 3.4
Цитата: "This GPT will only references and discusses the books in its knowledge base of uploaded files." (стр. 83)
Модели, цифры и пример: Ассистент "Classic Robot Reads GPT", загружающий 5 классических книг о роботах из библиотеки Gutenberg
Глава 4: Exploring multi-agent systems (Исследование многоагентных систем)
Сила многоагентных систем: Перекрестная критика и совместное обсуждение нескольких агентов снижают ошибки и повышают качество решений
Адрес: Глава 4 › Раздел 4.1
Цитата: "This ability to support and criticize agent solutions internally gives multi-agent systems more power." (стр. 69)
Модели, цифры и пример: Взаимодействие агентов между собой на естественном языке
Платформа Microsoft AutoGen: Фреймворк для создания диалоговых команд ИИ-агентов
Адрес: Глава 4 › Раздел 4.1
Цитата: "AutoGen is a conversational multi-agent platform because communication is done using natural language." (стр. 69)
Модели, цифры и пример: Связка агента пользователя UserProxyAgent и исполнителя ConversableAgent
Визуальная студия AutoGen Studio: Графический веб-интерфейс для простой разработки и проверки работы агентов
Адрес: Глава 4 › Раздел 4.1
Цитата: "AutoGen Studio is a powerful tool that employs multiple agents behind the scenes to solve tasks and problems a user directs." (стр. 69)
Модели, цифры и пример: Запуск интерфейса на порту 8081 с безопасной изоляцией кода в Docker
Агент-критик для повышения качества кода: Подключение специализированного агента-проверщика для глубокого аудита кода
Адрес: Глава 4 › Раздел 4.2
Цитата: "In the next exercise, we’ll add another agent critic to our agent system to help with coding tasks." (стр. 79)
Модели, цифры и пример: Роли "Engineer" и "Reviewer", взаимодействующие для создания игры "Snake" на базе Pygame
Групповые чаты (GroupChat) в AutoGen: Координация диалога нескольких агентов через единого модератора (GroupChatManager)
Адрес: Глава 4 › Раздел 4.3
Цитата: "The chat manager coordinates the message responses to reduce conversation overlap." (стр. 82)
Модели, цифры и пример: Настройка до 20 раундов обсуждения в общем чате формата Slack или Discord
Экосистема CrewAI: Фреймворк корпоративного уровня для сборки «экипажей» агентов с явным разделением задач
Адрес: Глава 4 › Раздел 4.4
Цитата: "CrewAI offers a structured approach to building multi-agent systems with a focus on enterprise applications." (стр. 96)
Модели, цифры и пример: Команда шутников: исследователь юмора "Senior Joke Researcher" и комедийный писатель "Joke Writer"
Параметры агента в CrewAI: Обязательное задание роли (role), цели (goal) и легенды/предыстории (backstory)
Адрес: Глава 4 › Раздел 4.4
Цитата: "The backstory is the agent’s background—its persona." (стр. 85)
Модели, цифры и пример: 3 обязательных элемента личности каждого агента
Наблюдаемость и стоимость операций с AgentOps: Отслеживание затрат и логов взаимодействия агентов в реальном времени
Адрес: Глава 4 › Раздел 4.4
Цитата: "Connecting to AgentOps is as simple as installing the package, getting an API key, and adding a line of code" (стр. 88)
Модели, цифры и пример: Создание одной хорошей шутки обошлось примерно в 0.50$ (50 центов) из-за избыточных циклов согласования
Глава 5: Empowering agents with actions (Наделение агентов действиями)
Наделение агентов действиями (Actions): Действия превращают чат-бот в активный инструмент, способный изменять внешнюю среду
Адрес: Глава 5 › Раздел 5.1
Цитата: "An agent action is an ability that allows it to use a function, skill, or tool." (стр. 100)
Модели, цифры и пример: Плагин рекомендации фильмов, запрашивающий внешний сайт и фильтрующий результаты
Вызов функций в OpenAI API (Function Calling): Нейросеть сама распознает нужную функцию и подготавливает аргументы для нее
Адрес: Глава 5 › Раздел 5.2
Цитата: "Adding a function definition allows the LLM to reply regarding the function’s input parameters." (стр. 101)
Модели, цифры и пример: Параметр tools со спецификацией типа function
Параллельный вызов нескольких функций: Модель может одновременно за один шаг подготовить вызовы нескольких функций
Адрес: Глава 5 › Раздел 5.2
Цитата: "This call uses a lower model such as GPT-3.5 because delegating functions is a more straightforward task" (стр. 105)
Модели, цифры и пример: Использование более дешевой модели gpt-3.5-turbo-1106 для параллельной генерации сразу 3 рекомендаций (фильм, рецепт, подарок)
Фреймворк Microsoft Semantic Kernel (SK): Открытый движок для создания и оркестрации плагинов ИИ
Адрес: Глава 5 › Раздел 5.3
Цитата: "The Semantic Kernel (SK) is an open source project from Microsoft that can be used to build AI applications and agent systems." (стр. 128)
Модели, цифры и пример: Поддержка языков Python, C# и Java
Семантические функции (Semantic Functions): Обертывание текстовых промптов-шаблонов в исполняемые функции
Адрес: Глава 5 › Раздел 5.3
Цитата: "A semantic function encapsulates the prompt/profile template used to engage an LLM." (стр. 128)
Модели, цифры и пример: Шаблон промпта с переменными контекста {{$format}}, {{$subject}}, {{$genre}}
Нативные функции (Native Functions): Обычный код на Python, оформленный в виде плагина для нейросети
Адрес: Глава 5 › Раздел 5.4
Цитата: "Native functions encapsulate code that performs or executes an action using an API or other interface." (стр. 128)
Модели, цифры и пример: Класс MySeenMoviesDatabase с декоратором @kernel_function, считывающий список просмотренных фильмов из локального файла
Семантический слой над сторонним API (TMDB): Превращение любого внешнего веб-сервиса в удобный естественный интерфейс
Адрес: Глава 5 › Раздел 5.5
Цитата: "SK can be used to create a GPT interface over the top of API calls in a semantic service layer" (стр. 128)
Модели, цифры и пример: Сервис The Movie Database (TMDB); функции get_movie_genre_id и get_top_movies_by_genre
Глава 6: Building autonomous assistants (Создание автономных ассистентов)
Деревья поведения (Behavior Trees): Модульная структура управления ИИ, пришедшая из робототехники и видеоигр
Адрес: Глава 6 › Раздел 6.1
Цитата: "Behavior trees are a long-established pattern used to control robotics and AI in games." (стр. 130)
Модели, цифры и пример: Выполнение узлов по принципу успеха (Success) или неудачи (Failure)
Типы узлов в деревьях поведения: 6 главных типов узлов: селекторы (Selector), последовательности (Sequence), условия (Condition), действия (Action), декораторы (Decorator) и параллели (Parallel)
Адрес: Глава 6 › Раздел 6.1
Цитата: "The primary nodes in behavior trees are the selector, sequence, condition, action, decorator, and parallel nodes." (стр. 182)
Модели, цифры и пример: 6 типов узлов; библиотечный пакет py_trees на Python
Инструмент GPT Assistants Playground: Веб-интерфейс на Gradio для тестирования ассистентов и локального запуска кода
Адрес: Глава 6 › Раздел 6.2
Цитата: "The GPT Assistants Playground project is a Gradio-based interface that mimics the OpenAI Assistants Playground with additional features" (стр. 182)
Модели, цифры и пример: Запуск локального интерфейса на порту 7860
Локальный запуск Python-кода: Использование действий run_code и run_shell_command для создания рабочих программ
Адрес: Глава 6 › Раздел 6.2
Цитата: "Unlike the Code Interpreter, running code locally provides numerous opportunities to iterate and tune quickly." (стр. 140)
Модели, цифры и пример: Создание игры "Snake" с автоматической автоустановкой библиотеки Pygame через консоль
Агентные деревья поведения (ABT): Использование языковых моделей для управления узлами действий и условий
Адрес: Глава 6 › Раздел 6.3
Цитата: "Agentic behavior trees (ABTs) implement behavior trees on assistant and agent systems." (стр. 143)
Модели, цифры и пример: Решение экспертной задачи программирования "Plant the Grass" с сайта Edabit
Изолированные потоки (Threads) для агентов: Разделение коммуникаций агентов по отдельным чатам для уменьшения шума
Адрес: Глава 6 › Раздел 6.3
Цитата: "Keeping the Verifier on its own thread isolates it from the noise of the solution-solving efforts." (стр. 147)
Модели, цифры и пример: Связка 3 агентов: программист "Hacker", судья "Judge" и верификатор "Verifier"
Автоматический публикатор в соцсеть X (Twitter): Комплексный ABT-пайплайн для поиска и суммаризации роликов с YouTube
Адрес: Глава 6 › Раздел 6.3
Цитата: "This assistant searches YouTube for videos, downloads and summarizes the transcripts, and saves to a file." (стр. 150)
Модели, цифры и пример: Ассистенты "YouTube Researcher v2", "Twitter Post Writer" и лимит поста в 280 символов
Метод обратной цепочки (Back Chaining): Построение дерева поведения от финальной цели к начальным действиям
Адрес: Глава 6 › Раздел 6.5
Цитата: "Back chaining is a method derived from logic and reasoning used to help build behavior trees by working backward from the goal." (стр. 155)
Модели, цифры и пример: 5 этапов конструирования ABT
Глава 7: Assembling and using an agent platform (Сборка и использование платформы агентов)
Платформа Nexus: Открытая платформа, созданная для изучения и развертывания мультиагентных систем
Адрес: Глава 7 › Раздел 7.1
Цитата: "Nexus is an open source platform developed with this book to teach the core concepts of building full-featured AI agents." (стр. 161)
Модели, цифры и пример: Веб-интерфейс на базе фреймворка Streamlit
Использование фреймворка Streamlit: Быстрое создание диалоговых веб-приложений на чистом Python
Адрес: Глава 7 › Раздел 7.2
Цитата: "Streamlit, a Python web application framework, enables the rapid development of user-friendly dashboards and chat applications." (стр. 179)
Модели, цифры и пример: Сохранение состояния сессии st.session_state и поле ввода st.chat_input
Определение профилей агентов через YAML: Конфигурация ролей, инструкций и доступных инструментов в виде файлов
Адрес: Глава 7 › Раздел 7.3
Цитата: "Add any agent profiles to Nexus by copying an agent YAML profile file into the Nexus/nexus/nexus_base/nexus_profiles folder." (стр. 170)
Модели, цифры и пример: Профиль fiona.yaml с персоной великана (Ogre), отвечающей зашифрованными фразами
Движки агентов (Agent Engines): Базовые адаптеры для подключения различных провайдеров нейросетей
Адрес: Глава 7 › Раздел 7.4
Цитата: "Agent engines power agents within Nexus. These engines can be tied to specific tool platforms" (стр. 172)
Модели, цифры и пример: Базовый класс BaseAgent и реализация OpenAIAgent (oai_agent.py)
Автоматическое обнаружение действий (Actions): Динамическое подключение Python-функций с помощью декоратора @agent_action
Адрес: Глава 7 › Раздел 7.5
Цитата: "Adding the agent_action decorator allows the functions to be inspected and automatically generates the OpenAI standard tool specification." (стр. 175)
Модели, цифры и пример: Папка nexus_actions; функции get_current_weather и recommend
Параллельное исполнение инструментов: Движок агента исполняет несколько вызванных функций одновременно
Адрес: Глава 7 › Раздел 7.5
Цитата: "This code demonstrates how the agent supports parallel function/tool calls." (стр. 176)
Модели, цифры и пример: Персона "Olly", одновременно вызывающая инструмент погоды и инструмент рекомендаций в одном ответе
Глава 8: Understanding agent memory and knowledge (Понимание памяти и знаний агента)
Поиск и дополненная генерация (RAG): Подмешивание внешних фактов из документов в промпт для устранения галлюцинаций
Адрес: Глава 8 › Раздел 8.2
Цитата: "The retrieval mechanism, called retrieval augmented generation (RAG), has become a standard for providing relevant context to a prompt." (стр. 182)
Модели, цифры и пример: Стратегии промпт-инжиниринга «Provide Reference Text» и «Use External Tools»
Векторный поиск и сходство документов: Преобразование текста в числа и измерение косинусного расстояния
Адрес: Глава 8 › Раздел 8.3
Цитата: "Cosine similarity is a measure used to calculate the cosine of the angle between two nonzero vectors" (стр. 186)
Модели, цифры и пример: Классический показатель TF-IDF; косинусное сходство от -1 до 1 и расстояние от 0 до 2
Векторные эмбеддинги: Преобразование глубокого смысла слов в многомерные векторы
Адрес: Глава 8 › Раздел 8.3
Цитата: "When a document is embedded using an OpenAI model, it transforms the text into a vector with dimensions of 1536." (стр. 190)
Модели, цифры и пример: Модель text-embedding-ada-002 (1536 измерений); сокращение методом PCA до 3D для наглядного графика
Локальная векторная база Chroma DB: Хранилище для быстрого смыслового поиска по текстам
Адрес: Глава 8 › Раздел 8.3
Цитата: "Chroma DB is an excellent local vector store for development or small-scale projects." (стр. 190)
Модели, цифры и пример: Локальная библиотека chromadb
Разбиение документов (Chunking) в LangChain: Деление больших текстов на небольшие куски с перекрытием
Адрес: Глава 8 › Раздел 8.4
Цитата: "Splitting a document is essential in breaking down content into semantically and specifically relevant sections." (стр. 193)
Модели, цифры и пример: Загрузчик HTML UnstructuredHTMLLoader; деление текстов «Mother Goose» на куски по 100 символов с перекрытием 25 символов или по 50 токенов (через tiktoken)
Базы знаний в платформе Nexus: Подключение векторного поиска по документам к диалоговому агенту
Адрес: Глава 8 › Раздел 8.5
Цитата: "Create a new Knowledge Store, and then upload the sample_documents/back_to_the_future.txt movie script." (стр. 197)
Модели, цифры и пример: База знаний по сценарию фильма «Назад в будущее»
Виды памяти ИИ-агента: Разделение памяти на кратковременную (контекст текущего диалога) и долгосрочную (факты)
Адрес: Глава 8 › Раздел 8.6
Цитата: "Explicit/declarative memory... Episodic memory (life events)... Semantic memory (facts, concepts)" (стр. 200)
Модели, цифры и пример: Семантическая, эпизодическая и процедурная память
Сжатие памяти и знаний (Compression): Автоматическое объединение повторяющихся воспоминаний с помощью кластеризации
Адрес: Глава 8 › Раздел 8.7
Цитата: "Memories or knowledge are first clustered using an algorithm such as k-means. Then, the groups of memories are passed through a compression function" (стр. 207)
Модели, цифры и пример: Кластеризация методом k-means и дальнейшая суммаризация через модель GPT-4
Глава 9: Mastering agent prompts with prompt flow (Освоение промптов агента с помощью Prompt Flow)
Систематический промпт-инжиниринг: Стратегия «Test Changes Systematically» для автоматизированного тестирования промптов
Адрес: Глава 9 › Раздел 9.1
Цитата: "Test Changes Systematically is such a core facet of prompt engineering that Microsoft developed a tool around this strategy called prompt flow" (стр. 212)
Модели, цифры и пример: Инструментарий Microsoft Prompt Flow
Шаблонизатор Jinja2 для промптов: Использование шаблонов для гибкой сборки профилей агента
Адрес: Глава 9 › Раздел 9.3
Цитата: "By default, prompt flow uses Jinja2 templates to define the content of the prompt or what we’ll call a profile." (стр. 222)
Модели, цифры и пример: Шаблоны с расширением .jinja2
Развертывание веб-приложения и API: Превращение графа промптов в готовый веб-сервис
Адрес: Глава 9 › Раздел 9.3
Цитата: "Prompt flow can be deployed as a local web application and API running from the terminal or as a Docker container." (стр. 223)
Модели, цифры и пример: Локальное веб-приложение или контейнер Docker
Варианты промптов (Prompt Variants): Параллельное тестирование нескольких версий промптов для выбора лучшей
Адрес: Глава 9 › Раздел 9.4
Цитата: "LLM blocks support prompt and profile variants, which allow for evaluating changes to the prompt/profile" (стр. 243)
Модели, цифры и пример: Сравнение вставки вводных данных в системный или пользовательский промпт
Оценка качества с помощью Рубрик и ИИ (LLM-as-a-judge): Автоматическая проверка ответов старшей нейросетью по критериям
Адрес: Глава 9 › Раздел 9.5 & 9.6
Цитата: "Using LLMs to evaluate prompts and profiles provides a strong baseline for comparing the performance of a profile." (стр. 231)
Модели, цифры и пример: Шкала оценки (рубрика) и обработка оценок скриптом parsing_results.py
Пакетное тестирование (Batch Processing): Массовый запуск промптов на наборе тестовых данных
Адрес: Глава 9 › Раздел 9.7
Цитата: "Prompt flow can batch-process any variations we want to test." (стр. 235)
Модели, цифры и пример: Файл bulk_recommend.jsonl с 10 тестовыми примерами
Сравнение прогонов (Visualize Runs): Наглядная панель для сравнения баллов и стоимости разного исполнения промптов
Адрес: Глава 9 › Раздел 9.7
Цитата: "The Visualize Runs option can compare the aggregated criteria from scoring the rubric across multiple runs." (стр. 243)
Модели, цифры и пример: Сравнение средних оценок по критериям
Глава 10: Agent reasoning and evaluation (Рассуждение и оценка агентов)
Прямое решение задач (Direct Solution Prompting): Базовый способ решения задач путем прямого вопроса к нейросети
Адрес: Глава 10 › Раздел 10.1
Цитата: "Direct solution prompting is generally the first form of prompt engineering that users employ when asking LLMs questions" (стр. 245)
Модели, цифры и пример: Вопросы по сюжету фильма «Назад в будущее»
Обучение с несколькими примерами (Few-Shot Prompting): Показ нейросети нескольких примеров ответа для адаптации к новым шаблонам
Адрес: Глава 10 › Раздел 10.1
Цитата: "Few-shot prompting provides LLMs with a few examples to guide them in handling new or unseen content" (стр. 271)
Модели, цифры и пример: Обучение ИИ правильно использовать вымышленное слово "sunner" или "whatpu" на 2 примерах
Нулевой пример (Zero-Shot Prompting): Генерация ответа на основе собственных обобщающих знаний модели без примеров
Адрес: Глава 10 › Раздел 10.1
Цитата: "Zero-shot prompting or learning is the ability to generate a prompt in such a manner that allows the LLM to generalize." (стр. 250)
Модели, цифры и пример: Задачи классификации и определения эмоциональной окраски текста
Цепочка мыслей (Chain of Thought, CoT): Побуждение модели рассуждать по шагам перед выдачей финального ответа
Адрес: Глава 10 › Раздел 10.2
Цитата: "Chain of thought prompting guides the LLMs through a reasoning process step by step to solve complex problems" (стр. 271)
Модели, цифры и пример: Задачи на логику путешествий во времени (истории путешественников Сары, Алекса и Макса)
Фраза Zero-Shot CoT: Простая фраза заставляет нейросеть рассуждать по шагам без единого примера
Адрес: Глава 10 › Раздел 10.2
Цитата: "The line in the prompt Let’s think step by step triggers the LLM to consider internal context showing reasoning." (стр. 258)
Модели, цифры и пример: Фраза "Let's think step by step"
Цепочка промптов (Prompt Chaining): Разбиение сложной задачи на несколько последовательных вызовов нейросети
Адрес: Глава 10 › Раздел 10.2
Цитата: "Prompt chaining breaks down a problem into a series of prompts that build upon each other" (стр. 271)
Модели, цифры и пример: 3 шага цепочки: разбиение задачи на шаги (decompose_steps), расчет значений (calculate_steps) и выдача ответа (calculate_solution)
Самосогласованность и голосование (Self-Consistency): Генерация нескольких независимых решений и выбор наиболее частого ответа
Адрес: Глава 10 › Раздел 10.3
Цитата: "Self-consistency generates multiple reasoning paths and selects the majority answer." (стр. 271)
Модели, цифры и пример: Генерация 5 независимых вариантов решения задачи и поиск наиболее частого ответа через сравнение эмбеддингов consistency.py
Дерево мыслей (Tree of Thought, ToT): Построение дерева поиска решений с отсечением неперспективных веток
Адрес: Глава 10 › Раздел 10.3
Цитата: "Tree of thought prompting combines self-evaluation and prompt chaining to create a comprehensive strategy for tackling complex problems" (стр. 271)
Модели, цифры и пример: Поиск в ширину (breadth-first); отсечение веток с оценкой ниже 25 баллов
Глава 11: Agent planning and feedback (Планирование и обратная связь агентов)
Планирование как основа агента: Агент отличается от обычного чат-бота способностью самостоятельно разбивать цель на последовательные действия
Адрес: Глава 11 › Раздел 11.1
Цитата: "Agents and assistants who can’t plan and only follow simple interactions are nothing more than chatbots." (стр. 273)
Модели, цифры и пример: Автоматический перевод пользовательской цели в список конкретных подзадач
Параллельное против последовательного планирования: Необходимость различать независимые действия и задачи с жесткой последовательностью
Адрес: Глава 11 › Раздел 11.1 & 11.2
Цитата: "Agents must differentiate between parallel and sequential actions." (стр. 297)
Модели, цифры и пример: Цель поиска статей в Википедии по теме "Calgary", скачивания страниц и сохранения в файл требует строго последовательного исполнения
Создание базового планировщика Nexus: Разработка модуля генерации и исполнения JSON-планов
Адрес: Глава 11 › Раздел 11.3
Цитата: "This planner uses JSON, but planners could use any format an LLM understands, including code." (стр. 279)
Модели, цифры и пример: Модуль basic_nexus_planner.py; поддержка специальной функции циклов for-each для итеративной обработки списков
Модель с встроенным планированием OpenAI Strawberry (o1-preview): Появление нейросетей со встроенным пошаговым рассуждением
Адрес: Глава 11 › Раздел 11.4
Цитата: "Models such as OpenAI Strawberry integrate reasoning, planning, evaluation, and feedback directly into the LLM" (стр. 298)
Модели, цифры и пример: Модель o1-preview (Strawberry)
Обратная связь для самокоррекции: Генерация критики и инструкций для исправления ошибок
Адрес: Глава 11 › Раздел 11.4
Цитата: "Feedback is crucial in guiding agents to correct their course and improve performance over time." (стр. 297)
Модели, цифры и пример: Промпт: "the correct answer is 27, please review what you did wrong and suggest feedback..." для коррекции рассуждений в логических задачах
Шесть сфер применения планирования и рассуждений: Анализ использования агентов в реальных системах
Адрес: Глава 11 › Раздел 11.5
Цитата: "Table 11.1 shows several varied application scenarios in which we may find an assistant or agent deployed" (стр. 289)
Модели, цифры и пример: 6 направлений: персональные ассистенты, боты поддержки, автономные агенты, совместные рабочие процессы, игровой ИИ и научные исследования

## Q3. Практические приёмы для ИИ-помощника в Claude Code

Вот практическое руководство по настройке и ежедневной эксплуатации ИИ-помощника в Claude Code, составленное на основе архитектурных принципов и паттернов из книги Майкла Лэнхэма «AI Agents in Action».
1. Правила (инструкции и персона, аналог CLAUDE.md)
Примечание: Конкретного файла с названием CLAUDE.md в книге нет, так как это специфичный файл настройки Claude Code, но сам концепт глобального системного промпта, жестких правил (RULES) и персоны подробно описан в книге
Что сделать: Создать системный промпт с четкой персоной (роль, квалификация), набором явных правил (RULES) и разделителями (XML-теги или тройные кавычки) для изоляции кода и данных
Зачем: Жесткие правила создают предсказуемый шаблон работы помощника, предотвращают отклонение от формата ответа и обеспечивают стабильность результатов
Когда: При создании проекта, первичной настройке помощника и формировании единого стандарта ответов команды.
Адрес в книге: Глава 2 › Раздел 2.3 (стр. 49, 53, 54), Глава 3 › Раздел 3.1 (стр. 67)
Цитата: "Defining rules for an assistant/agent essentially creates a template for what the agent will produce." (стр. 67)
2. Скиллы (нативные функции, инструменты и кастомные действия)
Что сделать: Оформить часто выполняемые операции (вызовы API, запуск линтеров, сборку, работу с БД) в виде чистых функций на Python или скриптов с четким описанием docstrings и явной декорацией
Зачем: Нативные навыки и действия дают помощнику возможность взаимодействовать с реальной окружением вместо попыток генерировать код «вслепую»
Когда: Когда ассистенту требуется выйти за рамки работы с текстом и выполнять физические действия в операционной системе или внешних сервисах.
Адрес в книге: Глава 5 › Раздел 5.1 (стр. 100), Раздел 5.4 (стр. 115), Глава 7 › Раздел 7.5 (стр. 175)
Цитата: "An agent action is an ability that allows it to use a function, skill, or tool." (стр. 100)
3. Память (долгосрочный контекст, RAG и сжатие)
Что сделать: Подключить векторный поиск (RAG) по базе знаний проекта, а при разрастании истории сессий применять алгоритмы сжатия (компрессии и кластеризации facts/memories)
Зачем: Предоставляет ИИ доступ к истории проекта и документации без переполнения контекстного окна и снижает риск галлюцинаций
Когда: При работе с крупными кодовыми базами, накоплении большого объема требований или в долгоживущих проектах.
Адрес в книге: Глава 8 › Раздел 8.2 (стр. 182), Раздел 8.6 (стр. 200), Раздел 8.7 (стр. 207)
Цитата: "The retrieval mechanism, called retrieval augmented generation (RAG), has become a standard for providing relevant context to a prompt." (стр. 182)
4. Субагенты (многоагентные системы и разделение ролей)
Что сделать: Разбить рефакторинг или разработку на специализированных субагентов (например, Coder для написания кода, Critic/Reviewer для аудита, Tester для написания unit-тестов)
Зачем: Специализация агентов и их взаимная критика в группе существенно повышают точность решения и находят скрытые ошибки
Когда: При проектировании сложных модулей, написании критически важного кода и проведении автоматического ревью.
Адрес в книге: Глава 1 › Раздел 1.1 (стр. 28), Глава 4 › Раздел 4.2 (стр. 79), Раздел 4.3 (стр. 82)
Цитата: "Where a single agent typically specializes in a single task, multi-agent systems can tackle multiple tasks in parallel." (стр. 28)
5. Проверка результата (верификаторы и циклы обратной связи)
Что сделать: Изолировать этап проверки от этапа написания (направить работу отдельному агенту-верификатору или запустить локальный тест-раннер) и не завершать сессию без подтверждения успеха тестов
Зачем: Изоляция верификатора в отдельном потоке общения спасает от «шума» промежуточных рассуждений и гарантирует, что пользователь получит только работоспособный код
Когда: После каждого сгенерированного решения перед его окончательным сохранением в проект.
Адрес в книге: Глава 4 › Раздел 4.1 (стр. 70), Глава 6 › Раздел 6.3 (стр. 147, 154)
Цитата: "Keeping the Verifier on its own thread isolates it from the noise of the solution-solving efforts." (стр. 147)
6. Оценка качества (рубрики и LLM-as-a-judge)
Что сделать: Разработать формальную шкалу оценки (рубрику) и запускать отдельный проверочный промпт (или батч-тесты через Prompt Flow) для проверки ответов помощника
Зачем: Оценка по шкале дает объективный, измеримый и воспроизводимый критерий того, стал ли ассистент работать лучше после изменения правил или промптов
Когда: При обновлении правил, добавлении новых скиллов или массовой проверке работы ассистента на тестовом наборе задач.
Адрес в книге: Глава 9 › Раздел 9.5 (стр. 228), Раздел 9.6 (стр. 231), Раздел 9.7 (стр. 235)
Цитата: "Using LLMs to evaluate prompts and profiles provides a strong baseline for comparing the performance of a profile." (стр. 231)
7. Безопасность (подтверждение пользователя и изоляция)
Что сделать: Изолировать среду выполнения кода агентов через контейнеры Docker (Dev Containers) и запрашивать явное подтверждение человека перед опасными операциями в ОС
Зачем: Защищает файловую систему и ОС от выхода агента из-под контроля («rogue agent»), удаления важных файлов или бесконечных циклов вызова платных API
Когда: Всегда, когда ИИ-помощнику предоставляется доступ к терминалу, запуск bash-команд или модификация файлов.
Адрес в книге: Глава 1 › Раздел 1.1 (стр. 26), Глава 4 › Раздел 4.1 (стр. 72), Глава 11 › Раздел 11.1 (стр. 275)
Цитата: "Executing AutoGen and AutoGen Studio using Docker is recommended, especially when working with code that may affect the operating system." (стр. 72)
8. Контекст (экономия токенов и лимиты)
Что сделать: Явно ограничивать длину вывода (например, 3 маркированных пункта или до 50 слов), разбивать документы на небольшие токены с перекрытием (chunking) и контролировать размер истории диалога
Зачем: Уменьшает финансовые затраты, ускоряет генерацию ответов и предотвращает ухудшение качества логики из-за избыточного «мусорного» текста
Когда: При частых повторных вызовах, передаче истории чата и загрузке фрагментов кода.
Адрес в книге: Глава 2 › Раздел 2.1 (стр. 44), Раздел 2.3 (стр. 57), Глава 8 › Раздел 8.4 (стр. 195)
Цитата: "Having fewer tokens typically means LLM interactions will be cheaper, respond faster, and produce better and more consistent results." (стр. 44)
[предложение NotebookLM, не из книги] 💡 Хотите, чтобы я помог составить готовый шаблон конфигурационного файла CLAUDE.md с правилами и ограничениями на основе этих принципов?

## Q4. Как проверяют, что агент сделал работу правильно

В книге проверяемость и контроль правильности работы ИИ-агентов рассматриваются как ключевой элемент перехода от простых чат-ботов к надежным автономным системам
. Для этого используются пять основных пошаговых методов:
1. Запуск кода и автоматические тесты (Unit Testing & Code Execution)
Как проверяется: Для кодирующих агентов проверка выполняется не на слух, а физическим запуском написанного кода в изолированной среде (например, Docker) и выполнением проверочных тестов (assertions)
. Прокси-агент (UserProxyAgent) либо специальный агент-тестировщик (Tester / Reviewer) запускает скрипт и проверяет, возвращает ли он ошибки
Адрес в книге: Глава 1 › Раздел 1.1 (стр. 28)
, Глава 4 › Раздел 4.1 (стр. 72)
Цитата: "Two agents—a coder and a tester—work in the background to create code and write unit tests to test the code." (стр. 28)
Цитата: "In many cases, proving the code runs and produces the required output is sufficient for the user proxy agent to approve the task's completion." (стр. 72)
2. Оценка качества с помощью модели-судьи (LLM-as-a-Judge & Rubrics)
Как проверяется: Когда результат агента невозможно проверить тестом кода (например, текстовый ответ, рекомендация или рецепт), подключается вторая модель-оценщик (судья)
. Ей передается рубрика (набор формальных критериев с описаниями и шкалой оценок от 1 до 5)
. Модель-судья автоматически анализирует результат первого агента и выставляет баллы по каждому критерию
Адрес в книге: Глава 9 › Раздел 9.5 & 9.6 (стр. 228, 230–231)
Цитата: "Using LLMs to evaluate prompts and profiles provides a strong baseline for comparing the performance of a profile." (стр. 231)
3. Числовые метрики и сходство векторных эмбеддингов (Metrics & Cosine Similarity)
Как проверяется: В пайплайнах тестирования (например, в Microsoft Prompt Flow) сгенерированный агентом ответ (predicted) и эталонный правильный ответ (expected) преобразуются в векторные эмбеддинги
. Затем специальный скрипт рассчитывает косинусное сходство (cosine similarity) между векторами и выводит точный числовой балл совпадения (от 0 до 1)
Адрес в книге: Глава 9 › Раздел 9.7 (стр. 238–240)
, Глава 10 › Раздел 10.1 (стр. 247)
Цитата: "Python: Evaluation (Python code to measure embedding similarity) Inputs: Embedding_predicted output Embedding_expected output Outputs: the similarity score between predicted and expected" (стр. 247)
4. Трассировка и наблюдаемость процессов (Tracing & Observability)
Как проверяется: В многоагентных системах (например, CrewAI или AutoGen) правильность работы отслеживается через платформы наблюдаемости (например, AgentOps) или логи вызова инструментов
. Это позволяет визуально и по метрикам проверять:
Не попал ли агент в замкнутый цикл одинаковых мыслей (метрика Repeat Thoughts)
Сколько токенов и денег было потрачено на каждый шаг
Какие конкретно вызовы функций (Tools/APIs) совершил агент
Адрес в книге: Глава 4 › Раздел 4.4 & 4.5 (стр. 87, 89, 94)
, Глава 6 › Раздел 6.2 (стр. 142)
Цитата: "Observability through application tracing is a key element of any complex system, especially one engaged in enterprise use." (стр. 87)
5. Пошаговая оценка и отсечение неверных веток (Tree of Thought Evaluation)
Как проверяется: При решении сложных задач методом «Дерева мыслей» (Tree of Thought) промежуточные шаги рассуждения агента оцениваются семантической функцией-оценщиком прямо в процессе генерации
. Если промежуточный шаг получает низкую оценку (например, eval <= 25), эта ветка решений мгновенно отсекается, и агент не тратит ресурсы на заведомо неверный путь
Адрес в книге: Глава 10 › Раздел 10.3 (стр. 268–269)
Цитата: "By evaluating before each step, ToT short-circuits the execution of plans it deems as not being valid." (стр. 269)
🔍 Хотите разбрать подробнее, как именно написать Python-код для автоматической оценки ответов агента через Prompt Flow или настроить AgentOps для отслеживания зацикливаний?

## Q5. Типичные ошибки и ловушки

В книге Майкла Лэнхэма подробнейшим образом разбираются архитектурные ловушки, в которые часто попадают разработчики при переходе от обычных промптов к автономным ИИ-агентам
. Ниже представлены ключевые ошибки, описанные автором, причины их возникновения и способы предотвращения:
1. Зацикливание и бесконечные повторения мыслей (Repetitive Thought Patterns)
В чем ловушка: При решении сложных или неоднозначных задач агент может застрять в бесконечном цикле генерации одинаковых мыслей и итераций, пытаясь переформулировать один и тот же ответ из-за нерешительности
Как избегать: Изменить тип обработки (например, с иерархического на последовательный), пересмотреть роли, сузить формулировку цели, предоставить более явные инструменты или ограничить максимальное количество раундов итераций (max_round / max_turns)
Адрес в книге: Глава 4 › Раздел 4.5, стр. 94
Цитата: "Overly repetitive thought patterns typically mean the agent isn’t being decisive enough and instead keeps trying to generate a different answer."
2. Выход автономных агентов из-под контроля («Rogue Agents»)
В чем ловушка: Придание агентам полной самостоятельности в сочетании с доступом к системным действиям может привести к непреднамеренному удалению файлов, сбоям или повреждению операционной системы
Как избегать: Запускать агентов только в изолированных контейнерах (Docker / WSL), запрашивать явное подтверждение человека (human_input_mode) перед выполнением опасных операций и ограничивать доступный набор функций
Адрес в книге: Глава 11 › Раздел 11.1, стр. 275
Цитата: "WARNING While writing this book... I have encountered several instances of agents going rogue with actions... deleting files they shouldn’t have."
3. «Испорченный телефон» во вложенных диалогах (The Telephone Game)
В чем ловушка: При последовательной передаче данных через цепочку вложенных чатов (nested chats) контекст первоначальной задачи постепенно искажается, превращаясь в совершенно другой результат
Как избегать: Использовать совместные групповые чаты (GroupChat) с агентом-модератором (GroupChatManager) или передавать информацию между агентами в виде структурированных файлов, а не через диалоговый контекст
Адрес в книге: Глава 4 › Раздел 4.3, стр. 82
Цитата: "With agents, this is certainly no different, and chatting through nested or sequential conversations can alter the task or even the desired result."
4. Попытка писать код вместо использования готовых инструментов (Coding vs. Actions)
В чем ловушка: Опора на то, что агент будет каждый раз на лету писать Python-код для выполнения задач, приводит к частым сбоям из-за использования устаревших библиотек и необходимости постоянно править написанный код
Как избегать: Предоставлять агентам готовые, отлаженные навыки и действия (Actions / Skills / Tools) для обращения к внешним системам вместо генерации нового кода с нуля
Адрес в книге: Глава 4 › Раздел 4.1, стр. 72
Цитата: "This highlights a bigger problem with agentic systems using packages or libraries that have expired... it’s generally better to get agents to execute actions"
5. Перегрузка агента избыточным набором инструментов (Overwhelming Actions)
В чем ловушка: Подключение слишком большого количества функций сбивает агента с толку: он путается в выборе нужного инструмента, совершает ошибки или начинает использовать действия незапланированным образом
Как избегать: Предоставлять агенту только минимально необходимый набор инструментов (Actions), строго соответствующий его узкой роли и текущей цели
Адрес в книге: Глава 11 › Раздел 11.1, стр. 275
Цитата: "More actions can confuse an agent into deciding which to use or even how to solve a goal."
6. Стремительный рост расходов и блокировка аккаунта (Resource Exhaustion)
В чем ловушка: Интенсивные многоагентные диалоги и частые вызовы внешних инструментов (генерация изображений, анализ видео) могут моментально исчерпать лимиты токенов или привести к временной блокировке аккаунта
Как избегать: Внедрять правила экономии ресурсов прямо в системные промпты (RULE), отслеживать трассировку вызовов и стоимость сессий через AgentOps и задавать ограничения на длину вывода
Адрес в книге: Глава 3 › Раздел 3.5.1, стр. 62
Цитата: "Making your assistant aware of resource usage can be as simple as adding the rule shown in listing 3.18 to the assistant’s instructions."
7. Обход петли обратной связи в внешних планировщиках (Bypassing Feedback Loop)
В чем ловушка: Использование жестких внешних планировщиков исключает этап промежуточной критики, из-за чего ошибка на первом шаге сводит на нет выполнение всей цепочки
Как избегать: Сочетать планирование с петлями обратной связи (Feedback Loops), запрашивая у модели регулярный самоаудит или привлекая агента-критика перед выдачей итогового ответа
Адрес в книге: Глава 11 › Раздел 11.3, стр. 285
Цитата: "The problem with external or prompt planning is that it bypasses the feedback iteration loop, which can help correct problems quickly."
[предложение NotebookLM, не из книги] 💡 Хотите разбрать подробнее, как защитить вашего агента от зацикливания или написать шаблон инструкции с жестким ограничением ресурсов?

## Q6. Инструменты, фреймворки, версии, цены; что устарело или спорно

В книге называются ключевые инструменты, фреймворки, модели, версии и ценовые условия, а также указываются их ограничения, устаревшие элементы и спорные моменты
:
1. ChatGPT Plus и GPT Store (OpenAI)
Инструменты и цены: Подписка ChatGPT Plus ($20 в месяц на момент написания книги) требуется для создания, использования и публикации кастомных ассистентов в GPT Store
Что спорно / меняется по книге: Модель монетизации и ценообразование GPT Store на момент написания книги не устоялись и в будущем могут измениться
Адрес: Глава 3 › Раздел 3.1 (стр. 64) / Глава 3 › Раздел 3.5.2 (стр. 87)
Цитата: "First, we’ll look at building GPT assistants through ChatGPT Plus, which requires a premium subscription." (стр. 64)
2. ChatGPT Plugins (Плагины ChatGPT)
Инструменты и функции: Ранний механизм расширения функционала ChatGPT внешними инструментами
Что устарело по книге: Плагины стали устаревающим подходом и вытесняются пользовательскими действиями (Custom Actions), вызовами функций (Function Calling) и GPT Assistants
Адрес: Глава 5 › Раздел 5.1 (стр. 123)
Цитата: "ChatGPT plugins were first introduced to provide a session with abilities, skills, or tools." (стр. 123)
3. Сторонние библиотеки Python в коде агентов (Expired Libraries)
Инструменты и версии: Пакеты Python, которые генеративные агенты пытаются устанавливать и использовать для решения задач на лету
Что устарело / проблемно по книге: Агенты часто используют устаревшие или вышедшие из обращения библиотеки Python, которые больше не работают, поэтому надежнее предоставлять агентам готовые нативные действия (Actions), а код исполнять в Docker
Адрес: Глава 4 › Раздел 4.1 (стр. 96)
Цитата: "with agentic systems using packages or libraries that have expired and no longer work." (стр. 96)
4. LM Studio
Инструменты и версии: Бесплатное приложение для локального запуска и хостинга open-source языковых моделей (Llama, Mistral и др.)
Что спорно / бета-статус по книге: Некоторые версии приложения находятся в бета-статусе и требуют ручной установки дополнительных системных утилит и библиотек в зависимости от ОС и железа
Адрес: Глава 2 › Раздел 2.2 (стр. 44)
Цитата: "some versions of LM Studio may be in beta and require installation of additional tools or libraries." (стр. 44)
5. AgentOps (Платформа наблюдаемости)
Инструменты и цены: Специализированная платформа наблюдаемости, трассировки и аудита вызовов для мультиагентных систем (CrewAI, AutoGen)
Что спорно / неопределено по книге: На момент написания книги у платформы отсутствовала четко определенная коммерческая модель или ценообразование
Адрес: Глава 4 › Раздел 4.4 (стр. 112)
Цитата: "Currently, no pricing or commercialization details are available." (стр. 112)
6. Microsoft Semantic Kernel (SK)
Инструменты и версии: Фреймворк Microsoft для разработки ИИ-приложений и агентов на Python, C# и Java
Что спорно / путаница в книге: Разработчики фреймворка переименовали концепт skills в plugins для соответствия стандартам OpenAI, однако в самом исходном коде библиотеки продолжал использоваться термин skills, что создает путаницу
Адрес: Глава 5 › Раздел 5.3 (стр. 132)
Цитата: "What is more confusing is that the code still uses the term skills." (стр. 132)
7. OpenAI Strawberry (o1-preview)
Инструменты и версии: Новое семейство моделей OpenAI со встроенным пошаговым рассуждением, планированием и самопроверкой
Что спорно / ограничено по книге: Встроенный механизм рассуждений обходит привычные внешние планировщики, а из-за вероятностного характера модель всё равно может допускать ошибки в сложных логических задачах, если ей не передать явную обратную связь
Адрес: Глава 11 › Раздел 11.4 (стр. 309, 322)
Цитата: "Models such as OpenAI Strawberry integrate reasoning, planning, evaluation, and feedback directly into the LLM" (стр. 322)
8. CrewAI (Затраты на токены в мультиагентных системах)
Инструменты и цены: Фреймворк для сборки автономных «экипажей» агентов с явным разделением ролей
Что проблемно по книге: Избыточные диалоги и согласования между агентами приводят к стремительному расходу токенов — в примере из книги генерация одной шутки обошлась более чем в $0.50
Адрес: Глава 4 › Раздел 4.4 (стр. 113)
Цитата: "Did you notice in figure 4.11 that creating a single joke costs a little over 50 cents?" (стр. 113)
[предложение NotebookLM, не из книги] 💡 Если вас интересует подробный разбор работы с конкретным фреймворком (например, настройка локального сервера в LM Studio или трассировка вызовов в AgentOps), я с радостью подготовлю пошаговое руководство.

## Q7. 20 карточек и 5 заданий

20 карточек «Вопрос — Ответ» по ключевым идеям книги
1. Понятие и сущность ИИ-агента
Вопрос: Что такое ИИ-агент и чем он отличается от традиционного чат-бота?
Ответ: ИИ-агент — это цифровой сущность-помощник, обладающая автономностью и способностью выполнять практические задачи от имени пользователя
. В отличие от обычного чат-бота, агент сочетает языковую модель с инструментами, памятью, способностью рассуждать и планировать шаги
Адрес: Глава 1 › Раздел 1.1, стр. 25–26
2. Режимы взаимодействия с LLM
Вопрос: Какие 4 уровня взаимодействия пользователя с языковыми моделями выделяются в архитектуре агентов?
Ответ: Выделяются: прямое общение (обычный чат)
, прокси-агент (ИИ переформулирует промпт для других моделей, например DALL-E 3)
, агент с функциями (запрашивает подтверждение человека перед вызовом API)
 и автономный агент (самостоятельно планирует и принимает решения)
Адрес: Глава 1 › Раздел 1.1, стр. 26
3. Архитектура одиночного агента
Вопрос: Из каких 5 базовых компонентов состоит архитектура любого одиночного ИИ-агента?
Ответ: Архитектура включает: профиль и персону (системный промпт и роль)
, действия и инструменты (вызовы функций и API)
, память и знания (RAG и история диалогов)
, рассуждения и оценку (CoT, ToT)
, планирование и обратную связь
Адрес: Глава 1 › Раздел 1.2, стр. 28–29
4. Генеративные модели против предиктивных
Вопрос: В чем главное отличие генеративных моделей (GPT) от классических предиктивных моделей?
Ответ: Генеративные модели обучены создавать совершенно новый контент (текст, код, изображения) на основе входного контекста, тогда как предиктивные модели предназначены только для классификации или предсказания категорий данных
Адрес: Глава 2 › Раздел 2.1, стр. 38
5. Роли сообщений в API
Вопрос: Какую роль выполняет системное сообщение (system) при отправке запросов через API?
Ответ: Системное сообщение определяет верхнеуровневый контекст, правила поведения, персонажа и ограничения, которые направляют генерацию всех последующих ответов модели
Адрес: Глава 2 › Раздел 2.1, стр. 42
6. Локальный запуск открытых моделей
Вопрос: Какую роль играет инструмент LM Studio в локальной разработке агентов?
Ответ: LM Studio позволяет бесплатно загружать, запускать и тестировать открытые нейросети (Open Source LLM) непосредственно на собственном компьютере, эмулируя локальный сервер с интерфейсом API OpenAI
Адрес: Глава 2 › Раздел 2.2, стр. 44
7. Задание персоны (Adopting Personas)
Вопрос: Зачем в промпт-инжиниринге применяется тактика задания персоны?
Ответ: Задание персоны с конкретным фоновым опытом и демографией задает базовый рамки контекста, кардинально меняя стиль, глубину и профессиональную специфику ответов нейросети
Адрес: Глава 2 › Раздел 2.3, стр. 53
8. Правила в кастомных GPT (RULES)
Вопрос: Какую функцию выполняют явные правила (RULES) в инструкциях для GPT-ассистентов?
Ответ: Правила служат жестким шаблоном вывода, гарантируя, что ассистент будет стабильно выполнять обязательные шаги (например, рассчитывать калории, генерировать изображения или форматировать цены)
Адрес: Глава 3 › Раздел 3.1, стр. 67
9. Анализ данных через Code Interpreter
Вопрос: Как ассистент использует инструмент Code Interpreter при обработке таблиц CSV?
Ответ: Ассистент выступает в роли дата-сайентиста: он генерирует и выполняет код на Python (pandas, matplotlib), самостоятельно проводит очистку данных, строит графики и рассчитывает статистику
Адрес: Глава 3 › Раздел 3.2, стр. 68
10. Преимущество многоагентных систем
Вопрос: В чем заключается ключевое преимущество командной работы нескольких агентов?
Ответ: Многоагентные системы позволяют агентам обмениваться мнениями на естественном языке, проводить перекрестную проверку и критику решений, что существенно снижает количество ошибок при решении сложных задач
Адрес: Глава 4 › Раздел 4.1, стр. 69
11. Роль UserProxyAgent в AutoGen
Вопрос: Какова главная функция прокси-агента пользователя (UserProxyAgent) во фреймворке AutoGen?
Ответ: UserProxyAgent перехватывает команды человека, направляет задачи ассистентам, автоматически исполняет сгенерированный код в рабочей директории или Docker и передает обратную связь о результатах выполнения
Адрес: Глава 4 › Раздел 4.1, стр. 70
12. Определение агента в CrewAI
Вопрос: Какие три ключевых параметра обязательно задаются для каждого агента в CrewAI?
Ответ: Обязательно задаются: роль (role), цель (goal) и предыстория/легенда (backstory), определяющая уникальный характер и область ответственности
Адрес: Глава 4 › Раздел 4.4, стр. 85
13. Вызов функций (Function Calling)
Вопрос: Что происходит при использовании Function Calling в API OpenAI?
Ответ: Модель анализирует запрос пользователя, определяет подходящую функцию из списка tools и извлекает аргументы в формате JSON, оставляя сам физический запуск функции на стороне вашего кода
Адрес: Глава 5 › Раздел 5.2, стр. 101
14. Назначение Semantic Kernel
Вопрос: Какую роль выполняет фреймворк Microsoft Semantic Kernel (SK) в построении агентов?
Ответ: SK работает как оркестратор плагинов, позволяя связывать нативные функции на Python/C# и семантические функции (промпты-шаблоны) в единый сервис
Адрес: Глава 5 › Раздел 5.3, стр. 107
15. Структура деревьев поведения (ABT)
Вопрос: Из каких базовых узлов управляются агентные деревья поведения?
Ответ: Деревья строятся из селекторов (выбор успешной ветки)
, последовательностей (пошаговое выполнение)
, условий (проверка состояния)
 и действий (выполнение задач)
Адрес: Глава 6 › Раздел 6.1, стр. 130–131
16. Суть технологии RAG
Вопрос: Как работает дополненная генерация с поиском (Retrieval-Augmented Generation)?
Ответ: Документы разбиваются на фрагменты и кодируются в векторы
. При запросе система находит наиболее похожие куски текста в векторной базе и подмешивает их в промпт для устранения галлюцинаций
Адрес: Глава 8 › Раздел 8.2, стр. 182
17. Принцип работы векторных эмбеддингов
Вопрос: Каким образом текстовые эмбеддинги обеспечивают смысловой поиск?
Ответ: Нейросеть превращает текст в многомерный вектор (например, 1536 измерений), что позволяет вычислять косинусное сходство между понятиями по их глубокому смыслу, а не по точным ключевым словам
Адрес: Глава 8 › Раздел 8.3, стр. 189–190
18. Назначение Microsoft Prompt Flow
Вопрос: Зачем используется инструмент Prompt Flow при разработке агентов?
Ответ: Для автоматизированного систематического тестирования
, оценки вариантов промптов на пакетах данных (batch processing)
 и сравнения их качества с помощью моделей-оценщиков
Адрес: Глава 9 › Раздел 9.1, стр. 212–213
19. Метод «Цепочка мыслей» (Chain of Thought)
Вопрос: В чем заключается техника CoT (Chain of Thought) в промпт-инжиниринге?
Ответ: Модели показывают примеры пошаговых логических рассуждений или добавляют ключевую фразу «Let's think step by step», что побуждает ИИ подробно расписывать ход мыслей перед выдачей ответа
Адрес: Глава 10 › Раздел 10.2, стр. 253
20. Последовательное планирование
Вопрос: В чем разница между параллельным вызовом инструментов и последовательным планированием?
Ответ: При параллельном вызове инструменты срабатывают одновременно и независимо
, а последовательное планирование строит цепочку задач, где результат предыдущего действия передается на вход следующему
Адрес: Глава 11 › Раздел 11.2, стр. 277–278
5 практических заданий для новичка
Задание 1: Создание диалогового ассистента с правилами и персоной
Цель: Освоить базовые техники промпт-инжиниринга, правила (RULES) и создание персоны
Инструкция:
Перейдите в интерфейс ChatGPT (или создайте системный промпт через API)
Задайте персону эксперта (например: "Ты — опытный инженер по автоматизации с 10-летним стажем")
Добавьте блок RULES: с жесткими правилами (например: обязательно форматировать ответ в 3 пункта, писать код с комментариями и указывать сложность алгоритма)
Протестируйте работу ассистента на 3 различных запросах и убедитесь в соблюдении формата
Адрес в книге: Глава 2 › Раздел 2.3 (стр. 53–57)
, Глава 3 › Раздел 3.1 (стр. 66–67)
Задание 2: Локальный запуск Open Source модели в LM Studio
Цель: Научиться заходить на открытые языковые модели локально без использования платных облачных API
Инструкция:
Скачайте и установите программу LM Studio с официального сайта
Найдите и загрузите небольшую открытую модель (например, Llama-3 или Mistral в формате GGUF)
Запустите локальный сервер взаимодействия на порту 1234
Напишите базовый скрипт на Python с помощью библиотеки openai, изменив base_url="http://localhost:1234/v1", и отправьте тестовый запрос
Адрес в книге: Глава 2 › Раздел 2.2 (стр. 44–48)
Задание 3: Построение мультиагентного ревью кода в AutoGen
Цель: На практике увидеть преимущество взаимодействия двух агентов с перекрестной проверкой
Инструкция:
Установите пакет pyautogen (pip install pyautogen)
Создайте двух агентов: Engineer (программист) и Reviewer (критик кода) с соответствующими системными промптами
Настройте агент UserProxyAgent и запустите между ними диалог по созданию простой игры на Python
Проследите в консоли, как критик указывает на ошибки, а инженер автоматически их исправляет
Адрес в книге: Глава 4 › Раздел 4.2 (стр. 77–81)
Задание 4: Создание мини-системы RAG и смыслового поиска
Цель: Понять принцип загрузки, векторного эмбеддинга и поиска по текстовым документам
Инструкция:
Подготовьте небольшой текстовый файл с фактами (например, описанием проекта или инструкцией)
С помощью библиотеки chromadb или langchain загрузите документ и разбейте его на небольшие фрагменты (chunks)
Сгенерируйте векторные эмбеддинги и сохраните их в локальную коллекцию Chroma DB
Выполните смысловой запрос (например: "Каковы основные условия гарантии?") и выведите топ-3 наиболее релевантные выдержки с их оценками расстояния
Адрес в книге: Глава 8 › Раздел 8.3 & 8.4 (стр. 190–195)
Задание 5: Сравнение точности решений с помощью метода Zero-Shot CoT
Цель: Оценить влияние фраз рассуждения на качество решения логических задач
Инструкция:
Выберите сложную текстовую или логическую задачу (например, задачу на путешествия во времени или расчет графика)
Отправьте модели прямой вопрос без дополнительных указаний и зафиксируйте ответ
Создайте второй запрос с той же задачей, но добавьте в конце системной инструкции управляющую фразу: «Let's think step by step» («Давай порассуждаем по шагам»)
Сравните полученные цепочки рассуждений и убедитесь, как пошаговая генерация помогает модели избежать логических ошибок
Адрес в книге: Глава 10 › Раздел 10.2 (стр. 257–258)

## Q8. Что не спросила; противоречия

1. Важные темы в книге, о которых вы ещё не спросили
Ниже представлены 5 крупных и ценных тем из книги, которые подробно разбирает автор, но которые не затрагивались в прошлых вопросах:
1. Деревья поведения агентов (Agentic Behavior Trees / ABTs) и обратная цепочка (Back Chaining)
О чем тема: Применение архитектуры деревьев поведения из gamedev и робототехники для управления логикой автономных ИИ-агентов. Деревья состоят из узлов Sequence, Selector, Condition и Action. Техника Back Chaining позволяет выстраивать дерево поведения «от противоположного» — от финальной цели к первоначальным действиям.
Адрес в книге: Глава 6 › Раздел 6.1 (стр. 130) и Раздел 6.5 (стр. 155)
Цитата: "Agentic behavior trees (ABTs) implement behavior trees on assistant and agent systems."
2. Архитектура графов Prompt Flow (DAG) и шаблонизация Jinja2
О чем тема: Проектирование автоматизированных пайплайнов для тестирования промптов в виде направленных ациклических графов (DAG)
. Использование шаблонизатора Jinja2 для гибкой подстановки системных ролей, контекста и переменных в промпты агентов
Адрес в книге: Глава 9 › Раздел 9.3 (стр. 217, 222)
Цитата: "Prompt flow can allow us to construct the prompts and code comprising the agent profile but also include the ability to evaluate its effectiveness."
3. Сжатие и кластеризация памяти и знаний (Memory and Knowledge Compression)
О чем тема: Методы предотвращения переполнения контекста при многократных диалогах. Автор описывает периодическую компрессию накопившихся воспоминаний: сначала они кластеризуются алгоритмом k-means, а затем каждый кластер суммаризируется моделью уровня GPT-4
Адрес в книге: Глава 8 › Раздел 8.7 (стр. 207–208)
Цитата: "Memories or knowledge are first clustered using an algorithm such as k-means. Then, the groups of memories are passed through a compression function"
4. Математика RAG: TF-IDF, косинусное сходство и снижение размерности PCA
О чем тема: Математическое устройство векторного поиска. Различие между базовым показателем TF-IDF
 и 1536-мерными семантическими эмбеддингами OpenAI
. Метод PCA (Principal Component Analysis) применяется для сжатия 1536 измерений вектора до 3D-графика с целью визуализации семантических кластеров
Адрес в книге: Глава 8 › Раздел 8.3 (стр. 184, 189–190)
Цитата: "When a document is embedded using an OpenAI model, it transforms the text into a vector with dimensions of 1536."
5. Экономика, SEO и монетизация GPT-ассистентов в GPT Store
О чем тема: Практическая сторона публикации кастомных GPT: защита пользователей от временных блокировок аккаунта из-за перерасхода ресурсов (генерация изображений/Code Interpreter)
, SEO-оптимизация описания ассистента для индексации в Google
 и потенциальные модели распределения прибыли (profit-sharing)
Адрес в книге: Глава 3 › Раздел 3.5 (стр. 61–64)
Цитата: "Upon the release of GPT Assistants and the GPT Store, OpenAI announced the potential for a future profit-sharing program for those who published GPTs."
2. Что в книге противоречит друг другу?
«в книге этого нет»
Прямых внутренних самопротиворечий в текстах и утверждениях автора в книге нет. Автор последовательно излагает материал от базовых концепций к сложным системам.
Однако сам автор явно указывает на внешнюю путаницу в терминологии между разработчиками и фреймворками:
Терминологический сдвиг в Semantic Kernel: Microsoft переименовала понятие skills в plugins, однако в исходном коде фреймворка сохранились упоминания skills, из-за чего автор использует их как синонимы
Адрес: Глава 5 › Раздел 5.3 (стр. 108)
Цитата: "What is more confusing is that the code still uses the term skills."
Различие между "Agent" и "Assistant": OpenAI избегает слова agent, предпочитая термин assistant, так как в традиционном машинном обучении агент всегда подразумевает полную автономность
Адрес: Глава 1 › Раздел 1.1 (стр. 2)
Цитата: "OpenAI avoids the word agent because of the history of machine learning, where an agent is self-deciding and autonomous."
