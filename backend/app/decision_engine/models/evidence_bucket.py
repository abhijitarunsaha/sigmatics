from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from datetime import UTC
from datetime import datetime
from uuid import uuid4

from app.decision_engine.models.evidence import Evidence


@dataclass(slots=True)
class EvidenceBucket:

    bucket_id: str = field(default_factory=lambda: str(uuid4()))

    provider: str = ""

    evidence: Evidence | None = None

    timestamp: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )