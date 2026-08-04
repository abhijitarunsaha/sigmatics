from enum import Enum


class StageStatus(str, Enum):
    """
    Outcome of a Decision Stage execution.
    """

    SUCCESS = "SUCCESS"

    WAIT = "WAIT"

    SKIPPED = "SKIPPED"

    FAILED = "FAILED"

    VETO = "VETO"