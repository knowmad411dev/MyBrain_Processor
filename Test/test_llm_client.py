"""
Test Script: test_llm_client.py
Description: Tests the `LLMClient` class for generating embeddings and interacting with ChromaDB.

Run Instructions:
    pytest test_llm_client.py

Reset Instructions:
    Ensure any test embeddings are removed from ChromaDB after running the tests.
"""

from config import Config
from llm_client import LLMClient

def test_llm_client():
    config = Config()
    llm_client = LLMClient(config)

    # Test embedding generation
    test_text = "This is a test sentence."
    embedding = llm_client.generate_embedding(test_text)
    assert embedding is not None, "Embedding generation failed!"

    # Test connection
    try:
        llm_client._check_connection()
    except Exception as e:
        assert False, f"LLM connection test failed: {e}"
