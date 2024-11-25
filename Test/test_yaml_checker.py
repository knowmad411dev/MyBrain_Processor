"""
Test Script: test_yaml_checker.py
Description: Tests the `yaml_checker` module for extracting YAML metadata and categorizing files with and without YAML metadata.

Run Instructions:
    pytest test_yaml_checker.py

Reset Instructions:
    No reset is necessary as the test operates only on mock data and does not create or modify files.
"""

from yaml_checker import extract_yaml_metadata, split_yaml_files
from pathlib import Path

def test_extract_yaml_metadata():
    valid_yaml_content = "---\nkey: value\n---\nBody text"
    invalid_yaml_content = "---Invalid YAML---\nBody text"

    # Test valid YAML
    metadata = extract_yaml_metadata(valid_yaml_content)
    assert "key" in metadata, "Valid YAML extraction failed!"

    # Test invalid YAML
    metadata = extract_yaml_metadata(invalid_yaml_content)
    assert "error" in metadata, "Error handling for invalid YAML failed!"

def test_split_yaml_files():
    # Create mock file paths
    yaml_files = [Path(f"file{i}.yaml") for i in range(3)]
    non_yaml_files = [Path(f"file{i}.txt") for i in range(3)]
    all_files = yaml_files + non_yaml_files

    # Test splitting
    detected_yaml_files, detected_non_yaml_files = split_yaml_files(all_files)
    assert set(detected_yaml_files) == set(yaml_files), "Failed to detect YAML files!"
    assert set(detected_non_yaml_files) == set(non_yaml_files), "Failed to detect non-YAML files!"
