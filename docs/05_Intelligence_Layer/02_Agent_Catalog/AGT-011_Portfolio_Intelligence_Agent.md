# AGT-011 — Portfolio Intelligence Agent

## Purpose

Continuously evaluate a user's investment portfolio and provide evidence-based Buy, Hold and Sell recommendations.

The agent analyses portfolio composition independently from intraday trading intelligence.

---

## Business Responsibility

Assess portfolio health and generate investment recommendations.

---

## Inputs

- Portfolio Snapshot
- Holdings
- Market Data
- User Investment Profile

---

## Produces

- Portfolio Recommendation

---

## Consumed By

- Reporting Engine
- User Interface

---

## Deterministic Responsibilities

Evaluate:

- Portfolio Diversification
- Sector Allocation
- Concentration Risk
- Unrealised Gains/Losses
- Risk Exposure

Generate:

- Portfolio Health Score

---

## AI-Assisted Responsibilities

Recommend:

- Buy
- Hold
- Sell

Suggest alternative stocks.

Explain portfolio strengths and weaknesses.

Generate reallocation suggestions.

---

## Never Responsible For

- Executing trades
- Intraday strategies
- Option recommendations

---

## Success Criteria

Publish:

Portfolio Recommendation

Portfolio Health Score

Supporting Evidence

Reallocation Suggestions