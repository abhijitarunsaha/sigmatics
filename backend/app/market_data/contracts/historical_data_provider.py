from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from datetime import datetime

from app.market_data.models.market_snapshot import MarketSnapshot


class HistoricalDataProvider(ABC):
    """
    Contract for retrieving historical market snapshots.
    """

    @abstractmethod
    def get_snapshot(
        self,
        at: datetime,
    ) -> MarketSnapshot | None:
        """
        Returns the market snapshot
        for the specified point in time.
        """

    @abstractmethod
    def get_snapshots(
        self,
        start: datetime,
        end: datetime,
    ) -> list[MarketSnapshot]:
        """
        Returns all snapshots
        between the supplied timestamps.
        """