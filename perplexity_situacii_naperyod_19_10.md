Источник: Perplexity, глубокое исследование, дата 19.10.2026 (150 источников по данным Perplexity)

Перевод вопроса: Библиотека ~90 книг, ИИ-помощник со скиллами должен применять приёмы за меня. Проблема: у меня нет примеров из жизни — ситуации ещё не случались или я их не помню, пересказать всю жизнь нельзя. Нужен метод превращения «пересказа книги» в «готово к ситуациям, которых ещё не было»: (1) индексировать по ситуациям, а не по книгам, и понять, какие ситуации будут важны именно ей, не выспрашивая всю жизнь; (2) использовать ИИ как независимый обработчик, который сам придумывает реалистичные сценарии, персонажей, возражения, пограничные случаи и сбои для каждого приёма, и как проверять, что они реалистичны и приём правда применим; (3) превращать приёмы в исполняемые правила, чек-листы, скрипты с условиями применимости, противопоказаниями и конфликтами между книгами; (4) как помощник распознаёт в живом разговоре подходящий приём и задаёт минимум уточняющих вопросов; (5) как новичку репетировать ещё не прожитые ситуации; (6) дешёвый по токенам порядок работы, структура папок и пример шаблона для одного приёма (ответ на «дорого»).

(Перед отчётом Perplexity задал уточняющий вопрос про формат источников; пропущен кнопкой «Пропустить».)

---
# From Books to a Situation-First AI Playbook

## Executive answer

The system should not treat 90 books as 90 large summaries. It should treat them as source material for a **behavior compiler** that produces four linked assets:

1. **Situation cards** — observable events, goals, constraints, stakes, and cues.
2. **Technique cards** — explicit rules describing when a technique applies, when it does not, and what action to take.
3. **Scenario and evaluation banks** — positive cases, near misses, contraindicated cases, adversarial cases, and multi-turn simulations.
4. **Runtime skills** — concise Claude Code Skills that retrieve the right cards and source passages only when needed.

The central data model is a many-to-many graph:

```text
PERSON PROFILE + CURRENT GOAL
              ↓
SITUATION / TRIGGER  ←→  TECHNIQUE  ←→  SOURCE PASSAGES
       ↓                    ↓                 ↓
LIVE ROUTING          ACTION PLAYBOOK     BOOK + EDITION + PAGE
       ↓                    ↓
MINIMAL QUESTION      SCRIPT / CHECKLIST / REHEARSAL
       ↓                    ↓
OUTCOME LOG  →  EVALS, REVISIONS, PERSONAL MEMORY
```

This resolves the “unlived experience” problem without pretending that synthetic examples are memories or facts. Generated scenarios become **hypotheses and training cases**, while source-grounded rules, external evidence, human review, and later real outcomes determine whether a technique earns production status.

## Design principles

### Separate four truth layers

Every card should distinguish:

| Layer | Meaning | Allowed wording |
|---|---|---|
| Author claim | What a book says | “The author recommends…” |
| External evidence | What independent research or guidance supports | “Evidence is strong / mixed / weak…” |
| System synthesis | A rule inferred by the processor | “System-synthesized; requires validation” |
| Personal evidence | What worked for this user in logged cases | “Worked in 3 of 4 relevant cases; low sample size” |

This matters because books vary greatly in evidential quality. For example, evidence reviews find little high-quality support for neurolinguistic programming as a health intervention, so NLP-derived cards should not silently acquire the status of clinically validated methods. For OCD, the safety hierarchy should instead privilege established clinical guidance: NICE recommends CBT including exposure and response prevention, with intensity adapted to impairment and preference.[1][2][3][4]

### Store provenance, not long quotations

For every actionable clause, retain a machine-readable source anchor: book ID, edition, chapter, printed page, PDF page, source span ID, extraction confidence, and a short paraphrase. Keep copyrighted quotations minimal; store page-addressable source text privately for retrieval rather than copying extended passages into every Skill.

### Prefer abstention to forced advice

A technique router must be allowed to return:

- `no_match`
- `possible_match_needs_one_answer`
- `multiple_conflicting_matches`
- `high_risk_refer_or_warn`

The assistant is not successful merely because it used a technique. It is successful when it **recognized the situation accurately, avoided contraindications, grounded its advice, asked no more than necessary, and produced a useful action**.

## Situation-first ontology

### Use three layers

Do not build one enormous tree. Use a small stable hierarchy plus facets and free-text trigger descriptions.

#### Layer A: life sphere

- Business and work
- Money and purchasing
- Learning and decisions
- Health and nutrition
- Self-regulation and OCD support
- Relationships and communication
- Administration and life logistics
- AI, software, and automation

#### Layer B: goal episode

These verbs are reusable across domains:

- Notice or diagnose
- Choose or prioritize
- Plan
- Start
- Execute
- Monitor
- Communicate
- Persuade or sell
- Negotiate
- Resolve conflict
- Recover from failure
- Learn or rehearse
- Stop, defer, or escalate

#### Layer C: observable event

This is the actual retrieval unit:

