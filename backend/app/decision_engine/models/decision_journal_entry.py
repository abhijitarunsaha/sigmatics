from __future__ import annotations

from dataclasses import dataclass, field


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

    evidence_bucket_id: str | None = None