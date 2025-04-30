# GitLab Contribution Mapper

**GitLab Contribution Mapper** automates the extraction and merging of contributions from multiple GitLab repositories into a single monorepo, while filtering and anonymizing commits based on author email.

Note: The script barely works at the moment, more features will be added in the future (automation through GitHub Actions, more parametrization on what's anonymized or not). Feel free to suggest ideas as GitHub `Discussions` or `Issues`.

---

## Setup & Usage

### Option 1: Using uv (faster alternative)

```bash
# 1. Clone this project:
git clone https://github.com/7PH/gitlab-contribution-mapper
cd gitlab-contribution-mapper

# 2. Configure your environment:
./scripts/env-generate.sh

# 3. Run the tool:
uv run python gitlab-contribution-mapper.py
bash scripts/monorepo-push.sh
```

### Option 2: Using venv (built-in Python virtual environment)

```bash
# 1. Clone this project:
git clone https://github.com/7PH/gitlab-contribution-mapper
cd gitlab-contribution-mapper

# 2. Create a virtual environment (optional):
python -m venv .venv
source .venv/bin/activate

# 3. Install dependencies:
pip install .

# 4. Configure your environment:
./scripts/env-generate.sh

# 5. Run the tool
python gitlab-contribution-mapper.py
bash scripts/monorepo-push.sh
```

