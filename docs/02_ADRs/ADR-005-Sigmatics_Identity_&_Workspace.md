# ADR-005 — Sigmatics Identity & Workspace

## Status

Accepted

---

## Context

Sigmatics integrates with one or more external brokerage platforms to provide trading intelligence and execution assistance.

Brokerage platforms authenticate users independently and maintain their own account identities.

If Sigmatics relied solely on broker identities, the platform would become tightly coupled to broker implementations, limiting future capabilities such as multi-broker support, paper trading, portfolio analytics, subscription management and user personalization.

---

## Decision

Sigmatics shall maintain its own independent user identity.

Every registered user shall possess a unique Sigmatics account that represents the primary identity within the platform.

Brokerage accounts shall be treated as linked external resources rather than user identities.

The Sigmatics account shall own:

- User Profile
- Authentication
- Session Management
- Trading Preferences
- Notification Preferences
- Compliance Acknowledgements
- Decision History
- Reports
- Linked Brokerage Accounts

---

## Consequences

### Benefits

- Enables support for multiple brokers.
- Decouples user identity from brokerage identity.
- Supports paper trading.
- Supports future subscription models.
- Simplifies user preference management.
- Maintains historical data independent of broker connectivity.

### Trade-offs

- Additional authentication service must be maintained.
- User onboarding becomes a two-step process:
  - Sigmatics Registration
  - Broker Linking

---

## Alternatives Considered

### Broker-Only Identity

Rejected.

Would tightly couple Sigmatics to broker implementations and prevent independent platform evolution.

---

## Related Capabilities

- CAP-001 – Identity & Access
- CAP-002 – Broker Connectivity

---

## Related Functional Requirements

FR-IAM-001 to FR-IAM-026

FR-BRC-001 to FR-BRC-008