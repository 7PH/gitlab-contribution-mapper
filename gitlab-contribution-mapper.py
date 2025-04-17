import asyncio
import os

REPO_FILE_PATH = "repos.txt"


def get_repos():
    with open(REPO_FILE_PATH) as f:
        for line in f:
            repo = line.strip()
            if repo:
                yield repo


async def process_repo(repo_url: str):
    # Clone the repository in repos/{repo}
    repo_name = repo_url.split("/")[-1]
    repo_path = os.path.join("repos", repo_name)
    os.system(f"rm -rf {repo_path}")
    os.makedirs(repo_path, exist_ok=True)
    os.system(f"git clone {repo_url} {repo_path}")

    # Execute `run-git-filter-repo.sh`
    os.system(f"cd {repo_path} && bash ../run-git-filter-repo.sh")


async def main():
    repos = get_repos()
    for repo in repos:
        await process_repo(repo)


if __name__ == "__main__":
    asyncio.run(main())
