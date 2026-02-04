# 11. DisableMockByDefault

**Goal**: Keep mock backend for dev only and block it in normal CLI runs.
**Est.**: ≤2 hours
**Dependencies**: Task 9

## Steps
- [x] Add explicit flag to allow mock backend.
- [x] Prevent `--backend mock` unless the flag is set.
- [x] Update CLI contract notes.

## Definition of Done
- [x] CLI rejects mock backend unless explicitly allowed.

## Outcome (fill after Iterate)
- **Actual Time**:
- **Result**: Mock backend gated behind `--allow-mock` flag.
- **Follow-ups**: Remove mock backend entirely once real backends are wired.
