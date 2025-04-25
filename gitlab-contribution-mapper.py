import asyncio
import os

EMAILS = [b"benjamin.raymond@cern.ch"]
DUMMY_FILE_PATH = b"CHANGELOG.md"
REPO_PATH = "repos"
REPO_FILE_PATH = "repos.txt"
MONOREPO_PATH = os.path.join(REPO_PATH, "_monorepo")


def get_repos():
    with open(REPO_FILE_PATH) as f:
        for line in f:
            repo = line.strip()
            if repo:
                yield repo


def process_repo(repo_url: str):
    # Clone the repository in repos/{repo}
    repo_name = repo_url.split("/")[-1]
    repo_path = os.path.join(REPO_PATH, repo_name)
    os.system(f"rm -rf {repo_path}")
    os.makedirs(repo_path, exist_ok=True)
    os.system(f"git clone {repo_url} {repo_path}")

    # Run filter-repo.py from the cloned repository
    os.system(f"cd {repo_path} && python ../../filter-repo.py")

    return repo_name


async def main():
    # Process all the repos
    repos = get_repos()
    repo_names = [process_repo(repo) for repo in repos]

    # Create the monorepo that contains all the repos
    os.system("bash scripts/monorepo-setup.sh")

    # Merge all the repos into the monorepo
    for repo_name in repo_names:
        repo_path = os.path.join("..", repo_name)
        os.system(
            f"cd {os.path.join(REPO_PATH, '_monorepo')} && git remote add {repo_name} {repo_path} && git fetch {repo_name} && git merge -X theirs --allow-unrelated-histories {repo_name}/master -m 'Auto-merge {repo_name} into _monorepo'"
        )


if __name__ == "__main__":
    asyncio.run(main())
