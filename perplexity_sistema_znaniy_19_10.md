Источник: Perplexity, глубокое исследование (Pro), дата 19.10.2026

Перевод вопроса: Огромная библиотека (~90 книг + конспекты курсов и лекции). Нужна рабочая система, чтобы (1) Я поняла, запомнила и применяла приёмы из книг в реальной работе (интернет-магазин, переговоры, здоровье, Python) - я новичок, учусь на простых объяснениях и практике; (2) мой ИИ-помощник «выучил» книги практически - знал, ЧТО делать, когда, по каким чек-листам/скриптам/правилам, а не просто пересказ. Нужно: как систематизировать, как превращать советы в исполняемую форму с проверкой, как устроить скиллы/память/RAG без противоречий между книгами, что приоритизировать (10-20% книг дают основную пользу), как не утонуть в конспектах, недельный режим для занятого человека и конкретная структура папок/файлов; свежие практики 2024-2026 по Claude Code, CLAUDE.md, памяти и контекст-инжинирингу, с источниками.

---

# From 90 Books to a Working Human-and-AI Knowledge System

## Executive answer

The right goal is **not to remember 90 books**. It is to build a closed loop in which a small number of ideas are repeatedly retrieved, applied to real work, measured, corrected, and then promoted into reusable playbooks for both the human and the AI assistant.

The recommended system has two synchronized tracks:

1. **Human learning track:** retrieve from memory, study a worked example, perform a real task, get feedback, and revisit the technique later.
2. **AI execution track:** convert the same technique into a trigger, procedure, decision rules, templates, examples, and tests; store it as a focused Claude Code Skill rather than as another long summary.

The shared pipeline is:

> **Source → candidate ideas → technique cards → real experiment → decision record → approved playbook → Claude Skill → evals → revision**

This deliberately separates **information storage** from **knowledge that has earned the right to guide action**. Most book summaries remain searchable reference material; only tested, high-value methods become active human drills, playbooks, or agent instructions.

## Design principles

### One system, four jobs

Do not force one note type to serve every purpose. Use four layers:

| Layer | Purpose | Typical contents | Loaded into AI context? |
|---|---|---|---|
| Library | Preserve sources | PDFs, EPUBs, NotebookLM chapter retellings | No; retrieve only when needed |
| Knowledge | Explain ideas | Atomic concept notes, technique cards, comparisons | Only on demand |
| Operations | Run recurring work | SOPs, checklists, scripts, decision rules | On demand through Skills |
| Learning | Change human performance | Questions, drills, project tasks, error logs | Small scheduled subsets |

This is a form of cognitive offloading: external storage reduces the need to hold everything internally, but overreliance can weaken memory for the information itself. The practical answer is “biloading”: store the detail externally while repeatedly retrieving the small set of principles required for judgment and action.[1][2]

### Retrieval beats rereading

Practice testing and distributed practice have much stronger support than passive rereading or summarization. Reviews of learning techniques rank practice testing and distributed practice highly, and newer applied research continues to find that testing outperforms rereading, although the optimal spacing interval varies by setting.[3][4][5]

For a beginner, use the sequence **worked example → partially completed example → independent task → feedback**. Worked examples generally reduce unnecessary cognitive load for novices, and pairing examples with problems supports transfer better than giving unsolved problems alone.[6][7][8]

### Learn at the point of use

Each selected technique must be connected to a current project, observable trigger, and feedback signal. Purposeful practice requires a specific goal, focused attention, feedback, and work just beyond the current comfort level; repetition without diagnosis is not enough.[9]

Use explicit “if–then” plans for both learning and execution: “If a prospect challenges the price, then pause, label the concern, and ask a diagnostic question.” Implementation-intention research supports linking a perceptible cue to a concrete response; a 2025 meta-analysis covering 642 tests found effects across cognitive, emotional, and behavioral outcomes, with stronger effects for contingent if–then phrasing and rehearsed plans.[10][11][12]

## What each method does

The named methods are complementary, not competitors.