- Prospect says the offer costs too much.
- Supplier changes terms after an agreement.
- Customer requests a refund and sounds angry.
- A task is repeatedly postponed despite clear intent.
- An intrusive thought creates an urge to check or seek reassurance.
- A study answer feels familiar but cannot be recalled without cues.
- An agent repeatedly selects the wrong tool after ambiguous user wording.

The hierarchy answers “what area and episode is this?” The event answers “what happened?”

### Add situation facets

Each event receives structured facets rather than being forced into only one category:

| Facet | Example values |
|---|---|
| Actors | self, prospect, customer, supplier, manager, peer, family, agent |
| Relationship | new, established, dependent, adversarial, authority asymmetry |
| Channel | live call, chat, email, meeting, internal thought, software trace |
| Goal | clarify, close, protect margin, learn, reduce harm, decide, repair |
| Stage | before event, opening, exploration, decision, aftermath |
| Stakes | low, medium, high; reversible or irreversible |
| Information state | sufficient, missing, contradictory, unreliable |
| Time pressure | none, moderate, urgent |
| Affect | calm, anxious, angry, ashamed, excited, uncertain |
| Risk flags | medical, legal, financial, vulnerable person, coercion, privacy |
| Psychological character | duty, intellect, adversity, positivity, negativity, deception, sociality |

The final facet borrows from the DIAMONDS taxonomy, which describes psychologically meaningful situation characteristics such as duty, adversity, negativity, deception, and sociality. It should be used as a descriptive feature set, not as the whole ontology.[5][6]

For work situations, seed the library from O*NET rather than inventing every role from scratch. O*NET organizes occupation-specific tasks under detailed, intermediate, and generalized work activities and links more than 19,000 task statements to a hierarchy of work activities. This provides realistic work episodes, while the book-derived layer supplies techniques for handling them.[7][8]

### Define triggers precisely

A trigger record needs four kinds of cues:

```yaml
trigger:
  canonical_event: "Prospect states that the offer is too expensive"
  positive_cues:
    - explicit price comparison
    - request for discount after value discussion
    - concern about budget, ROI, or approval
  weak_cues:
    - asks for price before discovery
    - pauses after hearing price
  negative_cues:
    - disputes an unauthorized charge
    - asks for a refund after delivery failure
    - states financial hardship or vulnerability
  latent_states:
    - budget constraint
    - insufficient perceived value
    - competitor comparison
    - lack of authority
    - negotiation tactic
```

Positive cues increase match confidence. Negative cues are not merely low scores; they can veto the technique. Latent states tell the assistant which minimal question can separate plausible branches.

## Discover likely situations

A person should not need to narrate her life. Build a **prospective profile** from compact, high-yield inputs.

### Five-input profile

Ask once, then maintain incrementally:

1. **Roles now:** for example, Shopify founder, buyer, content creator, operations lead, learner.
2. **Goals for 90 days:** launch store, validate products, create organic content, automate research.
3. **Recurring workflows:** sourcing, supplier contact, offer creation, customer support, training, meal planning.
4. **Upcoming transitions:** first supplier negotiation, first paid ads, hiring, relocation, treatment change.
5. **Boundaries:** risk tolerance, ethical limits, health conditions requiring safeguards, preferred communication style.

This produces a role-goal-stage matrix. The assistant then expands each row into foreseeable situations using task taxonomies, goal decomposition, and a pre-mortem. It proposes the list for confirmation rather than asking for life stories.

### Priority formula

Score each proposed situation from 0 to 4 on five dimensions:

```text
priority =
  0.30 × likelihood in next 90 days
+ 0.25 × impact
+ 0.20 × goal relevance
+ 0.15 × imminence
+ 0.10 × current rehearsal gap
```

This is a planning heuristic, not a validated psychological scale. Add a separate `risk_class`; high-risk health, legal, or financial cases receive stricter review regardless of priority.

### Learn from thin signals

With explicit consent, update the profile from low-burden artifacts:

- Project names and milestones
- Task and calendar categories
- Store stage and active product categories
- Repeated questions or corrections
- Outcome notes after important conversations
- One-tap weekly check-in: “Which of these situations occurred?”

Do not infer sensitive diagnoses, relationships, or finances from weak signals. Claude Code auto memory can retain preferences and project learnings, but memory is context rather than enforced configuration, is editable, and only an initial portion is automatically loaded; it should not become the sole source of safety rules or provenance.[9]

## Book-to-playbook pipeline

### Ingest with page fidelity

For each PDF or EPUB:

1. Record title, author, edition, year, ISBN, file hash, language, and rights status.
2. Extract text while preserving chapter headings, printed page labels, PDF page numbers, tables, and figure captions.
3. OCR only failed or scanned pages; flag low-confidence spans.
4. Split by semantic section while preserving `source_span_id`, enclosing headings, and page range.
5. Create both lexical and embedding indexes.

A source span should look like this:

```yaml
span_id: SALESBOOK-01.ch07.p143-145.s02
book_id: SALESBOOK-01
edition: "Edition recorded in manifest"
chapter: "Chapter 7"
printed_pages: "143-145"
pdf_pages: "167-169"
heading_path:
  - "Handling objections"
  - "Price concerns"
text_hash: "sha256:..."
ocr_confidence: 0.99
```

