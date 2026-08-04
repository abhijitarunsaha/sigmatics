from __future__ import annotations

from dataclasses import dataclass, field

from app.decision_engine.models.evidence_bucket import EvidenceBucket


@dataclass(slots=True)
class DecisionJournalEntry:
    """
    Represents a single reasoning step
    performed during an evaluation.
    """

    stage: str

    status: str

    decision_state: str | None

    observations: list[str] = field(
        default_factory=list,
    )

    evidence_bucket: EvidenceBucket | None = None