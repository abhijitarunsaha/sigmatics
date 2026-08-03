from __future__ import annotations

from app.market_data.models.market_index import (
    MarketIndex,
)


class QuoteMapper:
    """
    Converts Kite quote payloads into
    MarketIndex domain models.
    """

    @staticmethod
    def to_market_index(
        symbol: str,
        quote: dict,
    ) -> MarketIndex:

        last_price = quote["last_price"]

        previous_close = quote["ohlc"]["close"]

        change = last_price - previous_close

        change_percent = (
            (change / previous_close) * 100
            if previous_close
            else 0.0
        )

        return MarketIndex(
            symbol=symbol,
            value=last_price,
            change=change,
            change_percent=change_percent,
        )