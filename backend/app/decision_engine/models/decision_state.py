from enum import Enum


class DecisionState(str, Enum):
    """
    Represents the current reasoning state of an evaluation.
    """

    OBSERVING = "OBSERVING"

    WAITING_FOR_EVIDENCE = "WAITING_FOR_EVIDENCE"

    BUILDING_CONFIDENCE = "BUILDING_CONFIDENCE"

    ACTIONABLE = "ACTIONABLE"

    REJECTED = "REJECTED"

    COMPLETED = "COMPLETED"