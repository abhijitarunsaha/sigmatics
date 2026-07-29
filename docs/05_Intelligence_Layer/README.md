# AI Agent Ecosystem

## Purpose

The AI Agent Ecosystem defines the intelligence layer of the Sigmatics platform.

Rather than relying on a single monolithic AI model, Sigmatics distributes intelligence across a collection of specialised domain agents.

Each agent owns one business responsibility, consumes well-defined canonical domain objects, performs deterministic calculations and/or AI-assisted reasoning where appropriate, and publishes a new canonical domain object for downstream consumers.

This architecture promotes explainability, maintainability, replayability and independent evolution.

The AI Agent Ecosystem is designed around business responsibilities rather than technology choices.

Large Language Models (LLMs) are treated as reasoning tools, not decision makers.

---

# Design Philosophy

Sigmatics follows a domain-specialised intelligence model.

Every AI agent:

- Owns exactly one business capability.
- Performs one clearly defined responsibility.
- Has explicit inputs and outputs.
- Never bypasses the Decision Pipeline.
- Never mutates upstream decisions.
- Produces explainable outputs.
- Operates independently of broker implementations.
- Can be tested in isolation.

---

# Engineering Principles

The Intelligence Layer follows these core principles.

## IA-001

AI augments decision making.

It never replaces deterministic business rules.

---

## IA-002

Deterministic calculations always take precedence over probabilistic reasoning.

---

## IA-003

Every AI-generated insight shall be explainable.

---

## IA-004

Every published recommendation shall be reproducible.

---

## IA-005

Learning occurs offline.

Production behaviour changes only after human approval.

---

## IA-006

Every recommendation shall include confidence measurements where applicable.

---

## IA-007

When uncertainty exceeds acceptable thresholds, the preferred recommendation is WAIT rather than TRADE.

---

# AI Agent Categories

The Sigmatics Intelligence Layer consists of four logical categories.

## Market Intelligence

Responsible for observing and understanding current market behaviour.

Examples:

- Pre-Market Intelligence Agent
- Market Observer Agent
- Market Opportunity Agent

---

## Trading Intelligence

Responsible for transforming market understanding into trading decisions.

Examples:

- Trend Agent
- Structure Agent
- Context Agent
- Strategy Agent

---

## Trade Intelligence

Responsible for optimising and validating trade execution.

Examples:

- Risk Agent
- Trade Optimization Agent
- Execution Planner

---

## Learning Intelligence

Responsible for continuous improvement without affecting production behaviour.

Examples:

- Learning Agent
- Evolution Agent
- AI Coach

---

# Relationship with the Core Domain Model

AI agents never exchange raw market data directly.

Every interaction occurs through Canonical Domain Objects.

This separation enables:

- Independent testing
- Replayability
- Explainability
- Versioning
- Future extensibility

---

# Documents

| Document | Purpose |
|----------|---------|
| Agent_Architecture.md | Defines the architectural principles governing AI agents. |
| Agent_Catalog.md | Defines every specialised AI agent. |
| Agent_Contracts.md | Standardises the contract implemented by every agent. |
| Decision_Flow.md | Describes the end-to-end intelligence pipeline. |