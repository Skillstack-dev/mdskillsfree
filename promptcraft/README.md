# Prompt Engineering Skill

> Transforms raw user input into structured, production-ready prompts optimized for LLM performance.
> Works across Claude, ChatGPT, Gemini, and any OpenAI-compatible agent.

---

## What This Skill Does

Takes any vague, partial, or underspecified request and returns a structured prompt using a
consistent 5-part framework: **ROLE → TASK → CONTEXT → CONSTRAINTS → OUTPUT FORMAT**.

Includes token compression, prompt debugging, multi-step chain building, and domain-specific
optimization for writing, coding, UX, research, and business tasks.

---

## File Structure

```
prompt-engineering/
├── SKILL.md                    ← Entry point. Read this first.
├── skill.json                  ← Metadata, inputs/outputs, module index
├── meta-prompt.txt             ← Core transformation engine
├── README.md                   ← This file
│
├── modules/
│   ├── intent.md               ← Extracts the real action from vague input
│   ├── role.md                 ← Maps task type to optimal AI persona
│   ├── compress_debug.md       ← Token compression + prompt failure diagnosis
│   └── chain.md                ← Multi-step prompt sequencing
│
├── examples/
│   └── transformations.md      ← 5 full before/after prompt transformations
│
└── references/                 ← Domain-specific rules (extend as needed)
    └── [writing|coding|ux|research|business].md
```

---

## Quick Start

**Input:** Give any raw request
**Output:** Structured prompt + score + key changes + usage note

**Trigger phrases:**
- "Write me a prompt for..."
- "My prompt isn't working..."
- "Help me ask Claude to..."
- "Create a system prompt that..."
- "Improve this prompt: [paste]"

---

## Framework

```
ROLE        Who the AI is — expert persona that narrows response distribution
TASK        Single imperative sentence — one action, no "and"
CONTEXT     2-4 sentences of essential background only
CONSTRAINTS Numbered rules: format, tone, length, exclusions, quality bar
OUTPUT      Exact structure of the response — headers, length, format
```

---

## Prompt Patterns

| Use Case | Pattern |
|---|---|
| Simple | ROLE + TASK + OUTPUT |
| Standard | ROLE + TASK + CONTEXT + CONSTRAINTS + OUTPUT |
| Multi-step | See `modules/chain.md` |
| System prompt | IDENTITY + CAPABILITIES + BOUNDARIES + VOICE |
| Debug mode | ORIGINAL + FAILURE MODE + FIXED VERSION + REASON |

---

## Design Principles

1. **Minimal tokens, maximum clarity** — every word earns its place
2. **Deterministic structure** — same framework every time, regardless of domain
3. **Works without context** — prompts are self-contained; no prior conversation needed
4. **Role justifies itself** — only add a persona if it changes the output
5. **Constraints over hope** — explicit rules beat implicit expectations every time

---

## Compatible Agents

| Agent | Notes |
|---|---|
| Claude (all) | Full support; role prompting highly effective |
| GPT-4 / GPT-4o | Full support; explicit OUTPUT FORMAT improves JSON reliability |
| Gemini 1.5 Pro | Full support; add "Think step by step" for complex reasoning tasks |
| Open-source (Llama, Mistral) | Use simpler ROLE; avoid complex constraint lists |

---

## Extending the Skill

To add a new domain:
1. Create `references/[domain].md` with domain-specific rules
2. Add a row to the Domain Routing table in `SKILL.md`
3. Add one example to `examples/transformations.md`

To add a new module:
1. Create `modules/[name].md` with Responsibility + Process + Output sections
2. Register in `skill.json` modules array
3. Add a row to the Module Responsibilities table in `SKILL.md`
