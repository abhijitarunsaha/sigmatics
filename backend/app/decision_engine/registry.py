from app.decision_engine.stages.market_snapshot_stage import (
    MarketSnapshotStage,
)

from app.market_data.providers.mock.mock_market_snapshot_provider import (
    MockMarketSnapshotProvider,
)

from app.market_data.services.market_snapshot_service import (
    MarketSnapshotService,
)


class StageRegistry:

    def __init__(self) -> None:

        market_snapshot_provider = (
            MockMarketSnapshotProvider()
        )

        market_snapshot_service = (
            MarketSnapshotService(
                market_snapshot_provider,
            )
        )

        self._stages = (
            MarketSnapshotStage(
                service=market_snapshot_service,
            ),
        )

    @property
    def stages(self):

        return self._stages