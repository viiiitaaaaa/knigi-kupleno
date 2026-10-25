<!-- gpt-oss:120b (Hermes), глубокое чтение, build_ai_agent_10.txt -->
**Часть 8 — Кодовое исполнение и расширенные возможности агентов**  

---

## 8.2.2 Введение в E2B (стр. 244–245)  
- **Главная мысль** – Для безопасного и воспроизводимого выполнения кода LLM используется облачный sandbox E2B, который хранит состояние между вызовами.  
- **Как делать**  
  1. Зарегистрироваться на https://e2b.dev/sign-up и получить API‑ключ.  
  2. Добавить ключ в `.env` (`E2B_API_KEY=your_api_key_here`).  
  3. Установить пакет: `uv add e2b-code-interpreter`.  
  4. Создать sandbox: `sandbox = Sandbox.create()`.  
  5. Выполнить код: `execution = sandbox.run_code(code)`.  
  6. Ознакомиться с результатами через `execution.logs.stdout`, `execution.results`, `execution.error`.  
  7. Завершить sandbox: `sandbox.kill()`.  
- **Правила и числа**  
  * `timeout` указывается в секундах (по умолчанию 30 сек, задаётся при `Sandbox.create(timeout=…)`).  
  * Переменные среды передаются словарём `envs={…}`.  
- **Шаблоны и примеры**  
  ```python
  sandbox = Sandbox.create(
      timeout=300,
      envs={'TAVILY_API_KEY': os.getenv('TAVILY_API_KEY'), 'MY_CONFIG': 'some_value'}
  )
  sandbox.set_timeout(600)          # расширить до 10 минут
  ```  
- **Ошибки и предупреждения**  
  * Если `execution.error` не None – код завершился с ошибкой, но sandbox остаётся доступным.  
- **Где пригодится** – При построении запросов к LLM, где нужен «постепенный вывод» (передача результатов кода в следующий шаг).  

---

## 8.2.3 Подключение sandbox к агенту (стр. 247–248)  
- **Главная мысль** – Интеграция E2B‑sandbox в класс `Agent` через `ExecutionContext`, `code_execution` и управление жизненным‑циклом sandbox.  
- **Как делать**  
  1. Добавить поле `code_env: Optional["Sandbox"] = None` в `ExecutionContext`.  
  2. Расширить конструктор `Agent.__init__` параметром `code_execution: Optional[str] = None`.  
  3. В `_setup_tools` автоматически добавить инструмент `execute_python`, если `code_execution=="e2b"`.  
  4. В `Agent.run` создать sandbox один раз в начале (если `context.code_env is None`).  
  5. В `finally` вызвать `context.code_env.kill()`.  
- **Правила и числа** – При создании sandbox указывать `timeout=300` сек.  
- **Шаблоны и примеры**  
  ```python
  # 1. ExecutionContext
  @dataclass
  class ExecutionContext:
      ...
      code_env: Optional["Sandbox"] = None
  # 2. Agent ctor
  class Agent:
      def __init__(..., code_execution: Optional[str] = None, ...):
          self.code_execution = code_execution
  # 3. Автодобавление инструмента
  if self.code_execution == "e2b":
      from .tools.code_execution import execute_python
      tools.append(execute_python)
  ```  
- **Ошибки и предупреждения** – Если `code_execution` указан, но `ExecutionContext.code_env` остался `None`, `execute_python` бросит `RuntimeError`.  
- **Где пригодится** – При построении LLM‑агентов, которым нужен единый интерфейс для выполнения кода без явного управления sandbox‑ом.  

---

## 8.2.4 Тестирование агента с выполнением кода (стр. 249–250)  
- **Главная мысль** – Проверка работы агента‑кода через задачу вычисления 100‑го числа Фибоначчи, где LLM генерирует код, а sandbox‑окружение вычисляет точный результат.  
- **Как делать**  
  1. Создать `Agent` с `code_execution="e2b"` и `tools=[]`.  
  2. Вызвать `await agent.run("What is the 100th Fibonacci number?", verbose=True)`.  
  3. Агент генерирует функцию `fibonacci`, исполняет её в sandbox, получает число `354224848179261915075`.  