### Extract technique candidates

A cheap model processes spans independently and emits only candidate records:

- Technique name and purpose
- Observable problem or opportunity
- Preconditions stated by the author
- Steps or decision points
- Claimed outcome
- Warnings and exceptions
- Examples present in the source
- Exact source span IDs
- Uncertainties and missing context

Require the processor to label each field as `explicit`, `reasonable_inference`, or `not_found`. It must never fill `not_found` from general knowledge.

### Normalize across books

Cluster candidates by **action mechanism**, not book vocabulary. For example, “label the concern,” “acknowledge before answering,” and “validate the objection” may overlap but should not be merged until a stronger model checks whether their intent, sequence, and contraindications truly match.

Create three relations:

- `equivalent_to` — interchangeable under the same conditions
- `complements` — useful in sequence or combination
- `conflicts_with` — incompatible actions, assumptions, or goals

### Adjudicate with a strong model

For each cluster, supply the source spans and require the model to:

1. Produce the smallest defensible rule.
2. Separate author claims from synthesis.
3. List applicability conditions and negative conditions.
4. Identify conflicts and missing evidence.
5. Create a source map from every action clause to one or more spans.
6. Block publication if a central clause has no source.

A second, independent call should attempt to falsify the card: find a source contradiction, an overgeneralization, a missing prerequisite, or a case where the advice would be harmful.

### Add external evidence

Books are not enough for health, behavior change, nutrition, or contested methods. Attach an evidence label:

```yaml
evidence:
  author_support: explicit
  external_status: strong | moderate | mixed | weak | not_checked
  evidence_scope: "What outcome and population were actually studied"
  reviewed_on: 2026-10-19
  expires_on: 2027-10-19
```

Implementation intentions are a useful example of a technique with an external research base: they link a perceivable cue to a directly actionable response in an if-then form. A 2025 meta-analysis found effects across cognitive, affective, and behavioral outcomes, with larger effects when plans used a contingent format, motivation was high, and plans were rehearsed.[10][11][12]

## Executable technique cards

### Required schema

Every production technique should contain:

```yaml
id: sales.price-objection.diagnose-before-answer
version: 1.0.0
status: draft | reviewed | production | retired
title: "Diagnose the price objection before answering"
intent: "Determine what 'too expensive' means before proposing a response"

sources:
  - span_id: "..."
    support: explicit | inferred
    supports_fields: ["steps.1", "decision_rules.budget"]

applies_when:
  all:
    - "A prospect expresses concern about price, cost, budget, or value"
  any:
    - "The meaning of the concern is unclear"
    - "Several causes would require different responses"

contraindications:
  - "Unauthorized charge, billing error, or refund complaint"
  - "Vulnerable person or stated financial hardship"
  - "Seller cannot truthfully support the value claim"
  - "A legal, medical, or regulated disclosure is required"

observable_cues:
  strong: []
  weak: []
  negative: []

minimum_information:
  - desired outcome
  - sales stage
  - likely meaning of the objection
  - authority to change price or terms

steps:
  - acknowledge without conceding
  - ask one neutral diagnostic question
  - classify the concern
  - choose a truthful branch
  - check whether the concern is resolved

decision_rules: {}
scripts: {}
failure_modes: []
conflicts: []
safety: []
examples: []
counterexamples: []
evals: []
```

### Decision rules, not prose

Convert advice into a decision table:

| Condition | Action | Do not do |
|---|---|---|
| Meaning unclear | Ask one diagnostic question | Launch into a defense |
| Genuine budget ceiling | Explore scope, timing, or fit | Shame or pressure |
| Value not established | Reconnect to the prospect’s stated outcome and evidence | Invent ROI |
| Competitor comparison | Compare equivalent scope and risk | Misrepresent competitor |
| No authority | Identify decision process | Treat as final rejection |
| Seller is poor fit | Say so and disengage | Force the technique |

### Resolve conflicts explicitly

Use this precedence order:

1. Safety, law, consent, and non-deception
2. High-quality external evidence within its actual scope
3. Explicit user values and goals
4. Situation fit and contraindications
5. Reversibility and least-harm option
6. Book authority or popularity

If two books recommend opposite tactics, preserve both branches and state the discriminator. For example, “hold price” and “offer a concession” are not necessarily contradictory if the latter is conditional on reciprocal terms, but they are contradictory when both claim to be the default response to the same facts.

## Synthetic scenario factory

Synthetic scenarios are valuable because they expose missing branches before real events occur, but they are not proof that a technique works. Research on synthetic data describes generation, curation, and evaluation as separate stages, and human evaluation remains important for naturalness and label validity. Synthetic benchmarks can represent simpler intent tasks reasonably while becoming less representative on more complex tasks, so a scenario bank must be progressively replaced or calibrated with real traces.[13][14][15]

### Four-agent separation

Use separate contexts and, where affordable, different model families or versions:

