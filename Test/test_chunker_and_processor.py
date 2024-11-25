"""
Test Script: test_chunker_and_processor.py
Description: Tests the functionality of `chunker.py` and `chunk_processor.py`, including content chunking and processing.

Run Instructions:
    pytest test_chunker_and_processor.py

Reset Instructions:
    No reset is necessary as this script only uses in-memory mock data.
"""

from chunker import chunk_content_generator
from chunk_processor import process_chunk_limited
import asyncio

async def test_chunk_processing():
    test_content = "This is a test sentence. " * 10
    chunks = list(chunk_content_generator(test_content, chunk_size=50, overlap=10))
    assert len(chunks) > 0, "No chunks were generated!"

    async def mock_llm_client(chunk):
        return f"Processed: {chunk}"

    semaphore = asyncio.Semaphore(2)
    results = await asyncio.gather(
        *[process_chunk_limited(chunk["chunk"], semaphore, mock_llm_client, "test_file", i + 1, len(chunks))
          for i, chunk in enumerate(chunks)]
    )
    assert all(results), "Some chunks were not processed successfully!"
