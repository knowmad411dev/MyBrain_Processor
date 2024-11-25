"""
Test Script: test_utils.py
Description: Tests the `setup_logging` function for proper log configuration.

Run Instructions:
    pytest test_utils.py

Reset Instructions:
    No reset is necessary as the test removes the temporary log file (`test.log`) after completion.
"""

import logging
from utils import setup_logging
from pathlib import Path

def test_setup_logging():
    log_file = "test.log"
    setup_logging("DEBUG", "%(asctime)s - %(levelname)s - %(message)s", log_file)

    # Log messages
    logging.debug("This is a debug message.")
    logging.info("This is an info message.")
    logging.warning("This is a warning message.")
    logging.error("This is an error message.")

    # Validate log file
    with open(log_file, "r") as file:
        content = file.read()
        assert "This is a debug message." in content, "Debug message not logged!"
        assert "This is an info message." in content, "Info message not logged!"
        assert "This is a warning message." in content, "Warning message not logged!"
        assert "This is an error message." in content, "Error message not logged!"

    # Cleanup
    Path(log_file).unlink()
    assert not Path(log_file).exists(), "Test log file was not removed!"
