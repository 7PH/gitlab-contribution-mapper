#!/bin/bash

MONOREPO_REPO="$1"

rm -rf repos/_monorepo
mkdir -p repos/_monorepo
cd repos/_monorepo
git init
git config --local init.defaultBranch master
git config --local user.name 'Anonymous'
git config --local user.email ''
git remote add upstream $MONOREPO_REPO
