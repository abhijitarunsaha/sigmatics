# Domain Object Catalog

## Purpose

The Domain Object Catalog defines every canonical business object used within the Sigmatics decision pipeline.

Each object has a single owner, a defined producer, one or more consumers, and a well-defined lifecycle.

Canonical domain objects represent business concepts rather than persistence entities or API payloads.

---

# Domain Object Ownership Matrix

| Domain Object | Produced By | Consumed By | Owner Capability |
|---------------|-------------|-------------|------------------|
| Expected Market Snapshot | Pre-Market Intelligence Agent | Market Observer Agent | CAP-003 |
| Live Market Snapshot | Market Observer Agent | Market Observer Agent | CAP-003 |
| Market State | Market Observer Agent | Market Opportunity Agent | CAP-003 |
| Market Opportunity | Market Opportunity Agent | Trend Agent | CAP-003 |
| Trend Analysis | Trend Agent | Structure Agent | CAP-004 |
| Structure Analysis | Structure Agent | Context Agent | CAP-004 |
| Market Context | Context Agent | Strategy Agent | CAP-004 |
| Trading Decision | Strategy Agent | Risk Agent | CAP-004 |
| Decision Journal | Immutable reasoning history associated with a Decision Package | Context Agent | CAP-004 |
| Decision Journal Entry | Individual reasoning observation recorded during evaluation | Context Agent | CAP-004 |
| Reasoning Recorder | Runtime component responsible for constructing the active Decision Journal | Context Agent | CAP-004 |
| Risk Assessment | Risk Agent | Trade Optimization Engine | CAP-005 |
| Option Recommendation | Trade Optimization Engine | Execution Planner | CAP-005 |
| Execution Plan | Execution Planner | Broker Adapter | CAP-005 |
| Trade Snapshot | Broker Connectivity | Portfolio Intelligence | CAP-006 |
| Portfolio Snapshot | Portfolio Intelligence | Reporting | CAP-006 |
| Financial Summary | Reporting Engine | User Interface | CAP-007 |

---

# Domain Object Template

Every domain object shall define:

- Purpose
- Producing Capability
- Producing Component
- Consuming Components
- Lifecycle
- Version
- Timestamp
- Confidence (if applicable)
- Evidence (if applicable)
- Audit Identifier