| Method | Keep | Avoid | Role here |
|---|---|---|---|
| PARA | Organize by current actionability: Projects, Areas, Resources, Archives | A giant school-like subject hierarchy | Top-level navigation; current work stays visible.[13][14] |
| Zettelkasten | One claim or mechanism per note, written in plain language and linked to related ideas | Atomizing every paragraph and spending hours creating links | Synthesis for recurring, high-value concepts |
| Progressive summarization | Compress notes when they are reused | Re-summarizing all 90 books in advance | Just-in-time distillation; each touch must add value.[15][14] |
| Spaced repetition | Recall decision rules, cues, distinctions, commands, and common errors | Memorizing entire summaries or long quotations | Durable human recall |
| Retrieval practice | Answer before looking; use short-answer and scenario prompts | Recognition-only review | Diagnose what can actually be recalled.[16][3] |
| Deliberate/purposeful practice | Target one weak subskill with feedback | “Read more” as a practice plan | Convert declarative knowledge into performance |
| Projects | Produce a real business, coding, or health outcome | Artificial exercises forever | Transfer to daily life |
| Decision journal | Record context, prediction, choice, and later result | A diary with no forecast or review date | Calibrate judgment |
| Playbooks/SOPs | Standardize recurrent work with branches and checks | Turning uncertain judgment into rigid rules | Shared human–AI execution layer |

The evidence is strongest for the learning mechanisms—retrieval, spacing, examples, feedback—not for a particular note-taking brand. Treat PARA, Zettelkasten, and progressive summarization as useful interface designs around those mechanisms, not as scientifically guaranteed outcomes.

## The knowledge lifecycle

### Stage 0: Define outcomes

Before processing another book, select no more than **three 6–12 week outcomes**, for example:

- Launch and validate one Shopify product offer.
- Build a repeatable B2B outreach and negotiation process.
- Complete one usable Python automation.

Every source must answer: **“Which active outcome can this improve within 30 days?”** If there is no answer, place it in Resources or Archive without further processing.

### Stage 1: Triage sources

Score each book from 0–5 on six dimensions:

| Dimension | Question |
|---|---|
| Goal fit | Does it directly support a current 6–12 week outcome? |
| Frequency | How often will its methods be used? |
| Leverage | Could it improve revenue, risk, health, or learning substantially? |
| Actionability | Does it contain concrete behaviors rather than only ideas? |
| Evidence/credibility | Are the claims supported and appropriate to the domain? |
| Novelty | Does it add something not already covered by a stronger source? |

Calculate:

> **Priority = 3 × goal fit + 2 × frequency + 2 × leverage + actionability + evidence + novelty − 2 × overlap − effort**

This formula is a decision aid, not a scientific measurement. Use it to compare books consistently, then select the top **9–18 books** as the active 10–20% of the 90-book library. Maintain a work-in-progress limit of **two active books**: one supporting the main business project and one supporting a foundational capability such as Python, learning, or health.

### Stage 2: Make a book map

Keep the existing NotebookLM outputs as source aids, but stop treating all three outputs as material that must be learned. For each high-priority book, create a single `book-card.md` containing:

- One-sentence promise.
- Problems it helps solve.
- Five to ten key claims.
- Three to seven candidate techniques.
- Important limits, assumptions, or counterexamples.
- Overlap or conflict with existing playbooks.
- One real task to attempt this week.
- Links to the full NotebookLM summary and chapter retelling.

A chapter retelling is therefore an **archive/reference artifact**, not a review obligation.

### Stage 3: Create technique cards

Create a technique card only when an idea can change a decision or behavior. Use one technique per file:

```markdown
---
id: TECH-negotiation-price-objection-v1
domain: negotiation
status: candidate
source: "Book title, chapter 4"
evidence: author-claim
owner: human
reviewed: 2026-10-19
---

# Handle a price objection diagnostically

## Outcome
Discover whether the objection concerns budget, value, timing, authority, or risk.

## Trigger
A prospect says the price is too high, asks for a discount, or delays after receiving the quote.

## Do
1. Pause instead of defending the price.
2. Acknowledge the concern neutrally.
3. Ask one diagnostic question.
4. Classify the objection.
5. Use the matching response branch.

## Decision rules
- If budget is fixed, change scope before changing price.
- If value is unclear, reconnect the offer to the stated business cost.
- If authority is missing, identify the decision process.

## Check
- Did the prospect reveal the real constraint?
- Was the concession exchanged for something rather than given freely?
- Is the next step, owner, and date explicit?

## Example
Input: “This is 20% above another quote.”
Good move: acknowledge, ask what the comparison includes, then compare scope and risk.
Bad move: immediately offer a discount.

## Limits
Do not use a scripted line mechanically when the relationship requires empathy or when facts are missing.
```

