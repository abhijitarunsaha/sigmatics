from __future__ import annotations

import logging

from kiteconnect import KiteConnect

from app.core.config import get_settings
from app.market_data.providers.kite.kite_session import (
    KiteSession,
)


class KiteAuthenticator:
    """
    Responsible for creating Kite sessions.

    Authentication verification is delegated
    to KiteClient.
    """

    def __init__(self) -> None:

        self._logger = logging.getLogger(__name__)

        self._settings = get_settings()

    def authenticate(self) -> KiteSession:
        """
        Creates a Kite session using the configured
        API key and access token.
        """

        self._logger.info(
            "Orb Vision : Creating Kite session..."
        )

        client = KiteConnect(
            api_key=self._settings.kite.api_key,
        )

        access_token = (
            self._settings.kite.access_token
        )

        authenticated = False

        if access_token:

            client.set_access_token(
                access_token,
            )

            authenticated = True

            self._logger.info(
                "Access token attached."
            )

        else:

            self._logger.warning(
                "No access token configured."
            )

        return KiteSession(
            client=client,
            access_token=access_token,
            authenticated=authenticated,
        )