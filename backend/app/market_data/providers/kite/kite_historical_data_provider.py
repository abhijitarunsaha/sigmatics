from __future__ import annotations

from datetime import datetime

from app.market_data.contracts.historical_data_provider import (
    HistoricalDataProvider,
)
from app.market_data.models.market_snapshot import (
    MarketSnapshot,
)
from app.market_data.providers.kite.kite_session import (
    KiteSession,
)


class KiteHistoricalDataProvider(
    HistoricalDataProvider,
):
    """
    Retrieves historical market data
    from Kite.
    """

    def __init__(
        self,
        session: KiteSession,
    ) -> None:

        self._session = session

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