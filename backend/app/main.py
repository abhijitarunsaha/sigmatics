import logging

from app.core.config import get_settings
from app.core.logging import configure_logging
from app.decision_engine.orb import SigmaticsOrb

def bootstrap() -> None:

    settings = get_settings()
    
    configure_logging()

    logger = logging.getLogger("sigmatics.bootstrap")

    logger.info("=" * 60)
    logger.info("SIGMATICS")
    logger.info("=" * 60)

    logger.info(
        "Application : %s",
        settings.app.name,
    )

    logger.info(
        "Version     : %s",
        settings.app.version,
    )

    orb = SigmaticsOrb()

    orb.start()

    context = orb.execute()
    
    logger.info(
        "Evaluation ID : %s",
        context.evaluation_id,
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