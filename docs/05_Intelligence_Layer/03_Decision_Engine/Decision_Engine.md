# Decision Engine

| Attribute | Value |
|-----------|-------|
| Document ID | DE-001 |
| Version | 1.0 |
| Status | Frozen |
| Owner | Product Architecture |
| Last Updated | YYYY-MM-DD |

---

# Purpose

The Decision Engine is the cognitive core of Sigmatics.

It is responsible for transforming continuously changing market information into quantified, explainable and actionable trading decisions.

Unlike conventional trading platforms that primarily display charts and indicators, Sigmatics actively observes, analyses and synthesizes information from multiple specialized intelligence agents before producing a recommendation.

The Decision Engine does not execute trades.

Its responsibility ends with producing a complete, explainable execution recommendation for human review.

---

# Design Philosophy

The Decision Engine shall adhere to the following principles.

# Guiding Principle

The Decision Engine exists to answer one question.

> "Given everything currently known about the market, what is the highest-confidence action the user should consider next?"

That action may be:

- Buy CE
- Buy PE
- Hold an existing position
- Exit an existing position
- Wait

The Decision Engine shall always prefer recommending **WAIT** over producing a low-confidence trading recommendation.

A missed opportunity is preferable to an unjustified trade.

## Intelligence before Information

Sigmatics exists to produce intelligence, not merely display market information.

Raw market data shall never be presented as the primary output.

Instead, the Decision Engine shall continuously transform information into meaningful decisions.

---

## Quantified Decisions

Every recommendation shall be measurable.

Every recommendation shall include:

- Opportunity Score
- Confidence Score
- Risk Assessment
- Decision State

Recommendations shall never be qualitative alone.

---

## Explainable Decisions

Every recommendation shall be traceable back to its contributing factors.

Users shall always be able to understand:

- Why a recommendation was generated.
- Which agents contributed.
- Which observations influenced the outcome.
- Which assumptions were made.

---

## Human Governed Decisions

The Decision Engine shall never place trades.

Every recommendation requires explicit human approval.

Execution authority always remains with the user.

---

## Deterministic Core

Wherever deterministic calculations are possible, they shall be preferred over probabilistic reasoning.

AI reasoning augments the platform but never replaces mathematical validation.

---

# Architectural Position

The Decision Engine operates above the Intelligence Layer and below the User Experience Layer.

```
Market Data
        │
        ▼
Specialized AI Agents
        │
        ▼
Decision Engine
        │
        ▼
Execution Planner
        │
        ▼
Notification Service
        │
        ▼
User Interface
```

The Decision Engine never communicates directly with broker integrations.

---

# Responsibilities

The Decision Engine is responsible for:

- Collecting outputs from specialized agents.
- Validating recommendation completeness.
- Computing Opportunity Score.
- Computing Decision Confidence.
- Determining Decision State.
- Selecting the highest priority recommendation.
- Producing explainable execution recommendations.
- Publishing decision snapshots.
- Triggering downstream notification workflows.

The Decision Engine is not responsible for:

- Market data acquisition.
- Technical indicator calculation.
- Broker communication.
- Trade execution.
- Learning.
- Strategy evolution.

---

# Decision Lifecycle

Every recommendation progresses through the following lifecycle.

```
Observe
        │
Analyse
        │
Reason
        │
Quantify
        │
Validate
        │
Recommend
        │
Review
        │
Execute
        │
Monitor
        │
Complete
```

Only the first six stages belong to the Decision Engine.

---

# Inputs

The Decision Engine consumes structured outputs from:

- Pre-Market Intelligence Agent
- Market Observer Agent
- Market Opportunity Agent
- Trend Agent
- Structure Agent
- Context Agent
- Strategy Agent
- Risk Agent
- Trade Optimization Agent

Each input must comply with its published decision contract.

---

# Outputs

The Decision Engine produces exactly one Decision Package.

The Decision Package contains:

- Decision ID
- Timestamp
- Recommended Index
- Option Contract
- Entry Recommendation
- Stop Loss
- Target
- Opportunity Score
- Confidence Score
- Decision State
- Decision Expiry (TTL)
- Supporting Evidence
- Decision Trace Reference

---

# Decision States

Every recommendation shall belong to one of the following states.

## Observing

Insufficient evidence exists.

No recommendation shall be produced.

---

## Building Confidence

Evidence is accumulating.

Recommendations remain internal.

---

## Actionable

Confidence threshold has been exceeded.

Recommendation becomes available for user review.

---

## Monitoring

Recommendation has expired or trade is active.

Decision Engine monitors market evolution.

---

## Closed

Recommendation lifecycle has completed.

Decision Snapshot becomes immutable.

---

# Opportunity Score

Opportunity Score represents the attractiveness of the current market opportunity.

The score is derived from deterministic market analysis and agent outputs.

Range:

0 – 100

Higher values indicate greater trading opportunity.

Opportunity Score measures:

- Quality of setup
- Trend strength
- Market structure
- Liquidity
- Context alignment
- Option suitability

Opportunity Score does not represent probability of profit.

---

# Confidence Score

Confidence Score represents the platform's confidence in its own recommendation.

Range:

0 – 100

Confidence reflects:

- Agreement between agents.
- Historical reliability.
- Data completeness.
- Market consistency.
- Model certainty.

Confidence and Opportunity are intentionally independent.

A trade may present:

High Opportunity

Low Confidence

or

Moderate Opportunity

High Confidence.

---

# Decision Package

Every recommendation shall be represented by a Decision Package.

The Decision Package is immutable after publication.

Subsequent market changes generate a new Decision Package rather than modifying an existing one.

This guarantees complete replayability.

---

# Decision Snapshots

Every published Decision Package creates a Decision Snapshot.

Snapshots contain:

- Complete market context
- Agent outputs
- Recommendation
- Scores
- User interaction history
- Execution outcome (if applicable)

Snapshots become the foundation for:

- Replay
- Learning
- Backtesting
- Performance analytics

---

# Explainability

Every recommendation shall expose:

Why was this recommendation generated?

The answer shall identify:

- Agent contributions
- Supporting evidence
- Confidence contributors
- Risk factors
- Market assumptions

No recommendation shall exist without explainability.

---

# Future Evolution

The Decision Engine has been designed to support future capabilities including:

- Portfolio recommendations
- Multi-asset trading
- Learning Agent integration
- AI Coach
- Paper Trading
- Strategy evolution
- Multi-broker execution
- Global market support

The Decision Engine remains independent of implementation technology.

Its architectural contract shall remain stable across future platform releases.