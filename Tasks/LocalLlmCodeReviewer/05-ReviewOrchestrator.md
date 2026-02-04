# 5. ReviewOrchestrator

**Goal**: Loop chunks through model, collect findings (logic/security/todo), and optionally suggested fixes.
**Est.**: ≤2 hours
**Dependencies**: Tasks 3–4

## Steps
- [x] Define findings schema.
- [x] Implement review loop.
- [x] Aggregate findings per file and overall.

## Definition of Done
- [x] End-to-end run on a small folder produces aggregated findings.

## Outcome (fill after Iterate)
- **Actual Time**:
- **Result**: Added `src/review_orchestrator.py` with findings schema and review loop.
- **Follow-ups**: Parse model responses into structured findings.
