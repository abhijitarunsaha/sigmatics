# AGT-002 — Market Observer Agent

## Purpose

Continuously observe live market behaviour and compare it against the Expected Market Snapshot.

---

## Business Responsibility

Convert live observations into an explainable Market State.

---

## Inputs

- Expected Market Snapshot
- Live Market Feed

---

## Produces

Market State

---

## Consumed By

Market Opportunity Agent

---

## Deterministic Responsibilities

- Normalize market data.
- Compute Market Quality Score (MQS).
- Detect deviations from expected behaviour.
- Monitor liquidity.
- Measure volatility.
- Publish updated Market State.

---

## AI-Assisted Responsibilities

- Explain significant deviations.
- Classify unusual market behaviour.
- Highlight noteworthy market events.

---

## Never Responsible For

- Choosing markets.
- Trading decisions.
- Risk management.

---

## Success Criteria

- Publish Market State continuously.
- Maintain immutable snapshots.
- Attach deviation analysis.