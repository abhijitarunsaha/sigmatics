from __future__ import annotations

from abc import ABC
from abc import abstractmethod

from app.decision_engine.models.decision_context import DecisionContext


class DecisionStage(ABC):
    """
    Contract implemented by every Decision Engine stage.

    Every stage receives a DecisionContext,
    enriches it with evidence,
    and returns the same context.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """
        Friendly stage name.
        """

    @abstractmethod
    def execute(
        self,
        context: DecisionContext,
    ) -> DecisionContext:
        """
        Execute the stage.
        """