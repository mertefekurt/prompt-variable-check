# Prompt Variable Check

![Prompt Variable Check cover](assets/readme-cover.svg)

Audit prompt variables for undeclared, unused, and sensitive placeholders.

## The rule file is the product

- `sensitive-placeholder` (high): sensitive placeholder detected. Fix: avoid sensitive prompt variables.
- `declared-missing` (medium): variable declaration missing. Fix: declare all variables.
- `unused-variable` (low): unused variable present. Fix: remove stale prompt variable.

Everything else in the repo exists to feed records into those checks and render the answer in a way a person can act on.

## Shell session

```bash
git clone https://github.com/mertefekurt/prompt-variable-check.git
cd prompt-variable-check
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
prompt-variable-check examples/sample.txt
prompt-variable-check examples/sample.txt --json
```

## Repository shape

```text
.github/        CI workflow
examples/       sample inputs
src/            package source
tests/          test coverage
.gitignore      project file
pyproject.toml  package metadata
```
