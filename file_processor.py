import logging
from pathlib import Path
from llm_client import LLMClient
from metadata_handler import extract_metadata
from file_handler import FileHandler
from chunker import chunk_content_with_metadata
import asyncio


class FileProcessor:
    """
    Processes files for metadata extraction and embedding storage.
    """

    def __init__(self, config):
        """
        Initialize the file processor with the provided configuration.

        Args:
            config (Config): Configuration object containing settings.
        """
        self.config = config
        self.llm_client = LLMClient(config)

    def should_process_file(self, file_path: Path) -> bool:
        """
        Determine if a file should be processed based on its extension.

        Args:
            file_path (Path): The path of the file to check.

        Returns:
            bool: True if the file should be processed, False otherwise.
        """
        return file_path.suffix in set(self.config.allowed_extensions)

    async def validate_and_process_file(self, file_path: Path) -> dict:
        """
        Validate and process a file by extracting metadata, chunking, and storing embeddings.

        Args:
            file_path (Path): The path of the file to process.

        Returns:
            dict: Result of the processing operation.
        """
        try:
            # Read file content
            content = FileHandler.read_file(file_path)

            if not content.strip():
                raise ValueError(f"File {file_path} is empty or contains only whitespace.")

            # Extract metadata
            metadata = extract_metadata(content)
            metadata["file_path"] = str(file_path)

            # Generate chunks with metadata
            chunk_generator = chunk_content_with_metadata(content, metadata, chunk_size=500, overlap=50)

            # Process each chunk
            results = []
            for chunk_num, chunk_data in enumerate(chunk_generator, start=1):
                result = await self.llm_client.save_embedding(chunk_data["chunk"], chunk_data["metadata"], f"{file_path}_{chunk_num}")
                results.append(result)

            logging.info(f"Successfully processed file: {file_path}")
            return {"success": True, "results": results}
        except Exception as e:
            logging.error(f"Error processing file {file_path}: {e}")
            return {"success": False, "error": str(e)}

    async def process_files_in_parallel(self, file_paths: list, max_workers: int = 5):
        """
        Process multiple files concurrently.

        Args:
            file_paths (list): List of file paths to process.
            max_workers (int): Maximum number of parallel workers.
        """
        loop = asyncio.get_event_loop()
        tasks = [self.validate_and_process_file(file_path) for file_path in file_paths]
        results = await asyncio.gather(*tasks)
        for result in results:
            if result["success"]:
                logging.info(f"Processed file successfully: {result}")
            else:
                logging.error(f"File processing failed: {result['error']}")
