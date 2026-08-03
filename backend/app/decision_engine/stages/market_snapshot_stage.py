from __future__ import annotations


from app.decision_engine.models.stage_result import (
    StageResult,
)
from app.decision_engine.models.stage_status import (
    StageStatus,
)

from app.market_data.services.market_snapshot_service import (
    MarketSnapshotService,
)
from app.decision_engine.contracts.stage import DecisionStage
from app.decision_engine.models.evaluation_context import EvaluationContext


class MarketSnapshotStage(
    DecisionStage,
):
    """
    Captures the current market snapshot.

    This is the first intelligence layer executed
    by the Orb.
    """

    name = "Market Snapshot"

    def __init__(
        self,
        service: MarketSnapshotService,
    ) -> None:

        self._service = service

    def execute(
        self,
        context: EvaluationContext,
    ) -> StageResult:

        snapshot = self._service.get_snapshot()

        if snapshot is None:

            return StageResult.wait(
                stage=self.name,
                observations=[
                    "No market snapshot available.",
                ],
            )

        context.market_snapshot = snapshot

        return StageResult.success(
            stage=self.name,
            observations=[
                (
                    f"Snapshot captured "
                    f"from {snapshot.source}"
                ),
                (
                    f"Captured At : "
                    f"{snapshot.captured_at.isoformat()}"
                ),
                (
                    f"Market Status : "
                    f"{snapshot.status.value}"
                ),
                (
                    f"Market Session : "
                    f"{snapshot.session.value}"
                ),
            ],
        )