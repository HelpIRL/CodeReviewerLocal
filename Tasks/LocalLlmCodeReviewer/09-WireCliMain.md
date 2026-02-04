# 9. WireCliMain

**Goal**: Implement `CodeReview.py` CLI that connects scanner → context → adapter → orchestrator → report → VS Code opener.
**Est.**: ≤2 hours
**Dependencies**: Tasks 2–8

## Steps
- [x] Implement CLI argument parsing.
- [x] Wire scan → context → review → report flow.
- [x] Call VS Code opener when applicable.

## Definition of Done
- [x] `python CodeReview.py <path>` runs end-to-end using mock backend and generates reports.

## Outcome (fill after Iterate)
- **Actual Time**:
- **Result**: Added `CodeReview.py` CLI to orchestrate scan → review → report.
- **Follow-ups**: Integrate resume/state and non-mock backends.
