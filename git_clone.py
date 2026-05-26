"""Clone all repositories available to the authenticated GitHub user."""

import argparse
import os
import shutil
import subprocess

import httpx
import truststore
from dotenv import load_dotenv

truststore.inject_into_ssl()

load_dotenv()

gh_key = os.getenv('API_KEY')
gh_url = os.getenv('BASEURL', 'https://api.github.com')

current_directory = os.getcwd()


def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Clone all repositories available to the authenticated GitHub user."
    )
    parser.add_argument(
        "--protocol",
        choices=["https", "ssh"],
        default="https",
        help="Clone repositories using HTTPS or SSH URLs. Defaults to HTTPS.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print clone commands without running them.",
    )
    return parser.parse_args()


def get_github_token():
    """Get a GitHub token from API_KEY or an existing GitHub CLI login."""
    if gh_key:
        return gh_key

    if shutil.which("gh"):
        result = subprocess.run(
            ["gh", "auth", "token"],
            capture_output=True,
            check=False,
            text=True,
        )
        if result.returncode == 0 and result.stdout.strip():
            return result.stdout.strip()

    raise RuntimeError("No GitHub token found. Set API_KEY or run `gh auth login`.")


def get_repos(token):
    """Fetch all repositories available to the authenticated GitHub user."""
    repos = []
    page = 1
    headers = {"Authorization": f"Bearer {token}"}

    while True:
        response = httpx.get(
            f"{gh_url}/user/repos",
            headers=headers,
            params={"per_page": 100, "page": page},
        )
        response.raise_for_status()
        page_repos = response.json()

        if not page_repos:
            break

        repos.extend(page_repos)
        page += 1

    return repos


def clone_repos(repos, protocol, dry_run=False):
    """Clone repositories using the requested protocol."""
    for repo in repos:
        url = repo["ssh_url"] if protocol == "ssh" else repo["clone_url"]
        destination = os.path.join(current_directory, repo["name"])
        command = ["git", "clone", url]

        if os.path.exists(destination):
            print(f"Skipping {repo['full_name']}: {destination} already exists.")
            continue

        if dry_run:
            print(" ".join(command))
            continue

        subprocess.run(command, check=True)


def repo_clone(protocol, dry_run=False):
    """Clone all repos from a GitHub account."""
    token = get_github_token()
    repos = get_repos(token)
    clone_repos(repos, protocol, dry_run)


if __name__ == "__main__":
    args = parse_args()
    repo_clone(args.protocol, args.dry_run)
