# Token Optimization Strategy — Skill Creator

> Designed for high-frequency, production-scale deployments where cost and latency matter.

---

## Budget Tiers

| Tier | Token Range | Use When |
|---|---|---|
| **LOW** | < 800 tokens | Rapid prototyping, high-volume pipelines, cost-sensitive deployments |
| **MEDIUM** | 800–2,000 tokens | Standard production use — balances depth with efficiency |
| **HIGH** | 2,000–5,000 tokens | One-time skill generation, complex multi-domain skills, onboarding |

---

## LOW Mode (Compressed)

**What to remove:**
- README.md (skip entirely — human-only artifact)
- All prose explanations in skill_md (keep only YAML frontmatter + numbered steps)
- example_2 (include only example_1)
- extensions.md (skip)
- evaluation.md narrative (replace with rubric table only)
- `justification` fields in evaluation dimensions (scores only)

**What to keep:**
- YAML frontmatter (name, description, trigger_phrases)
- core.prompt.md (all steps — never compress the reasoning prompt itself)
- schema.json (full — never truncate the schema)
- example_1 (complete)

**Compressed system prompt (LOW mode):**
```
Skill Engineer. Task: generate skill package for {skill_name}: {skill_purpose}.
Output JSON with keys: skill_md (YAML + steps only), core_prompt (numbered steps),
schema (full JSON Schema), example (one valid pair), eval_scores (5 dimensions, scores only).
No prose. All fields required. Schema must be valid JSON Schema draft-07.
```

**Estimated token savings: ~60% vs HIGH mode**

---

## MEDIUM Mode (Standard)

**What to include:** Everything except README.md and extensions.md

**What to compress:**
- core.prompt.md: Remove template scaffolding, keep only the final prompt text
- evaluation.md: Include rubric table but skip score-calculation formula prose
- token.md: Reference this file rather than reproducing it

**Standard system prompt (MEDIUM mode):**
```
You are an AI Skill Engineer. Generate a complete skill package for the specification below.
Include: SKILL.md (YAML + workflow), core.prompt.md (layered steps), schema.json (full),
2 examples (simple + complex), evaluation.md (rubric table), token.md (3 tiers defined).
Output as a single JSON object. All values are strings except schema (object) and examples (objects).
Specification: {input}
```

---

## HIGH Mode (Full Reasoning)

**Include everything.** No truncation.

**Additional in HIGH mode:**
- Chain-of-thought reasoning visible per layer
- Ambiguity flags with resolution options
- Multiple schema variants if the use case is ambiguous
- Subagent coordination plan if required

**When to use HIGH mode:**
- First-time skill creation (invest in quality)
- Skills with complex multi-domain logic
- Skills that will be used >1,000 times (amortize the upfront token cost)

---

## Prompt Compression Techniques

### 1. Role Compression
Instead of:
> "You are an expert AI Skill Engineer with deep knowledge of prompt engineering, JSON Schema, multi-agent systems, and token optimization..."

Use:
> "You are an AI Skill Engineer."

**Savings: ~30 tokens per call**

### 2. Instruction Density
Instead of:
> "Please make sure to carefully read the entire input before you begin generating the output. It's important that you..."

Use:
> "Read full input before output."

**Savings: ~15 tokens per instruction**

### 3. Schema Reference vs. Inline
Instead of repeating the full schema in every prompt, assign it an ID:

```json
{ "schema_ref": "skill-creator/schema.json@1.0" }
```

Then inject only on first call; subsequent calls reference by ID.

**Savings: ~200–400 tokens per repeat call**

### 4. Example Compression
In LOW mode, examples can be represented as diff objects:
```json
{
  "example_2_delta": {
    "_base": "example_1",
    "input.skill_purpose": "New purpose here",
    "output.intent.reasoning_type": "HYBRID"
  }
}
```

### 5. Field Aliasing (Extreme Compression)
For ultra-low-token environments, alias long field names:
```
sn = skill_name
rt = reasoning_type
tf = trigger_phrases
```
Provide alias table once; use codes in all subsequent calls.

---

## Caching Strategy

| Content | Cache? | TTL |
|---|---|---|
| WCAG reference table | ✅ Yes | Indefinite |
| JSON Schema draft-07 spec | ✅ Yes | Indefinite |
| Trigger phrase examples | ✅ Yes | 30 days |
| Generated examples | ⬜ Per-skill | Per session |
| Core prompts | ⬜ Per-skill | Per session |

---

## Token Budget by File

| File | HIGH (tokens) | MEDIUM | LOW |
|---|---|---|---|
| README.md | ~400 | — | — |
| SKILL.md | ~300 | ~200 | ~100 |
| core.prompt.md | ~500 | ~400 | ~300 |
| schema.json | ~400 | ~400 | ~400 |
| example_1.json | ~300 | ~300 | ~300 |
| example_2.json | ~400 | ~400 | — |
| evaluation.md | ~300 | ~200 | ~100 |
| token.md | ~300 | ~150 | — |
| extensions.md | ~200 | — | — |
| **Total** | **~3,100** | **~2,050** | **~1,200** |
