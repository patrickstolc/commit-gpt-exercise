import argparse
import os
import git
import json
import time
import requests
from typing import List, Dict

SYSTEM_PROMPT = """
Instruct the LLM in what to do with the data that is provided to it.
"""
MODEL_NAME = ""  # TODO: Replace with the actual model name from ollama
API_ENDPOINT = ""  # TODO: Replace with the actual API endpoint from ollama

API_KEY = "YOUR_API_KEY"  # TODO: Replace with the actual API key from ollama (maybe not needed)
MAX_RETRIES = 3  # Number of retries for the LLM API call
BASE_DELAY = 1  # Base delay in seconds between retries


def is_git_repository(path: str) -> bool:
    try:
        _ = git.Repo(path).git_dir
        return True
    except git.exc.InvalidGitRepositoryError:
        return False


def get_git_diffs(repo_path: str) -> str:
    """
    Get the git diffs for the repository.
    --------------------------------------------------------------------------------
    Example output:
    [
        {
            "file": "main.py",
            "changes": "diff --git a/main.py b/main.py
            index c174289..6a1b2a8 100644
            --- a/main.py
            +++ b/main.py
            @@ -23,8 +23,10 @@ def is_git_repository(path: str) -> bool:
                def get_git_diffs(repo_path: str) -> List[Dict[str, str]]:
                    repo = git.Repo(repo_path)
                    diffs = []
                    -    for diff in repo.index.diff(None):
                    -        diffs.append({\"file\": diff.a_path, \"changes\": diff.diff.decode(\"utf-8\")})
                    +    for item in repo.index.diff(None):
                    +        diff_text = repo.git.diff(item.a_path)
                    +        diffs.append({\"file\": item.a_path, \"changes\": diff_text})
                    +    print(diffs)
                            return diffs


                    @@ -35,7 +37,7 @@ def generate_commit_message(diffs: List[Dict[str, str]]) -> str | None:
                    def call_llm_api(prompt: str) -> str | None:
                    # TODO: Implement LLM API call to generate commit message
                    -    return None
                    +    return \"hahah\"


                        def main():"
        }
    ]
    --------------------------------------------------------------------------------
    Args:
        repo_path (str): The path to the git repository.

    Returns:
        List[Dict[str, str]]: A list of dictionaries containing the file path and the changes.
    """
    repo = git.Repo(repo_path)
    diffs = []
    for item in repo.index.diff(None):
        """
        TODO: Implement the logic to get the git diffs

        Think about what should be passed to the LLM.
        Can you in any way guide the LLM to write a good commit message by preprocessing the data in any way?
        """
        diff_text = repo.git.diff(item.a_path)

        # remove lines without + or -
        diff_text = "\n".join(
            [
                line
                for line in diff_text.split("\n")
                if line.startswith("+") or line.startswith("-")
            ]
        )
        diffs.append(diff_text)

    return "\n".join(diffs)


def generate_commit_message(diffs: str) -> str | None:
    # TODO: Implement the logic to generate the commit message from the LLM response
    return None


def call_llm_api(prompt: str) -> str | None:
    # TODO: Implement the logic to call the LLM API
    return None


def main():
    parser = argparse.ArgumentParser(
        description="Generate commit message suggestions using an LLM."
    )
    parser.add_argument("repo_path", help="Path to the git repository")
    args = parser.parse_args()

    if not is_git_repository(args.repo_path):
        print("Error: The specified path is not a valid git repository.")
        return

    diffs = get_git_diffs(args.repo_path)
    if not diffs:
        print("No changes detected in the repository.")
        return

    try:
        commit_message = generate_commit_message(diffs)
        if commit_message is None:
            print("No commit message generated.")
            return

        print("Suggested commit message: ")
        print(commit_message)
    except Exception as e:
        print(f"An error occurred while generating the commit message: {str(e)}")
        print("Please try again later or write the commit message manually.")


if __name__ == "__main__":
    main()