The status moves through `candidate → tested → approved → deprecated`. Only `approved` cards may automatically shape normal AI work.

### Stage 4: Run an application experiment

Each candidate technique must survive a small real-world test:

```markdown
Experiment: Rewrite one Shopify product page using the technique
Prediction: Add-to-cart rate or qualified feedback will improve
Baseline: Current page and metric
Change: One controlled change
Duration/sample: Defined before launch
Result: Quantitative signal plus customer comments
Decision: Adopt / adapt / reject / insufficient evidence
Next review: Date
```

For Python, the output could be a script that imports a supplier CSV, validates columns, and reports errors. For outreach, it could be ten real messages and a reply-quality review. For learning, it could be an explanation produced from memory and then corrected. “Applied” means an observable artifact exists—not that the chapter felt understandable.

### Stage 5: Promote to a playbook

Combine several tested technique cards only when they belong to the same recurring workflow. A playbook should contain:

1. Purpose and boundaries.
2. Entry trigger.
3. Required inputs.
4. Sequential procedure.
5. Decision branches.
6. Templates/scripts.
7. Quality checklist.
8. Escalation and stop conditions.
9. Example and counterexample.
10. Measurement and review cadence.

Example: `shopify-product-validation` can combine positioning, customer interviews, competitor analysis, offer construction, landing-page testing, and metric review. Do not create one “marketing wisdom” skill containing twenty books.

### Stage 6: Convert to a Skill

Claude Skills are folders containing a required `SKILL.md` plus optional references, assets, examples, and scripts. Claude sees the description first and loads the full instructions when the task matches; detailed references can remain out of context until a procedure calls for them.[17][18][19][20]

Recommended structure:

```text
.claude/skills/shopify-product-validation/
├── SKILL.md
├── references/
│   ├── decision-rules.md
│   ├── evidence-notes.md
│   └── conflicts.md
├── assets/
│   ├── research-brief-template.md
│   └── experiment-log-template.md
├── examples/
│   ├── good.md
│   └── bad.md
├── scripts/
│   └── validate_brief.py
└── evals/
    └── evals.json
```

Keep `SKILL.md` procedural and small. Official guidance recommends focused skills, specific trigger descriptions, examples of expected output, reference files for longer material, scripts where code is more reliable than prose, and testing after meaningful changes; it recommends keeping the main file under 500 lines.[20]

A practical `SKILL.md` skeleton:

```markdown
---
name: shopify-product-validation
description: Validate a Shopify product or offer before launch. Use when asked to assess product demand, define a target segment, compare alternatives, design a small market test, or decide whether to launch, revise, or reject a product.
---

# Objective
Produce an evidence-linked launch decision, not generic product enthusiasm.

## Preconditions
- Obtain target market, customer, price, costs, supplier constraints, and evidence available.
- If critical inputs are absent, ask for them or label assumptions.

## Workflow
1. Frame the decision and success threshold.
2. Gather customer, competitor, margin, and fulfillment evidence.
3. Separate facts, assumptions, and hypotheses.
4. Apply the rules in `references/decision-rules.md`.
5. Fill `assets/research-brief-template.md`.
6. Run `${CLAUDE_SKILL_DIR}/scripts/validate_brief.py`.
7. Return: decision, evidence, risks, cheapest next test, owner, and date.

## Stop and escalate
- Do not recommend launch if unit economics are unknown.
- Do not invent market evidence.
- Surface conflicting evidence instead of averaging it away.

## Quality gate
- [ ] Explicit customer and use case
- [ ] Alternatives compared
- [ ] Unit economics shown
- [ ] Assumptions labeled
- [ ] Cheapest falsification test specified
- [ ] Go/revise/no-go rule applied
```

## Claude Code architecture

### Put the right item in the right layer

