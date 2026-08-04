from __future__ import annotations

from dataclasses import dataclass

from app.decision_engine.models.evidence import (
    Evidence,
)
from app.decision_engine.models.evidence_type import (
    EvidenceType,
)

from app.market_data.models.market_snapshot import (
    MarketSnapshot,
)


@dataclass(slots=True)
class MarketSnapshotEvidence(Evidence):
    """
    Evidence produced from the
    Market Snapshot Stage.
    """

    snapshot: MarketSnapshot

    @property
    def evidence_type(
        self,
    ) -> EvidenceType:

        return EvidenceType.MARKET_SNAPSHOT
    
    def summary(
        self,
    ) -> list[str]:
        """
        Returns a human-readable summary of
        the market snapshot.
        """

        snapshot = self.snapshot

        return [

            f"Provider : {snapshot.source}",

            (
                "Captured : "
                f"{snapshot.captured_at.astimezone().strftime('%d-%b-%Y %H:%M:%S %Z')}"
            ),

            f"Status : {snapshot.status.value}",

            f"Session : {snapshot.session.value}",

            (
                "NIFTY : "
                f"{snapshot.nifty.value:,.2f} "
                f"({snapshot.nifty.change_percent:+.2f}%)"
            ),

            (
                "BANK NIFTY : "
                f"{snapshot.bank_nifty.value:,.2f} "
                f"({snapshot.bank_nifty.change_percent:+.2f}%)"
            ),

            (
                "SENSEX : "
                f"{snapshot.sensex.value:,.2f} "
                f"({snapshot.sensex.change_percent:+.2f}%)"
            ),

            (
                "INDIA VIX : "
                f"{snapshot.india_vix.value:,.2f} "
                f"({snapshot.india_vix.change_percent:+.2f}%)"
            ),
        ]