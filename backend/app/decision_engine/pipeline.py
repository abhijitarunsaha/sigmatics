from __future__ import annotations

import logging

from app.decision_engine.models.decision_context import DecisionContext
from app.decision_engine.registry import StageRegistry


class DecisionPipeline:
    """
    Executes registered Decision Stages.
    """

    def __init__(
        self,
        registry: StageRegistry,
    ) -> None:

        self._logger = logging.getLogger(__name__)
        self._registry = registry

    def execute(
        self,
        context: DecisionContext,
    ) -> DecisionContext:

        self._logger.info(
            "Executing Decision Pipeline (%d stages)",
            len(self._registry.stages),
        )

        for stage in self._registry.stages:

            self._logger.info(
                "Executing stage: %s",
                stage.name,
            )

            context = stage.execute(context)

        return context