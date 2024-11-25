import logging
from typing import Generator, Dict
import re


def validate_chunk_params(content: str, chunk_size: int, overlap: int):
    """
    Validate parameters for chunking.
    """
    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than 0.")
    if overlap < 0:
        raise ValueError("overlap must be non-negative.")
    if chunk_size <= overlap:
        raise ValueError("chunk_size must be greater than overlap.")
    if len(content) == 0:
        raise ValueError("Content cannot be empty.")


def extract_code_blocks(content: str) -> list:
    """
    Extract code blocks from the content.

    Args:
        content (str): Full content to extract code from.

    Returns:
        list: List of tuples with start index, end index, and code block.
    """
    code_pattern = r"```[\s\S]*?```"
    matches = [(m.start(), m.end(), m.group()) for m in re.finditer(code_pattern, content)]
    return matches


def chunk_content_with_metadata(content: str, metadata: dict, chunk_size: int, overlap: int = 0) -> Generator[Dict, None, None]:
    """
    Generate chunks of content with optional overlap, distinguishing code and text.
    Includes metadata with each chunk.

    Args:
        content (str): The file content to split into chunks.
        metadata (dict): Metadata extracted from the file.
        chunk_size (int): Maximum size of each chunk.
        overlap (int): Number of overlapping characters between chunks.

    Yields:
        Dict: A dictionary containing chunk data, type (text/code), and metadata.

    Logs:
        - Info: Number of chunks generated (logged after yielding all chunks).
    """
    validate_chunk_params(content, chunk_size, overlap)
    chunks = []
    code_blocks = extract_code_blocks(content)

    # Remove code blocks and keep only text
    for start_idx, end_idx, code in code_blocks:
        content = content[:start_idx] + " " * (end_idx - start_idx) + content[end_idx:]
        chunks.append({"chunk": code, "type": "code", "metadata": metadata})

    # Chunk remaining text
    chunk_count = 0
    for i in range(0, len(content), chunk_size - overlap):
        chunk = content[i:i + chunk_size].strip()
        if chunk:
            chunks.append({"chunk": chunk, "type": "text", "metadata": metadata})
            chunk_count += 1

    for chunk in chunks:
        yield chunk

    logging.info(f"Generated {chunk_count} text chunks and {len(code_blocks)} code blocks.")


# Example usage:
# metadata = {"title": "My Note", "tags": ["AI", "Learning"]}
# content = "This is a test note.\n```python\nprint('Hello, World!')\n```\nEnd of note."
# for chunk in chunk_content_with_metadata(content, metadata, 100, 10):
#     print(chunk)
