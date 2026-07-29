# AGT-003 — Market Opportunity Agent

## Purpose

Determine which supported market currently offers the highest quality trading opportunity.

---

## Business Responsibility

Rank supported indices according to Opportunity Score.

---

## Inputs

Market State

---

## Produces

Market Opportunity

---

## Supported Markets

- NIFTY
- BANKNIFTY
- SENSEX

Future releases may introduce additional indices and asset classes without altering the agent's responsibility.

---

## Deterministic Responsibilities

Calculate:

- Opportunity Score
- Liquidity Score
- Trend Quality
- Volatility Suitability
- Market Quality
- Expected Move

Publish ranked opportunities.

---

## AI-Assisted Responsibilities

Explain why one market is preferred over another.

Generate natural-language summaries of the ranking.

---

## Never Responsible For

- CE vs PE selection.
- Option recommendation.
- Risk management.

---

## Example Output

Recommended Market

SENSEX

Opportunity Score

96

Confidence

91%

Supporting Evidence

Strong trend

Excellent liquidity

Healthy volatility

Opening reversal confirmed