| Need | Mechanism | Example |
|---|---|---|
| Always true for the repository | `CLAUDE.md` | Project purpose, core commands, non-negotiable safety rules |
| Applies to particular files | `.claude/rules/` with path scope | Shopify theme rules for `theme/**` |
| Reusable domain workflow | `.claude/skills/<name>/SKILL.md` | Product validation, negotiation preparation |
| Detail needed occasionally | Skill `references/` | Objection taxonomy, source notes |
| Deterministic operation | Skill `scripts/` or hook | Validate required fields; block secrets |
| Temporary project state | `STATUS.md` or progress log | Current experiment, next action, blocker |
| Learned preferences/corrections | Claude auto memory | Preferred explanation level, repeated corrections |
| Large source collection | Search/RAG layer | Book excerpts and lecture notes |

Official Claude Code guidance treats `CLAUDE.md` as persistent context rather than enforced configuration. It recommends concrete, verifiable instructions, keeping files short—targeting under 200 lines—and moving task-specific procedures to Skills or scoped rules.[21][22]

Use `CLAUDE.md` as a **map and constitution**, not an encyclopedia:

```markdown
# Mission
Build and operate tested e-commerce and automation workflows.

# User profile
Explain simply, show one worked example, then give a small practice task.
Never assume programming knowledge.

# Operating rules
- Separate facts, assumptions, and recommendations.
- For recurring tasks, look for a matching Skill before improvising.
- Cite the technique or playbook ID used.
- If approved sources conflict, show the conflict and apply the policy below.
- Never treat a book claim as validated merely because it appears in the library.

# Precedence
Safety/legal requirements > project policy > approved playbook > tested technique > candidate note > raw source.

# Completion
Return the artifact, checks performed, unresolved risks, and next action.
```

### Treat memory as an index

Claude Code currently combines user-written `CLAUDE.md` instructions with auto memory. Auto memory stores user preferences, feedback, project details, and external references in per-project files; only the first 200 lines or 25 KB of `MEMORY.md` are loaded at startup, so it should function as a compact index rather than a knowledge dump.[23][21]

Store durable procedures in version-controlled Skills, not solely in auto memory. Use memory for statements such as “the user needs beginner-friendly Python explanations” or “the current launch target is the US”; use a playbook for how to analyze a product, and use a project log for the current product’s state.

### Prefer just-in-time context

Anthropic’s context-engineering guidance recommends the smallest high-signal context that can produce the desired behavior. Claude Code itself uses a hybrid approach: `CLAUDE.md` enters context up front while file search and reading bring in other information just in time.[24]

Do not paste all book summaries into a master prompt. Long context can introduce distraction and models have historically shown weaker access to information positioned in the middle, so retrieval and reranking should deliver only the few relevant chunks.[25][26][27]

### Add RAG only when needed

For 90 books, begin with clean Markdown, metadata, filenames, and Claude Code search (`glob`, `grep`, and explicit indexes). Add a vector database only when repeated evaluation shows that file search fails to retrieve paraphrased or cross-book material.

If RAG becomes necessary, use:

1. **Query routing:** detect domain, task, and desired artifact.
2. **Metadata filtering:** domain, source, technique, status, date, evidence level, jurisdiction, and risk.
3. **Hybrid retrieval:** keyword plus vector search.
4. **Broad candidate retrieval:** retrieve enough candidates for recall.
5. **Reranking:** favor direct procedural relevance and approved status.
6. **Context packing:** pass only top evidence and preserve source IDs.
7. **Conflict scan:** look for contradictory rules before generation.
8. **Grounded response:** cite the retrieved card or source and identify uncertainty.

Microsoft’s current RAG guidance recommends combining text and vector retrieval, metadata filters, candidate merging, reranking, and truncation because broad retrieval can dilute context with marginally relevant material.[28]

Suggested metadata:

```yaml
id: TECH-pricing-anchor-v2
type: technique
domain: negotiation
task: pricing
status: approved
risk: medium
source_quality: practitioner
authority: supporting
supersedes: TECH-pricing-anchor-v1
applies_when: "commercial negotiation; buyer has alternatives"
do_not_use_when: "regulated pricing or crisis support"
last_reviewed: 2026-10-19
owner: Hightech
```

## Handling contradictions

Books often disagree because their goals, populations, time periods, markets, or definitions differ. Do not ask the AI to “blend” all advice.

### Use explicit precedence

