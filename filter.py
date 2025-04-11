EMAILS = [b"benjamin.raymond@cern.ch"]

# Suppress type error in IDE
if __name__ == "__main__":
    commit = None

if commit.author_email not in EMAILS:
    print(f"Skipping commit {commit.original_id} by {commit.author_email}")
    commit.skip()
else:
    print(f"Processing commit {commit.original_id} by {commit.author_email}")
    commit.file_changes.clear()
