# 4. LocalLlmAdapterLayer

**Goal**: Pluggable interface to local model backends (initially stubbed for llama/DeepSeek style).
**Est.**: ≤2 hours
**Dependencies**: Task 1

## Steps
- [x] Define adapter interface and config.
- [x] Implement one backend or clear stub wiring.
- [x] Document how to add a new backend.

## Definition of Done
- [x] Adapter interface created and wired.

## Outcome (fill after Iterate)
- **Actual Time**:
- **Result**: Added `src/llm_adapter.py` with adapter protocol and mock backend.
- **Follow-ups**: Implement Ollama/llama.cpp/vLLM adapters.