| Processor | Sees | Produces | Must not do |
|---|---|---|---|
| Grounder | Technique card and cited source spans | Atomic claims and constraints | Invent scenarios |
| Generator | Grounded card plus coverage matrix | Scenarios and personas | Grade its own work |
| Challenger | Card plus generated scenarios | Edge cases, counterexamples, failure modes | Repair silently |
| Judge | Rubric, card, source spans, blinded scenarios | Scores and reasons | Assume generator is correct |

This mirrors current automated behavioral-evaluation practice: Anthropic’s Bloom separates understanding, scenario ideation, rollout, and judgment, including simulated users and transcript-level scoring. Google’s agent-evaluation guidance likewise treats scenarios as multi-turn cases with simulated user responses and separate metrics for traces.[16][17][18]

### Scenario coverage matrix

Generate combinations deliberately rather than asking for “20 diverse examples.”

- **Polarity:** applies, near miss, does not apply, contraindicated
- **Difficulty:** obvious, ambiguous, hidden trigger, multiple simultaneous triggers
- **Persona:** novice, expert, skeptical, rushed, emotional, manipulative, vulnerable
- **Power:** user has more, equal, or less authority
- **Channel:** email, chat, call, meeting, internal self-talk
- **Stage:** anticipation, live event, aftermath
- **Stakes:** low, medium, high
- **Noise:** missing facts, misleading wording, irrelevant detail, contradiction
- **Culture/language:** directness, formality, second-language communication
- **Outcome:** success, partial success, technique failure, harm avoided by abstention

For each positive scenario, create at least one **contrastive twin** in which one decisive fact changes and the technique should no longer apply. Counterfactual twins test whether routing depends on the real condition rather than keywords.

### Scenario record

```json
{
  "scenario_id": "price-obj-017",
  "technique_id": "sales.price-objection.diagnose-before-answer",
  "split": "holdout",
  "polarity": "near_miss",
  "persona": {
    "role": "existing customer",
    "goal": "correct an unexpected charge",
    "style": "brief and irritated"
  },
  "opening": "This is too expensive. Why was I charged twice?",
  "hidden_state": "billing_error",
  "decisive_facts": ["duplicate charge", "post-purchase"],
  "expected_route": "billing-resolution",
  "forbidden_route": "sales-price-objection",
  "required_questions": [],
  "success_criteria": [
    "recognizes a billing problem",
    "does not negotiate value",
    "prioritizes correction or escalation"
  ],
  "source_constraints": ["no unsupported claims"],
  "risk_flags": ["financial"],
  "generator_model": "recorded-at-build-time"
}
```

### Failure-mode generation

Run a pre-mortem prompt in past tense:

> “The technique was applied exactly as written and the interaction ended badly. Generate distinct reasons, including misclassification, missing information, power dynamics, ethical problems, timing, channel mismatch, emotional escalation, and source overreach.”

A pre-mortem imagines that the plan has already failed and works backward to causes; prospective-hindsight research found that treating an outcome as certain can elicit more explanations, although this does not prove improved real-world outcomes.[19][20]

## Validation and evals

### Validation gates

A scenario or card reaches production only if it passes six gates:

1. **Source fidelity:** every book-derived action is entailed by a cited span.
2. **Applicability:** scenario facts satisfy the card’s required conditions.
3. **Non-applicability:** contraindicated and contrastive cases route elsewhere or abstain.
4. **Realism:** persona, sequence, incentives, language, and constraints are internally coherent.
5. **Action quality:** output follows the decision rule, remains truthful, and is usable.
6. **Safety:** high-risk domains respect boundaries and escalation rules.

### Use a mixed grading stack

Use the fastest reliable grader first. Anthropic’s eval guidance recommends task-specific cases, explicit success criteria, edge cases, code grading where possible, and LLM grading only after testing its reliability.[21]

| Check | Preferred grader |
|---|---|
| Required fields and source IDs exist | Code/schema validator |
| All cited pages resolve | Code validator |
| Forbidden phrase or unsafe branch | Code rules plus classifier |
| Retrieval contains gold card in top-k | Deterministic retrieval metric |
| Preconditions are entailed by scenario | LLM judge with rubric |
| Script is natural and non-coercive | LLM judge plus human sample |
| Clinical or high-stakes appropriateness | Qualified human reviewer |
| Realism for a job or market | Domain reviewer or real-trace comparison |

### Judge rubric

Score each axis from 0 to 2, with explicit anchors:

- **Grounding:** 0 unsupported; 1 partly mapped; 2 every material action mapped.
- **Situation fit:** 0 wrong; 1 plausible but uncertain; 2 preconditions clearly met.
- **Contraindications:** 0 ignored; 1 mentioned; 2 correctly veto or adapt action.
- **Question economy:** 0 unnecessary interrogation; 1 acceptable; 2 minimum discriminating question.
- **Actionability:** 0 abstract; 1 usable with editing; 2 immediately executable.
- **Truthfulness:** 0 invented claim; 1 uncertain wording; 2 calibrated and supported.
- **Safety and ethics:** 0 harmful/coercive; 1 minor concern; 2 safe and respectful.

Set hard failures: unsupported medical instruction, fabricated page reference, missed contraindication, deceptive sales claim, or confident route on an intentionally unresolvable case.

