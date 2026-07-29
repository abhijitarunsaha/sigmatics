# Decision Engine

## Purpose

## Scope

The Decision Engine is the central orchestration engine of Sigmatics.

It is responsible for transforming validated intelligence from one or more Intelligence Domains into explainable, confidence-based Decision Packages.

The Decision Engine is domain agnostic.

Although the MVP focuses on intraday options trading, the same engine shall support Portfolio Intelligence, capital reallocation, Buy/Hold/Sell recommendations and future decision domains without architectural changes.

The Decision Engine itself never analyses markets or portfolios directly. Instead, it orchestrates evidence supplied by specialized Intelligence Domains before constructing a Decision Package.

---

## Core Principles

## Architectural Responsibilities

## Decision Engine Workflow
    Stage 1 – Trading Eligibility
    Stage 2 – Pre-Market Intelligence
    Stage 3 – Market Assessment
    Stage 4 – Strategy Selection
    Stage 5 – Option Selection
    Stage 6 – Trade Validation
    Stage 7 – Confidence Synthesis
    Stage 8 – Trade Construction
    Stage 9 – Explainability Package
    Stage 10 – Review & Execute

---

### Stage 1
────────
Trading Eligibility
• Market Open
• User Authenticated
• Compliance Verified
• Broker Connected
• Market Data Healthy
• Trading Session Valid

        │
        ▼

### Stage 2
────────
Pre-Market Intelligence
• Global Markets
• GIFT NIFTY
• VIX
• Overnight News
• FII/DII
• Macro Events
• Opening Bias

        │
        ▼

### Stage 3
────────
Market Assessment

For each supported market:

• Market State
• Opportunity Analysis

Markets:

• NIFTY
• BANKNIFTY
• SENSEX
(Future: FINNIFTY, MIDCPNIFTY...)

↓

Select Highest Opportunity Market

        │
        ▼

### Stage 4
────────
Strategy Selection

Determine:

• Trend Following
• Breakout
• Pullback
• Reversal
• Momentum
• Range
• WAIT

        │
        ▼

### Stage 5
────────
Option Selection

Affordability Gate

↓

Available Funds

↓

Affordable Contracts

↓

Greeks Evaluation

↓

Liquidity

↓

Premium Optimisation

↓

Best Option Contract

        │
        ▼

Stage 6
────────
Trade Validation

Validate:

• Market Quality
• Risk
• Liquidity
• Strategy Compatibility
• Option Suitability
• Margin Sufficiency

        │
        ▼

Stage 7
────────
Confidence Synthesis

↓

Confidence ≥ Threshold?

        │
   No ─────────► WAIT

        │
       Yes

        ▼

Stage 8
────────
Trade Construction

Generate:

• Entry
• Editable Entry
• Stop Loss
• Trailing Stop
• Target
• TTL
• Risk Reward

        │
        ▼

Stage 9
────────
Explainability Package

Generate:

• Why this Trade?
• Supporting Evidence
• Agent Contributions
• Risk Factors
• Decision Trace

        │
        ▼

Stage 10
────────
Review & Execute

↓

Human Decision

↓

Broker Execution



## Mandatory Evidence

## Decision Outcomes

## Relationship with Intelligence Domains

## Relationship with Decision Guardian

## Future Evolution