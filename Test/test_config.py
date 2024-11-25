"""
Test Script: test_config.py
Description: Tests the `Config` class for loading, validation, and dynamic updates.

Run Instructions:
    pytest test_config.py

Reset Instructions:
    No reset is necessary as the test operates on mock data and does not modify persistent files or variables.
"""

from config import Config
import os

def test_load_default_config():
    # Test loading default configuration
    config = Config.load_default()
    assert config is not None, "Failed to load default configuration!"
    assert hasattr(config, "ollama_url"), "Default configuration missing 'ollama_url'!"

def test_env_variable_override(monkeypatch):
    # Test loading configuration with environment variable override
    monkeypatch.setenv("OLLAMA_URL", "http://mock-ollama-url")
    config = Config.load_default()
    assert config.ollama_url == "http://mock-ollama-url", "Environment variable override failed!"

def test_validate_config():
    # Test validation of required fields
    config = Config.load_default()
    try:
        config.validate()
    except Exception as e:
        assert False, f"Validation failed unexpectedly: {e}"

    # Test missing required field
    del config.ollama_url
    try:
        config.validate()
        assert False, "Validation should have failed for missing 'ollama_url'!"
    except Exception as e:
        assert "ollama_url" in str(e), "Unexpected validation error message!"

def test_dynamic_config_updates():
    # Test updating configuration dynamically
    config = Config.load_default()
    original_url = config.ollama_url
    config.ollama_url = "http://new-ollama-url"
    assert config.ollama_url == "http://new-ollama-url", "Dynamic update of configuration failed!"
    assert config.ollama_url != original_url, "Configuration did not update dynamically!"
