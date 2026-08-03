from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC
from datetime import datetime

from app.market_data.models.market_index import MarketIndex
from app.market_data.models.market_session import MarketSession
from app.market_data.models.market_status import MarketStatus


@dataclass(slots=True)
class MarketSnapshot:
    """
    Represents the current market snapshot.

    This is a normalized domain model produced by the
    Market Data subsystem and consumed by the Decision Engine.
    """

    captured_at: datetime

    source: str

    status: MarketStatus

    session: MarketSession

    nifty: MarketIndex

    bank_nifty: MarketIndex

    sensex: MarketIndex

    india_vix: MarketIndex
    
    def is_market_open(self) -> bool:
        """
        Returns whether the market
        is currently open.
        """

        return self.status == MarketStatus.OPEN

    @classmethod
    def create(
        cls,
        *,
        source: str,
        status: MarketStatus,
        session: MarketSession,
        nifty: MarketIndex,
        bank_nifty: MarketIndex,
        sensex: MarketIndex,
        india_vix: MarketIndex,
        captured_at: datetime | None = None,
    ) -> "MarketSnapshot":

        return cls(
            captured_at=captured_at or datetime.now(UTC),
            source=source,
            status=status,
            session=session,
            nifty=nifty,
            bank_nifty=bank_nifty,
            sensex=sensex,
            india_vix=india_vix,
        )