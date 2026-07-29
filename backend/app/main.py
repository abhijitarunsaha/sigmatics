import logging

from app.core.config import settings
from app.core.logging import configure_logging
from app.decision_engine.orb import SigmaticsOrb


def bootstrap() -> None:

    configure_logging()

    logger = logging.getLogger("sigmatics.bootstrap")

    logger.info("=" * 60)
    logger.info("SIGMATICS")
    logger.info("=" * 60)

    logger.info(
        "Application : %s",
        settings.application_name,
    )

    logger.info(
        "Version     : %s",
        settings.version,
    )

    orb = SigmaticsOrb()

    orb.start()

    context = orb.execute()
    
    logger.info(
        "Decision Context : %s",
        context.decision_id,
    )

    logger.info("=" * 60)
    logger.info(
        "Orb Status : %s",
        orb.status.value,
    )
    logger.info(
        "Awaiting Market Snapshot..."
    )
    logger.info("=" * 60)


if __name__ == "__main__":
    bootstrap()