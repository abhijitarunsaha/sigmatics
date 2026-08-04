import logging
import sys

from app.core.config import get_settings


LOG_FORMAT = (
    "%(asctime)s | "
    "%(levelname)-8s | "
    "%(name)-25s | "
    "%(message)s"
)

settings = get_settings()


def configure_logging() -> None:
    """
    Configure global logging.
    """

    logging.basicConfig(
        level=settings.log.log_level,
        format=LOG_FORMAT,
        stream=sys.stdout,
        force=True,
    )