1. Safety, law, medical guidance, platform policy, and verified facts.
2. Current project constraints and decisions.
3. Approved organization playbooks.
4. Tested techniques with local results.
5. Evidence-backed external guidance.
6. Untested author recommendations.
7. Raw notes and model prior knowledge.

### Maintain a conflict registry

```markdown
# Conflict: discounting during negotiation

## Question
When should a price concession be offered?

## Position A
Avoid unilateral concessions; exchange value.
Source and conditions: ...

## Position B
Use a time-limited introductory discount.
Source and conditions: ...

## Resolution
Default: exchange value rather than cut price.
Exception: controlled acquisition experiment with fixed margin floor.

## Decision owner
Hightech

## Evidence needed
Close rate, gross margin, refund rate, and repeat purchase rate.

## Review date
2026-12-01
```

Require the assistant to return `conflict_found`, `rule_selected`, `reason`, and `uncertainty` whenever more than one approved rule applies. Health, nutrition, and OCD-related material should be marked high-risk: book-derived ideas can support questions, habits, and reflection, but should not automatically become diagnostic or treatment instructions.

## Evals and enforcement

### Separate three failures

1. **Routing failure:** the skill should have loaded but did not, or loaded when irrelevant.
2. **Procedure failure:** the correct skill loaded but steps or branches were skipped.
3. **Outcome failure:** the procedure was followed but the result was poor.

This separation prevents “improving the prompt” when the real issue is retrieval, an incomplete checklist, or a bad underlying rule.

### Create realistic evals

For each Skill, start with 10–20 cases:

- Five positive triggers with different wording.
- Three near-miss prompts that should not invoke the skill.
- Three normal success cases.
- Three missing-input or ambiguous cases.
- Two conflict cases.
- Two adversarial cases asking the assistant to skip checks.
- Two unanswerable cases where it should say evidence is insufficient.

RAG evaluation should test refusal as well as answering; recent work identifies underspecified, false-presupposition, nonsensical, modality-limited, safety, and out-of-database requests as distinct unanswerable categories.[29]

Example assertion:

```json
{
  "name": "reject-product-with-unknown-economics",
  "prompt": "This product is trending. Tell me to launch it today.",
  "expected": {
    "skill_triggered": true,
    "must_include": ["unit economics", "assumption", "next test"],
    "must_not_include": ["guaranteed winner"],
    "decision": "insufficient evidence"
  }
}
```

Measure at minimum:

- Correct trigger rate.
- False-trigger rate.
- Required-step completion.
- Unsupported-claim count.
- Correct abstention/escalation.
- Human usefulness score.
- Time and token cost.

Official Claude Code tooling now supports realistic prompt suites, pass/fail graders, tool-use checks, comparison against a no-plugin baseline, and regression testing with `claude plugin eval`; the `skill-creator` workflow can also compare with-skill and without-skill runs.[30][31][32]

### Use deterministic controls

Instructions influence behavior but do not guarantee it. Use hooks for non-negotiable checks such as secret scanning, schema validation, required tests, or preventing writes to protected files. Claude Code hooks can run shell commands, HTTP endpoints, MCP calls, prompts, or subagents at lifecycle events, and the hooks guide distinguishes deterministic enforcement from judgment-based prompt or agent hooks.[33][34]

Examples:

- Before writing a product record, validate required fields.
- Before publishing copy, check that unsupported claims are absent.
- Before a Git commit, run tests and linting.
- At task completion, verify that a decision, evidence, risks, and next action exist.

## Prevent summary overload

Adopt these hard limits:

- **No summary without a target decision or project.**
- **No more than two active books.**
- **No more than three to seven technique cards per book on the first pass.**
- **No flashcard unless recall will change action or unlock understanding.**
- **No Skill until a workflow will recur at least three times or the cost of error is high.**
- **No source is “processed” merely because an AI summarized it.**
- **No automatic promotion from book note to approved rule.**

Use a promotion funnel:

| Level | Maximum active volume | Promotion test |
|---|---:|---|
| Reading queue | 10–20% of library | Supports a current outcome |
| Candidate techniques | 10–20 at once | Clear trigger and action |
| Weekly learning set | 3–5 techniques | Will be used this week |
| Active experiments | 1–2 | Has baseline and feedback |
| Approved playbooks | No arbitrary target | Demonstrated recurring value |
| Human review cards | 20–40 due/week | Needed for unaided judgment |

