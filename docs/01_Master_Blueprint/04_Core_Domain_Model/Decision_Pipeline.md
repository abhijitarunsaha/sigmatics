# Decision Pipeline

## Purpose

The Sigmatics Decision Pipeline defines the end-to-end transformation of raw market information into an explainable, human-governed trading recommendation.

Every stage in the pipeline consumes canonical domain objects and produces new canonical domain objects.

No component bypasses the pipeline.

---

# Flow Summary

Decision Engine

↓

Executes Decision Stages

↓

Collects Evidence

↓

Records Reasoning

↓

Synthesizes Confidence

↓

Constructs Decision

↓

Produces Decision Package

↓

Hands Journal for Persistence

---

# Pipeline

External Signals

↓

Pre-Market Intelligence Agent

↓

Expected Market Snapshot

↓

Market Observer Agent

↓

Live Market Snapshot

↓

Deviation Analysis

↓

Market State

↓

Market Opportunity Agent

↓

Market Opportunity

↓

Trend Agent

↓

Trend Analysis

↓

Structure Agent

↓

Structure Analysis

↓

Context Agent

↓

Market Context

↓

Strategy Agent

↓

Trading Decision

↓

Risk Agent

↓

Risk Assessment

↓

Trade Optimization Engine

↓

Option Recommendation

↓

Execution Planner

↓

Execution Plan

↓

Broker Adapter

↓

Broker API

↓

Exchange

---

# Design Principles

- Observe before deciding.
- Compare expectation with reality.
- Rank opportunities before selecting strategies.
- Quantify every recommendation.
- Explain every recommendation.
- Optimise every trade mathematically.
- Require human confirmation before execution.
- Record every published domain object.
- Enable complete decision replay.