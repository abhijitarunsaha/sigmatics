from __future__ import annotations

from app.decision_engine.contracts.stage import DecisionStage


class StageRegistry:
    """
    Registry responsible for maintaining
    the ordered list of Decision Stages.
    """

    def __init__(self) -> None:
        self._stages: list[DecisionStage] = []

    def register(
        self,
        stage: DecisionStage,
    ) -> None:
        """
        Register a Decision Stage.
        """

        self._stages.append(stage)

    @property
    def stages(self) -> tuple[DecisionStage, ...]:
        """
        Returns an immutable view
        of the registered stages.
        """

        return tuple(self._stages)