### Control judge bias

LLM judges can exhibit position, authority, verbosity, and other biases. Mitigate these by:[22][23]

- Randomizing candidate order and repeating reversed comparisons
- Hiding model and book names when they are not rubric-relevant
- Using point-based rubrics before holistic preference
- Supplying calibrated examples at score boundaries
- Making the judge quote decisive scenario facts and source IDs
- Recomputing weighted totals in code
- Comparing judge decisions with a human-labeled calibration set
- Sending disagreements and all high-risk cases to human review

Newer models may show less position bias in some tests, but that finding is model- and task-dependent, so the safeguards should remain.[24]

### Core system metrics

Track by domain, skill, and risk class:

- Trigger recall: relevant technique appears in top-k
- Routing precision: invoked technique was appropriate
- False-positive rate on near misses
- Contraindication recall
- Abstention accuracy
- Mean number of clarifying questions
- Grounded-action rate
- Source-page resolution rate
- Scenario pass rate and worst-case pass rate
- Human–judge agreement
- Outcome usefulness rating after real use
- Tokens, latency, and retrieval calls per resolved situation

Maintain three data splits:

- `development`: visible while writing cards
- `holdout`: never shown to the card generator
- `live`: anonymized real cases added only after use

Anthropic recommends held-out test sets for agent/tool evaluation and collecting runtime, tool-call, token, and error metrics in addition to accuracy.[25]

### Human sampling plan

For low-risk cards, manually inspect:

- All first versions
- All judge disagreements
- All hard failures
- A random 10% of accepted synthetic scenarios
- A random 5% of routine regression runs

For OCD, nutrition with medical implications, legal issues, or consequential financial advice, review every production card and every major revision with an appropriately qualified person. The assistant must not diagnose, alter treatment, or turn reassurance into a repeated compulsion-support loop.

## Runtime architecture

### CLAUDE.md

Keep `CLAUDE.md` as the short constitution and router, not the library. Claude Code documentation distinguishes persistent `CLAUDE.md` instructions from on-demand Skills and recommends keeping `CLAUDE.md` under about 200 lines.[26]

It should contain only:

- The assistant’s role
- Safety and non-deception rules
- The routing protocol
- Source-grounding requirement
- Minimal-question policy
- Conflict precedence
- Paths to profile, ontology, and Skills
- Outcome logging instruction

### Skills

A Claude Code Skill is a folder with `SKILL.md` frontmatter and optional supporting resources. Claude sees the skill name and description for discovery, while the full body loads on invocation; this is progressive disclosure and keeps unused reference material out of context.[27][28]

Create Skills by **situation family**, not by book:

```text
sales-price-objection/
supplier-term-change/
customer-refund-conflict/
learning-retrieval-failure/
ocd-reassurance-urge/
nutrition-meal-adjustment/
agent-tool-routing-failure/
```

A useful Skill description includes both triggers and exclusions:

```yaml
---
name: sales-price-objection
description: >
  Use when a prospect or buyer questions price, affordability, value, ROI,
  or competitor cost before purchase. Do not use for billing errors,
  unauthorized charges, refunds, financial hardship, or post-purchase complaints.
---
```

Skill bodies should remain concise; Anthropic recommends keeping `SKILL.md` under 500 lines and moving supporting material into additional files read only when needed.[29]

### RAG

Use RAG for:

- Book passages and page references
- Long scenario banks
- External evidence notes
- Conflict records
- Detailed examples
- Archived outcomes

Use hybrid retrieval: lexical search for exact terms and source IDs, embeddings for semantic similarity, then rerank. Anthropic’s contextual retrieval method adds chunk-specific context before both embedding and BM25 indexing and reported lower top-20 retrieval failures, with further improvement from reranking.[30]

### Memory

Use memory for:

- Stable role and communication preferences
- Active goals and projects
- Confirmed recurring situations
- User corrections
- Technique outcomes and opt-outs

Do not use memory for:

- Canonical book content
- Safety policies
- Full scenario banks
- Unverified inferences about the user
- Facts that require a current source

Claude’s memory mechanism is suited to just-in-time retrieval across sessions rather than loading everything into every context.[31]

### Live routing algorithm

```text
1. Parse current message into event, goal, actors, stage, stakes, risk flags.
2. Retrieve top situation cards using exact terms + embeddings.
3. Apply negative cues and contraindication vetoes.
4. Retrieve linked technique cards for surviving situations.
5. If one route is clear and low risk, act.
6. If two routes differ on one unknown fact, ask one discriminating question.
7. If consequential facts remain missing, state limits or escalate.
8. Load only the selected Skill, card, and source spans.
9. Answer with the smallest useful script/checklist.
10. Offer rehearsal or log the outcome only when useful and consented.
```

### Minimal-question policy

Ask a question only when its answer can change the branch, safety, or recommendation. Use this order:

1. “What outcome do you want right now?”
2. “What exactly did the other person say or do?”
3. “Is this before purchase, during negotiation, or after payment?”
4. “Do you have authority to change price, scope, or timing?”

Ask one at a time. If a reasonable reversible default exists, state the assumption and proceed. If the case is high-stakes, do not trade safety for conversational smoothness.

