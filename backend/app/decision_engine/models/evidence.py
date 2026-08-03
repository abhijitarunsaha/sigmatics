from __future__ import annotations

from abc import ABC
from dataclasses import dataclass


@dataclass(slots=True)
class Evidence(ABC):
    """
    Base class for all evidence produced
    by Decision Stages.
    """