from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field

from app.decision_engine.models.evidence_bucket import EvidenceBucket


@dataclass(slots=True)
class DecisionEvidence:

    buckets: list[EvidenceBucket] = field(
        default_factory=list
    )

    def add(
        self,
        bucket: EvidenceBucket,
    ) -> None:
        """
        Adds an evidence bucket.
        """
        self.buckets.append(bucket)
    
    def count(self) -> int:
        return len(self.buckets)
    
    def __len__(
        self,
    ) -> int:

        return self.count()