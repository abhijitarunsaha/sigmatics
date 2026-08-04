from __future__ import annotations

import logging
from datetime import UTC
from datetime import datetime

from app.market_data.contracts.market_snapshot_provider import (
    MarketSnapshotProvider,
)
from app.market_data.models.market_session import MarketSession
from app.market_data.models.market_snapshot import MarketSnapshot
from app.market_data.models.market_status import MarketStatus

from app.market_data.providers.kite.kite_authenticator import (
    KiteAuthenticator,
)
from app.market_data.providers.kite.kite_client import (
    KiteClient,
)
from app.market_data.providers.kite.quote_mapper import (
    QuoteMapper,
)
from app.market_data.services.market_calendar import (
    MarketCalendar,
)


class KiteMarketSnapshotProvider(
    MarketSnapshotProvider,
):
    """
    Produces a live MarketSnapshot
    using Zerodha Kite.
    """

    def __init__(self) -> None:

        self._logger = logging.getLogger(__name__)

        authenticator = KiteAuthenticator()

        session = authenticator.authenticate()

        self._client = KiteClient(
            session,
        )
        
        self._calendar = MarketCalendar()

    def get_snapshot(
        self,
    ) -> MarketSnapshot | None:

        if not self._client.health():

            self._logger.warning(
                "Kite connection unavailable."
            )

            return None

        #
        # Fetch profile simply to prove
        # connectivity.
        #

        quotes = self._client.quote(
            "NSE:NIFTY 50",
            "NSE:NIFTY BANK",
            "BSE:SENSEX",
            "NSE:INDIA VIX",
        )
        
        nifty = QuoteMapper.to_market_index(
            "NIFTY 50",
            quotes["NSE:NIFTY 50"],
        )

        bank_nifty = QuoteMapper.to_market_index(
            "BANK NIFTY",
            quotes["NSE:NIFTY BANK"],
        )

        sensex = QuoteMapper.to_market_index(
            "SENSEX",
            quotes["BSE:SENSEX"],
        )

        india_vix = QuoteMapper.to_market_index(
            "INDIA VIX",
            quotes["NSE:INDIA VIX"],
        )

        status, session = (
            self._calendar.current()
        )

        return MarketSnapshot.create(
            source="kite",
            status=status,
            session=session,
            nifty=nifty,
            bank_nifty=bank_nifty,
            sensex=sensex,
            india_vix=india_vix,
        )