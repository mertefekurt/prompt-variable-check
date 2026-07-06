# Prompt Variable Check

<p align="center">
  <img src="assets/readme-cover.svg" alt="Prompt Variable Check cover" width="100%" />
</p>

![stack](https://img.shields.io/badge/stack-Python-4b5563?style=flat-square) ![python](https://img.shields.io/badge/python-3.11-2563eb?style=flat-square) ![license](https://img.shields.io/badge/license-MIT-16a34a?style=flat-square) ![ci](https://img.shields.io/badge/ci-GitHub%20Actions-dc2626?style=flat-square)

Audit prompt variables for undeclared, unused, and sensitive placeholders.

## The short version

`prompt-variable-check` is intentionally small: feed it a file, get deterministic findings, and decide whether the result should block a merge or just guide cleanup.

## Rule surface

| Rule | Severity | What it catches |
| --- | --- | --- |
| `sensitive-placeholder` | high | sensitive placeholder detected |
| `declared-missing` | medium | variable declaration missing |
| `unused-variable` | low | unused variable present |

## Usage

```bash
python -m pip install -e ".[dev]"
prompt-variable-check examples/sample.txt
prompt-variable-check examples/sample.txt --json --fail-on medium
```

## Useful defaults

| Option | Reason |
| --- | --- |
| `--json` | machine-readable output for scripts |
| `--fail-on medium` | stricter CI gate when warnings matter |
| `--format auto` | let the reader detect text, CSV, JSON, or JSONL |

## Local checks

```bash
python -m pip install -e ".[dev]"
ruff check .
pytest
python -m prompt_variable_check --help
```