- **Шаблон кода, генерируемый агентом**  
  ```python
  def fibonacci(n):
      if n <= 1: return n
      a, b = 0, 1
      for _ in range(2, n + 1):
          a, b = b, a + b
      return b
  result = fibonacci(100)
  print(result)
  ```  
- **Ошибки и предупреждения** – При генерации кода с ошибками (деление на 0 и т.п.) агент получает информацию из `execution.error` и может скорректировать код (паттерн ReAct).  
- **Где пригодится** – При запросах, требующих точных вычислений, недоступных «чистому» LLM.  

---

## 8.3.1 Необходимость портируемости инструментов (стр. 250–251)  
- **Главная мысль** – Вместо многократных вызовов инструмента (31 раз) лучше сгенерировать код, который сам вызывает инструмент в sandbox, тем самым сократив количество LLM‑вызовов и токенов.  
- **Пример сравнения**  
  * Подход 1: 31 отдельный вызов инструмента → 31 LLM‑итераций, большой объём контекста.  
  * Подход 2: один LLM‑запрос генерирует цикл, который внутри sandbox вызывает инструмент 31 раз → один LLM‑вызов, токены минимум.  
- **Где пригодится** – При обработке больших наборов данных (многократные запросы к API, парсинг страниц и т.п.).  

---

## 8.3.2 Расширение `FunctionTool` для sandbox‑выполнения (стр. 252)  
- **Главная мысль** – Добавить к `FunctionTool` флаг `sandbox_executable`, позволяющий регистрировать чистые функции в удалённом sandbox.  
- **Как делать**  
  1. Добавить параметр `sandbox_executable: bool = False` в конструктор.  
  2. Проверять конфликт с `needs_context` и бросать `ValueError`, если оба true.  
- **Шаблон**  
  ```python
  class FunctionTool(BaseTool):
      def __init__(..., sandbox_executable: bool = False):
          self.sandbox_executable = sandbox_executable
          if sandbox_executable and self.needs_context:
              raise ValueError(...)
  ```  
- **Ошибки и предупреждения** – Присвоение `sandbox_executable=True` инструментам, которые требуют `context`, немедленно выкидывает исключение.  
- **Где пригодится** – При переносе существующих функций‑инструментов в sandbox без изменения их логики.  

---

## 8.3.3 Реализация инструмента‑ревизии Wikipedia (стр. 253)  
- **Главная мысль** – Пример чистой функции `get_wikipedia_revisions`, помеченной `sandbox_executable=True`, которая делает запрос к API Wikipedia и возвращает список ревизий.  
- **Код функции**  
  ```python
  @tool(sandbox_executable=True)
  def get_wikipedia_revisions(title, before_date, limit=10,
                              language="en", output="full") -> list:
      import requests
      api_url = f"https://{language}.wikipedia.org/w/api.php"
      params = {"action":"query","titles":title,"prop":"revisions",
                "rvprop":"ids|timestamp|user|content","rvlimit":limit,
                "rvstart":before_date,"rvdir":"older","format":"json"}
      data = requests.get(api_url, params=params).json()
      ...
  ```  
- **Характеристики sandbox‑инструментов**  
  * Нет `context`.  
  * Импорт внутри функции.  
  * Чётко определённый возвращаемый тип (структурированные данные).  
- **Где пригодится** – При необходимости выполнить API‑вызовы из sandbox без доступа к локальному коду.  

---

