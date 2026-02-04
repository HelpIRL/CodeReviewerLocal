# Project Context

## Project Structure

- **Source code**: `src/`
- **Tests**: none yet
- **Config files**: `CONTEXT.md`, `AGENTS.md`, `README.md`, `.codex/settings.json` (if added)
- **Generated artifacts**: none yet

## Language & Tooling

- **Language**: Python (3.11/3.12; choose the version compatible with selected LLM backend)
- **Framework**: none
- **Build**: none yet
- **Test**: none yet
- **Package manager**: pip (assumed)

## Build & Test Entry Points

These are the approved commands. Do not invent alternatives.

- Build: none yet
- Test: none yet
- Lint: none yet

## Task Management

Tasks are stored under `Tasks/{FeatureName}/` with numbered task files.
See `.codex/commands/brain.md` for the BRAIN workflow.

## Constraints

- CLI tool invoked as `python CodeReview.py <target_path>` with flags for model, depth, report path, and context/state.
- Easy way to use several common local models (Llama, DeepSeek, etc.) via a pluggable backend layer.
- Assume 16 GB GPU; keep defaults friendly for smaller models.
- Reports must be generated (Markdown + JSON) and optionally opened when run from VS Code terminal.
- Persist context/state for resuming on failure.
- Avoid Python version conflicts with LLM tooling.
