#!/bin/bash

set -e

REPO_NAME="$1"
REPO_PATH="$2"
MONOREPO_PATH="repos/_monorepo"

cd "$MONOREPO_PATH"
git remote add "$REPO_NAME" "$REPO_PATH"
git fetch "$REPO_NAME"
git merge -X theirs --allow-unrelated-histories "$REPO_NAME/master" -m "Auto-merge $REPO_NAME into _monorepo"
