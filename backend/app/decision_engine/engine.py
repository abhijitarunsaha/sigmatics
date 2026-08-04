from __future__ import annotations

import logging

from time import perf_counter

from app.decision_engine.models.decision_journal_entry import (
    DecisionJournalEntry,
)
from app.decision_engine.models.evaluation_context import (
    EvaluationContext,
)
from app.decision_engine.models.stage_result import StageResult
from app.decision_engine.models.stage_status import StageStatus
from app.decision_engine.pipeline import DecisionPipeline
from app.decision_engine.recorder.reasoning_recorder import (
    ReasoningRecorder,
)


class DecisionEngine:

    def __init__(
        self,
        pipeline: DecisionPipeline,
    ) -> None:

        self._logger = logging.getLogger(__name__)
        self._pipeline = pipeline

    def evaluate(
        self,
        context: EvaluationContext,
    ) -> EvaluationContext:

        evaluation_start = perf_counter()
        
        self._logger.info(
            "Starting Evaluation [%s]",
            context.evaluation_id,
        )

        recorder = ReasoningRecorder(
            context.journal,
        )

        for stage in self._pipeline.stages:

            self._logger.info(
                "Executing Stage [%s]",
                stage.name,
            )

            stage_start = perf_counter()

            result = stage.execute(
                context,
            )

            elapsed_ms = (
                perf_counter() - stage_start
            ) * 1000

            self._logger.info(
                "Completed Stage [%s] (%0.2f ms)",
                stage.name,
                elapsed_ms,
            )       

            self._process_stage_result(
                context=context,
                result=result,
                recorder=recorder,
            )

            if self._should_terminate(result):

                self._logger.info(
                    "Evaluation terminated at stage [%s]",
                    stage.name,
                )

                break
            
            evaluation_elapsed = (
                        perf_counter() - evaluation_start
                    ) * 1000
            
            self._logger.info(
                "Evaluation completed in %.2f ms",
                    evaluation_elapsed,
                )

        return context

    def _process_stage_result(
        self,
        *,
        context: EvaluationContext,
        result: StageResult,
        recorder: ReasoningRecorder,
    ) -> None:

        if result.evidence is not None:

            context.evidence.add(
                result.evidence,
            )
            
        self._logger.info(
            "StageResult evidence present: %s",
            result.evidence is not None,
        )

        recorder.record(
            DecisionJournalEntry(
                stage=result.stage,
                status=result.status.value,
                decision_state=(
                    result.decision_state.name
                    if result.decision_state
                    else None
                ),
                observations=result.observations,
                evidence_bucket=(
                    result.evidence
                    if result.evidence
                    else None
                ),
            )
        )

        if result.decision_state is not None:

            context.decision_state = (
                result.decision_state
            )
        
        self._logger.info(
            "[%s] -> %s",
            result.stage,
            result.status.value,
        )

    def _should_terminate(
        self,
        result: StageResult,
    ) -> bool:

        return result.status in (
            StageStatus.WAIT,
            StageStatus.VETO,
            StageStatus.FAILED,
        )