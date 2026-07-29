# AGT-004 — Trend Agent

## Purpose

Determine the prevailing directional behaviour of the selected market and quantify the quality of the observed trend.

The Trend Agent analyses price action using deterministic mathematical models and publishes a Trend Analysis domain object.

---

## Business Responsibility

Determine whether the selected market is exhibiting a statistically meaningful trend.

The agent evaluates:

- Trend Direction
- Trend Strength
- Trend Continuity
- Trend Confidence

The agent does not recommend trades.

---

## Inputs

- Market Opportunity

---

## Produces

- Trend Analysis

---

## Consumed By

- Structure Agent

---

## Deterministic Responsibilities

Calculate:

- Trend Direction
- Trend Strength Index (TSI)
- Moving Average Alignment
- Momentum
- Rate of Change
- Multi-Timeframe Trend Alignment

Publish Trend Analysis.

---

## AI-Assisted Responsibilities

- Explain trend quality.
- Describe significant changes in trend behaviour.
- Summarise observations for downstream agents.

---

## Never Responsible For

- Support/Resistance
- Strategy selection
- Risk calculations
- Option selection

---

## Success Criteria

- Trend direction classified.
- Trend confidence published.
- Supporting evidence attached.

---

## Failure Behaviour

If conflicting trend signals exist:

- Publish reduced-confidence Trend Analysis.
- Allow downstream agents to determine suitability.