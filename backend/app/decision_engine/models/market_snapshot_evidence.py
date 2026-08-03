from __future__ import annotations

from dataclasses import dataclass

from app.decision_engine.models.evidence import Evidence
from app.market_data.models.market_snapshot import MarketSnapshot


@dataclass(slots=True)
class MarketSnapshotEvidence(Evidence):
    """
    Evidence produced by the Market Snapshot Stage.
    """

    snapshot: MarketSnapshot