# AGT-001 — Pre-Market Intelligence Agent

## Purpose

Produces the Expected Market Snapshot before the market opens by analysing overnight and pre-market information.

---

## Business Responsibility

Establish the expected market conditions for the upcoming trading session.

The agent does not recommend trades.

---

## Inputs

External Signals

- GIFT NIFTY
- Global Indices
- India VIX
- Previous Trading Session
- Economic Calendar
- Market Holidays
- Scheduled Events

---

## Produces

Expected Market Snapshot

---

## Consumed By

Market Observer Agent

---

## Deterministic Responsibilities

- Collect market data
- Calculate expected opening bias
- Estimate expected volatility
- Calculate confidence
- Publish snapshot

---

## AI-Assisted Responsibilities

- Summarise overnight macro events.
- Classify market sentiment from validated news sources (future capability).
- Explain expected market bias in natural language.

---

## Never Responsible For

- Trade recommendations
- Strategy selection
- Risk calculations
- Option selection
- Order execution

---

## Success Criteria

- Snapshot published before market opening.
- Snapshot versioned.
- Confidence calculated.
- Supporting evidence attached.

---

## Failure Behaviour

If insufficient data is available:

- Publish reduced-confidence snapshot.
- Notify downstream agents.
- Never fabricate missing observations.