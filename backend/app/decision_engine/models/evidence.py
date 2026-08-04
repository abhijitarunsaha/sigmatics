from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from dataclasses import dataclass

from app.decision_engine.models.evidence_type import (
    EvidenceType,
)


@dataclass(slots=True)
class Evidence(ABC):
    """
    Base class for all evidence produced
    by Decision Stages.
    """

    @property
    @abstractmethod
    def evidence_type(
        self,
    ) -> EvidenceType:
        """
        Returns the evidence category.
        """

    @abstractmethod
    def summary(
        self,
    ) -> list[str]:
        """
        Returns a display summary of
        the evidence.
        """