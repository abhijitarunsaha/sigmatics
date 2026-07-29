# AGT-010 — Execution Planner

## Purpose

Convert an Option Recommendation into a broker-independent execution plan while remaining fully compliant with regulatory requirements.

The Execution Planner prepares trades but never executes them autonomously.

---

## Business Responsibility

Generate a complete execution plan for user approval.

The execution plan includes:

- Entry
- Stop Loss
- Target
- Trailing Stop Loss
- Order Sequence

---

## Inputs

- Option Recommendation
- Risk Assessment
- User Execution Preferences

---

## Produces

- Execution Plan

---

## Consumed By

- Broker Adapter

---

## Deterministic Responsibilities

Generate:

- Recommended Entry Price
- Acceptable Entry Range
- Stop Loss
- Target
- Trailing Stop Recommendation
- Order Sequence

Validate:

- Capital Availability
- Broker Constraints
- Exchange Constraints

---

## AI-Assisted Responsibilities

Explain execution strategy.

Explain risk associated with delayed entry.

Provide guidance when market conditions change during execution.

---

## Never Responsible For

- Placing trades automatically
- Strategy selection
- Market analysis

---

## Success Criteria

Produce a complete Execution Plan ready for user approval.

---

## Failure Behaviour

If execution constraints cannot be satisfied:

Publish execution warning.

Request user review.