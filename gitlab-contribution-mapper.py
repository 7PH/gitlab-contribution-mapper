import asyncio
import os

EMAILS = [b"benjamin.raymond@cern.ch"]
DUMMY_FILE_PATH = b"CHANGELOG.md"
REPO_FILE_PATH = "repos.txt"


def get_repos():
    with open(REPO_FILE_PATH) as f:
        for line in f:
            repo = line.strip()
            if repo:
                yield repo


def process_repo(repo_url: str):
    # Clone the repository in repos/{repo}
    repo_name = repo_url.split("/")[-1]
    repo_path = os.path.join("repos", repo_name)
    os.system(f"rm -rf {repo_path}")
    os.makedirs(repo_path, exist_ok=True)
    os.system(f"git clone {repo_url} {repo_path}")

    # Run filter-repo.py from the cloned repository
    os.system(f"cd {repo_path} && python ../../filter-repo.py")

    return repo_name


async def main():
    # Process all the repos
    repos = get_repos()
    for repo in repos:
        process_repo(repo)


if __name__ == "__main__":
    asyncio.run(main())
