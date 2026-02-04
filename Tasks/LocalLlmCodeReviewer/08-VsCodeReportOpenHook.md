# 8. VsCodeReportOpenHook

**Goal**: If run in VS Code terminal, open the report automatically.
**Est.**: ≤2 hours
**Dependencies**: Task 6

## Steps
- [x] Detect VS Code terminal environment.
- [x] Open report file (best effort) or print command.

## Definition of Done
- [x] Report opens or guidance printed when running in VS Code terminal.

## Outcome (fill after Iterate)
- **Actual Time**:
- **Result**: Added `src/vscode_hook.py` with VS Code detection and opener.
- **Follow-ups**: Add fallback for non-VS Code terminals.
