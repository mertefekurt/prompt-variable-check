# prompt-variable-check

> Audit prompt variables for undeclared, unused, and sensitive placeholders.

## Field memo Overview

Audit prompt variables for undeclared, unused, and sensitive placeholders. It solves review drift by turning plain-text plans into deterministic CI-friendly findings.

## Input Contract

Accepts prompt variable map. The reader supports plain text, JSON, JSONL, and CSV so the
tool can fit into scripts, CI jobs, and review exports.

## CLI Walkthrough

```bash
python -m pip install -e ".[dev]"
prompt-variable-check examples/sample.txt
prompt-variable-check examples/sample.txt --json --fail-on medium
python -m prompt_variable_check --help
```

## Rule Surface

| Rule | Severity | Meaning |
|---|---:|---|
| `sensitive-placeholder` | high | sensitive placeholder detected |
| `declared-missing` | medium | variable declaration missing |
| `unused-variable` | low | unused variable present |

## Validation Notes

```bash
ruff check .
pytest
python -m prompt_variable_check --help
```

Example risky input:

```text
uses {ssn} declared missing unused customer_name
```

Architecture: `cli.py` handles arguments, `core.py` reads and evaluates records, and
`rules.py` keeps the project-specific policy explicit.

License: MIT.
