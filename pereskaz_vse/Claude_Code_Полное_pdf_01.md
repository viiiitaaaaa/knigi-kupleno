<!-- gpt-oss:120b (модель Hermes), Claude_Code_Полное_pdf_01.txt -->
## Part I. Introduction and Basics (Введение и основы) (стр. 7)

### Chapter 1. What is Claude Code and why it is needed (Что такое Claude Code и зачем он нужен)

#### 1.1 Brief history of Anthropic and the Claude line (Краткая история Anthropic и линейки Claude) (стр. 8)  
- Anthropic founded in 2021 by former OpenAI researchers, including Dario Amodei (vice‑president of research at OpenAI) and his sister Daniela Amodei (operations) (стр. 8).  
- Company focuses on **Constitutional AI (CAI)** – model trained to follow a set of natural‑language principles (“constitution”) defining permissible behavior (стр. 8).  
- First public model **Claude** released March 2023; later **Claude 2** (July 2023) with longer context (100 k tokens) and improved code, math, document abilities (стр. 8).  
- **Claude 3** released March 2024 in three variants – **Haiku**, **Sonnet**, **Opus** – achieving results comparable to or surpassing GPT‑4 on many benchmarks; Opus leads in deep reasoning, Sonnet balances speed, cost, quality (стр. 8).  
- **Claude 3.5 Sonnet** (summer 2024) set new standards in programming, outperforming more expensive competitors (стр. 8).  
- **Claude Code** – an **agentic CLI tool** that reads files, writes code, runs tests, analyses errors, manages dependencies, and interacts with external services, living inside your terminal with direct project access (стр. 8).

#### 1.2 Claude Code’s place among AI development tools (Место Claude Code среди AI‑инструментов для разработки) (стр. 9)  
Four categories of existing tools:  

| Category | Examples | Limitations |
|----------|----------|--------------|
| **Code autocompleters** | GitHub Copilot, Codeium, TabNine, Amazon CodeWhisperer | Work at line‑level, no project‑wide understanding, cannot execute multi‑step tasks or access filesystem/terminal (стр. 9). |
| **AI‑oriented IDEs** | Cursor (plus Gemini IDE, Void) | Provide multi‑file changes but tied to a specific editor (стр. 9). |
| **Chat‑bots for code** | ChatGPT, Gemini, Perplexity | Operate isolated from your project; you must copy/paste code manually (стр. 9). |
| **Agentic tools** | **Claude Code** | Can **explore codebase, plan multi‑step solutions, modify files, run terminal commands, use Git, run tests, interact via MCP, open browser**; works from CLI on any system with Node.js (стр. 9‑10). |

#### 1.3 Detailed comparison with main competitors (Подробное сравнение с основными конкурентами) (стр. 10‑11)

- **GitHub Copilot** (most popular AI tool, millions of users, integrates with many IDEs) (стр. 10)  
  - *Advantages*: deep GitHub integration, low subscription cost, multi‑file planning via Copilot Workspace (стр. 10).  
  - *Claude Code advantages*: agent mode with filesystem & terminal access, 200 k+ token context vs ~8 k, complex reasoning & planning, editor‑agnostic, MCP for any external service, better architecture & pattern understanding, fully autonomous operation (стр. 10).  

- **Cursor IDE** (closest philosophical competitor) (стр. 10‑11)  
  - *Advantages*: full IDE with visual UI, diff viewer, multiple models (including Claude Sonnet), multi‑file editing, tab‑completion, built‑in chat (стр. 10‑11).  
  - *Claude Code advantages*: terminal‑based (no editor switch), full command execution & result analysis, MCP ecosystem, deeper project context, superior automation & scripting, SSH remote capability, transparent pricing (API calls) (стр. 11).  

- **Amazon CodeWhisperer (Q Developer)** (стр. 11)  
  - *Advantages*: free for individuals, deep AWS integration, built‑in security analysis, many languages (стр. 11).  
  - *Claude Code advantages*: more powerful base model, agent capabilities, provider‑agnostic, MCP for integrations, better code generation quality across most languages (стр. 11).  

- **Google Gemini Code Assist** (стр. 11‑12)  
  - *Advantages*: huge context window (up to 1 M tokens), Cloud integration, free tier, multimodal (images, screenshots) (стр. 11‑12).  
  - *Claude Code advantages*: agent mode with real actions, superior code quality, MCP ecosystem, provider‑agnostic, mature security architecture (стр. 12).  

