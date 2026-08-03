from __future__ import annotations

import logging

from app.decision_engine.models.evaluation_context import EvaluationContext
from app.decision_engine.runtime import OrbRuntime
from app.decision_engine.status import OrbStatus


class SigmaticsOrb:

    def __init__(self) -> None:

        self._logger = logging.getLogger(__name__)

        self._runtime: OrbRuntime | None = None

        self._status = OrbStatus.INITIALIZING

    @property
    def status(self) -> OrbStatus:
        return self._status

    def _transition_to(
        self,
        status: OrbStatus,
    ) -> None:

        self._logger.info(
            "Orb transition: %s → %s",
            self._status.value,
            status.value,
        )

        self._status = status

    def start(self) -> None:

        self._logger.info(
            "Starting Sigmatics Orb..."
        )

        self._runtime = OrbRuntime()

        self._transition_to(
            OrbStatus.IDLE,
        )

    def execute(self) -> EvaluationContext:
        """
        Execute a Decision Cycle.

        Currently executes an empty pipeline.
        """

        if self._runtime is None:
            raise RuntimeError(
                "Orb has not been started."
            )

        self._transition_to(
            OrbStatus.OBSERVING,
        )

        context = EvaluationContext()

        context = self._runtime.engine.evaluate(
            context,
        )

        self._logger.info(
            "\n%s",
            context.summary(),
        )

        self._logger.info(
            "\n%s",
            context.journal.pretty_print(),
        )
        
        self._transition_to(
            OrbStatus.IDLE,
        )

        return context