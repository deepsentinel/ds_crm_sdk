from loguru import logger
import sys
logger = logger.bind(name='ds_crm_sdk')


def set_logger_level(level: str):
    """
    Set the logging level for the ds_crm_sdk logger.
    :param level: The logging level to set (e.g., 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL').
    """
    logger.remove()
    logger.add(sys.stderr, level=level.upper())
    logger.info(f"[ds-crm-sdk] Logger level set to {level}")
