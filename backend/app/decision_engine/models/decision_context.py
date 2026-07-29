from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC
from datetime import datetime
from uuid import uuid4


@dataclass(slots=True)
class DecisionContext:
    """
    Shared execution context that flows
    through the Decision Pipeline.

    Every stage enriches this object.
    """

    decision_id: str = field(default_factory=lambda: str(uuid4()))

    created_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )

    metadata: dict[str, object] = field(default_factory=dict)