import os
import subprocess

import git_filter_repo as fr

EMAILS = [b"benjamin.raymond@cern.ch"]
DUMMY_FILE_PATH = b"CHANGELOG.md"
FMODE = b"100755"


# Copy the dummy file within the repository
os.system(f"cp ../../{DUMMY_FILE_PATH.decode()} ./")

fhash = subprocess.check_output(["git", "hash-object", "-w", DUMMY_FILE_PATH]).strip()
with open(DUMMY_FILE_PATH, "rb") as f:
    base_changelog = f.read()


def fixup_commits(commit: fr.Commit, _metadata):
    if len(commit.parents) == 0:
        commit.file_changes = [fr.FileChange(b"M", DUMMY_FILE_PATH, fhash, FMODE)]
        if commit.author_email not in EMAILS:
            # Make the commit anonymous
            commit.author_name = b"Anonymous"
            commit.author_email = b""
    elif commit.author_email in EMAILS:
        # Update the changelog content to something else
        blob = fr.Blob(base_changelog + b"\n" + commit.message)
        filter.insert(blob)
        commit.file_changes = [fr.FileChange(b"M", DUMMY_FILE_PATH, blob.id, FMODE)]
    else:
        # We do not want this commit
        commit.file_changes = []


# Change to repo directory and run the custom git filter
fr_args = fr.FilteringOptions.parse_args(["--force"])
filter = fr.RepoFilter(fr_args, commit_callback=fixup_commits)
filter.run()
