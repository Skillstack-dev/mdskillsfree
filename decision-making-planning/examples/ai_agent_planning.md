# Example: AI Agent Workflow Planning

**Scenario**: A team wants to automate their weekly competitive intelligence report. Currently 4 hours of manual work every Monday. They have access to Claude API, web scraping tools, and a Notion workspace. They must decide how to architect the agent workflow.

---

## DECISION: AI Agent Architecture for Competitive Intelligence

**Date**: 2024-Q3  
**Type**: Technical / Operational  
**Urgency**: Medium  
**Confidence**: High (technical constraints are well understood)

---

## Goal

Build an automated agent workflow that produces a weekly competitive intelligence report with <30 minutes of human review time, replacing 4 hours of manual work.

---

## Constraints

**Hard**
- Budget: ≤ $200/month API costs
- Must not hallucinate — all claims must be sourced
- Output must land in Notion (existing team workflow)
- Must run autonomously on Mondays at 8am

**Soft**
- Prefer minimal custom infrastructure (use existing tools)
- Report quality must match current manual quality (no regression)
- Should be extensible to other report types later

---

## Assumptions

| Assumption | Confidence | Risk if Wrong |
|-----------|-----------|--------------|
| Web scraping competitor sites is reliable | Medium | Rate limiting / site changes break pipeline |
| Claude can produce accurate summaries without hallucinating | High | Need citation enforcement in prompts |
| Notion API integration is straightforward | High | Low risk — well-documented |

---

## Options

### Plan A — Single Orchestrator Agent
One Claude agent runs the full pipeline: search → scrape → summarize → format → push to Notion.

**Strengths**: Simple architecture, easy to debug, single point of control  
**Weaknesses**: Long context = high token cost, all-or-nothing failure mode, hard to parallelize

### Plan B — Multi-Agent Pipeline (Specialist Agents)
Separate agents for each role:
- **Scout Agent**: Finds URLs to monitor (runs once, updates weekly)
- **Scraper Agent**: Fetches and cleans content from each source
- **Analyst Agent**: Summarizes and extracts insights per source
- **Editor Agent**: Synthesizes all insights into a formatted report
- **Publisher Agent**: Pushes to Notion with correct formatting

**Strengths**: Parallel execution (faster), each agent optimized for its task, failure isolated per step, extensible  
**Weaknesses**: More complex setup, inter-agent communication overhead, harder to debug initially

### Plan C — Human-in-the-Loop Hybrid
Agents handle research + summarization; human reviews and curates before publishing.

**Strengths**: High output quality, catches errors, lower trust requirement on AI  
**Weaknesses**: Doesn't achieve full automation goal, still requires ~60 min human time

---

## Evaluation

*Weights: Feasibility 20%, Impact 30%, Risk 25%, Cost 15%, Time 10%*

| Option | Feasibility (×0.20) | Impact (×0.30) | Risk (×0.25) | Cost (×0.15) | Time (×0.10) | **TOTAL** |
|--------|--------------------|--------------  |-------------|-------------|-------------|-----------|
| A — Single | 5 → 1.00 | 3 → 0.90 | 3 → 0.75 | 4 → 0.60 | 4 → 0.40 | **3.65** |
| B — Multi | 3 → 0.60 | 5 → 1.50 | 4 → 1.00 | 3 → 0.45 | 3 → 0.30 | **3.85** |
| C — Hybrid | 5 → 1.00 | 2 → 0.60 | 5 → 1.25 | 5 → 0.75 | 5 → 0.50 | **4.10** |

**Note**: Plan C scores highest on safety but fails the core goal (full automation). Exclude from final selection — it violates the impact requirement.

**Revised selection from Plans A and B**: Plan B (3.85 > 3.65)

---

## Selected Plan

**Winner**: Plan B — Multi-Agent Pipeline

**Why**: Parallelization reduces runtime from ~25 min to ~8 min. Failure isolation means one broken scraper doesn't kill the whole report. Extensible design means adding a new competitor source = adding one Scraper Agent instance, not rewriting the pipeline.

**Trade-off vs. Plan A**: More complex initial setup (~6 hours vs ~2 hours). Requires inter-agent shared context schema.

**Why acceptable**: One-time setup cost. The modular architecture pays back within the first month.

---

## Agent Architecture

```
SCHEDULER (cron: Monday 8am)
    ↓
SCOUT AGENT — reads competitor watchlist from Notion
    ↓ (list of URLs)
SCRAPER AGENTS × N — one per competitor, run in parallel
    ↓ (structured content per source)
ANALYST AGENTS × N — one per source, summarize + extract signals
    ↓ (insights per source)
EDITOR AGENT — synthesizes all insights, produces report draft
    ↓ (formatted report markdown)
PUBLISHER AGENT — writes to Notion, notifies Slack
    ↓
HUMAN REVIEW (< 30 min)
```

---

## Execution Steps

| # | Action | Owner | By When | Output |
|---|--------|-------|---------|--------|
| 1 | Define competitor watchlist + signal taxonomy | PM | Week 1 | Notion database schema |
| 2 | Build Scout + Scraper agents, test on 3 competitors | Eng | Week 1–2 | Working scrape pipeline |
| 3 | Build Analyst Agent with citation enforcement prompt | Eng | Week 2 | Summarization with sources |
| 4 | Build Editor + Publisher Agents, connect Notion API | Eng | Week 3 | End-to-end draft report |
| 5 | Run 2 full test cycles (Mon + Mon), compare to manual | PM + Eng | Week 4–5 | Quality validation |
| 6 | Go live, monitor cost + quality for 4 weeks | Eng | Week 6 | Stable automated pipeline |

**First checkpoint**: Week 2 — scraper reliability > 90% before building downstream agents  
**First value**: Week 4–5 — first automated report generated for human review

---

## Multi-Agent Shared Context Schema

```json
{
  "run_id": "2024-W32",
  "competitors": ["CompA", "CompB", "CompC"],
  "sources": {
    "CompA": { "urls": [...], "scrape_status": "done", "raw_content": "..." },
    "CompB": { "urls": [...], "scrape_status": "failed", "error": "403" }
  },
  "insights": {
    "CompA": { "summary": "...", "signals": [...], "citations": [...] }
  },
  "report_draft": "...",
  "publish_status": "pending"
}
```

---

## Top Risks

| # | Risk | Score | Mitigation | Warning Signal |
|---|------|-------|-----------|---------------|
| 1 | Scraper fails (site blocks, structure changes) | 6 | Fallback to cached last week's content + flag in report | Scrape success rate < 80% |
| 2 | Analyst Agent hallucinates a claim | 6 | Enforce citation in prompt: "only state facts directly from the source text" | Report contains unlinked claims |
| 3 | API cost exceeds $200/month | 4 | Track tokens per run, set alert at $150/month, optimize prompts if needed | Monthly API dashboard > $150 |

---

## Fallback Plan

**Trigger**: Scrape reliability < 70% OR hallucination detected in 2+ consecutive reports  
**Fallback**: Switch to Plan C (Hybrid) — agents still run but human reviews before publishing. Buy time to improve scraper reliability.  
**Owner**: Engineering lead decides by end of week 6 evaluation period