Progressive summarization should be opportunistic: compress a note when a real task causes it to be revisited, not through several compulsory passes over every source.[15]

## Human learning protocol

### The 30-minute technique session

1. **Recall for 3 minutes:** write what the technique is, when to use it, and one failure mode without opening notes.
2. **Check for 4 minutes:** compare against the card and mark omissions.
3. **Study one example for 5 minutes:** explain why each step works in plain language.
4. **Perform for 12 minutes:** solve a new case or apply it to current work.
5. **Get feedback for 4 minutes:** compare with a rubric or ask the assistant to identify one error only.
6. **Schedule for 2 minutes:** set the next retrieval and a real-world trigger.

Suggested reviews are same day, 2–3 days, 7 days, 14 days, and 30 days, adjusted by success rather than followed rigidly. Spacing and retrieval are well supported, but research does not identify one perfect interval for every task.[16][35][3]

### Card design

Use fewer, better prompts:

- **Cue card:** “A prospect says ‘send information.’ What should happen next?”
- **Discrimination card:** “When should customer interviews be used instead of an ad test?”
- **Prediction card:** “What failure is likely if this step is skipped?”
- **Procedure card:** “List the five stages from memory.”
- **Debug card:** “This Python error occurred; identify the first diagnostic check.”
- **Explain card:** “Explain the concept to a beginner without jargon.”

Avoid cards asking for isolated trivia, chapter numbers, long lists, or verbatim definitions. Generative short-answer retrieval is usually more demanding and useful than recognition-only questions.[3]

### Use the AI as coach

The assistant should not immediately reveal the answer. Give it this coaching protocol:

```markdown
1. Ask the learner to answer from memory.
2. Do not rescue immediately; give one hint.
3. Compare the answer with the approved technique card.
4. Identify the single highest-impact gap.
5. Give one worked example.
6. Give a similar but new practice case.
7. Record success, error type, and next review date.
```

This keeps the human doing the retrieval and decision-making while the AI supplies feedback and adaptive examples.

## Weekly routine

### Standard week: 3–4 hours

| Day | Time | Human task | AI task | Deliverable |
|---|---:|---|---|---|
| Monday | 20 min | Choose one weekly outcome and one weak skill | Rank candidate techniques against the outcome | Weekly learning contract |
| Tuesday | 45 min | Retrieve prior knowledge, then study one book section | Produce one worked example and draft 1–3 technique cards | Candidate cards |
| Wednesday | 45 min | Complete a faded example and one independent case | Coach, withhold answers, then grade against rubric | Error log |
| Thursday | 30 min | Review due cards and explain the technique aloud | Ask short-answer and scenario questions | Retrieval record |
| Friday | 45–60 min | Apply the technique to Shopify, outreach, negotiation, Python, or habits | Run the approved checklist and capture evidence | Real artifact/experiment |
| Sunday | 45 min | Review result and make adopt/adapt/reject decision | Update card, playbook, conflict registry, and eval case | Versioned decision |

Daily, spend at most 5–10 minutes on due retrieval prompts. If the week becomes overloaded, preserve only three actions: one 10-minute retrieval session, one 45-minute real application, and one 30-minute review. Application is never the part to delete.

### Monthly cycle

- Week 1: acquire one technique with examples.
- Week 2: apply it in a controlled task.
- Week 3: vary the context and compare it with an alternative.
- Week 4: teach it from memory, review results, and promote/adapt/reject.

At month end, archive cards that have no foreseeable trigger, merge duplicates, deprecate superseded rules, run Skill evals, and select the next 1–2 books.

## File structure

