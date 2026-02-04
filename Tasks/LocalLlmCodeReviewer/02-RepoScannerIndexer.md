# 2. RepoScannerIndexer

**Goal**: Scan target folder with recursion depth; collect files by extension; ignore binaries and common noise.
**Est.**: ≤2 hours
**Dependencies**: Task 1

## Steps
- [x] Define default ignore patterns.
- [x] Implement deterministic file collection.
- [x] Record basic stats (file counts, size, etc.).

## Notes

- Default ignored directories: `.git`, `.hg`, `.svn`, `.idea`, `.vscode`, `.venv`, `venv`, `node_modules`, `dist`, `build`, `__pycache__`, `.mypy_cache`, `.pytest_cache`, `.ruff_cache`.
- Default ignored files: `.DS_Store`, `Thumbs.db`.
- Max file size default: 2 MB.

## Definition of Done
- [x] Function returns deterministic file list + stats.

## Outcome (fill after Iterate)
- **Actual Time**:
- **Result**: Implemented `scan_repo` in `src/repo_scanner.py` with deterministic ordering and stats.
- **Follow-ups**: Decide on default include extensions list (or keep open).
