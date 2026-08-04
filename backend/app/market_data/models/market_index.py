from dataclasses import dataclass


@dataclass(slots=True)
class MarketIndex:
    """
    Represents a market index snapshot.
    """

    symbol: str

    value: float

    change: float

    change_percent: float