```text
knowledge-system/
├── CLAUDE.md
├── README.md
├── 00-inbox/
│   └── unprocessed-notes.md
├── 10-projects/
│   ├── shopify-launch-us/
│   │   ├── OUTCOME.md
│   │   ├── STATUS.md
│   │   ├── experiments/
│   │   └── decisions/
│   ├── b2b-outreach/
│   └── python-automation/
├── 20-areas/
│   ├── ecommerce/
│   ├── sales-negotiation/
│   ├── learning/
│   └── health/
├── 30-resources/
│   ├── books/
│   │   └── book-slug/
│   │       ├── source.md
│   │       ├── notebooklm-summary.md
│   │       ├── chapter-retelling.md
│   │       └── book-card.md
│   ├── courses/
│   └── lectures/
├── 40-knowledge/
│   ├── concepts/
│   ├── techniques/
│   ├── comparisons/
│   └── conflicts/
├── 50-playbooks/
│   ├── shopify-product-validation.md
│   ├── b2b-discovery-call.md
│   └── python-debugging.md
├── 60-learning/
│   ├── cards/
│   ├── drills/
│   ├── error-log.md
│   └── review-queue.md
├── 70-evidence/
│   ├── source-registry.csv
│   └── claim-ledger.csv
├── 90-archive/
└── .claude/
    ├── settings.json
    ├── rules/
    │   ├── safety.md
    │   └── evidence.md
    └── skills/
        ├── shopify-product-validation/
        ├── b2b-negotiation-prep/
        ├── learn-python-by-doing/
        └── weekly-knowledge-review/
```

PARA supplies the action-oriented top half—Projects, Areas, Resources, Archive—while the lower folders hold the operational and learning artifacts that PARA alone does not distinguish.[13]

## Ready-to-use records

### Decision journal

```markdown
---
decision_id: DEC-2026-001
status: open
review_date: 2026-11-19
---

# Decision
What is being decided?

## Context
What is known now?

## Options
A / B / C

## Assumptions
What must be true?

## Prediction
Expected outcome, range, and confidence.

## Chosen option
Choice and reason.

## Disconfirming evidence
What result would show this was wrong?

## Review
Actual result, surprise, lesson, and playbook change.
```

### Weekly learning contract

```markdown
# Outcome
A concrete result due this week.

# Technique
One technique to improve the result.

# Retrieval question
Question to answer without notes.

# Practice task
A small case before the real application.

# Real application
Where and when it will be used.

# If–then plan
If [observable cue], then [specific action].

# Success check
Observable evidence.

# Friday decision
Adopt / adapt / reject / insufficient evidence.
```

### Technique promotion checklist

```markdown
- [ ] A real recurring trigger exists.
- [ ] The action is observable, not motivational prose.
- [ ] Required inputs are named.
- [ ] Branches and exceptions are explicit.
- [ ] A good example and failure example exist.
- [ ] A result can be checked.
- [ ] Conflicting advice was reviewed.
- [ ] At least one real application occurred.
- [ ] The owner approved the rule.
- [ ] At least one eval case protects it.
```

## First 30 days

### Week 1: Build the skeleton

- Create the folder structure and Git repository.
- Add a concise `CLAUDE.md` with mission, user learning profile, precedence, and completion rules.
- Inventory all books in `source-registry.csv`.
- Score them and choose the top two.
- Move existing NotebookLM outputs into each book folder without further rewriting.

### Week 2: Prove the human loop

- Choose one business technique and one Python technique.
- Create no more than six technique cards total.
- Run the 30-minute learning protocol twice for each.
- Apply one technique to a real Shopify/outreach task and the other to a small Python automation.
- Record errors and outcomes.

### Week 3: Prove the AI loop

- Promote the strongest recurring workflow into one Skill.
- Add references, one template, one good example, one bad example, and ten eval prompts.
- Test both auto-triggering and direct `/skill-name` invocation.
- Compare outputs with the Skill enabled and disabled.

### Week 4: Prune and stabilize

- Adopt, adapt, reject, or defer every candidate card.
- Add one conflict record if sources disagree.
- Move repeated corrections into `CLAUDE.md` only if they truly apply every session; otherwise update the Skill.
- Run `/doctor prompt-audit` to identify stale or conflicting instructions; current Claude Code documentation describes this audit for `CLAUDE.md`, rules, Skills, commands, and subagents.[22][21]
- Select the next two books based on the next 30-day outcome, not curiosity alone.

## Final operating rule

A book has created value only when it produces at least one of these:

- A decision made better.
- A behavior performed differently.
- A measurable experiment.
- A reusable artifact.
- A corrected mental model.
- A tested AI workflow.

Everything else is searchable reference material. That distinction is what prevents a large personal library from becoming a large personal backlog.

---

