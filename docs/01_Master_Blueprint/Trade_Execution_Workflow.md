# Trade Execution Workflow

## Purpose

The Trade Execution Workflow provides a structured review process before a broker order is submitted.

Its objective is to ensure that every trade is reviewed, explainable and user-approved.

---

# Workflow

Trading Recommendation

↓

Execution Plan

↓

Execution Review Screen

↓

User Confirmation

↓

Broker Adapter

↓

Broker API

↓

Exchange

---

# Execution Review Screen

The Execution Review screen displays:

- Recommended Option Contract
- Entry Price
- Quantity
- Stop Loss
- Target
- Trailing Stop Loss
- Decision Valid Until

---

# Editable Fields

The user may modify:

- Entry Price
- Quantity
- Stop Loss
- Target
- Trailing Stop Loss

Sigmatics shall automatically validate all edits against applicable risk limits before execution.

---

# Primary Actions

The Execution Review screen exposes only two primary actions:

- Execute Trade
- Cancel

No additional primary actions shall compete for user attention.

---

# Decision Intelligence

A contextual link labelled:

View Decision Intelligence → (Secondary Link)

provides access to the reasoning behind the recommendation.

This link is intentionally presented as secondary navigation to maintain focus on the primary execution workflow.

---

# Decision Intelligence Contents

The Decision Intelligence view presents:

- Opportunity Score
- Confidence Score
- Trend Analysis
- Structure Analysis
- Market Context
- Strategy Decision
- Risk Assessment
- Trade Optimisation Summary
- Decision ID
- Decision Version
- Decision Validity

---

# Decision Trace

The Decision Intelligence view provides access to the complete decision trace:

Expected Market Snapshot

↓

Observed Market State

↓

Market Opportunity

↓

Trend Analysis

↓

Structure Analysis

↓

Market Context

↓

Trading Strategy

↓

Risk Assessment

↓

Trade Optimisation

↓

Execution Plan

Every stage shall be expandable to expose the supporting evidence and deterministic calculations.

---

# Validation Before Execution

Immediately before submitting an order, Sigmatics shall validate:

- Recommendation validity (TTL)
- Current market conditions
- Broker session status
- Available trading balance
- Risk constraints

If any validation fails, the user shall be informed and a refreshed recommendation shall be generated where appropriate.

---

# Regulatory Compliance

Sigmatics shall never submit broker orders without explicit user confirmation.

The platform operates as a trading intelligence and execution support system.

Final execution authority always rests with the authenticated user.