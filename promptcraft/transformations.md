# Prompt Engineering Examples
## 5 Transformations: Vague Input → Structured Prompt

---

## Example 1: Writing

**Raw Input:**
> "Write something about productivity for my newsletter"

**Prompt Score:** Weak — no audience, no angle, no format, no length

**Structured Prompt:**
```
ROLE: Senior content strategist who writes for knowledge worker audiences and specializes in
actionable, research-backed productivity writing.

TASK: Write a newsletter section on one underrated productivity habit most professionals ignore.

CONTEXT: Audience is busy mid-career professionals (30-45) who read during commutes. They are
skeptical of generic advice and respond to specificity and counterintuitive framing.

CONSTRAINTS:
- Lead with a surprising or counterintuitive claim
- Back with one concrete mechanism (why it works)
- One real-world implementation example
- No listicles, no bullet points — prose only
- Max 280 words
- Do not use: "game-changer", "unlock", "supercharge"

OUTPUT FORMAT:
Hook (1-2 sentences) → Core argument (2-3 sentences) → Implementation (3-4 sentences) →
Closing line that creates desire to try it
```

**Key Changes:** Added expert role; specified audience psychology; constrained format to prose;
set word limit; banned clichés; defined narrative arc.

---

## Example 2: Coding

**Raw Input:**
> "Help me write a function to parse dates"

**Prompt Score:** Partial — no language, no input format, no error handling spec

**Structured Prompt:**
```
ROLE: Staff Python engineer who writes production-quality, well-documented utility functions.

TASK: Write a Python function that parses date strings in multiple formats into a standardized
ISO 8601 datetime object.

CONTEXT:
- Input strings may be: "Jan 5, 2024", "2024-01-05", "01/05/24", "5th January 2024"
- Function will be used in a data pipeline processing user-submitted form data
- Python 3.10+, no external libraries beyond the standard library

CONSTRAINTS:
- Handle all 4 input formats listed above
- Raise ValueError with descriptive message for unrecognized formats
- Include type hints (input: str, output: datetime)
- Include docstring with Args, Returns, Raises, and one Example
- No regex — use datetime.strptime or dateutil patterns only
- Max 40 lines including docstring

OUTPUT FORMAT:
Python code block only. No explanation outside the docstring.
```

**Key Changes:** Specified language and version; defined all input formats explicitly; set library
constraint; required type hints + docstring; capped length; isolated code from prose.

---

## Example 3: UX / Design

**Raw Input:**
> "Help me design the onboarding for my app"

**Prompt Score:** Weak — no product type, no user, no deliverable type

**Structured Prompt:**
```
ROLE: Lead UX Designer at a B2B SaaS company with deep expertise in onboarding flows that
reduce time-to-value for non-technical users.

TASK: Design a 4-step onboarding flow for a project management tool targeting first-time users
who are non-technical team leads.

CONTEXT:
- Product: web-based project management tool (Notion/Asana-level complexity)
- User: team lead, 35-50 years old, non-technical, managing 5-15 people
- Goal: get user to create their first project and invite one team member within 10 minutes
- Platform: desktop web, responsive mobile secondary

CONSTRAINTS:
- Maximum 4 steps — no carousels or tutorial walls
- Each step must have one clear action (not "explore" or "learn")
- Use progressive disclosure: don't show advanced features in onboarding
- Must include an explicit skip option on every step
- Accessibility: keyboard navigable, no color-only indicators

OUTPUT FORMAT:
For each step provide:
- Step name
- Screen description (2-3 sentences, no wireframe notation)
- Primary CTA text
- What user accomplishes
- Micro-copy note (1 sentence of help text or tooltip)

End with: 2-sentence rationale for the flow structure chosen.
```

**Key Changes:** Defined product type; specified user persona precisely; set measurable success
condition; capped steps; required skip affordance; structured per-step output format.

---

## Example 4: Research

**Raw Input:**
> "Tell me about the impact of remote work"

**Prompt Score:** Weak — no scope, no depth, no angle, no format

**Structured Prompt:**
```
ROLE: Research analyst specializing in future-of-work trends with expertise in synthesizing
academic and industry data for executive audiences.

TASK: Analyze the measurable impact of remote work adoption on employee productivity,
retention, and company real estate costs since 2020.

CONTEXT:
- Audience: C-suite executives evaluating a return-to-office policy decision
- They need data to make a decision, not a cultural opinion piece
- Scope: large companies (500+ employees) in knowledge-work industries
- Time frame: 2020–2024

CONSTRAINTS:
- Lead each section with a quantified finding (%, $, ratio)
- Cite finding type (academic study / industry survey / company report) — no specific citations needed
- Acknowledge conflicting data where it exists; do not paper over it
- Exclude: anecdote, personal opinion, generic statements without data backing
- Max 500 words

OUTPUT FORMAT:
## Executive Summary (3 sentences, key number in each)
## Productivity (2-3 quantified findings + one counterpoint)
## Retention (2-3 quantified findings + one counterpoint)
## Real Estate Costs (2-3 quantified findings)
## Key Tension (1 paragraph — where the evidence is genuinely split)
```

**Key Changes:** Named the decision context; scoped the research precisely; required quantified
leads; forced acknowledgment of conflicting data; structured as executive briefing.

---

## Example 5: Business

**Raw Input:**
> "Write a business case for hiring a designer"

**Prompt Score:** Partial — no audience, no company context, no format

**Structured Prompt:**
```
ROLE: Senior management consultant who specializes in making the ROI case for design investment
to non-design executive stakeholders.

TASK: Write a business case memo recommending the hire of a first in-house UX designer at a
50-person B2B SaaS startup currently using freelancers.

CONTEXT:
- Audience: CEO and CFO with engineering and sales backgrounds; skeptical of design as a cost
- Current state: design is outsourced to 2 freelancers at ~$8,000/month total
- Company pain: inconsistent UI, slow design turnaround (2-week freelancer lag), no design
  system
- Strategic context: preparing for Series A in 12 months; product polish matters to investors

CONSTRAINTS:
- Lead with business outcome, not design value
- Every claim must connect to revenue, retention, or speed
- Include a rough cost comparison (in-house vs. freelancer status quo)
- Acknowledge the risk (hire takes 3 months to ramp)
- Tone: direct, data-oriented, no design jargon
- Max 400 words

OUTPUT FORMAT:
## Recommendation (2 sentences)
## Problem (current state cost in time + money)
## Proposed Solution (what the hire does, not what design is)
## ROI Case (3 numbered business outcomes with rough estimates)
## Cost Comparison (simple table: freelancer vs. in-house, Year 1)
## Risk & Mitigation (1 paragraph)
## Decision Ask (1 sentence)
```

**Key Changes:** Defined the skeptical audience explicitly; grounded in real numbers; framed as
ROI not design advocacy; required cost table; included risk acknowledgment; set word limit.
