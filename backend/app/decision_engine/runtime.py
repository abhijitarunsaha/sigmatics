from __future__ import annotations

import logging

from app.decision_engine.engine import DecisionEngine
from app.decision_engine.pipeline import DecisionPipeline
from app.decision_engine.registry import StageRegistry


class OrbRuntime:
    """
    Runtime responsible for hosting
    the Decision Engine infrastructure.
    """

    def __init__(self) -> None:

        self._logger = logging.getLogger(__name__)

        self.registry = StageRegistry()

        self.pipeline = DecisionPipeline(
            self.registry,
        )

        self.engine = DecisionEngine(
            self.pipeline,
        )

        self._logger.info(
            "Orb Runtime initialized."
        )