#### 1.4 Claude Code philosophy: AI as a partner (Философия Claude Code: AI как напарник) (стр. 12‑13)  
- Positioning: **partner**, not replacement; AI executes tasks but humans retain decision‑making (стр. 12).  
- Contrasts two extremes on the market:  
  1. **Smart autocomplete** – minimal risk, minimal workflow change (стр. 13).  
  2. **Full autonomy** – maximal automation, high risk (loss of control, unpredictable decisions) (стр. 13).  
- Claude Code occupies a **middle ground**: autonomous enough to plan & execute complex tasks, yet:  
  - **Requests confirmation** before dangerous operations (file deletion, dependency installation, unknown commands) (стр. 13).  
  - **Explains actions** – each step described (стр. 13).  
  - **Maintains transparency** – shows which tools are invoked and what changes are made (стр. 13).  
  - **Allows iteration** – you can steer direction any time (стр. 13).  
  - **Respects boundaries** – permission system defines what AI can/cannot do (стр. 13).  

- **Human‑In‑The‑Loop (HITL)** concept: human stays in decision loop, delegates routine, focuses on strategy (стр. 13).  
- Practical consequences:  
  - Better with **iterative dialogue** rather than a single huge prompt (стр. 13).  
  - Respects **your coding style** – follows naming, formatting, architecture conventions (стр. 13).  
  - **Recognizes errors** – will re‑evaluate and propose alternatives if something goes wrong (стр. 13).  
  - **Learns from context** – file **CLAUDE.md** at project root provides persistent instructions (style, architecture, business context) (стр. 13).  

#### 1.5 Use‑case scenarios: from learning to production (Сценарии использования: от обучения до продакшена) (стр. 13‑14)  

| Scenario | Description |
|----------|-------------|
| **Rapid prototyping** | Describe idea, Claude Code generates project structure, dependencies, basic functionality, e.g., “Create task‑management web app with Google OAuth, drag‑and‑drop Kanban boards, assign tasks. Use Next.js, Prisma, PostgreSQL.” Claude creates file tree, DB schema, API, frontend, auth, basic tests (стр. 13‑14). |
| **Refactoring & modernization** | Migrate legacy code: JS → TS, class components → hooks, Python 2 → 3, update outdated APIs, reorganize file structure, extract reusable modules. Claude analyses whole project for consistent changes (стр. 14). |
| **Complex debugging** | Analyze stack traces, logs, source; locate race conditions, memory leaks, version conflicts, DevOps config issues, SQL errors within minutes (стр. 14). |
| **Test generation** | Generate unit, integration, E2E tests; add boundary‑case tests; set up CI pipeline (стр. 14). |
| **Documentation** | Generate JSDoc/Docstring/KDoc, README, API docs, developer guides, CHANGELOG from commits, architectural decision records (ADR) (стр. 14). |
| **DevOps & infrastructure** | Write Dockerfile, docker‑compose, Kubernetes manifests, Helm charts, CI/CD pipelines (GitHub Actions, GitLab CI, Jenkins), Terraform configs, web‑server configs (Nginx, Apache, Caddy), monitoring (Prometheus, Grafana) (стр. 14). |
| **Learning & mentorship** | Explain complex concepts, show best practices, walk through design patterns, help understand чужой код, suggest alternatives with pros/cons (стр. 14). |

#### 1.6 Limitations & realistic expectations (Ограничения и реалистичные ожидания) (стр. 15‑16)

- **Context‑window limitation**  
  - 200 k token window may be insufficient for very large projects (thousands of files, hundreds of thousands of lines). Claude uses smart search & selective file reading, but may miss distant dependencies. **Recommendation**: split large tasks into local, file‑limited subtasks; use **CLAUDE.md** for high‑level architecture context (стр. 15).  

- **Hallucinations**  
  - Models can generate plausible but incorrect answers: nonexistent standard‑library functions, wrong API behavior, subtle logical bugs, outright false facts. **Recommendation**: always verify critical code – run tests, code review; treat Claude output as a draft (стр. 15).  

- **Cost**  
  - Pricing based on token usage; large‑context operations are expensive. **Recommendation**: use `/compact` to compress context, avoid loading unnecessary files, plan tasks to minimize iterations (стр. 15).  

