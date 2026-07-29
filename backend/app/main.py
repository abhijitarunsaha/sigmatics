import logging

from app.core.config import settings
from app.core.logging import configure_logging
from app.decision_engine.status import OrbStatus


def bootstrap() -> None:
    """
    Bootstraps the Sigmatics runtime.
    """

    configure_logging()

    logger = logging.getLogger("sigmatics.bootstrap")

    logger.info("=" * 60)
    logger.info("SIGMATICS")
    logger.info("=" * 60)

    logger.info("Application : %s", settings.application_name)
    logger.info("Version     : %s", settings.version)

    logger.info("Configuration Loaded")

    logger.info("Decision Pipeline Pending")

    logger.info("Decision Stages Pending")

    logger.info("Orb Status : %s", OrbStatus.INITIALIZING)

    logger.info("=" * 60)


if __name__ == "__main__":
    bootstrap()