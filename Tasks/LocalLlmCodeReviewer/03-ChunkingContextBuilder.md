# 3. ChunkingContextBuilder

**Goal**: Build manageable chunks and a context bundle to fit small LLMs; capture `//HACK` and `//TODO` lines.
**Est.**: ≤2 hours
**Dependencies**: Task 2

## Steps
- [x] Define chunking strategy (size, overlaps).
- [x] Extract TODO/HACK lines by language.
- [x] Create structured context bundle format.

## Definition of Done
- [x] Chunker produces structured inputs.
- [x] TODO/HACK list emitted.

## Outcome (fill after Iterate)
- **Actual Time**:
- **Result**: Added `src/context_builder.py` with chunking, annotations, and a context bundle.
- **Follow-ups**: Decide if we should tag language-specific TODO/HACK patterns.