- **Knowledge freshness**  
  - Model trained on data up to a cutoff; may lack latest libraries, API changes, security fixes. Claude can read current project docs but cannot browse internet unless MCP‑server is configured. **Recommendation**: supply up‑to‑date documentation in project or via prompt (стр. 15).  

- **Domain specificity**  
  - Performs best with mainstream tech (Python, JS/TS, Go, Java, Rust, C/C++). For niche languages (COBOL, Fortran, Erlang, Haskell) or specialized frameworks, quality may drop. **Recommendation**: provide extra context – code examples, docs, naming conventions (стр. 15).  

#### 1.7 What you will gain from this book (Что вы получите от этой книги) (стр. 16)  
- Master Claude Code from installation to advanced scenarios; use MCP, hooks, automation, teamwork.  
- Learn effective AI prompting (skill development).  
- Build six complete projects (SaaS platform, mobile app, CLI utility, Telegram bot, Data pipeline, microservice system).  
- Understand architectural principles through Claude‑assisted learning.  
- Implement Claude Code in team settings (security, standardization).  
- Acquire strategic view of AI’s impact on software development (future readiness).  

#### 1.8 Chapter structure & symbols (Структура глав и условные обозначения) (стр. 17‑18)  
- **Structure of each chapter**: Introduction, Theory, Practical steps, Tips & warnings, Summary.  
- **Notation**:  
  - **Code blocks** – runnable snippets.  
  - **Comments** – explanations inside code.  
  - **Prompts** – italic, prefixed with “>”.  
  - **Tip** – actionable recommendation.  
  - **Warning** – potential trap or typical mistake.  
  - **Note** – additional deep‑dive info.  

---

## Chapter 2. Installation and Environment Setup (Установка и настройка окружения) (стр. 18)

### 2.1 System requirements (Системные требования) (стр. 19)

**Hardware**  
- RAM: ≥ 4 GB (recommended ≥ 8 GB).  
- Disk: ~ 500 MB for tool + project files.  
- CPU: any modern processor (computations off‑loaded to Anthropic servers).  
- Internet: stable; ≥ 10 Mbps recommended (стр. 19).  

**Software**  
- **Node.js** ≥ 18.0 (LTS preferred).  
- **npm** ≥ 9.0.  
- OS: macOS 12+, Ubuntu 20.04/Debian 11+, Windows 10/11 with WSL2, other Linux with glibc 2.31+.  
- Terminal emulator (iTerm2, Windows Terminal, Alacritty, Kitty, WezTerm).  
- **Git** ≥ 2.30 (стр. 19).  

**Verification commands** (стр. 19):

```bash
node --version
npm --version
git --version
```

