from enum import Enum


class MarketSession(str, Enum):
    """
    Represents the trading session.
    """

    PRE_MARKET = "PRE_MARKET"

    REGULAR = "REGULAR"

    POST_MARKET = "POST_MARKET"

    CLOSED = "CLOSED"