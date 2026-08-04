from __future__ import annotations

from datetime import datetime
from datetime import time
from zoneinfo import ZoneInfo

from app.market_data.models.market_session import (
    MarketSession,
)
from app.market_data.models.market_status import (
    MarketStatus,
)


class MarketCalendar:
    """
    Determines the current NSE market session.

    Version 1 supports:

    • IST timezone
    • Weekends
    • Pre-open
    • Regular session
    • Post-market

    Future versions will support:

    • NSE holidays
    • Muhurat Trading
    • MCX sessions
    • Half trading days
    """

    IST = ZoneInfo("Asia/Kolkata")

    PRE_OPEN_START = time(9, 0)
    REGULAR_START = time(9, 15)
    REGULAR_END = time(15, 30)
    POST_MARKET_END = time(16, 0)

    def current(
        self,
    ) -> tuple[
        MarketStatus,
        MarketSession,
    ]:

        now = datetime.now(
            self.IST,
        )

        #
        # Weekend
        #

        if now.weekday() >= 5:

            return (
                MarketStatus.CLOSED,
                MarketSession.CLOSED,
            )

        current = now.time()

        if current < self.PRE_OPEN_START:

            return (
                MarketStatus.CLOSED,
                MarketSession.CLOSED,
            )

        if current < self.REGULAR_START:

            return (
                MarketStatus.OPEN,
                MarketSession.PRE_MARKET,
            )

        if current <= self.REGULAR_END:

            return (
                MarketStatus.OPEN,
                MarketSession.REGULAR,
            )

        if current <= self.POST_MARKET_END:

            return (
                MarketStatus.CLOSED,
                MarketSession.POST_MARKET,
            )

        return (
            MarketStatus.CLOSED,
            MarketSession.CLOSED,
        )