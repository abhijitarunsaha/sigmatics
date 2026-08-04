from __future__ import annotations

from abc import ABC
from abc import abstractmethod

from app.decision_engine.models.evaluation_context import (
    EvaluationContext,
)
from app.decision_engine.models.stage_result import (
    StageResult,
)


class DecisionStage(ABC):
    """
    Represents a single reasoning stage
    within the Decision Pipeline.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        ...

    @abstractmethod
    def execute(
        self,
        context: EvaluationContext,
    ) -> StageResult:
        """
        Executes the stage and returns
        the observations produced by it.

        The stage must NOT mutate the
        EvaluationContext.
        """