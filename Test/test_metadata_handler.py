"""
Test Script: test_metadata_handler.py
Description: Tests the `metadata_handler` module for extracting metadata from YAML frontmatter.

Run Instructions:
    pytest test_metadata_handler.py

Reset Instructions:
    No reset is necessary as the test operates only on strings.
"""

from metadata_handler import extract_metadata

def test_metadata_handler():
    valid_content = "---\nkey: value\n---\nBody text"
    invalid_content = "---Invalid YAML---\nBody text"

    # Test valid metadata
    metadata = extract_metadata(valid_content)
    assert "key" in metadata, "Valid metadata extraction failed!"

    # Test invalid metadata
    metadata = extract_metadata(invalid_content)
    assert "error" in metadata, "Error handling for invalid YAML failed!"