## 8.3.4 Обращение с sandbox‑инструментами в `Agent` (стр. 254–255)  
- **Главная мысль** – Хранить отдельный список `_sandbox_tools`, регистрировать их в sandbox при его создании и добавить их подписи в системный промпт.  
- **Как делать**  
  1. В `Agent.__init__` создать `self._sandbox_tools: List[FunctionTool] = []`.  
  2. В `_setup_tools`  
     * Отделить инструменты с `sandbox_executable=True`.  
     * Если такие инструменты есть, а `code_execution` не `"e2b"` → бросить `ValueError`.  
  3. При инициализации sandbox вызвать `_register_sandbox_tools(context.code_env)`, где каждый инструмент передаёт свой исходный код (`tool.get_source_code()`) в sandbox через `run_code`.  
  4. Сгенерировать часть системного промпта, описывающую доступные sandbox‑инструменты (`_get_sandbox_tools_prompt`).  
- **Шаблоны**  
  *Регистрация*:  
  ```python
  combined_source = "\n\n".join(t.get_source_code() for t in self._sandbox_tools)
  result = sandbox.run_code(combined_source)
  if result.error:
      raise RuntimeError(...)
  ```  
  *Промпт*:  
  ```python
  def _get_sandbox_tools_prompt(self):
      tool_definitions = [t.tool_definition for t in self._sandbox_tools]
      tools_json = json.dumps(tool_definitions, indent=2, ensure_ascii=False)
      return "\n\n## Sandbox-Executable Tools\n" \
             "The following functions are pre-registered in the sandbox ...\n" + tools_json
  ```  
- **Ошибки и предупреждения** – При несоответствии `sandbox_executable` и `code_execution` будет `ValueError`. Ошибки регистрации в sandbox поднимают `RuntimeError`.  
- **Где пригодится** – При работе агента с большими потоками данных, где требуется локальная логика (например, обработка Википедии) без многократных LLM‑вызовов.  

---

## 8.3.5 Практический тест (стр. 256)  
- **Главная мысль** – Демонстрируется решение задачи подсчёта упоминаний Twitter/X в англоязычных страницах Wikipedia за каждый день августа, используя `get_wikipedia_revisions` в sandbox‑цикле.  
- **Как делать**  
  1. Создать `Agent` с `tools=[get_wikipedia_revisions]` и `code_execution="e2b"`.  
  2. Запросить задачу через `await agent.run(question, verbose=True)`.  
  3. LLM генерирует код, который внутри sandbox:  
     * цикл `for day in range(1,32)`;  
     * вызов `get_wikipedia_revisions(..., before_date="2023-07-01T00:00:00Z")`;  
     * выделение regex‑паттернов `twitter\.com|x\.com`;  
     * подсчёт и вывод итогового количества.  
- **Где пригодится** – При необходимости выполнить многократные, похожие запросы к API, экономя токены и время.  

---

## 8.4 Рабочее пространство: файловая система и CLI (стр. 257–259)  

### 8.4.1 Концепция рабочего пространства  
- **Главная мысль** – Полноценный workspace объединяет исполнение кода, файловую систему и доступ к командной строке, позволяя агенту работать так же, как человек‑разработчик.  
- **Как делать**  
  * Для поиска файлов в каталоге создавать Python‑код (`glob.glob`, `open`) **или** выполнять прямую CLI‑команду (`grep -r …`).  
  * В E2B sandbox использовать `sandbox.commands.run("…")` для любой терминальной команды.  
  * Для загрузки локальных файлов в sandbox: `sandbox.files.write("/home/user/data.xlsx", file_obj)`.  
- **Шаблоны**  
  ```python
  result = sandbox.commands.run("ls -la")
  print(result.stdout)
  ```  
- **Где пригодится** – При задачах, требующих чтения/записи файлов, установки пакетов, работы с терминальными утилитами.  

### 8.4.2 Реализация инструментов workspace  
- **Главная мысль** – Реализованы два базовых инструмента: `bash_tool` (выполнение CLI) и `upload_file` (перенос файлов).  
- **Как делать**  
  1. `bash_tool(context, command)` → `sandbox.commands.run(command)` → форматировать вывод через `_format_command_result`.  
  2. `upload_file(context, local_path, sandbox_path=None)` → проверка существования локального файла, копирование в sandbox (по умолчанию `/home/user/<filename>`).  
