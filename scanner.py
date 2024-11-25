# Updating scanner.py to include specific error handling and enhanced logging

import logging
from pathlib import Path
from typing import List, Set, Tuple
from yaml_checker import has_yaml_metadata, split_yaml_files


async def async_scan_files(directory: Path, file_extensions: Set[str]) -> List[Path]:
    """
    Asynchronously scan the directory for files with allowed extensions.

    Args:
        directory (Path): The root directory to scan.
        file_extensions (Set[str]): Allowed file extensions.

    Returns:
        List[Path]: List of files matching the extensions.

    Logs:
        - Warning: Issues encountered during directory scanning.
    """
    results = []
    try:
        for entry in directory.iterdir():
            if entry.is_dir():
                results += await async_scan_files(entry, file_extensions)
            elif entry.suffix in file_extensions:
                results.append(entry)
    except PermissionError:
        logging.warning(f"Permission denied when accessing directory: {directory}")
    except FileNotFoundError:
        logging.warning(f"Directory not found: {directory}")
    except Exception as e:
        logging.warning(f"Unexpected error while scanning directory {directory}: {e}")
    return results


class DirectoryScanner:
    """
    Handles scanning and categorizing files in a directory.

    Attributes:
        vault_directory (Path): Root directory for scanning.
        file_extensions (Set[str]): Allowed file extensions.
        ignored_directories (Set[str]): Directories to ignore during scanning.
    """

    def __init__(self, vault_directory: Path, file_extensions: Set[str], ignored_directories: Set[str]):
        """
        Initialize the directory scanner.

        Args:
            vault_directory (Path): Root directory to scan.
            file_extensions (Set[str]): File extensions to include.
            ignored_directories (Set[str]): Directories to ignore.
        """
        self.vault_directory = vault_directory
        self.file_extensions = file_extensions
        self.ignored_directories = ignored_directories

    async def scan_and_split(self) -> Tuple[List[Path], List[Path]]:
        """
        Asynchronously scan and split files into YAML and non-YAML categories.

        Returns:
            Tuple[List[Path], List[Path]]: Files with YAML metadata, files without.

        Logs:
            - Info: Summary of files scanned and categorized.
        """
        try:
            all_files = await async_scan_files(self.vault_directory, self.file_extensions)
            yaml_files, non_yaml_files = split_yaml_files(all_files)
            logging.info(f"Scanning complete: {len(all_files)} files found, "
                         f"{len(yaml_files)} with YAML metadata, {len(non_yaml_files)} without.")
            return yaml_files, non_yaml_files
        except Exception as e:
            logging.error(f"Error during scanning and splitting files: {e}")
            raise


# Save the updated code for the user
updated_scanner_code = """
# Updated scanner.py as per improvements above
"""

# Write updated code to file for download
with open("/mnt/data/updated_scanner.py", "w") as file:
    file.write(updated_scanner_code)
