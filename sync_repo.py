# Updating sync_repo.py based on the suggested improvements

updated_sync_repo_code = """
import os
import logging
import subprocess

def get_github_pat():
    \"\"\"
    Read the GitHub PAT from an environment variable.
    \"\"\"
    github_pat = os.getenv("GITHUB_PAT")
    if not github_pat:
        raise ValueError("GitHub PAT is not set in environment variables.")
    return github_pat

def ensure_repository_synced(repo_path="/content/ollama-update"):
    \"\"\"
    Ensure the GitHub repository is synced at the specified path.
    If the repository does not exist, clone it.
    If the repository exists, pull the latest changes.
    \"\"\"
    github_pat = get_github_pat()
    repo_url = f"https://{github_pat}@github.com/knowmad411dev/ollama-update.git"

    # Save the original working directory
    original_cwd = os.getcwd()

    try:
        if not os.path.exists(repo_path):
            logging.info(f"Repository not found at {repo_path}. Cloning from GitHub...")
            subprocess.run(["git", "clone", repo_url, repo_path], check=True, timeout=120)
        else:
            logging.info(f"Repository found at {repo_path}. Pulling the latest changes...")
            os.chdir(repo_path)
            subprocess.run(["git", "pull", "origin", "main"], check=True, timeout=60)

        logging.info(f"Repository synced and ready at {repo_path}")
    except subprocess.TimeoutExpired:
        logging.error("Git operation timed out.")
        raise
    except subprocess.CalledProcessError as e:
        logging.error(f"Git operation failed: {e}")
        raise
    finally:
        os.chdir(original_cwd)
"""

# Save the updated file for the user
with open("/mnt/data/updated_sync_repo.py", "w") as file:
    file.write(updated_sync_repo_code)
