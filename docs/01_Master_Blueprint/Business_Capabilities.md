---
Document ID: SIG-SRS-001
Document Name: Business Capabilities
Project: SIGMATICS
Tagline: Signals, Quantified.
Version: 1.0
Status: Baseline Approved
Owner: Sigmatics Engineering
Classification: Internal

Related Documents:
- Executive Summary
- Product Vision
- Product Principles
- Engineering Principles
- Functional Requirements
- Decision Pipeline
- Architecture Overview
---

# Business Capabilities

---

# Purpose

This document defines the business capabilities of Sigmatics.

A business capability represents a stable area of responsibility that delivers measurable business value independent of the underlying technology, implementation or user interface.

Capabilities define **what Sigmatics does**, not **how it is implemented**.

These capabilities form the foundation for:

- Backend module boundaries
- Frontend feature organization
- API ownership
- Database design
- AI agent responsibilities
- Testing strategy
- Security model
- Future service decomposition

---

# Guiding Principles

The capability model follows these principles:

- Capabilities are business-driven.
- Each capability has a single primary responsibility.
- Capabilities communicate through well-defined contracts.
- Capabilities remain stable even when implementations evolve.
- AI agents are implementations of capabilities, not capabilities themselves.
- Capabilities may depend on other capabilities but should remain loosely coupled.

---

# Capability Hierarchy

```
SIGMATICS

├── Identity & Access
├── Broker Connectivity
├── Market Intelligence
├── Trading Intelligence
├── Trade Management
├── Portfolio Intelligence
├── Financial Intelligence
├── Learning Intelligence
├── Reporting
├── Administration
└── Platform Services
```

---

# Capability Catalogue

Each business capability is assigned a permanent identifier and mnemonic code.

The identifier provides traceability across requirements, architecture, implementation, testing and future releases.

| Capability ID | Capability Code | Capability Name | Capability Owner | Capability Owner |
|---------------|-----------------|-----------------|-----------------|-----------------|
| CAP-000 | CMP | Regulatory Compliance & User Consent | TBD | Planned |
| CAP-001 | IAM | Identity & Access | TBD | Planned |
| CAP-002 | BRC | Broker Connectivity | TBD | Planned |
| CAP-003 | MKT | Market Intelligence | TBD | Planned |
| CAP-004 | TRD | Trading Intelligence | TBD | Planned |
| CAP-005 | TMG | Trade Management | TBD | Planned |
| CAP-006 | PFI | Portfolio Intelligence | TBD | Planned |
| CAP-007 | FIN | Financial Intelligence | TBD | Planned |
| CAP-008 | LRN | Learning Intelligence | TBD | Planned |
| CAP-009 | RPT | Reporting | TBD | Planned |
| CAP-010 | ADM | Administration | TBD | Planned |
| CAP-011 | PLS | Platform Services | TBD | Planned |

---

# Capability Definitions

## CAP-000 — Regulatory Compliance & User Consent (CMP)

### Purpose

Manage user regulatory compliance acknowledgementsby the user.

### Responsibilities

- Present regulatory disclosures before any trading capability is enabled.
- Manage Terms of Use acceptance.
- Manage Privacy Policy acceptance.
- Manage AI Disclosure acceptance.
- Manage Risk Disclosure acceptance.
- Maintain version-controlled consent records.
- Record user acknowledgements for regulatory purposes.
- Prevent broker connectivity until mandatory consents are completed.
- Prevent live trading until all compliance prerequisites are satisfied.
- Maintain an immutable audit trail of compliance events.

### Inputs

- User registration.
- User login.
- Policy version updates.
- Regulatory updates.
- User consent actions.
- First trade initiation.
- Broker connection request.

### Outputs

- Compliance status.
- Consent records.
- Policy acceptance history.
- Broker access authorization.
- Trading eligibility.
- Compliance audit events.

 ### Dependencies

- IAM
- Notification Service
- Broker Connectivity
- Audit Service
- Configuration Service
- Owned Domain Objects
- TermsOfUse
- PrivacyPolicy
- RiskDisclosure
- AIDisclosure
- ConsentRecord
- ComplianceEvent

---

## CAP-001 — Identity & Access (IAM)

### Purpose

Manage user identity, authentication, authorization, compliance acknowledgements and user preferences.

### Responsibilities

- User registration
- Authentication
- Session management
- Compliance & Consent
- User Profile
- Trading Preferences
- Device Management
- Audit & Security

### Inputs

- User credentials
- Broker identity
- Consent documents

### Outputs

- Authenticated session
- Access token
- User profile
- Compliance status

---

## CAP-002 — Broker Connectivity (BRC)

### Purpose

Provide a broker-agnostic integration layer between Sigmatics and supported brokerage platforms.

### Responsibilities

- Broker authentication
- Order submission
- Order modification
- Order cancellation
- Order status synchronization
- Holdings synchronization
- Position synchronization