**Node version manager (nvm) installation** (стр. 19):

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
nvm install --lts
nvm use --lts
```

**Windows nvm‑windows** (стр. 19):

```bash
winget install CoreyButler.NVMforWindows
nvm install lts
nvm use lts
```

### 2.2 Claude Code installation (Установка Claude Code) (стр. 19‑20)

**Via npm (recommended)** (стр. 19‑20):

```bash
npm install -g @anthropic-ai/claude-code
claude --version
```

**Fixing permission errors on Linux/macOS** (стр. 19‑20):

```bash
sudo npm install -g @anthropic-ai/claude-code
mkdir -p ~/.npm-global
npm config set prefix '~/.npm-global'
echo 'export PATH=~/.npm-global/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
npm install -g @anthropic-ai/claude-code
npx @anthropic-ai/claude-code
```

**Homebrew (macOS)** (стр. 20):

```bash
brew install claude-code
brew tap anthropic-ai/tap
brew install anthropic-ai/tap/claude-code
```

**Windows via WSL2** (стр. 20):

```bash
wsl --install
sudo apt update && sudo apt upgrade -y
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
source ~/.bashrc
nvm install --lts
npm install -g @anthropic-ai/claude-code
```
*Important*: keep project inside WSL filesystem (e.g., `/home/username/projects/`), not on Windows drive (`/mnt/c/...`) (стр. 20).

**Docker image** (стр. 20):

```Dockerfile
FROM node:20-slim
RUN npm install -g @anthropic-ai/claude-code
WORKDIR /app
COPY . .
CMD ["claude", "--print", "Analyze this project"]
```

**Updating** (стр. 20‑21):

```bash
npm update -g @anthropic-ai/claude-code
npm install -g @anthropic-ai/claude-code@latest
```
*Recommend updating at least every two weeks* (стр. 21).

### 2.3 Authentication and API keys (Аутентификация и API‑ключи) (стр. 22)

**Method 1 – Direct login via Anthropic web** (стр. 22):

```bash
claude
# Open the provided link in a browser, sign in, authorize.
```
*Token stored locally for subsequent sessions* (стр. 22).

**Method 2 – API key via environment variable** (стр. 22):

```bash
export ANTHROPIC_API_KEY="sk-ant-…"
echo 'export ANTHROPIC_API_KEY="sk-ant-…"' >> ~/.bashrc
source ~/.bashrc
```
*Secure storage alternatives* (стр. 22):

```bash
echo 'export ANTHROPIC_API_KEY="sk-ant-…"' > .envrc
direnv allow
export ANTHROPIC_API_KEY=$(op read "op://Development/Anthropic API Key/credential")
aws-vault exec dev -- claude
```
*Never commit keys; add `.envrc` to `.gitignore`* (стр. 22).

**Method 3 – AWS Bedrock** (стр. 22‑23):

```bash
export CLAUDE_CODE_USE_BEDROCK=1
export AWS_REGION=us-east-1
export AWS_ACCESS_KEY_ID="AKIA…"
export AWS_SECRET_ACCESS_KEY="…"
```
*Benefits*: unified AWS billing, corporate‑level SLA, compliance (SOC2, HIPAA, FedRAMP) (стр. 22).

**Method 4 – Google Vertex AI** (стр. 22):

```bash
export CLAUDE_CODE_USE_VERTEX=1
export CLOUD_ML_REGION=us-east5
export ANTHROPIC_VERTEX_PROJECT_ID="your-project-id"
```

**Authentication check** (стр. 22):

```bash
claude --print "Hello, world!"
```
*If error occurs, verify key, account balance, API status, network (proxy/VPN) settings* (стр. 22).

### 2.4 Configuration files (Конфигурационные файлы) (стр. 23‑25)

**Hierarchy of configuration (стр. 23)**  

| Priority (high → low) | Source |
|------------------------|--------|
| Command‑line arguments | — |
| Environment variables | — |
| Project config (`.claude/`) | — |
| User config (`~/.claude/`) | — |
| System defaults | — |

#### File **CLAUDE.md** (стр. 23‑24)  
Markdown file at project root (or sub‑dir) providing permanent instructions to Claude Code.

*Example* (стр. 24):

```markdown
## Описание
REST API для приложения управления задачами. Python 3.12, FastAPI, SQLAlchemy, PostgreSQL.

## Архитектура
- `app/` – основной код
- `api/` – маршруты
- `models/` – SQLAlchemy модели
- `schemas/` – Pydantic схемы
- `services/` – бизнес‑логика
- `core/` – конфигурация, безопасность, зависимости
- `tests/` – pytest
- `alembic/` – миграции

## Соглашения по коду
- Используй type hints везде
- async/await для всех эндпоинтов
- snake_case для функций, PascalCase для классов
- Формат строк: f‑strings
- Макс. длина строки: 100 символов
- Ruff для форматирования и линтинга

## Команды
- Запуск: `uvicorn app.main:app --reload`
- Тесты: `pytest -v`
- Линтинг: `ruff check .`
- Миграции: `alembic upgrade head`

