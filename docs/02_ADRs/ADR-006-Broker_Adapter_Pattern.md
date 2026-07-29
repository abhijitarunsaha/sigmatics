# ADR-006 — Broker Adapter Pattern

## Status

Accepted

---

## Context

Sigmatics is designed to support multiple brokerage platforms while maintaining a consistent trading experience.

Broker APIs differ significantly in their authentication mechanisms, order management APIs, market data formats, rate limits and operational capabilities.

Embedding broker-specific logic throughout the application would increase coupling and make future broker integrations difficult.

---

## Decision

All broker integrations shall implement a common Broker Adapter interface.

Each supported brokerage platform shall provide an independent adapter responsible for translating between broker-specific APIs and the internal Sigmatics integration contract.

Business capabilities shall communicate only with the Broker Adapter abstraction.

---

## Architectural Representation

Trading Intelligence

↓

Broker Integration Service

↓

Broker Adapter Interface

↓

├── Zerodha Adapter

├── Angel One Adapter

├── Dhan Adapter

├── Upstox Adapter

└── Paper Trading Adapter

---

## Consequences

### Benefits

- Broker independence.
- Simplified future integrations.
- Testability using mock adapters.
- Consistent business logic.
- Easier maintenance.

### Trade-offs

- Additional abstraction layer.
- Initial implementation effort.

---

## Alternatives Considered

### Direct Broker API Integration

Rejected.

Would require application-wide modifications whenever a broker changes its APIs.

---

## Related Capabilities

- CAP-002 – Broker Connectivity

---

## Related Functional Requirements

FR-BRC-001 to FR-BRC-030