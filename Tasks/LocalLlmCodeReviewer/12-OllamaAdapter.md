# 12. OllamaAdapter

**Goal**: Implement an Ollama backend adapter for local model inference.
**Est.**: ≤2 hours
**Dependencies**: Task 4

## Steps
- [x] Implement Ollama adapter that calls the local API.
- [x] Wire adapter into backend resolver.
- [x] Add basic error handling and timeouts.

## Definition of Done
- [x] `--backend ollama` is supported and documented in code.

## Outcome (fill after Iterate)
- **Actual Time**:
- **Result**: Added `src/ollama_adapter.py` and wired it into `resolve_adapter`.
- **Follow-ups**: Add health check and model listing.
