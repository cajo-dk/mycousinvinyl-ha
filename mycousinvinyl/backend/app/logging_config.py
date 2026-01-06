import logging


def configure_logging(log_level: str) -> None:
    level_name = (log_level or "INFO").upper()
    level = logging._nameToLevel.get(level_name, logging.INFO)

    logging.basicConfig(level=level)

    sqlalchemy_logger = logging.getLogger("sqlalchemy.engine")
    if level <= logging.DEBUG:
        sqlalchemy_logger.setLevel(logging.INFO)
    else:
        sqlalchemy_logger.setLevel(logging.WARNING)
