# 🧠 Skill Creator — AI Skill Package

> A production-ready meta-skill for designing, generating, and validating reusable AI skills across Claude, ChatGPT, and other LLM agents.

---

## What This Skill Does

The **Skill Creator** takes a plain-language description of a capability you want an AI agent to have, and produces a complete, structured, immediately-deployable skill package — including reasoning prompts, output schemas, examples, evaluation rubrics, and token optimization strategies.

Think of it as a **compiler for AI behavior**: you describe intent, it produces structured instructions.

---

## When TO Use This Skill

| Trigger Phrase | Example |
|---|---|
| "Create a skill for..." | "Create a skill for extracting action items from meeting notes" |
| "I want Claude to always..." | "I want Claude to always respond in a structured JSON format for legal queries" |
| "Turn this workflow into a skill" | (after demonstrating a multi-step process) |
| "Build a reusable prompt for..." | "Build a reusable prompt for competitor analysis" |
| "Package this as a skill" | Any repeated, well-defined task |

## When NOT TO Use This Skill

- For one-off, single-use tasks with no reuse potential
- When the output is entirely subjective (e.g., "make this poem more beautiful")
- When the user just needs a quick answer, not a system
- When the task is too vague to parameterize

---

## Input Expectations

The skill accepts a natural language description containing:

| Field | Required | Description |
|---|---|---|
| `skill_name` | ✅ | Short identifier, kebab-case preferred |
| `skill_purpose` | ✅ | One sentence describing what the skill does |
| `use_cases` | ✅ | 1–5 concrete scenarios |
| `output_format` | ⬜ Optional | JSON / Markdown / Plain text |
| `domain` | ⬜ Optional | Legal, Medical, Engineering, General |
| `token_budget` | ⬜ Optional | Low / Medium / High |

---

## Output Structure Overview

```
skill-package/
├── README.md              ← This file: human-readable overview
├── SKILL.md               ← Triggering metadata + core instructions
├── core.prompt.md         ← Layered reasoning prompt
├── schema.json            ← Strict output schema
├── token.md               ← Token optimization strategy
├── evaluation.md          ← Quality rubric (1–5 scale)
├── extensions.md          ← Upgrade paths and integrations
├── examples/
│   ├── example_1.json     ← Simple use case
│   └── example_2.json     ← Complex use case
├── agents/
│   ├── grader.md          ← Evaluation subagent instructions
│   └── analyzer.md        ← Output analysis subagent
└── references/
    └── schemas.md         ← JSON schema documentation
```

---

## Example Use Cases

1. **Meeting Intelligence** — "Create a skill that extracts tasks, owners, and deadlines from meeting transcripts"
2. **Design Review** — "Create a skill that evaluates UI designs against WCAG accessibility standards"
3. **Legal Drafting** — "Create a skill for generating NDA clauses from deal parameters"
4. **Competitor Analysis** — "Create a skill that structures competitive intelligence from web research"
5. **Onboarding Automation** — "Create a skill that generates personalized onboarding plans from a job role description"

---

## Compatibility

- ✅ Claude (all versions)
- ✅ GPT-4 / GPT-4o
- ✅ Gemini Pro / Ultra
- ✅ Any OpenAI-compatible API
- ✅ LangChain / LlamaIndex agent frameworks
- ✅ Multi-agent systems (spawnable as subagent)
