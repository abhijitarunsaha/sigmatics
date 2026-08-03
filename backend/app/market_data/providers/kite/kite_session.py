from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class KiteSession:
    """
    Represents an authenticated Kite session.

    This class will later encapsulate the KiteConnect
    client instance, access token lifecycle, and session
    metadata.
    """

    authenticated: bool = False