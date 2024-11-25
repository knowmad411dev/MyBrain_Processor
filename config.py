# Updating config.py for security and dynamic path handling

from pathlib import Path
import os


class Config:
    """
    Configuration class to store application settings.
    """

    def __init__(self):
        # Logging configuration
        self.log_level = os.getenv("LOG_LEVEL", "INFO")  # Default to INFO if not set in the environment
        self.log_format = os.getenv("LOG_FORMAT", "%(asctime)s - %(levelname)s - %(message)s")
        self.log_file = os.getenv("LOG_FILE", "app.log")

        # GitHub configuration
        self.github_pat = os.getenv("GITHUB_PAT", "")  # Securely load from environment variables
        self.github_repo = os.getenv("GITHUB_REPO", "knowmad411dev/ollama-update")

        # File handling
        self.timestamp_file = Path(os.getenv("TIMESTAMP_FILE", str(Path.home() / "note_timestamps.json")))
        self.allowed_extensions = os.getenv("ALLOWED_EXTENSIONS", ".md,.txt,.yaml,.yml").split(",")

        # ChromaDB configuration
        self.chromadb_path = Path(os.getenv("CHROMADB_PATH", str(Path.home() / "ChromaDB")))

    @classmethod
    def load_default(cls):
        """
        Load default configuration settings.
        """
        return cls()

    def validate(self):
        """
        Validate critical configuration settings.
        Raises an error if any required setting is missing or invalid.
        """
        if not self.github_pat:
            raise ValueError("GitHub PAT is not configured. Set the GITHUB_PAT environment variable.")
        if not self.github_repo:
            raise ValueError("GitHub repository is not configured. Set the GITHUB_REPO environment variable.")
        if not self.chromadb_path:
            raise ValueError("ChromaDB path is not configured. Set the CHROMADB_PATH environment variable.")


# Save the updated code for the user.
updated_config_code = """
from pathlib import Path
import os


class Config:
    \"\"\"
    Configuration class to store application settings.
    \"\"\"

    def __init__(self):
        # Logging configuration
        self.log_level = os.getenv("LOG_LEVEL", "INFO")  # Default to INFO if not set in the environment
        self.log_format = os.getenv("LOG_FORMAT", "%(asctime)s - %(levelname)s - %(message)s")
        self.log_file = os.getenv("LOG_FILE", "app.log")

        # GitHub configuration
        self.github_pat = os.getenv("GITHUB_PAT", "")  # Securely load from environment variables
        self.github_repo = os.getenv("GITHUB_REPO", "knowmad411dev/ollama-update")

        # File handling
        self.timestamp_file = Path(os.getenv("TIMESTAMP_FILE", str(Path.home() / "note_timestamps.json")))
        self.allowed_extensions = os.getenv("ALLOWED_EXTENSIONS", ".md,.txt,.yaml,.yml").split(",")

        # ChromaDB configuration
        self.chromadb_path = Path(os.getenv("CHROMADB_PATH", str(Path.home() / "ChromaDB")))

    @classmethod
    def load_default(cls):
        \"\"\"
        Load default configuration settings.
        \"\"\"
        return cls()

    def validate(self):
        \"\"\"
        Validate critical configuration settings.
        Raises an error if any required setting is missing or invalid.
        \"\"\"
        if not self.github_pat:
            raise ValueError("GitHub PAT is not configured. Set the GITHUB_PAT environment variable.")
        if not self.github_repo:
            raise ValueError("GitHub repository is not configured. Set the GITHUB_REPO environment variable.")
        if not self.chromadb_path:
            raise ValueError("ChromaDB path is not configured. Set the CHROMADB_PATH environment variable.")
"""

# Save updated code for the user.
with open("/mnt/data/updated_config.py", "w") as file:
    file.write(updated_config_code)
