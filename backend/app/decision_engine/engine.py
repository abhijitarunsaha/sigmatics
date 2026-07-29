from __future__ import annotations

import logging

from app.decision_engine.models.decision_context import DecisionContext
from app.decision_engine.pipeline import DecisionPipeline


class DecisionEngine:
    """
    Core reasoning engine.
    """

    def __init__(
        self,
        pipeline: DecisionPipeline,
    ) -> None:

        self._logger = logging.getLogger(__name__)
        self._pipeline = pipeline

    def process(
        self,
        context: DecisionContext,
    ) -> DecisionContext:

        self._logger.info(
            "Decision Engine processing DecisionContext %s",
            context.decision_id,
        )

        return self._pipeline.execute(context)