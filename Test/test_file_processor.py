"""
Test Script: test_file_processor.py
Description: Tests the `FileProcessor` class for processing files with metadata and embeddings.

Run Instructions:
    pytest test_file_processor.py

Reset Instructions:
    No reset is necessary as the test removes the temporary file (`test_file.md`) after completion.
"""

import asyncio
from pathlib import Path
from config import Config
from file_handler import FileHandler
from file_processor import FileProcessor

async def test_file_processor():
    config = Config()
    processor = FileProcessor(config)
    test_file = Path("test_file.md")
    test_content = "# Test Metadata\nThis is the body of the test file."

    # Create a test file
    FileHandler.write_file(test_file, test_content)

    # Process the file
    if processor.should_process_file(test_file):
        result = await processor.validate_and_process_file(test_file)
        assert result["success"], f"Processing failed: {result.get('error', 'Unknown error')}"
    else:
        assert False, f"File {test_file} should have been valid for processing."

    # Cleanup
    test_file.unlink()
    assert not test_file.exists(), "Test file was not removed!"
