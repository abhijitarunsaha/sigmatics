from enum import Enum


class MarketStatus(str, Enum):
    """
    Represents the current status of the market.
    """

    PRE_OPEN = "PRE_OPEN"

    OPEN = "OPEN"

    CLOSED = "CLOSED"

    HOLIDAY = "HOLIDAY"

    POST_CLOSE = "POST_CLOSE"

    UNKNOWN = "UNKNOWN"