- **Шаблоны**  
  ```python
  # bash_tool
  result = sandbox.commands.run(command)
  # формат
  parts = []
  if result.stdout: parts.append(f"[stdout]\n{result.stdout}")
  if result.stderr: parts.append(f"[stderr]\n{result.stderr}")
  if result.error:  parts.append(f"[error]\n{result.error}")
  parts.append(f"[exit_code] {result.exit_code}")
  return "\n\n".join(parts)
  ```  
  ```python
  # upload_file
  if not os.path.isfile(local_path):
      return f"Error: Path is not a file: {local_path}"
  if sandbox_path is None:
      sandbox_path = f"/home/user/{os.path.basename(local_path)}"
  with open(local_path, "rb") as f:
      sandbox.files.write(sandbox_path, f)
  return f"Successfully uploaded '{local_path}' to '{sandbox_path}'"
  ```  
- **Ошибки и предупреждения** – Отсутствие `context.code_env` → `RuntimeError`. Ошибки доступа к файлам → строковые сообщения.  
- **Где пригодится** – Для загрузки данных (Excel, CSV, изображения) в sandbox и выполнения shell‑команд (установка пакетов, `pip install`, `curl` и т.д.).  

### 8.4.3 Практический пример: анализ Excel‑файла (стр. 260–261)  
- **Главная мысль** – С помощью `bash_tool` и `upload_file` агент может загрузить локальный Excel‑файл, установить `pandas`, выполнить анализ и вернуть результат, всё в изолированном sandbox.  
- **Как делать**  
  1. Создать `Agent` с `code_execution="e2b"` и добавить инструменты `[bash_tool, upload_file]`.  
  2. В запросе указать путь к локальному файлу.  
  3. Агент:  
     * вызывает `upload_file` → файл попадает в `/home/user/…` в sandbox;  
     * через `bash_tool` ставит `pip install pandas`;  
     * через `execute_python` читает Excel, агрегирует продажи, сравнивает города и выводит ответ.  
- **Где пригодится** – При задачах, где требуется работа с данными в специфических форматах (Excel, CSV, JSON), а также установка временных зависимостей без риска для хоста.  

---

## 8.5 Agent Skills (стр. 262–269)  

### 8.5.1 Концепция Agent Skills  
- **Главная мысль** – Вместо включения полных определений всех 100 инструментов в системный промпт, предоставляются лишь имена и однострочные описания (skill‑list), а подробные детали читаются по‑требованию из файлов `SKILL.md`.  
- **Структура** – Каждый навык – отдельная папка с файлом `SKILL.md`, в котором в **YAML‑front‑matter** указаны `name` и `description`. Тело markdown содержит полное руководство и, при необходимости, дополнительные скрипты.  

### 8.5.2 Прогрессивное раскрытие информации (стр. 263)  
- **Уровень 1** – Список навыков (имя + краткое описание) в системном промпте (потрачено ≈ 50 токенов на 100 навыков).  
- **Уровень 2** – При выборе навыка LLM вызывает `bash_tool` `cat <skill>/SKILL.md`, читает полное описание (тысячах токенов).  
- **Уровень 3** – При необходимости дополнительные файлы/скрипты (десятки тысяч токенов) читаются по запросу.  

