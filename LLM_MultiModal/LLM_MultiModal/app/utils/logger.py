"""
Centralized logger configuration.

This module provides a reusable logger across all
implementations in the project.
"""

import logging


def get_logger(logger_name: str) -> logging.Logger:
    """
    Create and return a configured logger instance.
    """

    logger = logging.getLogger(logger_name)

    if not logger.handlers:

        logger.setLevel(logging.INFO)

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
        )

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        logger.addHandler(console_handler)

    return logger
