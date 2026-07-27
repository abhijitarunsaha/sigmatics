# Agent Architecture

## Purpose

The Sigmatics Intelligence Layer is composed of specialised business agents rather than a single general-purpose artificial intelligence.

Each agent represents a domain expert responsible for one clearly defined stage within the Decision Pipeline.

This architecture enables modularity, explainability and controlled evolution.

---

# Architectural Principles

## AGT-001

Each agent shall own exactly one business responsibility.

---

## AGT-002

Agents communicate exclusively using Canonical Domain Objects.

---

## AGT-003

Agents shall never directly invoke downstream business logic.

All orchestration occurs through the Decision Pipeline.

---

## AGT-004

Agents shall be stateless wherever practical.

Persistent knowledge belongs to dedicated repositories.

---

## AGT-005

Agents shall never modify published upstream decisions.

---

## AGT-006

Every published decision shall be timestamped.

---

## AGT-007

Every decision shall be traceable.

---

## AGT-008

Every decision shall be replayable.

---

## AGT-009

LLMs provide reasoning.

Deterministic engines perform calculations.

---

## AGT-010

Human approval remains mandatory before trade execution.

---

# Agent Lifecycle

Every specialised agent follows a common lifecycle.

Receive Domain Object

↓

Validate Input

↓

Perform Deterministic Processing

↓

Invoke AI Reasoning (when required)

↓

Validate Result

↓

Publish Canonical Domain Object

↓

Audit

---

# Agent Responsibilities

Each AI agent is responsible for exactly one business capability.

Responsibilities shall never overlap.

Where additional functionality is required, a new specialised agent shall be introduced instead of expanding existing responsibilities.

---

# Explainability

Every published recommendation shall provide sufficient evidence to explain:

- Why the recommendation was generated.
- Which observations contributed.
- Which deterministic calculations were applied.
- Which AI reasoning was performed.
- Confidence level.
- Supporting evidence.

---

# Failure Behaviour

If an agent cannot produce a sufficiently confident output:

- The decision pipeline shall continue where possible.
- Appropriate warnings shall be published.
- Downstream agents shall receive uncertainty indicators.
- Where required, the platform shall recommend WAIT instead of TRADE.

---

# Relationship with Business Capabilities

Every AI agent exists solely to implement one Business Capability.

Business Capabilities define WHAT.

AI Agents define HOW.

Canonical Domain Objects define WHAT FLOWS.