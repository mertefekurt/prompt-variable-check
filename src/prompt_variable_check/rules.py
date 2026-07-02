from __future__ import annotations

from prompt_variable_check.models import Rule

PROJECT_NAME = 'prompt-variable-check'
SUMMARY = 'Audit prompt variables for undeclared, unused, and sensitive placeholders.'
SAMPLE_RISK = 'uses {ssn} declared missing unused customer_name'
SAMPLE_CLEAN = 'uses {ticket_id} declared ticket_id unused none'
TEXT_FIELDS = ("text", "content", "description", "summary", "body", "notes", "message")
SUBJECT_FIELDS = ("id", "name", "path", "service", "endpoint", "field", "event")

RULES = (
    Rule(
        code='sensitive-placeholder',
        severity='high',
        pattern='\\{(ssn|password|token|secret)\\}',
        message='sensitive placeholder detected',
        recommendation='avoid sensitive prompt variables',
    ),
    Rule(
        code='declared-missing',
        severity='medium',
        pattern='declared\\s+missing',
        message='variable declaration missing',
        recommendation='declare all variables',
    ),
    Rule(
        code='unused-variable',
        severity='low',
        pattern='unused\\s+(?!none\\b)\\w+',
        message='unused variable present',
        recommendation='remove stale prompt variable',
    ),
)
