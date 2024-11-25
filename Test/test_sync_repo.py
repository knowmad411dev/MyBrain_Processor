"""
Test Script: test_sync_repo.py
Description: Tests the `sync_repo.py` module for cloning or pulling a GitHub repository.

Run Instructions:
    pytest test_sync_repo.py

Reset Instructions:
    Remove the `test_repo` directory after running the test.
"""

from sync_repo import ensure_repository_synced
from pathlib import Path
import shutil

def test_sync_repo():
    repo_path = Path("test_repo")
    try:
        ensure_repository_synced(repo_path=repo_path)
        assert repo_path.exists(), "Repository was not cloned!"
    except Exception as e:
        assert False, f"Sync repository test failed: {e}"
    finally:
        shutil.rmtree(repo_path, ignore_errors=True)
        assert not repo_path.exists(), "Test repository directory was not removed!"
