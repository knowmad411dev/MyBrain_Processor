"""
Test Script: test_scanner.py
Description: Tests the `DirectoryScanner` class for scanning and categorizing files with and without YAML metadata.

Run Instructions:
    pytest test_scanner.py

Reset Instructions:
    Remove the `test_dir` directory after running the test.
"""

from pathlib import Path
from scanner import DirectoryScanner

def test_scanner():
    test_dir = Path("test_dir")
    test_dir.mkdir(exist_ok=True)

    # Create test files
    (test_dir / "file1.md").write_text("---\nmetadata: test\n---\nContent 1")
    (test_dir / "file2.txt").write_text("No metadata")
    (test_dir / "file3.yaml").write_text("---\nmetadata: test\n---")

    # Initialize scanner
    scanner = DirectoryScanner(test_dir, {".md", ".txt", ".yaml"}, set())

    # Scan and split files
    yaml_files, non_yaml_files = scanner.scan_and_split()
    assert len(yaml_files) == 2, "Failed to detect YAML files!"
    assert len(non_yaml_files) == 1, "Failed to detect non-YAML files!"

    # Cleanup
    for file in test_dir.iterdir():
        file.unlink()
    test_dir.rmdir()
    assert not test_dir.exists(), "Test directory was not removed!"
