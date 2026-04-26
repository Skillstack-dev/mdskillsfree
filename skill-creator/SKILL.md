---
name: skill-creator
description: >
  Generates complete, production-ready AI skill packages from a plain-language
  description of desired agent behavior. Use this skill whenever the user says
  "create a skill", "build a reusable prompt", "turn this into a skill",
  "I want Claude to always do X", or "package this workflow". Also trigger when
  a user demonstrates a multi-step workflow and wants to systematize it. This
  skill produces the full package: README, prompt, schema, examples, evals, and
  token strategy — immediately deployable, no edits required.
compatibility:
  tools: [bash, create_file, present_files]
  optional: [web_search, conversation_search]
---

# Skill Creator

## Core Workflow

Follow this sequence precisely. Do not skip steps.

### Step 1 — Capture Intent

Before writing anything, extract from the user (or from conversation history if available):

1. **Skill name** — what should this be called? (kebab-case)
2. **Purpose** — single sentence: what does this skill enable?
3. **Use cases** — 2–5 specific scenarios with concrete inputs/outputs
4. **Output format** — JSON / Markdown / Plain text / Mixed
5. **Constraints** — domain rules, tone, length limits, required fields
6. **Trigger conditions** — what user phrases should activate this skill?

If any of the above are missing or ambiguous, ask targeted questions before proceeding. Never guess on purpose — it's the foundation everything else builds on.

### Step 2 — Research & Architecture

Before writing files:
- Check if a similar skill already exists (search conversation history or filesystem)
- Identify the reasoning pattern: Is this extractive? Generative? Evaluative? Decision-making?
- Choose the right output schema structure
- Decide token mode: Low (compressed) / Medium (standard) / High (full reasoning)

### Step 3 — Generate the Skill Package

Generate ALL files in this order. Each file depends on the one before it.

```
1. README.md         → Human overview, when to use, examples
2. SKILL.md          → Triggering metadata (this file pattern)
3. core.prompt.md    → Layered reasoning prompt
4. schema.json       → Strict output schema
5. examples/         → example_1.json (simple), example_2.json (complex)
6. evaluation.md     → Quality rubric
7. token.md          → Token optimization strategy
8. extensions.md     → Upgrade paths
```

### Step 4 — Self-Test

After generating, run a mental simulation:
- Would the core prompt produce the schema output given example_1 input?
- Does the schema cover all fields referenced in the prompt?
- Is evaluation.md specific enough to score real outputs?

Fix any inconsistencies before presenting to the user.

### Step 5 — Package & Present

```bash
# Create the output archive
zip -r skill-{name}.zip skill-{name}/
```

Present files to the user with `present_files`. Show the folder structure clearly.

---

## File Writing Standards

### SKILL.md (for the skill being created)
- YAML frontmatter: `name`, `description`, `compatibility`
- Description must be "trigger-pushy" — include specific phrases users might say
- Body under 500 lines; use `references/` for overflow

### core.prompt.md
- Use Layer 1 → Layer N structure (see core.prompt.md in this package)
- Each layer has: Input → Processing → Output contract
- No fluff. Every sentence must instruct, not describe.

### schema.json
- Use JSON Schema draft-07
- All fields: `type`, `description`, `required`
- Include `scoring` sub-object for evaluative skills

### examples/
- Must strictly validate against schema.json
- example_1: single-domain, minimal inputs
- example_2: multi-domain, edge case inputs, complex output

---

## Quality Gates

Before calling a skill "done", verify:

| Gate | Check |
|---|---|
| Schema coherence | Every prompt output field exists in schema |
| Example validity | Both examples parse against schema |
| Trigger coverage | Description includes 3+ trigger phrases |
| Token efficiency | Prompt has no redundant instructions |
| Eval specificity | Rubric has measurable criteria, not vague adjectives |

---

## Reference Files

- `references/schemas.md` — JSON Schema patterns for common skill types
- `references/prompt-patterns.md` — Proven layered reasoning patterns
- `agents/grader.md` — Subagent for scoring outputs
- `agents/analyzer.md` — Subagent for diagnosing skill failures