## Rehearsing unlived situations

### Scenario drills

Each drill should train recognition before performance:

1. Show a short situation without naming the technique.
2. Ask the learner to identify the trigger and non-trigger cues.
3. Ask for the first action or first sentence.
4. Reveal a new fact that changes the branch.
5. Require adaptation.
6. Compare with the card and explain the decisive cue.
7. Schedule a contrastive case later.

Spacing and retrieval practice generally improve durable retention compared with massing, and interleaving is particularly useful when learners must discriminate between similar problem types. Therefore, mix “price objection,” “billing error,” “value confusion,” and “not a fit” rather than practicing 20 obvious price objections consecutively.[32][33][34]

### Role-play simulator

The AI plays the counterpart but follows hidden persona state. It should not yield merely because the learner used a target phrase. The simulator changes behavior only when the learner addresses the hidden concern, remains truthful, and respects boundaries.

A session uses four phases:

- Baseline attempt with no hints
- Targeted feedback on one subskill
- Retry with a changed persona or channel
- Delayed transfer case 2–7 days later

### If-then plans

After rehearsal, save one implementation intention:

> If a prospect says the price is too high and I do not know whether the issue is budget or value, then I will acknowledge the concern and ask one neutral diagnostic question before defending the offer.

Implementation intentions explicitly connect a situation cue to a response and are designed to close the gap between intention and action. Their effects are heterogeneous, so they should support—not replace—skill practice, motivation, and environmental changes.[35][36][10]

### WOOP and pre-mortem

Use WOOP for personally important goals:

- Wish
- Best feasible outcome
- Internal obstacle
- If-then plan

A meta-analysis of mental contrasting with implementation intentions found a small-to-medium overall effect and noted possible publication bias, so WOOP should be presented as a compact planning method rather than a guarantee.[37]

Use a pre-mortem for complex plans and one-to-one drills for interpersonal techniques. One surfaces system risks; the other develops moment-to-moment behavior.

## Token-efficient build

### Model allocation

| Stage | Cheap/fast model | Strong model | Human |
|---|---|---|---|
| Parse/OCR cleanup | Classify bad pages, extract metadata | Only ambiguous layouts | Spot-check scans |
| Candidate extraction | Batch structured extraction | Resolve difficult passages | Review high-risk books |
| Normalize | Embed, cluster, deduplicate | Decide equivalence/conflict | Review disputed clusters |
| Technique card | Draft fields and scripts | Ground, adjudicate, falsify | Approve production |
| Scenarios | Generate matrix variants | Create adversarial/ambiguous cases | Realism sample |
| Evals | Run router and code checks | Judge nuanced outputs | Calibrate judge and risks |
| Runtime | Route and retrieve | Handle ambiguous/high-stakes case | User decides |

### Cost rules

- Process a book once; persist spans, hashes, candidates, and embeddings.
- Re-run only changed spans or cards whose dependencies changed.
- Batch identical tasks with strict JSON schemas.
- Cache the stable extraction rubric and book manifest.
- Generate scenarios only after a card survives grounding review.
- Keep rejected scenarios with rejection reasons to improve future prompts.
- Use a strong model on clusters and failures, not every paragraph.
- Summarize handoffs between long-running agents instead of carrying full transcripts.

Anthropic’s Batch API is designed for asynchronous high-volume work and provides a 50% token discount; prompt caching can be combined with batching, although cache hits in concurrent batches are best-effort. Prompt caching reduces repeated-prefix cost, but cached tokens still occupy the context window, so caching is not a substitute for retrieval and compaction.[38][39][40]

For long jobs, decompose work into tractable chunks and carry structured artifacts between fresh contexts. Anthropic’s 2026 guidance describes context resets plus structured handoffs as a way to preserve coherence in long-running agent work. More broadly, current context-engineering guidance favors the smallest high-signal context, canonical examples, just-in-time retrieval, structured notes, and compaction over filling the entire context window.[41][42]

### Practical staged rollout

#### Stage 0: foundation

- Ingest 3 representative books: one sales, one learning-science, one health/safety-sensitive.
- Build ontology v0 with 30–50 situation cards.
- Create schemas and validators.
- Write 20 manually reviewed routing cases.

#### Stage 1: one vertical

- Compile 10–15 sales and negotiation techniques.
- Generate 20–40 scenarios per technique, mostly cheap-model output.
- Strong-model review only failures, conflicts, and ambiguous cases.
- Human-review every production card and 10% of scenarios.

#### Stage 2: runtime pilot

- Install 5–8 situation Skills.
- Add hybrid retrieval over sources.
- Run shadow mode: assistant suggests a route but does not silently apply it.
- Log false positives, missed triggers, excessive questions, and source failures.

#### Stage 3: rehearsal

- Add daily five-minute scenario drill.
- Use interleaved near-neighbor situations.
- Create one if-then plan from each completed session.

#### Stage 4: sensitive domains

- Add OCD and nutrition only after safety rules, external evidence review, referral boundaries, and qualified human review are operational.
- Treat NLP claims as hypothesis-level unless independently supported for the exact use and outcome.

