import asyncio
import os
import subprocess
import sys

DUMMY_FILE_PATH = b"CHANGELOG.md"
REPO_PATH = "repos"
MONOREPO_PATH = os.path.join(REPO_PATH, "_monorepo")

MONOREPO_REPO = os.environ.get("MONOREPO_REPO")

REPOS = os.environ.get("REPOS", "").split(",")
REPOS = [repo.strip() for repo in REPOS if repo.strip()]

GITHUB_EMAIL = os.environ.get("GITHUB_EMAIL")


def process_repo(repo_url: str):
    repo_name = repo_url.split("/")[-1]
    repo_path = os.path.join(REPO_PATH, repo_name)

    try:
        subprocess.run(
            [
                "bash",
                "scripts/repo-process.sh",
                repo_url,
                repo_path,
                repo_name,
                GITHUB_EMAIL,
            ],
            check=True,
        )
    except subprocess.CalledProcessError:
        print(f"❌ Processing failed for {repo_name}")
        sys.exit(1)

    return repo_name


async def main():
    repo_names = [process_repo(repo) for repo in REPOS]

    subprocess.run(["bash", "scripts/monorepo-setup.sh", MONOREPO_REPO], check=True)

    for repo_name in repo_names:
        repo_path = os.path.join("..", repo_name)
        subprocess.run(
            ["bash", "scripts/monorepo-merge-repo.sh", repo_name, repo_path],
            check=True,
        )


if __name__ == "__main__":
    asyncio.run(main())
