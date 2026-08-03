from __future__ import annotations

from app.market_data.contracts.market_snapshot_provider import (
    MarketSnapshotProvider,
)
from app.market_data.models.market_snapshot import (
    MarketSnapshot,
)
from app.market_data.providers.kite.kite_session import (
    KiteSession,
)


class KiteMarketSnapshotProvider(
    MarketSnapshotProvider,
):
    """
    Retrieves the current market snapshot
    from Kite.
    """

    def __init__(
        self,
        session: KiteSession,
    ) -> None:

        self._session = session

    def get_snapshot(
        self,
    ) -> MarketSnapshot | None:

        return None