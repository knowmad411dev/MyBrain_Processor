"""
Shared utility functions for the application.

This module provides reusable utilities such as logging configuration.
"""

import logging


def setup_logging(log_level: str, log_format: str, log_file: str) -> None:
    """
    Set up logging for the application.

    Args:
        log_level (str): Logging level (e.g., "INFO").
        log_format (str): Format string for log messages.
        log_file (str): File path to save log messages.

    Logs:
        - Info: Indicates that logging setup is complete.
    """
    logging.basicConfig(
        level=log_level,
        format=log_format,
        filename=log_file,
        filemode="a"
    )
    logging.info("Logging setup complete.")
