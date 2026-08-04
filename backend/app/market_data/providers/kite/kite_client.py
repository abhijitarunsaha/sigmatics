from __future__ import annotations

import logging

from kiteconnect import KiteConnect

from app.market_data.providers.kite.kite_session import (
    KiteSession,
)


class KiteClient:
    """
    Thin wrapper around the Kite SDK.

    This class isolates the rest of Sigmatics
    from the KiteConnect SDK.
    """

    def __init__(
        self,
        session: KiteSession,
    ) -> None:

        self._logger = logging.getLogger(__name__)

        self._session = session

    @property
    def client(
        self,
    ) -> KiteConnect:

        return self._session.client

    def health(self) -> bool:
        """
        Validates the current Kite session.
        """

        if not self._session.is_authenticated:

            return False

        try:

            self.client.profile()

            return True

        except Exception as ex:

            self._logger.exception(ex)

            return False

    def profile(
        self,
    ) -> dict:

        return self.client.profile()
    
    def quote(
        self,
        *symbols: str,
    ) -> dict:
        """
        Returns live quote data for one or more
        instruments.
        """

        return self.client.quote(
            list(symbols),
        )