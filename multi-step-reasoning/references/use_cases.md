# Real-World Use Cases — Worked Examples

---

## USE CASE 1: Debugging (Engineering)

**Problem:** "My API returns 200 but the frontend shows an empty state. It started after
yesterday's deploy. I haven't changed the response schema."

**Mode selected:** Chain-of-Thought (linear — one root cause to find)

**Reasoning:**
- [SP-1] Verify the API actually returns data: Check network tab. Does the 200 response
  body contain data? → Yes, data is present.
- [SP-2] Check data transformation: Is the frontend parsing the response correctly?
  Look for `.data`, `.results`, `.items` key mismatch → Found: backend changed `items`
  to `results`, frontend still reads `.items`.
- [SP-3] Confirm fix: Update frontend to read `.results`. Test against staging.

**Output:** The schema DID change — the key `items` was renamed `results`. The developer's
assumption ("haven't changed the schema") was the wrong premise. Step 1 flagged it.

**Confidence:** High

---

## USE CASE 2: Product Decision

**Problem:** "We need to decide whether to build a mobile app or stay web-only for our
B2B SaaS tool. We have 6 months runway."

**Mode selected:** Tree-of-Thought (strategic — real trade-offs between paths)

**Branches:**
- Path A: Build native iOS/Android app
  - Feasibility: 2/5 (expensive, 6 months is very tight)
  - Goal alignment: 3/5 (B2B users often work at desks)
  - Score: 5 → Pruned
- Path B: Progressive Web App (PWA)
  - Feasibility: 4/5 (reuses web codebase)
  - Goal alignment: 4/5 (app-like on mobile, works on desktop)
  - Score: 8 → Selected
- Path C: Stay web-only, invest in mobile-responsive polish
  - Feasibility: 5/5 (already done)
  - Goal alignment: 3/5 (misses mobile-first users)
  - Score: 8 → Tied with B

**Synthesis:** PWA wins because it unlocks mobile without duplicating codebases. Path C
stays as a fast fallback if PWA scope creeps.

**Confidence:** Medium (depends on whether mobile usage is actually needed — recommend
checking analytics for mobile session % before committing)

---

## USE CASE 3: UX Flow Design

**Problem:** "Users are dropping off at step 3 of our 5-step onboarding. How do we fix it?"

**Mode selected:** Tree-of-Thought (UX_DECISION template)

**Options generated:**
- Option A: Reduce onboarding to 3 steps (merge/cut steps)
  - User effort: 5 | Goal: 4 | Feasibility: 3 | Consistency: 3 = 15
- Option B: Add a progress bar + skip option to step 3
  - User effort: 4 | Goal: 3 | Feasibility: 5 | Consistency: 4 = 16
- Option C: Move step 3 content post-onboarding (progressive disclosure)
  - User effort: 5 | Goal: 5 | Feasibility: 4 | Consistency: 3 = 17 ← Winner

**Recommendation:** Move non-essential step 3 content to the first session in-app. Users
complete onboarding faster and encounter the feature when they're ready for it.

---

## USE CASE 4: Business Strategy

**Problem:** "We're considering entering the APAC market. Is now the right time?"

**Mode selected:** Self-Consistency (high-stakes, verifiable with data)

**Chain 1:** Market timing → competitor analysis → resource requirement → No (too early)
**Chain 2:** Customer demand signals → revenue opportunity → risk tolerance → Maybe (pilot)
**Chain 3:** Regulatory landscape → localization cost → team bandwidth → No (wrong quarter)

**Vote:** 2/3 chains say Not yet. Confidence: Medium.

**Final answer:** Delay full entry. Run a lightweight pilot (1 market, 1 quarter) to
validate demand signals from Chain 2 before committing.

---

## USE CASE 5: AI Agent Planning

**Problem:** "Summarize all Slack messages mentioning 'Q3 launch' from the past 2 weeks,
find the key decisions made, and draft a status update email."

**Mode selected:** AGENT_PLAN template

**Task breakdown:**
- [T-1] Fetch Slack messages — Slack MCP — last 14 days, filter: "Q3 launch"
- [T-2] Extract key decisions — LLM reasoning on T-1 output
- [T-3] Draft email — LLM with T-2 as context

**Dependencies:** T-2 → T-1; T-3 → T-2

**Decision point:** After T-2 — user confirms the extracted decisions are correct before
the email is drafted.

**Risk:** T-1 may return noise (unrelated "Q3 launch" mentions) — flag for human review.
