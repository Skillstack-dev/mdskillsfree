# Extensions — Skill Creator

> Upgrade paths organized by complexity. Each extension is independently adoptable.

---

## Tier 1 — Drop-In Enhancements (Low effort, high value)

### 1.1 Skill Versioning
Add semantic version tracking to all generated packages.
- Add `previous_versions` array to schema
- Diff-based update mode: user provides existing skill, agent outputs only changes
- Changelog auto-generation from diffs

### 1.2 Multilingual Output
Generate skill packages in non-English languages.
- Add `language` parameter to input schema
- All user-facing text (README, examples) localized
- System prompts kept in English for model reliability

### 1.3 Domain Templates
Pre-built scaffolds for common domains — faster generation, higher accuracy.

| Domain | Pre-filled elements |
|---|---|
| Legal | NDA clauses, jurisdiction fields, liability scoring |
| Medical | ICD-10 code fields, clinical trial phases, contraindication checks |
| UX Design | WCAG dimensions, heuristic scoring, component library references |
| Finance | Regulatory fields, risk scoring, currency handling |
| Engineering | Test case generation, error code taxonomy, SLA fields |

---

## Tier 2 — Multi-Agent Mode

### 2.1 Parallel Layer Processing
Instead of sequential layer processing, spawn one subagent per layer:

```
Orchestrator → Layer 1 Agent (Intent)
            → Layer 2 Agent (Architecture)   [parallel]
            → Layer 3 Agent (Prompt Writing)
            → Layer 4 Agent (Schema Design)  [parallel]
            → Layer 5 Agent (Examples)
            → Evaluator Agent
```

**Result**: ~40% faster for complex skills with HIGH token budget.

### 2.2 Adversarial Review Mode
After generation, spawn an "adversarial agent" that tries to break the generated skill:
- Inputs designed to produce schema violations
- Edge cases designed to confuse the core prompt
- Results fed back to refine the skill before shipping

### 2.3 Blind A/B Comparison
Generate two variants of the core prompt; evaluate both against test cases; ship the winner.
Pattern from `agents/comparator.md`.

---

## Tier 3 — Tool Integrations

### 3.1 RAG Integration
Connect to a skill library (vector database) to:
- Check for existing similar skills before generating (avoid duplication)
- Pull reference patterns from high-performing existing skills
- Auto-suggest `reuse_components` based on semantic similarity

**Setup**:
```json
{
  "tools": ["vector_search"],
  "skill_library_url": "https://your-skill-db.example.com",
  "similarity_threshold": 0.85
}
```

### 3.2 GitHub Integration
Automatically commit generated skill packages:
- Creates a new branch per skill
- Commits all files with conventional commit messages
- Opens a PR with README as the PR description
- Assigns reviewers based on domain tag

### 3.3 Skill Registry (skills.sh compatible)
Publish generated skills to a registry:
- Package as `.skill` file format
- Generate registry metadata (tags, domain, compatibility, version)
- Upload to registry with API key

### 3.4 Testing Pipeline Integration
Connect generated skills to automated evaluation:
- CI/CD trigger: on skill update → run eval suite
- Slack/Teams notification with eval scores
- Automatic rollback if overall_score drops below 3.5

---

## Tier 4 — Domain-Specific Adaptations

### 4.1 Code-Aware Skills
For engineering teams:
- Generate skills that operate on code files (not just text)
- Add language-specific output schemas (Python, TypeScript, SQL)
- Include AST-aware field extraction patterns

### 4.2 Real-Time Streaming Skills
For applications requiring live output:
- Modify output schema to support streaming (partial outputs)
- Chunk large outputs by layer
- First token latency optimization guidance

### 4.3 Memory-Augmented Skills
For agents with persistent memory:
- Add `memory_hooks` to skill design (what to remember, what to forget)
- Long-running skill sessions with state management
- Cross-conversation skill state retrieval

---

## Tier 5 — Platform-Specific Builds

### 5.1 LangChain Tool Wrapper
Auto-generate a LangChain `Tool` wrapper from the skill package:
```python
# Auto-generated
from langchain.tools import Tool
skill_tool = Tool(
    name="meeting-action-extractor",
    description=skill_md_description,
    func=lambda x: call_claude_with_skill(x, core_prompt)
)
```

### 5.2 OpenAI Function Definition
Convert skill schema to OpenAI function-calling format:
```json
{
  "name": "meeting_action_extractor",
  "description": "...",
  "parameters": { ... }  // auto-converted from schema.json
}
```

### 5.3 Claude Tool Use Format
Convert skill to Claude tool_use format with input_schema auto-populated from schema.json.

---

## Requested Extensions Log

Track feature requests here as the skill evolves:

| Extension | Requester | Priority | Status |
|---|---|---|---|
| Figma plugin integration | Design teams | Medium | Planned |
| Skill deprecation workflow | Platform team | Low | Backlog |
| Automated trigger testing | QA teams | High | In progress |
