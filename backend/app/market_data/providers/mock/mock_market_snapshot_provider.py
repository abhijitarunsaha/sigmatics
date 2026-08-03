from __future__ import annotations

from app.market_data.contracts.market_snapshot_provider import (
    MarketSnapshotProvider,
)
from app.market_data.models.market_snapshot import MarketSnapshot


class MockMarketSnapshotProvider(
    MarketSnapshotProvider,
):
    """
    Temporary provider used during development.

    The provider intentionally returns no market
    data so that the Decision Engine exercises
    its WAIT behaviour.
    """

    def get_snapshot(
        self,
    ) -> MarketSnapshot | None:

        return None