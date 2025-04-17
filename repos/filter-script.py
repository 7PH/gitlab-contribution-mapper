EMAILS = [b"benjamin.raymond@cern.ch"]

# Suppress type error in IDE
if __name__ == "__main__":
    commit = None

if commit.author_email not in EMAILS:
    # commit.skip()
    pass
else:
    # print(
    #     f"Processing commit {commit.branch} {len(commit.parents)} ({commit.message}) by {commit.author_email}"
    # )
    if commit.file_changes:
        print(
            commit.file_changes[0].type,
            commit.file_changes[0].filename,
            commit.file_changes[0].blob_id,
        )
