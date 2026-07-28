# ADR-009: Compliance Gate Before Trading

| Attribute | Value |
|-----------|-------|
| ADR ID | ADR-009 |
| Title | Compliance Gate Before Trading |
| Status | Accepted |
| Date | YYYY-MM-DD |
| Authors | Sigmatics Architecture Team |

---

# Context

Sigmatics is an AI-native Trading Intelligence Platform intended for use in regulated financial markets.

The platform provides decision support for trading and portfolio management while allowing users to execute trades through supported brokerage integrations.

Indian financial regulations, including those prescribed by the Securities and Exchange Board of India (SEBI), require that users remain responsible for their own investment decisions. The platform must therefore ensure that users acknowledge applicable legal agreements, risk disclosures, and platform policies before any live trading capability is enabled.

Compliance shall not be treated as a user interface feature. It shall be implemented as a platform-wide architectural capability governing access to broker connectivity, trade execution and regulated functionality.

---

# Decision

Sigmatics shall implement a mandatory Compliance Gate prior to enabling any regulated trading capability.

No user shall be permitted to:

- Connect a brokerage account.
- Receive executable trade recommendations.
- Place live orders.
- Manage a connected trading portfolio.

until all mandatory compliance requirements have been satisfied.

The Compliance Gate shall verify:

- Terms of Use acceptance.
- Privacy Policy acceptance.
- Risk Disclosure acknowledgement.
- AI Disclosure acknowledgement.
- Applicable regulatory declarations.
- Version validity of all accepted policies.

Each acceptance shall be stored as an immutable compliance event with appropriate audit information.

---

# Rationale

This decision supports the following architectural principles:

- Compliance by Design
- Human-Governed Decision Making
- Explainable AI
- Auditability
- Regulatory Readiness

Separating compliance into its own architectural capability ensures that regulatory requirements remain enforceable regardless of user interface implementation or future platform integrations.

---

# Consequences

## Positive

- Regulatory requirements become centrally governed.
- Broker integrations remain protected by compliance checks.
- User consent is fully auditable.
- Future policy revisions become version-controlled.
- Additional jurisdictions can be supported without redesigning application flows.

## Negative

- Slightly longer onboarding flow.
- Additional persistence and audit infrastructure.
- Version management of legal documents.

These trade-offs are considered acceptable in exchange for improved regulatory compliance and legal defensibility.

---

# Architectural Principles

The following principles are established:

1. Compliance precedes capability.
2. Every regulated capability requires prior user consent where applicable.
3. User consent shall be version controlled.
4. Compliance events shall be immutable.
5. Trading shall always require explicit human approval.
6. AI recommendations are advisory and shall never bypass user confirmation.

---

# Related Documents

- CAP-000 – Regulatory Compliance & User Consent
- ADR-004 – Human Governed Decisions
- ADR-008 – Broker Adapter Pattern
- Business Capabilities
- Functional Requirements