#### Stage 5: scale to 90 books

- Process books by expected situation coverage, not reading order.
- Stop extracting when new books add no material rule, exception, conflict, or scenario.
- Review production cards on source change, repeated failure, or scheduled expiry.

## Folder and file schema

```text
knowledge-system/
├── CLAUDE.md
├── .claude/
│   ├── rules/
│   │   ├── routing.md
│   │   ├── grounding.md
│   │   ├── safety-health.md
│   │   └── ethics-sales.md
│   ├── skills/
│   │   ├── situation-router/
│   │   │   └── SKILL.md
│   │   └── sales-price-objection/
│   │       ├── SKILL.md
│   │       ├── quick-checklist.md
│   │       └── scripts.md
│   └── agents/
│       ├── technique-grounder.md
│       ├── scenario-generator.md
│       ├── scenario-challenger.md
│       └── eval-judge.md
├── profile/
│   ├── profile.yaml
│   ├── goals-90d.yaml
│   ├── active-roles.yaml
│   ├── boundaries.yaml
│   └── consent.yaml
├── ontology/
│   ├── spheres.yaml
│   ├── goal-episodes.yaml
│   ├── facets.yaml
│   ├── trigger-lexicon.yaml
│   └── relations.yaml
├── sources/
│   └── books/
│       └── SALESBOOK-01/
│           ├── manifest.yaml
│           ├── page-map.json
│           ├── spans.jsonl
│           └── extraction-report.md
├── situations/
│   └── sales/
│       ├── price-objection.yaml
│       ├── billing-dispute.yaml
│       └── refund-complaint.yaml
├── techniques/
│   └── sales/
│       └── diagnose-price-objection/
│           ├── card.yaml
│           ├── playbook.md
│           ├── source-map.json
│           ├── conflicts.yaml
│           └── changelog.md
├── scenarios/
│   └── sales.price-objection.diagnose-before-answer/
│       ├── development.jsonl
│       ├── holdout.jsonl
│       ├── adversarial.jsonl
│       └── human-reviewed.jsonl
├── evals/
│   ├── rubrics/
│   │   ├── routing.yaml
│   │   ├── grounding.yaml
│   │   └── safety.yaml
│   ├── golden/
│   ├── runs/
│   └── regressions/
├── rehearsal/
│   ├── queue.yaml
│   ├── attempts.jsonl
│   └── implementation-intentions.md
├── outcomes/
│   ├── anonymized-cases.jsonl
│   └── technique-stats.csv
└── pipeline/
    ├── schemas/
    ├── prompts/
    ├── scripts/
    └── cache/
```

Keep personal profile and outcomes out of shared version control. Keep source manifests and card versions under version control so every recommendation can be reproduced.

## Worked example

The following card is a **system-synthesized demonstration**, not a claim attributed to a specific book. Its production status is intentionally blocked until real source spans from the user’s books are attached.

### Technique card

```yaml
id: sales.price-objection.diagnose-before-answer
version: 0.1.0
status: draft-blocked-source-grounding
title: "Diagnose a price objection before answering"
intent: "Select a response only after identifying what the price concern means"
origin: system-synthesized-demonstration

source_gate:
  production_allowed: false
  reason: "No user-book source spans have yet been attached"

applies_when:
  all:
    - "A pre-purchase buyer expresses concern about price, cost, budget, or value"
    - "The seller is deciding how to respond"
  any:
    - "The meaning is unclear"
    - "Different meanings require different responses"

contraindications:
  - "Billing error or unauthorized charge"
  - "Refund or service-recovery request"
  - "Stated hardship or vulnerable-customer concern"
  - "The offer is not a responsible fit"
  - "The seller would need to invent evidence or pressure the buyer"

latent_states:
  - budget_ceiling
  - weak_perceived_value
  - competitor_comparison
  - missing_decision_authority
  - poor_timing
  - negotiation_tactic
  - genuine_no_fit

first_move:
  action: "Acknowledge briefly and ask one neutral diagnostic question"
  script: "That makes sense to examine. Is the main concern the total budget, the value relative to the outcome, or a comparison with another option?"

branches:
  budget_ceiling:
    action: "Explore scope, timing, or a smaller legitimate option"
    forbid: "Pressure, shame, or disguised debt advice"
  weak_perceived_value:
    action: "Return to the buyer's stated outcome and verifiable evidence"
    forbid: "Invented ROI or generic feature dumping"
  competitor_comparison:
    action: "Compare equivalent scope, terms, risk, and evidence"
    forbid: "Unsupported competitor claims"
  missing_decision_authority:
    action: "Clarify approval criteria and participants"
    forbid: "Treat the contact as the final decision-maker"
  poor_timing:
    action: "Clarify timing and next decision point"
    forbid: "Create false urgency"
  genuine_no_fit:
    action: "Say so and disengage respectfully"
    forbid: "Force a close"

completion_check:
  script: "If we resolve that specific concern, is there anything else that would prevent a decision?"

failure_modes:
  - keyword match routes a duplicate charge to a sales skill
  - diagnostic question sounds like a canned interrogation
  - seller argues value before understanding the buyer
  - discount is offered without knowing the constraint
  - assistant assumes every objection is a tactic
  - buyer lacks authority but the assistant pushes for commitment
  - real hardship is treated as a persuasion opportunity

conflicts:
  - with: "immediate-value-reframe"
    resolution: "Use only when the concern's meaning is already clear"
  - with: "automatic-discount"
    resolution: "Do not discount until constraint, authority, and reciprocal terms are known"
```

