# Documentation Tracking

# Maps source code patterns to documentation targets.
# Created by /gabe-init based on project type.
# Used by /gabe-commit CHECK 7 (doc drift).
#
# Columns:
#   Source Pattern — glob matching changed files in git diff
#   Doc Target — the documentation file that should be updated (or "skip")
#   Section — the heading within the doc target to check/update
#   Priority — critical (blocks) | high (warns) | medium (info) | low (info)
#
# Glob syntax: * matches within directory, ** matches across directories
# To exclude a pattern explicitly, set Doc Target to "skip"
# To add project-specific mappings, append rows to the table.

## CLI

| Source Pattern | Doc Target | Section | Priority |
|---|---|---|---|
| src/cli/*.py | README.md | Usage | high |
| src/commands/*.py | README.md | Commands | high |
| pyproject.toml | README.md | Installation | medium |
| tests/** | skip | | |
| .kdbp/** | skip | | |
| tiptally/cli.py | README.md | Usage | high |
| tiptally/split.py | docs/design.md | The shares | high |
