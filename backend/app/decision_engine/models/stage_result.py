from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field

from app.decision_engine.models.decision_state import DecisionState
from app.decision_engine.models.evidence_bucket import EvidenceBucket
from app.decision_engine.models.stage_status import StageStatus


@dataclass(slots=True)
class StageResult:
    """
    Represents the outcome of a Decision Stage.
    """

    stage: str

    status: StageStatus

    decision_state: DecisionState | None = None

    evidence: EvidenceBucket | None = None

    observations: list[str] = field(
        default_factory=list,
    )

    @classmethod
    def success(
        cls,
        *,
        stage: str,
        observations: list[str] | None = None,
        evidence: EvidenceBucket | None = None,
        decision_state: DecisionState | None = None,
    ) -> "StageResult":
        """
        Creates a successful StageResult.
        """

        return cls(
            stage=stage,
            status=StageStatus.SUCCESS,
            decision_state=decision_state,
            evidence=evidence,
            observations=observations or [],
        )

    @classmethod
    def wait(
        cls,
        *,
        stage: str,
        observations: list[str] | None = None,
        decision_state: DecisionState | None = None,
    ) -> "StageResult":
        """
        Creates a WAIT StageResult.
        """

        return cls(
            stage=stage,
            status=StageStatus.WAIT,
            decision_state=decision_state,
            observations=observations or [],
        )

    @classmethod
    def failed(
        cls,
        *,
        stage: str,
        observations: list[str] | None = None,
        decision_state: DecisionState | None = None,
    ) -> "StageResult":
        """
        Creates a FAILED StageResult.
        """

        return cls(
            stage=stage,
            status=StageStatus.FAILED,
            decision_state=decision_state,
            observations=observations or [],
        )