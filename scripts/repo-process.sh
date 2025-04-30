#!/bin/bash

set -e

REPO_URL="$1"
REPO_PATH="$2"
REPO_NAME="$3"
GITHUB_EMAIL="$4"

rm -rf "$REPO_PATH"
mkdir -p "$REPO_PATH"
echo ${REPO_URL}
git clone "$REPO_URL" "$REPO_PATH"

cd "$REPO_PATH"
GITHUB_EMAIL="$GITHUB_EMAIL" python3 ../../filter-repo.py