### 8.5.3 Реализация (стр. 264–267)  
- **Главная мысль** – Описана полная цепочка: `SkillInfo` → парсер YAML → обнаружение навыков → генерация списка в системном промпте → загрузка папок‑навыков в sandbox.  
- **Как делать**  
  1. **`SkillInfo` dataclass** (`name`, `description`, `path`).  
  2. **Парсер `parse_frontmatter(content)`** – ищет блок `--- … ---` и вытаскивает ключ‑значения.  
  3. **`load_skill(skill_dir)`** – читаем `SKILL.md`, создаём `SkillInfo`.  
  4. **`discover_skills(skills_path)`** – рекурсивно собирает все `SkillInfo`.  
  5. **`generate_skills_prompt(skills, sandbox_path)`** – формирует секцию `## Available Skills` со списком и инструкцией `cat …/SKILL.md`.  
  6. В конструкторе `Agent` добавить параметр `skills_path`.  
  7. При инициализации sandbox вызвать `_upload_skills_to_sandbox`, используя `discover_skills` и копируя файлы в sandbox.  
- **Шаблоны**  
  ```python
  # YAML‑front‑matter parser
  pattern = r'^---\s*\n(.*?)\n---'
  # generate prompt
  lines = ["## Available Skills", f"Skills are installed at `{sandbox_path}`.", ""]
  for s in skills:
      lines.append(f"- **{s.name}**: {s.description}")
  ```  
- **Ошибки и предупреждения** – Если `SKILL.md` отсутствует или в нём нет `name/description` → навык игнорируется.  

### 8.5.4 Практический пример: навык pdf‑merge (стр. 268–269)  
- **Главная мысль** – Показан навык, который объединяет несколько PDF‑файлов, используя библиотеку `pypdf`. Описание находится в `skills/pdf-merge/SKILL.md`.  
- **Как работать**  
  1. Указываем `skills_path="./skills"` при создании агента.  
  2. При запросе «Merge report_q1.pdf …» агент:  
     * читает список навыков → видит `pdf-merge`;  
     * через `bash_tool` выполняет `cat /home/user/skills/pdf-merge/SKILL.md`;  
     * изучает пример кода;  
     * через `execute_python` пишет и исполняет код объединения PDF‑файлов;  
     * отправляет пользователю подтверждение о созданном `merged.pdf`.  
- **Где пригодится** – Любые задачи, требующие одноразовых скриптов (конвертация форматов, генерация отчётов), где не хочется писать отдельный инструмент заранее.  

### 8.5.5 Иерархическая структура инструментов (стр. 270–271)  
- **Главная мысль** – Инструменты делятся на три уровня:  
  1. **Core tools** (всегда в промпте): `execute_python`, `bash_tool`, `upload_file`.  
  2. **Installable tools** — `Agent Skills` (имя + описание в промпте, детали в файловой системе).  
  3. **Generated tools** — код, написанный LLM‑ом «на лету» и исполняемый `execute_python`.  
- **Преимущества** – Сокращение токенов, более чистый контекст, возможность добавлять новые навыки без изменения кода агента.  

---

## Сводка (стр. 270–271)  
- **Sandbox** — изолированное окружение: защита хоста, ограничение ресурсов, восстановление состояния.  
- **Кодовое исполнение** добавляет контрольный поток, хранение промежуточных данных и компоновку инструментов.  
- **Портирование инструментов** в sandbox (через `sandbox_executable`‑флаг) повышает эффективность при работе с большими объёмами данных.  
- **Workspace** → полный набор: код, файловая система, CLI.  
- **Agent Skills** — прогрессивное открытие информации о навыках, экономия токенов, упрощение переносимости.  
- **Трёхуровневая иерархия** инструментов позволяет держать в контексте только необходимое, а всё остальное хранить в workspace.  

---  

**Для ИИ‑помощника Claude**:  
- Используйте блоки **«где пригодится»**, чтобы быстро подобрать нужный подход (запрос → код → sandbox → workspace → skill).  
- При формировании системных промптов включайте только **уровень 1** (core tools) и список **skill‑names** (уровень 2); детали запрашивайте через `bash_tool` в процессе решения.  
- При необходимости обработки больших наборов данных переходите к **sandbox‑инструментам** и **workflow‑коду**, минимизируя количество LLM‑вызовов.