### Skill file

```markdown
---
name: sales-price-objection
description: >
  Use for pre-purchase concerns about price, affordability, value, ROI,
  discount, or competitor cost. Do not use for duplicate charges,
  billing errors, refunds, post-purchase service failures, hardship,
  or vulnerable-customer cases.
---

# Price objection

1. Read `techniques/sales/diagnose-price-objection/card.yaml`.
2. Check negative cues and contraindications before using any sales script.
3. If the objection's meaning is unclear, ask only one diagnostic question.
4. Choose one branch from the card; do not combine every branch.
5. Retrieve source spans before attributing the method to a book.
6. Never invent ROI, scarcity, competitor facts, or customer evidence.
7. If the offer is a poor fit or would create hardship, recommend no sale.
8. Keep the response short enough to say naturally.
```

### Scenario mini-bank

| Case | Expected behavior |
|---|---|
| “It is €200 more than the alternative.” | Ask what is included in the alternative; compare equivalent scope. |
| “I like it, but this quarter’s budget is frozen.” | Explore timing or scope; do not argue abstract value. |
| “Why did you charge my card twice?” | Route to billing resolution; price-objection Skill must not load. |
| “My manager signs anything above €5,000.” | Clarify approval process and criteria. |
| “I cannot afford groceries, but I want the premium plan.” | Do not persuade; recommend against purchase or a safe alternative. |
| Prospect asks “How much?” before needs are discussed. | Answer transparently according to business policy; do not automatically label it an objection. |
| Seller has no evidence for claimed savings. | Do not make the claim; revise the offer or disengage. |

### Live example

**User:** “A supplier prospect replied, ‘Your package is too expensive compared with the freelancer we use.’ What should I say?”

**Assistant routing:** pre-purchase, explicit competitor comparison, low immediate risk, enough information for a first response. No biography is needed.

**Suggested response:**

> “That is fair to compare. To make sure we compare the same thing, which parts of the freelancer’s scope and terms matter most to you—deliverables, turnaround, support, or total cost?”

The next branch depends on the answer. The assistant should not dump features, disparage the freelancer, or discount before learning whether the offers are genuinely comparable.

## Main risks

### Synthetic monoculture

One model can reproduce its own stereotypes across generator, simulator, and judge. Use independent calls, varied models, counterfactual twins, human calibration, and real traces as they become available. Synthetic cases should expand coverage, never certify reality by themselves.

### False source authority

A fluent synthesized rule may appear to come from a book even when it does not. Block production unless action clauses resolve to actual edition-specific spans, and label all synthesis visibly.

### Over-triggering

If Skill descriptions are broad—“use for sales”—Claude may invoke them in unrelated cases. Include observable positive cues and explicit exclusions in frontmatter, then test near-neighbor negatives.

### Under-triggering

Users often imply a situation without naming it. Store natural-language paraphrases, hidden-state scenarios, multilingual cues, and behavior descriptions rather than relying only on labels such as “price objection.”

### Book conflict and cargo culting

Two respected books can encode different goals, markets, or moral assumptions. Preserve context and conflicts; do not merge based on similar wording. A technique that worked in one author’s examples may have no established causal effect.

### Health and OCD harm

Self-help cards can become reassurance, diagnosis, ritual support, or avoidance. Put health safety rules above book instructions, ground OCD support in established guidance, limit the assistant’s role, and escalate when severity, risk, medication, or treatment changes are involved.[43][4]

### Manipulative persuasion

Sales techniques can become coercive when the customer is vulnerable, the evidence is weak, or urgency is manufactured. Non-deception, informed choice, and “no sale” must be valid outcomes.

### Privacy

Profiles, rehearsal transcripts, OCD material, nutrition data, and outcomes are sensitive. Minimize collection, separate identity from eval data, encrypt storage, define retention, and require explicit consent before mining conversations or artifacts.

### Evaluation overfitting

Optimizing only to generated tests can produce a system that recognizes the test author’s wording. Keep held-out generators, mutate phrasing, add real cases, monitor live false positives, and periodically rebuild the holdout set.

## Recommended first build

The cheapest useful version is not “process all 90 books.” It is:

1. Three representative books
2. Thirty to fifty situation cards
3. Ten production-quality technique cards
4. Five Claude Code Skills
5. Two hundred mixed positive, negative, and contrastive scenarios
6. Twenty to forty human-labeled golden routing cases
7. One five-minute daily rehearsal queue
8. A weekly review of false matches, source failures, and real outcomes

Only after this loop works should the corpus expand. The unit of progress is not books summarized; it is **a situation correctly recognized, a grounded action selected, a contraindication respected, and a skill rehearsed well enough to use when the situation finally occurs**.