## Важно
- Не используй `print()` – всегда `logging`
- Все эндпоинты должны иметь описание и теги для OpenAPI
- Бизнес‑логика НЕ в маршрутах – выноси в `services`
- Пароли хэшировать через `bcrypt`
- JWT‑токены сроком жизни 30 минут
```

Claude follows these instructions as a “README for your AI partner” (стр. 24).

#### Directory **.claude/** (стр. 24‑25)

```
.claude/
+-- settings.json      # Project‑level settings
+-- commands/          # Custom commands
|   +-- review.md      # /project:review
|   +-- deploy.md     # /project:deploy
+-- .cursorrules      # Compatibility with Cursor IDE
```

**`settings.json` example** (стр. 24):

```json
{
  "permissions": {
    "allow": [
      "Read",
      "Write",
      "Bash(npm run *)",
      "Bash(pytest *)",
      "Bash(git *)"
    ],
    "deny": [
      "Bash(rm -rf *)",
      "Bash(sudo *)",
      "Bash(curl * | bash)"
    ]
  },
  "model": "claude-sonnet-4-20250514",
  "maxTurns": 50
}
```

#### User‑level configuration **~/.claude/** (стр. 25)

```
~/.claude/
+-- settings.json      # Global settings
+-- commands/          # Global commands
|   +-- standup.md    # /user:standup
+-- credentials.json   # Auth tokens (do not edit)
+-- projects/         # Cache & project state
```

**Global `settings.json` example** (стр. 25):

```json
{
  "theme": "dark",
  "verbose": false,
  "autoApprove": ["Read"],
  "notifications": true,
  "defaultModel": "claude-sonnet-4-20250514"
}
```

#### Environment variables (стр. 25‑26)

| Variable | Purpose |
|----------|---------|
| `ANTHROPIC_API_KEY` | API key |
| `CLAUDE_CODE_USE_BEDROCK` | Use AWS Bedrock |
| `CLAUDE_CODE_USE_VERTEX` | Use Google Vertex |
| `CLAUDE_MODEL` | Default model |
| `HTTP_PROXY`, `HTTPS_PROXY`, `NO_PROXY` | Proxy configuration |
| `CLAUDE_CODE_MAX_TURNS` | Max dialogue steps |
| `CLAUDE_CODE_DISABLE_TELEMETRY` | Disable telemetry |

### 2.5 Integration with code editors (Интеграция с редакторами кода) (стр. 26‑27)

**Visual Studio Code** (стр. 26‑27)  

```bash
code --install-extension anthropic.claude-code-vscode
```
*Features*: Claude panel, send selected code, diff view, CLAUDE.md syntax highlight, status bar (стр. 26).  

**VS Code settings (example)** (стр. 26):

```json
{
  "files.autoSave": "afterDelay",
  "files.autoSaveDelay": 1000,
  "editor.formatOnSave": true,
  "git.autofetch": true,
  "terminal.integrated.scrollback": 10000
}
```

**JetBrains IDEs** (IntelliJ IDEA, PyCharm, WebStorm) (стр. 26) – install “Claude Code” plugin via Settings → Plugins → Marketplace.

**Vim / Neovim** (стр. 27) – use terminal multiplexers (tmux, screen) or Neovim plugin:

```bash
tmux new-session -d -s dev
tmux split-window -h
tmux send-keys -t dev:0.0 'vim .' Enter
tmux send-keys -t dev:0.1 'claude' Enter
tmux attach -t dev
```

Neovim plugin (`lazy.nvim`) configuration (стр. 27):

```lua
{
  "anthropic/claude-code.nvim",
  config = function()
    require("claude-code").setup({
      auto_open = false,
      split = "vertical",
    })
  end,
}
```

**Emacs** (стр. 27) – package `claude-code.el`:

```elisp
(use-package claude-code
  :ensure t
  :config
  (setq claude-code-auto-approve-reads t))