### Design Principle

Business logic must never depend directly on a broker-specific API.

---

## CAP-003 — Market Intelligence (MKT)

### Purpose

Continuously observe, ingest and interpret live market information.

### Responsibilities

- Market data ingestion
- Index monitoring
- Option chain monitoring
- OI analysis
- Volume analysis
- Volatility analysis
- Trend identification
- Market structure analysis
- Context analysis

### Primary AI Components

- Market Observer Agent
- Trend Agent
- Structure Agent
- Context Agent

---

## CAP-004 — Trading Intelligence (TRD)

### Purpose

Transform market intelligence into explainable trading recommendations.

### Responsibilities

- Strategy evaluation
- Signal generation
- Opportunity ranking
- Risk evaluation
- Option selection
- Execution planning
- Recommendation explainability

### Outputs

- Decision Contract
- Execution Plan
- Confidence Score
- Evidence Summary

### Primary AI Components

- Strategy Agent
- Risk Agent
- Option Selection Agent

---

## CAP-005 — Trade Management (TMG)

### Purpose

Manage the lifecycle of an active trade after execution.

### Responsibilities

- Position monitoring
- Stop-loss recommendations
- Target recommendations
- Trailing stop recommendations
- Manual exit support
- Trade state tracking
- Decision receipts
- Trade completion processing

### Design Principle

Trade Management begins only after broker-confirmed execution.

---

## CAP-006 — Portfolio Intelligence (PFI)

### Purpose

Provide continuous visibility into portfolio performance and investment positions.

### Responsibilities

- Holdings analysis
- Position valuation
- Buy / Hold / Sell recommendations
- Portfolio allocation
- Sector exposure
- Risk exposure

---

## CAP-007 — Financial Intelligence (FIN)

### Purpose

Transform trading and portfolio activity into actionable financial insights.

### Responsibilities

- P&L analysis
- Tax-ready summaries
- Capital utilisation
- Performance analytics
- Return analysis
- Financial dashboards

---

## CAP-008 — Learning Intelligence (LRN)

### Purpose

Observe historical decisions and generate validated improvement opportunities.

### Responsibilities

- Historical analysis
- Pattern discovery
- Hypothesis generation
- Backtest orchestration
- Paper trading evaluation

### Constraint

Learning shall never modify production behaviour automatically.

---

## CAP-009 — Reporting (RPT)

### Purpose

Provide structured operational, financial and analytical reports.

### Responsibilities

- Daily reports
- Weekly reports
- Monthly reports
- Yearly reports
- Trade history
- Portfolio reports
- Decision history
- Learning reports

---

## CAP-010 — Administration (ADM)

### Purpose

Support platform administration and operational governance.

### Responsibilities

- User management
- Broker management
- Feature flags
- Configuration
- System health
- Audit review

---

## CAP-011 — Platform Services (PLS)

### Purpose

Provide shared services used across all business capabilities.

### Responsibilities

- Notification Service
- Audit Service
- Replay Service
- Compliance Engine
- Logging
- Monitoring
- Configuration Service
- Event Bus
- Notification Management
    - Desktop Notifications
    - Mobile Push Notifications
    - In-App Notifications
    - Notification Preferences

---

# Capability Relationships

The following high-level interaction sequence describes the flow of business capabilities.

```
Identity & Access
        │
        ▼
Broker Connectivity
        │
        ▼
Market Intelligence
        │
        ▼
Trading Intelligence
        │
        ▼
Trade Management
        │
        ├────────► Portfolio Intelligence
        │
        ├────────► Financial Intelligence
        │
        ├────────► Reporting
        │
        └────────► Learning Intelligence
```

Platform Services support every capability.

---

# Future Evolution

The capability model has been intentionally designed to support future expansion.

Potential future capabilities include:

- AI Coach
- Strategy Marketplace
- Multi-Broker Execution
- Multi-Asset Trading
- Institutional Workspaces
- Compliance Dashboard
- Mobile Notifications
- Voice Assistant

---

# Closing Statement

The Business Capability Model represents the stable functional architecture of Sigmatics.

Implementations, technologies and AI models will evolve over time.

The capability model shall remain the primary reference for organizing responsibilities, defining module boundaries and guiding the long-term evolution of the platform.

---

# Capability Governance

The Business Capability Model is the authoritative representation of Sigmatics' functional architecture.

The following governance rules apply:

1. Business capabilities represent stable business responsibilities and shall not be created to mirror implementation details.

2. Every Functional Requirement shall trace back to exactly one primary business capability.

3. Every backend module shall have a clearly defined owning capability.

4. Every frontend module shall map to one or more business capabilities.

5. AI agents are implementations of capabilities and shall not define architectural boundaries.

6. Any modification to the capability hierarchy requires an approved Architecture Decision Record (ADR).

7. Capability identifiers (CAP-XXX) are immutable and shall never be reassigned.