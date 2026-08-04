from __future__ import annotations

from app.market_data.providers.kite.kite_session import (
    KiteSession,
)


class KiteFactory:
    """
    Factory responsible for constructing Kite infrastructure.
    """

    @staticmethod
    def create_session() -> KiteSession:

        return KiteSession()