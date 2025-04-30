#!/bin/bash

# Ask for emails
echo "Enter email addresses to filter commits by (press Enter when done):"
EMAILS=""
while true; do
  read -p "Email: " email
  if [[ -z "$email" ]]; then
    break
  fi
  if [[ -z "$EMAILS" ]]; then
    EMAILS="$email"
  else
    EMAILS="$EMAILS,$email"
  fi
done

# Ask for repositories
echo "Enter repository URLs (HTTPS or SSH) to monitor (press Enter when done):"
REPOS=""
while true; do
  read -p "Repository URL: " repo
  if [[ -z "$repo" ]]; then
    break
  fi
  if [[ -z "$REPOS" ]]; then
    REPOS="$repo"
  else
    REPOS="$REPOS,$repo"
  fi
done

# Ask for remote repository URL
read -p "Enter the remote repository URL to push anonymized commits to: " MONOREPO_REPO

# Ask for GitHub email
read -p "Enter your GitHub email (from https://github.com/settings/emails): " GITHUB_EMAIL

# Ask for GitHub email
read -p "Enter your GitHub username: " GITHUB_USER

# Generate .env file
cat > .env <<EOL
# Emails used to filter commits. Any commit not made by these emails will be ignored.
EMAILS=$EMAILS

# Repositories to monitor.
REPOS=$REPOS

# Remote repository to push the generated monorepo to.
MONOREPO_REPO=$MONOREPO_REPO

# GitHub email to use for commits.
# Find it in https://github.com/settings/emails
GITHUB_EMAIL=$GITHUB_EMAIL

# GitHub Username to use for commits.
GITHUB_USER=$GITHUB_USER
EOL

echo ".env file generated"