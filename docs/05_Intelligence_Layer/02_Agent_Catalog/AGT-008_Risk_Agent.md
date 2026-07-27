# AGT-008 — Risk Agent

## Purpose

Determine whether the proposed Trading Decision satisfies acceptable risk criteria.

---

## Business Responsibility

Validate the suitability of executing the proposed trade.

---

## Inputs

- Trading Decision
- User Trading Profile
- Broker Account Balance

---

## Produces

- Risk Assessment

---

## Consumed By

- Trade Optimization Agent

---

## Deterministic Responsibilities

Calculate:

- Position Size
- Maximum Risk
- Stop Loss Recommendation
- Target Recommendation
- Risk-Reward Ratio

Validate exposure limits.

---

## AI-Assisted Responsibilities

Explain identified risks.

Highlight unusual exposure.

Recommend conservative alternatives.

---

## Never Responsible For

- Choosing options.
- Executing trades.

---

## Success Criteria

Publish complete Risk Assessment.

Recommend rejection if unacceptable.