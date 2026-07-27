# Canonical Domain Model

## Purpose

The Canonical Domain Model defines the authoritative business objects that flow through the Sigmatics decision pipeline.

These objects capture progressively richer representations of market understanding, trading intelligence and execution planning.

Rather than allowing individual components to exchange raw market data or broker-specific payloads, Sigmatics standardizes communication using immutable canonical domain objects.

This enables explainability, replayability, independent testing and future evolution.

---

# Architectural Principles

## CDM-001

Every business concept shall have a single canonical representation.

---

## CDM-002

Every domain object shall have one owning capability.

---

## CDM-003

Every domain object shall have one producing component.

---

## CDM-004

Domain objects shall be immutable after publication.

---

## CDM-005

Consumers shall never modify received domain objects.

---

## CDM-006

Every domain object shall contain sufficient information to explain its own creation.

---

## CDM-007

Domain objects shall be technology independent.

---

## CDM-008

Every published domain object shall be timestamped and versioned.

---

## CDM-009

Historical domain objects shall remain available for replay.

---

## CDM-010

Every AI agent shall consume and produce canonical domain objects.

---

# Domain Object Categories

The canonical model groups business objects into the following categories.

## Market Intelligence

- Expected Market Snapshot
- Live Market Snapshot
- Market State
- Market Opportunity

---

## Trading Intelligence

- Trend Analysis
- Structure Analysis
- Market Context
- Trading Decision

---

## Risk Intelligence

- Risk Assessment
- Position Recommendation

---

## Trade Optimization

- Option Recommendation
- Execution Plan

---

## Portfolio Intelligence

- Portfolio Snapshot
- Holdings Snapshot

---

## Reporting

- Financial Summary
- Decision Replay

---

# Lifecycle

Observe

↓

Normalize

↓

Understand

↓

Evaluate

↓

Optimize

↓

Execute

↓

Learn

---

## Relationship with AI Agents

Every AI agent exists to transform one canonical domain object into another.

AI agents do not communicate directly.

They communicate exclusively through canonical domain objects.

This architecture minimizes coupling while maximizing explainability.