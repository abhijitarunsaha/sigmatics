# ADR-007 — Observation Before Decision

## Status

Accepted

---

## Context

Trading recommendations should never be generated directly from raw market data.

Market conditions are dynamic, noisy and often contradictory. Different analytical components require a consistent representation of the market before performing specialized analysis.

Coupling trading decisions directly to broker data would reduce explainability, reproducibility and maintainability.

---

## Decision

Sigmatics shall separate market observation from trading decision making.

The Market Intelligence capability shall continuously observe and normalize market information before passing a unified market state to downstream decision-making capabilities.

Trading Intelligence shall consume only the normalized market state and shall not access raw broker market feeds directly.

---

## Decision Flow

Market Data

↓

Observe

↓

Normalize

↓

Validate

↓

Contextualize

↓

Publish Market State

↓

Trading Intelligence

↓

Trade Recommendation

---

## Consequences

### Benefits

- Clear separation of responsibilities.
- Improved explainability.
- Easier testing.
- Deterministic replay.
- Broker independence.

### Trade-offs

- Additional processing stage.
- Slight increase in architectural complexity.

---

## Alternatives Considered

### Trading directly from broker feeds

Rejected.

Would tightly couple trading logic to data providers and reduce explainability.

---

## Related Capabilities

CAP-003 – Market Intelligence

CAP-004 – Trading Intelligence

CAP-005 – Trade Management