```
Or run via `M-x shell` / `M-x vterm`.

### 2.6 Workspace setup (Настройка рабочего окружения) (стр. 28‑29)

**Terminal multiplexer (tmux)** (стр. 28):

```bash
brew install tmux          # macOS
sudo apt install tmux      # Linux
set -g mouse on
set -g history-limit 50000
set -g default-terminal "screen-256color"
bind | split-window -h
bind - split-window -v
```

*Typical layout*: left panel – code editor (Vim/Neovim); right‑top – Claude Code; right‑bottom – manual terminal (стр. 28).

**File‑viewing utilities** (стр. 28):

```bash
brew install bat
sudo apt install bat
brew install fd            # or apt install fd-find
brew install ripgrep
brew install fzf
brew install eza          # or cargo install eza
brew install git-delta
```

**Git‑delta configuration** (стр. 28):

```ini
[core]
pager = delta
[interactive]
diffFilter = delta --color-only
[delta]
navigate = true
side-by-side = true
line-numbers = true
```

**Shell enhancements** (стр. 28):

```bash
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
plugins=(
  git docker kubectl node npm python fzf zsh-autosuggestions zsh-syntax-highlighting
)
alias cc='claude'
alias ccp='claude --print'
alias ccr='claude --resume'
alias ccc='claude --continue'
```

### 2.7 First launch and orientation (Первый запуск и ориентация) (стр. 29‑30)

**Launch** (стр. 30):

```bash
cd ~/projects/my-project
claude
```

*Welcome screen* (ASCII art) (стр. 30):

```
+==============================================+
| Welcome to Claude Code!                       |
|                                              |
| Model: claude-sonnet-4-20250514              |
| Context: 200,000 tokens                      |
| Working directory: ~/projects/my-project      |
+==============================================+
Type your request or /help for commands.
>
```

**Slash commands reference** (стр. 30‑31):

| Command | Description |
|---------|-------------|
| `/help` | Show command help |
| `/clear` | Reset dialogue & context |
| `/compact` | Compress context to save tokens |
| `/status` | Session information |
| `/cost` | Current session cost |
| `/model` | Switch model |
| `/permissions` | Manage permissions |
| `/config` | Settings |
| `/bug` | Send bug report |
| `/quit` or `Ctrl+C` | Exit |
| … | (стр. 30) |

**Simple test request** (стр. 30):

```
> Покажи список файлов в текущем каталоге и опиши структуру проекта
```
Claude runs `ls`/`find`, reads key files (`package.json`, `requirements.txt`, `README.md`), returns description (стр. 30).

### 2.8 Common installation problems & solutions (Типичные проблемы при установке и их решение) (стр. 31‑32)

| Problem | Cause | Fix |
|---------|-------|-----|
| `command not found: claude` | Binary not in PATH | `npm list -g @anthropic-ai/claude-code`; `echo $PATH`; `export PATH=$(npm config get prefix)/bin:$PATH` (стр. 31). |
| `EACCES: permission denied` | Global install permissions | Create `~/.npm-global`; set prefix; update `PATH`; reinstall via nvm LTS (стр. 31). |
| `401 Unauthorized` (authentication) | Wrong/expired API key | `echo $ANTHROPIC_API_KEY`; `claude logout`; `claude login` (стр. 31). |
| `rate limit exceeded` | API throttling | Wait, upgrade plan, use `/compact`, split task (стр. 31). |
| Proxy/VPN issues | Missing proxy env vars | Set `HTTP_PROXY`, `HTTPS_PROXY`, `NO_PROXY`, `NODE_EXTRA_CA_CERTS` (стр. 31). |
| Windows/WSL issues | WSL version, DNS | `wsl --list --verbose`; `wsl --set-version Ubuntu 2`; `nslookup api.anthropic.com`; update `/etc/resolv.conf` (стр. 31). |

### 2.9 Cost management (Управление затратами) (стр. 31‑33)

**Pricing model** (стр. 31‑32)  
- **Input tokens** (prompt + context) – lower rate.  
- **Output tokens** (Claude response) – higher rate.  
- **Cached tokens** – discounted when context unchanged.  
- Prices vary by model: **Claude Sonnet** (balanced cost/quality), **Claude Opus** (more expensive, better for complex tasks), **Claude Haiku** (cheapest, simple tasks) (стр. 31).

**Saving strategies** (стр. 32‑33)  

- Run `/compact` regularly – compresses dialogue, keeps essential info (стр. 33).  
- Start with **Sonnet**; switch to **Opus** only for very complex tasks (стр. 32).  
- Be **specific** in prompts to reduce iterations (e.g., “In `auth.py` the `login_user` function returns 500 for invalid email; it should return 422 with detailed error” vs “fix bugs”) (стр. 32).  
- Use **CLAUDE.md** to supply persistent context, lowering repeated explanations (стр. 32).  
- **Split tasks** to keep context small (стр. 32).  
- **Monitor spend** via `/cost` and Anthropic console (стр. 32‑33).  

**Budget estimates** (стр. 33)  

- Average developer: **$10–$50/month**.  
- Heavy usage (full workday): **$100–$200/month**.  
- Teams often use centralized billing via **AWS Bedrock** or **Google Vertex** (стр. 33).

### Chapter 3. First steps with Claude Code (Первые шаги с Claude Code) (стр. 33‑38)

#### 3.1 Launching and CLI interface (Запуск и интерфейс командной строки) (стр. 34‑35)

**Basic workflow** (стр. 34):  

```bash
mkdir -p ~/projects/my-first-project
cd ~/projects/my-first-project
claude
```

*Interface components* (стр. 34‑35):  

- **Prompt line** (`>`) – enter natural‑language requests.  
- **Output area** – Claude’s responses (text, code, visual progress).  
- **Tool indicators** – show which tool (ReadFile, Bash, WriteFile) is being used and its parameters (стр. 35).  
- **Status line** – model, session cost, token usage (стр. 35).  

**Operating modes** (стр. 35‑36):  

| Mode | Command | Use case |
|------|---------|----------|
| Interactive (default) | `claude` | Dialogues, iterative work |
| Print (single request) | `claude --print "Explain file main.py"` | Scripts, automation |
| Continue (resume) | `claude --continue` or `claude --resume` | Pick from previous sessions |
| Pipe mode | `cat error.log \| claude --print "Analyze these error logs"` | Embed in Unix pipelines (e.g., `git diff \| claude --print "Code review"` ) (стр. 36).  

*Pipe‑mode examples* (стр. 36‑37):

```bash
grep -rn "TODO:" src/ | claude --print "Prioritize these tasks"
git log --oneline -20 | claude --print "Write changelog from these commits"
npm audit --json | claude --print "Explain vulnerabilities and suggest fixes"
```

#### 3.2 Dialogue anatomy (Анатомия диалога) (стр. 35‑36)

Four phases:  

1. **Request acquisition** – user input + system context (CLAUDE.md, history) sent for processing (стр. 35).  
2. **Planning** – Claude determines needed actions, may outline explicit plan (example shown for adding JWT auth) (стр. 35‑36).  
3. **Tool execution** – Sequential tool calls (ReadFile, Bash, WriteFile) displayed in interface (стр. 36).  
4. **Confirmation** – For risky operations, Claude asks “Allow? [Y/n/always]” (стр. 36).  
5. **Summary** – Claude lists what was done (installed packages, created files, updated routes, middleware) and provides test command (стр. 36‑37).  

#### 3.3 Basic commands and navigation (Базовые команды и навигация) (стр. 36‑38)

**Slash‑command list** (стр. 36‑37) – full verbatim output:

```
/help – Show this help
/clear – Clear dialog context
/compact – Compress context (save tokens)
/status – Session info
/cost – Cost of current session
/model – Switch model
/permissions – Manage permissions
/config – Settings
/bug – Report bug
/quit – Exit
```

**`/clear`** – resets dialogue (use when changing tasks, context too large, Claude confused) (стр. 36).  

**`/compact`** – compresses dialogue, retains key info, reduces token count (example output) (стр. 37):

```
> /compact
Context compressed:
Before: 45,832 tokens
After: 12,447 tokens
Saved: 33,385 tokens (~73%)
```

*Can focus compression*:  

```
> /compact Focus on database work
```

**`/status`** – shows session snapshot (example) (стр. 37):

```
Session Info:
Model: claude-sonnet-4-20250514
Context used: 23,451 / 200,000 tokens (12%)
Messages: 14
Files read: 8
Files written: 3
Commands executed: 5
Duration: 12m 34s
Cost: $0.47
```

**`/cost`** – detailed cost breakdown (стр. 37):

```
Cost Breakdown:
Input tokens: 187,234 ($0.32)
Output tokens: 41,892 ($0.15)
Cached tokens: 124,891 ($0.04)
Total: $0.47
```

**Hotkeys** (стр. 38):  

- `Ctrl+C` – cancel current operation / exit  
- `Ctrl+D` – exit Claude Code  
- `↑/↓` – navigate request history  
- `Tab` – autocomplete slash commands  
- `Ctrl+L` – clear screen (without resetting context)  
- `Esc` – cancel current prompt  

**Multiline input** – end line with `\` or use `Shift+Enter` (in supporting terminals) (стр. 38). Example:

```
> Создай REST API со следующими эндпоинтами: \
GET /users – список пользователей, \
POST /users – создание пользователя, \
GET /users/:id – получение пользователя, \
PUT /users/:id – обновление, \
DELETE /users/:id – удаление. \
Используй Express.js и MongoDB.
```

#### 3.4 Managing the context window (Управление контекстным окном) (стр. 38)

- **Context window size** per model: ~200 k tokens for **Sonnet**, **Opus**, **Haiku** (стр. 38).  
- Approx. **1 token ≈ 4 characters (English), 1‑2 characters (Russian)**; a 1 k‑line file ≈ 10‑20 k tokens (стр. 38).  

**Strategies** (стр. 38):  

1. **Be selective** – request specific files or directories instead of “read whole project”.  
2. **Use `/compact` regularly** to free space.  
3. **Split tasks** – finish one function, start a new dialogue for the next.  

---  

*End of part 1 (pages 1‑38).*
