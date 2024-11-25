"""
Handles detection and processing of YAML metadata in files.
"""

from pathlib import Path
from typing import Tuple, List, Dict
import yaml


def extract_yaml_metadata(file_path: Path) -> Tuple[bool, Dict]:
    """
    Extract YAML metadata from a file.

    Args:
        file_path (Path): Path to the file to check.

    Returns:
        Tuple[bool, Dict]: A tuple indicating YAML presence and the extracted metadata (if any).

    Notes:
        - YAML metadata must start with "---" and end with "---".
        - Returns an empty dictionary if metadata extraction fails or if no YAML block is found.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()
        if lines and lines[0].strip() == "---":
            end_idx = next(i for i, line in enumerate(lines[1:], 1) if line.strip() == "---")
            yaml_content = "\n".join(lines[1:end_idx])
            return True, yaml.safe_load(yaml_content)
    except Exception as e:
        return False, {}
    return False, {}


def split_yaml_files(files: List[Path]) -> Tuple[List[Path], List[Path]]:
    """
    Split files into those with and without YAML metadata.

    Args:
        files (List[Path]): List of file paths to process.

    Returns:
        Tuple[List[Path], List[Path]]: A tuple of two lists:
            - Files with YAML metadata.
            - Files without YAML metadata.

    Notes:
        - Uses `extract_yaml_metadata` to check and extract metadata for each file.
    """
    yaml_files = []
    non_yaml_files = []
    for file_path in files:
        has_yaml, _ = extract_yaml_metadata(file_path)
        if has_yaml:
            yaml_files.append(file_path)
        else:
            non_yaml_files.append(file_path)
    return yaml_files, non_yaml_files
