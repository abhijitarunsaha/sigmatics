# AGT-007 — Strategy Agent

## Purpose

Determine the most appropriate trading action based on the current Market Context.

---

## Business Responsibility

Recommend one of:

- BUY CE
- BUY PE
- WAIT

The Strategy Agent does not select option contracts.

---

## Inputs

- Market Context

---

## Produces

- Trading Decision

---

## Consumed By

- Risk Agent

---

## Deterministic Responsibilities

Evaluate:

- Strategy Rules
- Trend Alignment
- Context Score
- Opportunity Score
- Trading Window
- Market Health

Generate Decision Confidence.

---

## AI-Assisted Responsibilities

Explain why the selected strategy is preferred.

Explain why WAIT was recommended.

Generate human-readable reasoning.

---

## Never Responsible For

- Risk calculations
- Option selection
- Order placement

---

## Success Criteria

Publish:

Trading Decision

Decision Confidence

Supporting Evidence

Recommended Action

---

## Failure Behaviour

When uncertainty exceeds configured thresholds:

Publish WAIT.