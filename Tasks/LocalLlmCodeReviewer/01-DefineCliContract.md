# 1. DefineCliContract

**Goal**: Define CLI args and defaults (`CodeReview.py {folder}` with flags for model, depth, report path, and context path).
**Est.**: ≤2 hours
**Dependencies**: none

## Steps
- [x] Define required/optional CLI arguments and defaults.
- [x] Decide on output paths and naming convention.
- [x] Document usage in task notes or README (if requested).

## CLI Contract

**Primary command**

```bash
python CodeReview.py <target_path> [options]
```

**Required**
- `<target_path>`: Folder to review (absolute or relative).

**Options**
- `--model <name>`: Model identifier (default: `llama-3`).
- `--backend <name>`: Backend driver (default: `auto`). Expected values: `auto`, `ollama`, `llama_cpp`, `vllm`.
- `--max-depth <int>`: Max recursion depth (default: `6`).
- `--report-dir <path>`: Output directory for reports (default: `./reports`).
- `--context-dir <path>`: Directory for persisted context/state (default: `./.codereview`).
- `--state-file <path>`: Override state file path (default: `{context-dir}/state.json`).
- `--resume`: Resume from last saved state (default: `false`).
- `--format <list>`: Report formats (comma-separated). Supported: `md`, `json` (default: `md,json`).

**Output naming**
- Report base name: `report-YYYYMMDD-HHMMSS`
- Files: `{report-dir}/{base}.md` and `{report-dir}/{base}.json`

## Definition of Done
- [x] CLI contract captured in this task file (or referenced location).

## Outcome (fill after Iterate)
- **Actual Time**:
- **Result**: Defined CLI usage, options, and output naming defaults.
- **Follow-ups**: Confirm default model/backend names match selected runtime.
