from __future__ import annotations

from app.market_data.contracts.market_snapshot_provider import (
    MarketSnapshotProvider,
)
from app.market_data.models.market_snapshot import (
    MarketSnapshot,
)


class MarketSnapshotService:
    """
    Service responsible for retrieving the latest
    normalized market snapshot.

    The Decision Engine communicates only with this
    service and never directly with a provider.
    """

    def __init__(
        self,
        provider: MarketSnapshotProvider,
    ) -> None:

        self._provider = provider

    def get_snapshot(
        self,
    ) -> MarketSnapshot | None:
        """
        Returns the latest market snapshot.
        """

        return self._provider.get_snapshot()