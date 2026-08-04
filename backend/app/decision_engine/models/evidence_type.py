from __future__ import annotations

from enum import Enum


class EvidenceType(str, Enum):
    """
    Categorizes evidence produced during
    an evaluation.
    """

    MARKET_SNAPSHOT = "Market Snapshot"

    TREND = "Trend"

    MOMENTUM = "Momentum"

    VOLATILITY = "Volatility"

    MARKET_STRUCTURE = "Market Structure"

    OPTIONS = "Options"

    RISK = "Risk"

    TRADE_SETUP = "Trade Setup"