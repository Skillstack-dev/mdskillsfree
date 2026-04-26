# Compression Rules Reference

Full ruleset for the Prompt Compression Layer. Apply in order.

---

## Layer 1 — Filler Removal (always apply)

Remove these patterns with no replacement:

| Pattern | Example | Action |
|---------|---------|--------|
| Politeness openers | "Please could you kindly..." | DELETE |
| Self-referential context | "As an AI assistant..." | DELETE |
| Redundant affirmations | "Sure! Great question!" | DELETE |
| Sign-offs | "Let me know if you need anything else!" | DELETE |
| Hedge phrases | "I think maybe you might want to consider possibly..." | COMPRESS to verb |
| Restating the question | "So you want me to help you with X. I'll now help you with X." | DELETE second sentence |

---

## Layer 2 — Structural Compression

### 2a. Paragraph → Bullets
Convert multi-sentence instructions to numbered steps.

**Before:**
```
First, you should load the dataset. Then you need to clean it by removing null values. 
After that, you should normalize the numeric columns. Finally, split into train/test sets.
```

**After:**
```
1. Load dataset
2. Remove nulls
3. Normalize numeric columns
4. Split train/test
```
Savings: ~40%

### 2b. Prose → JSON Schema
When defining expected structure:

**Before:**
```
I want you to return the name of the person, their age, and the city they live in. 
These should be returned as separate pieces of information.
```

**After:**
```
Return: {"name": string, "age": int, "city": string}
```
Savings: ~55%

### 2c. Example Reduction
Keep max 2 examples. If 3+ examples exist, remove the most similar ones.

---

## Layer 3 — Semantic Compression

### 3a. Abbreviation Substitution
Define on first use, abbreviate after:

```
System prompt: "You are analyzing Customer Support Tickets (CST)."
Later: "Classify each CST by urgency."  ← not "customer support ticket"
```

### 3b. Implicit Context Removal
Don't repeat what's already in the system prompt:

**System prompt says:** "You are a Python expert."
**User prompt should NOT say:** "As a Python expert, please help me with..."

### 3c. Constraint Consolidation
Merge multiple constraint sentences:

**Before:**
```
Please keep your response concise. Don't be too long. Try to be brief. 
Avoid unnecessary details.
```

**After:**
```
Be concise.
```

---

## Layer 4 — Format Standardization

Use these standard blocks for common patterns:

### Task Definition Block
```
TASK: [verb] [object]
INPUT: [description or variable]
OUTPUT: [format]
CONSTRAINTS: [list]
```

### Code Review Block
```
REVIEW: [language] function below
FIND: [bugs | performance issues | style issues]
RETURN: [inline comments | summary list | fixed code]
[CODE]
```

### Data Extraction Block
```
EXTRACT from text:
- [field_1]: [type]
- [field_2]: [type]
Return JSON only.
[TEXT]
```

---

## Layer 5 — Redundant Instruction Removal

Flag and remove these common duplications:

| Redundancy Type | Example | Fix |
|----------------|---------|-----|
| Format + example | "Return as JSON. Example: {}" | Keep example, drop instruction |
| Length + format | "Be brief. Return 1 bullet." | Keep format, drop "be brief" |
| Role + task | "As an expert, give expert advice" | Drop role reference |
| Negative + positive | "Don't be vague. Be specific." | Keep positive only |

---

## Compression Scoring

After applying rules, score each prompt:

```
compression_ratio = compressed_tokens / original_tokens
```

| Ratio | Assessment |
|-------|------------|
| > 0.9 | Minimal compression — check for missed redundancy |
| 0.6–0.9 | Good — standard result |
| 0.4–0.6 | Aggressive — verify intent preserved |
| < 0.4 | Very aggressive — manual review required |

**Never compress below 0.3 without human review.**
