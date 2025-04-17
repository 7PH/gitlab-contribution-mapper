# SCRIPT_PATH="$(dirname "$0")/filter-script.py"

# git filter-repo --refs refs/heads/master --commit-callback "$(cat $SCRIPT_PATH)"

cp ../CHANGELOG.md ./
python ../insert-beginning.py --file CHANGELOG.md
