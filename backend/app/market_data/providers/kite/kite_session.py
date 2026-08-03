from __future__ import annotations

from dataclasses import dataclass

from kiteconnect import KiteConnect


@dataclass(slots=True)
class KiteSession:
    """
    Represents an authenticated Kite session.
    """

    client: KiteConnect

    access_token: str

    authenticated: bool = False

    @property
    def is_authenticated(self) -> bool:

        return (
            self.authenticated
            and bool(self.access_token)
        )