from __future__ import annotations

from app.decision_engine.registry import StageRegistry
from app.decision_engine.contracts.stage import DecisionStage


class DecisionPipeline:
    """
    Defines the ordered sequence of
    Decision Stages.

    The pipeline does not execute stages.

    Execution is orchestrated exclusively
    by the Decision Engine.
    """

    def __init__(
        self,
        registry: StageRegistry,
    ) -> None:

        self._registry = registry

    @property
    def stages(
        self,
    ) -> tuple[DecisionStage, ...]:

        return tuple(self._registry.stages)