# Module: Role Selector

## Responsibility
Match the task type to the optimal AI persona. A well-chosen role narrows the model's
response distribution — it produces more expert, consistent, and contextually appropriate output.

## Role Selection Matrix

| Task Type | Optimal Role |
|---|---|
| Technical writing | Senior Technical Writer with experience in [industry] documentation |
| Code generation | Staff Software Engineer specializing in [language] at a [company type] |
| UX copy / flows | Lead UX Designer at a [product type] company with accessibility focus |
| Marketing copy | Senior Brand Copywriter with [tone] voice expertise |
| Research synthesis | Research Analyst with background in [domain] |
| Business strategy | Senior Management Consultant specializing in [industry] |
| Data analysis | Data Scientist with expertise in [domain] metrics |
| Educational content | Curriculum Designer with expertise in [subject] for [audience level] |
| Legal / compliance | [Domain] Compliance Specialist (add: "Do not provide legal advice") |
| Product management | Senior PM with experience shipping [product type] |

## Role Construction Rules

**Structure:** `[Seniority] [Title] with [N] years of experience in [specific niche]`

**Seniority signals:**
- `Senior` / `Lead` — adds depth and precision
- `Principal` / `Staff` — adds systems thinking
- `Founding` — adds scrappiness and pragmatism
- Omit seniority for factual/neutral tasks

**Niche specificity matters:**
- Weak: "You are an expert writer"
- Strong: "You are a Senior UX Writer at a B2B SaaS company who specializes in onboarding flows"

**When to skip the role:**
- Pure factual lookup (no persona needed)
- Simple format transformations (list → table)
- Math or logic tasks where persona adds no signal

## Voice Modifiers (append to role when relevant)

- "known for your ability to explain complex topics simply"
- "with a track record of shipping under tight deadlines"
- "who prioritizes user empathy over feature specs"
- "who writes for non-technical executive audiences"
