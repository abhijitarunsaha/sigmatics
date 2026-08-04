from __future__ import annotations

from abc import ABC
from abc import abstractmethod

from app.market_data.models.market_snapshot import MarketSnapshot


class MarketSnapshotProvider(ABC):
    """
    Contract for obtaining the current market snapshot.

    Implementations may fetch data from:

    - Mock Provider
    - Kite Provider
    - Replay Provider
    - Future Providers
    """

    @abstractmethod
    def get_snapshot(
        self,
    ) -> MarketSnapshot | None:
        """
        Returns the latest market snapshot.

        Returns
        -------
        MarketSnapshot | None

        Returns None if no snapshot is currently available.
        """