# Evaluation Criteria — Skill Creator

> This document defines how to score the output of the Skill Creator skill. Apply this rubric to every generated skill package before marking it `READY`.

---

## Scoring Scale

| Score | Label | Meaning |
|---|---|---|
| **5** | Excellent | Exceeds expectations. No changes needed. |
| **4** | Good | Minor gaps. Ship with small improvements. |
| **3** | Acceptable | Functional but incomplete. Requires revision. |
| **2** | Poor | Major gaps. Do not ship without rework. |
| **1** | Fail | Non-functional or wrong. Start over. |

---

## Evaluation Dimensions

### 1. Schema Coherence
*Does the output schema perfectly mirror what the core prompt produces?*

| Score | Criteria |
|---|---|
| 5 | Every field the prompt references exists in schema. All types match. No orphan fields. |
| 4 | 1–2 minor field mismatches (e.g., wrong type, missing optional field). |
| 3 | Schema present but missing 3–5 fields the prompt outputs. |
| 2 | Schema structure doesn't match prompt output pattern. |
| 1 | No schema, or schema is invalid JSON. |

**Auto-disqualifier**: Schema fails JSON Schema validation → Score = 1.

---

### 2. Trigger Coverage
*Will the skill activate for all the scenarios it should?*

| Score | Criteria |
|---|---|
| 5 | 5+ distinct trigger phrases, covering varied phrasings and contexts. |
| 4 | 3–4 trigger phrases covering main use cases. |
| 3 | 2 trigger phrases, or phrases are too similar (paraphrases of each other). |
| 2 | 1 trigger phrase, or phrases don't match realistic user language. |
| 1 | No trigger phrases defined. |

**Test**: For each trigger phrase, ask: "Would a non-technical user actually say this?"

---

### 3. Example Validity
*Do the examples correctly demonstrate and validate the skill?*

| Score | Criteria |
|---|---|
| 5 | Both examples: realistic inputs, outputs parse against schema, show different complexity levels, demonstrate edge case handling. |
| 4 | Both examples valid, but similar complexity or one edge case missing. |
| 3 | One example valid; the other has schema violations or unrealistic data. |
| 2 | Examples present but neither validates against schema. |
| 1 | No examples, or examples contain placeholder/nonsense data. |

**Auto-disqualifier**: Either example contains `"foo"`, `"bar"`, `"test"`, or similar dummy values → Requires revision.

---

### 4. Reasoning Quality
*Does the core prompt produce reliable, correct outputs?*

| Score | Criteria |
|---|---|
| 5 | Layered structure clear. Each step has action verb + object + constraint. No ambiguity in instructions. Output format explicitly stated. |
| 4 | Mostly clear. 1–2 steps slightly vague or missing constraints. |
| 3 | Prompt present but written as prose paragraphs instead of steps. Outputs not explicitly defined. |
| 2 | Prompt is too short (<5 instructions) or too generic to be skill-specific. |
| 1 | No prompt, or prompt contradicts the schema. |

---

### 5. Token Efficiency
*Is the skill designed to minimize token waste?*

| Score | Criteria |
|---|---|
| 5 | LOW/MEDIUM/HIGH modes defined. Specific fields identified for truncation. Caching opportunities noted. |
| 4 | Two modes defined. General compression advice given. |
| 3 | One mode with vague compression advice ("shorten if needed"). |
| 2 | Token strategy mentioned but no actionable guidance. |
| 1 | No token strategy. |

---

### 6. Completeness
*Are all required files present and non-empty?*

| File | Required | Check |
|---|---|---|
| README.md | ✅ | Has: name, when-to-use, when-NOT-to-use, input/output overview |
| SKILL.md | ✅ | Has: YAML frontmatter with name + description + workflow |
| core.prompt.md | ✅ | Has: layered steps, output format instruction |
| schema.json | ✅ | Valid JSON Schema, all required fields typed |
| example_1.json | ✅ | Simple, valid, realistic |
| example_2.json | ✅ | Complex, valid, demonstrates different capability |
| evaluation.md | ✅ | This file — rubric with measurable criteria |
| token.md | ✅ | At least LOW + MEDIUM mode defined |
| extensions.md | ✅ | At least 2 upgrade paths described |

**Scoring**:
- All 9 files present and non-empty → 5
- 7–8 files → 4
- 5–6 files → 3
- 3–4 files → 2
- < 3 files → 1

---

## Overall Score Calculation

```
Overall = (Schema + Triggers + Examples + Reasoning + Efficiency + Completeness) / 6
```

| Overall | Recommendation |
|---|---|
| 4.5–5.0 | ✅ READY — Deploy immediately |
| 3.5–4.4 | 🔄 NEEDS_REVIEW — Minor fixes, re-score |
| 2.0–3.4 | ⚠️ INCOMPLETE — Significant revision required |
| < 2.0 | ❌ FAIL — Regenerate from scratch |

---

## Automatic Disqualifiers

Any of the following → package is NOT shippable regardless of score:

- [ ] Schema fails JSON Schema validation
- [ ] Either example contains dummy placeholder values
- [ ] Core prompt has fewer than 5 distinct instructions
- [ ] SKILL.md frontmatter is missing `name` or `description`
- [ ] Trigger phrases include fewer than 3 distinct phrasings
- [ ] Prompt instructions contradict schema fields

---

## Evaluator Notes

When using this rubric, record your reasoning per dimension, not just the score. A score without justification is not actionable. The goal is a skill that any AI agent can pick up and deploy correctly, with no additional context from its creator.