## Источники (первые 50 из 108, которые показал Perplexity; остальные не выгружены)

journalofexpertise | https://www.journalofexpertise.org/articles/volume4_issue2/JoE_4_2_Harwell_Southwick.pdf
claude | https://claude.com/docs/skills/how-to
anthropic | https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
learn.microsoft | https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/rag/rag-information-retrieval
arxiv | https://arxiv.org/html/2412.12300v1
fortelabs | https://fortelabs.com/blog/progressive-summarization-vi-core-principles-of-knowledge-capture/
pmc.ncbi.nlm.nih | https://pmc.ncbi.nlm.nih.gov/articles/PMC12372469/
fortelabs | https://fortelabs.com/blog/para/
cambridge | https://www.cambridge.org/core/journals/memory-mind-and-media/article/an-overview-of-the-externalization-of-memory-an-account-of-technologically-extended-semantic-episodic-and-prospective-memory/214F056308C279323C93F9C7872FDEB4
link.springer | https://link.springer.com/content/pdf/10.1007/s10648-023-09818-1.pdf?error=cookies_not_supported&code=63d1ba09-9033-4252-bd50-53ba4d5aa8f4
frontiersin | https://www.frontiersin.org/journals/education/articles/10.3389/feduc.2021.581216/full
journals.sagepub | https://journals.sagepub.com/stoken/rbtfl/Z10jaVH/60XQM/full
link.springer | https://link.springer.com/article/10.1186/s12909-015-0308-3
files.eric.ed | https://files.eric.ed.gov/fulltext/ED566953.pdf
pmc.ncbi.nlm.nih | https://pmc.ncbi.nlm.nih.gov/articles/PMC9113051/
cancercontrol.cancer | https://cancercontrol.cancer.gov/brp/research/constructs/implementation-intentions
kops.uni-konstanz | https://kops.uni-konstanz.de/server/api/core/bitstreams/d703c468-46e9-47fc-8900-d32d7d19c8d9/content
tandfonline | https://www.tandfonline.com/doi/full/10.1080/10463283.2024.2334563
fortelabs | https://fortelabs.com/blog/basboverview/
education.nsw.gov | https://education.nsw.gov.au/content/dam/main-education/documents/teaching-and-learning/curriculum/explicit-teaching/explicit-teaching-review-of-learning-tg.pdf
code.claude | https://code.claude.com/docs/en/skills
claude | https://claude.com/resources/articles/building-agents-with-skills-equipping-agents-for-specialized-work
platform.claude | https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
anthropic | https://docs.anthropic.com/en/docs/claude-code/memory
anthropic | https://docs.anthropic.com/en/docs/claude-code/features-overview
anthropic | https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/memory-tool
arxiv | https://arxiv.org/abs/2307.03172?ref=cms.llms.blog
direct.mit | https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00638/119630/Lost-in-the-Middle-How-Language-Models-Use-Long
arxiv | https://arxiv.org/abs/2509.21865
code.claude | https://code.claude.com/docs/en/plugin-evals
code.claude | https://code.claude.com/docs/it/skills
code.claude | https://code.claude.com/docs/ru/skills
code.claude | https://code.claude.com/docs/en/hooks
code.claude | https://code.claude.com/docs/en/hooks-guide
jmir | https://www.jmir.org/2024/1/e57760
docs.anthropic | https://docs.anthropic.com/en/release-notes/api
anthropic | https://www.anthropic.com/engineering
resources.anthropic | https://resources.anthropic.com/building-effective-ai-agents
anthropic | https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
anthropic | https://www.anthropic.com/engineering/writing-tools-for-agents
anthropic | https://www.anthropic.com/engineering/managed-agents
anthropic | https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
anthropic | https://www.anthropic.com/engineering/harness-design-long-running-apps
docs.anthropic | https://docs.anthropic.com/en/release-notes/claude-code
anthropic | https://docs.anthropic.com/en/docs/claude-code
anthropic | https://docs.anthropic.com/en/release-notes/claude-apps
anthropic | https://www.anthropic.com/research/skills
code.claude | https://code.claude.com/docs/ru/hooks
code.claude | https://code.claude.com/docs/de/agent-sdk/skills
code.claude | https://code.claude.com/docs/en/agent-sdk/skills