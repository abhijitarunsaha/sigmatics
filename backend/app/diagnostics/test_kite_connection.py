from __future__ import annotations

from requests import session

from app.market_data.providers.kite.kite_authenticator import (
    KiteAuthenticator,
)

from app.market_data.providers.kite.kite_client import (
    KiteClient,
)


def run() -> None:
    """
    Tests Kite connectivity.
    """

    print()

    print("=" * 60)
    print("SIGMATICS DIAGNOSTICS")
    print("=" * 60)

    print()
    print("Testing Kite Connectivity...")
    print()

    authenticator = KiteAuthenticator()

    session = authenticator.authenticate()

    client = KiteClient(session)
    
    print()

    print("Broker Profile")

    print("-" * 60)

    profile = client.profile()

    print(
        f"User Name : {profile['user_name']}"
    )

    print(
        f"User ID   : {profile['user_id']}"
    )

    print(
        f"Broker    : {profile['broker']}"
    )

    print()

    if client.health():

        print("[PASS] Kite Session Verified")

    else:

        print("[FAIL] Kite Session Invalid")

    print()

    print("=" * 60)
    print()


if __name__ == "__main__":
    run()