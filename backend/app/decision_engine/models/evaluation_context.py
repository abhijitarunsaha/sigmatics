from __future__ import annotations

from dataclasses import dataclass, field
from uuid import uuid4

from app.decision_engine.models.decision_evidence import DecisionEvidence
from app.decision_engine.models.decision_journal import DecisionJournal
from app.decision_engine.models.decision_state import DecisionState


@dataclass(slots=True)
class EvaluationContext:

    evaluation_id: str = field(
        default_factory=lambda: str(uuid4())
    )

    decision_state: DecisionState = (
        DecisionState.OBSERVING
    )

    evidence: DecisionEvidence = field(
        default_factory=DecisionEvidence
    )

    journal: DecisionJournal = field(
        default_factory=DecisionJournal
    )

    metadata: dict[str, object] = field(
        default_factory=dict
    )
    
    def summary(
        self,
    ) -> str:

        recommendation = getattr(
            self,
            "recommendation",
            None,
        )

        recommendation_text = (
            recommendation
            if recommendation
            else "WAIT"
        )

        lines: list[str] = []

        lines.append("=" * 60)
        lines.append("Evaluation Summary")
        lines.append("=" * 60)
        lines.append("")

        lines.append(
            f"Evaluation ID       : {self.evaluation_id}"
        )

        lines.append(
            f"Decision State      : {self.decision_state.name}"
        )

        lines.append(
            f"Recommendation      : {recommendation_text}"
        )

        lines.append(
            f"Evidence Buckets    : {len(self.evidence)}"
        )

        lines.append(
            f"Journal Entries     : {len(self.journal.entries)}"
        )

        lines.append("")
        lines.append("=" * 60)

        return "\n".join(lines)