from __future__ import annotations

from datetime import datetime

from app.market_data.contracts.historical_data_provider import (
    HistoricalDataProvider,
)
from app.market_data.models.market_snapshot import (
    MarketSnapshot,
)


class MockHistoricalDataProvider(
    HistoricalDataProvider,
):
    """
    Mock implementation used for
    testing and development.
    """

    def get_snapshot(
        self,
        at: datetime,
    ) -> MarketSnapshot | None:

        return None

    def get_snapshots(
        self,
        start: datetime,
        end: datetime,
    ) -> list[MarketSnapshot]:

        return []