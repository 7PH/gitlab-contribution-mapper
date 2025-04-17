import subprocess

import git_filter_repo as fr

EMAILS = [b"benjamin.raymond@cern.ch"]
FILE_PATH = b"CHANGELOG.md"

fhash = subprocess.check_output(["git", "hash-object", "-w", FILE_PATH]).strip()
fmode = b"100755"
with open(FILE_PATH, "rb") as f:
    base_changelog = f.read()


def fixup_commits(commit: fr.Commit, metadata):
    if len(commit.parents) == 0:
        print(">>>>> Adding file to root commit")
        commit.file_changes = [fr.FileChange(b"M", FILE_PATH, fhash, fmode)]
    elif commit.author_email in EMAILS:
        # Update the changelog content to something else
        blob = fr.Blob(base_changelog + b"\n" + commit.message)
        filter.insert(blob)
        commit.file_changes = [fr.FileChange(b"M", FILE_PATH, blob.id, fmode)]
    else:
        # We do not want this commit
        print(f"Skipping commit {commit.original_id} by {commit.author_email}")
        # commit.skip() TODO: This removes LOTS of commits for some reason


fr_args = fr.FilteringOptions.parse_args(["--force"])
filter = fr.RepoFilter(fr_args, commit_callback=fixup_commits)
filter.run()
