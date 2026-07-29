# AGT-009 — Trade Optimization Agent

## Purpose

Transform an approved Trading Decision and Risk Assessment into the most suitable option contract recommendation.

The Trade Optimization Agent evaluates all eligible option contracts mathematically to determine the optimal contract based on capital availability, liquidity, Greeks, risk exposure and expected reward.

---

## Business Responsibility

Recommend the single most suitable option contract for execution.

The recommendation includes:

- Option Contract
- Entry Recommendation
- Recommended Quantity
- Option Suitability Score (OSS)
- Confidence Score

---

## Inputs

- Trading Decision
- Risk Assessment
- Live Option Chain
- User Trading Preferences
- Available Broker Funds

---

## Produces

- Option Recommendation

---

## Consumed By

- Execution Planner

---

## Deterministic Responsibilities

Evaluate every candidate contract using:

- Delta
- Gamma
- Theta
- Vega
- Implied Volatility
- Open Interest
- Bid/Ask Spread
- Liquidity
- Premium Affordability
- Expected Risk
- Capital Utilisation

Calculate:

- Option Suitability Score (OSS)

Rank all eligible contracts.

Publish the highest scoring recommendation.

---

## AI-Assisted Responsibilities

Explain why the selected contract is preferred.

Summarise the trade-off between competing contracts.

Highlight unusual option chain behaviour.

---

## Never Responsible For

- Broker execution
- Order placement
- Portfolio management

---

## Success Criteria

Publish:

- Recommended CE/PE
- Quantity
- Entry Range
- Confidence
- Option Suitability Score
- Supporting Evidence

---

## Failure Behaviour

If no suitable option satisfies minimum quality thresholds:

Publish:

Recommendation = WAIT

Reason = No suitable option available.