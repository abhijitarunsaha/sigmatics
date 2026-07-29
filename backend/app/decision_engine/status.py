from enum import Enum


class OrbStatus(str, Enum):
    """
    Lifecycle state of the Sigmatics Orb.
    """

    INITIALIZING = "INITIALIZING"

    IDLE = "IDLE"

    OBSERVING = "OBSERVING"

    BUILDING_CONFIDENCE = "BUILDING_CONFIDENCE"

    ACTIONABLE = "ACTIONABLE"

    EXECUTING = "EXECUTING"

    PAUSED = "PAUSED"

    ERROR = "ERROR"