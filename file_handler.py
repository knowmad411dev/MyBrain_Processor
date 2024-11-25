# Updating file_handler.py to add file writing and improved logging

import logging
from pathlib import Path


class FileHandler:
    """
    Manages file operations such as reading and writing.
    """

    @staticmethod
    def read_file(file_path: Path) -> str:
        """
        Read the content of a file.

        Args:
            file_path (Path): The path to the file.

        Returns:
            str: The content of the file.

        Raises:
            FileNotFoundError: If the file does not exist.
            IOError: If an I/O error occurs.
        """
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
            return content
        except FileNotFoundError:
            logging.error(f"File not found: {file_path}. Please check the file path.")
            raise
        except IOError as e:
            logging.error(f"Error reading file {file_path}: {e}. Ensure the file is accessible.")
            raise

    @staticmethod
    def write_file(file_path: Path, content: str) -> None:
        """
        Write content to a file.

        Args:
            file_path (Path): The path to the file.
            content (str): The content to write to the file.

        Raises:
            IOError: If an I/O error occurs.
        """
        try:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(content)
            logging.info(f"Content written successfully to file: {file_path}")
        except IOError as e:
            logging.error(f"Error writing to file {file_path}: {e}. Ensure the file is writable.")
            raise


# Save the updated code for the user.
updated_file_handler_code = """
import logging
from pathlib import Path


class FileHandler:
    \"\"\"
    Manages file operations such as reading and writing.
    \"\"\"

    @staticmethod
    def read_file(file_path: Path) -> str:
        \"\"\"
        Read the content of a file.

        Args:
            file_path (Path): The path to the file.

        Returns:
            str: The content of the file.

        Raises:
            FileNotFoundError: If the file does not exist.
            IOError: If an I/O error occurs.
        \"\"\"
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
            return content
        except FileNotFoundError:
            logging.error(f"File not found: {file_path}. Please check the file path.")
            raise
        except IOError as e:
            logging.error(f"Error reading file {file_path}: {e}. Ensure the file is accessible.")
            raise

    @staticmethod
    def write_file(file_path: Path, content: str) -> None:
        \"\"\"
        Write content to a file.

        Args:
            file_path (Path): The path to the file.
            content (str): The content to write to the file.

        Raises:
            IOError: If an I/O error occurs.
        \"\"\"
        try:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(content)
            logging.info(f"Content written successfully to file: {file_path}")
        except IOError as e:
            logging.error(f"Error writing to file {file_path}: {e}. Ensure the file is writable.")
            raise
"""

# Save updated code for the user.
with open("/mnt/data/updated_file_handler.py", "w") as file:
    file.write(updated_file_handler_code)
