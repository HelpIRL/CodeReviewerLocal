# Project Context

## Project Structure

- **Source code**: `src/`
- **Tests**: none yet
- **Config files**: `CONTEXT.md`, `AGENTS.md`, `README.md`, `.codex/settings.json` (if added)
- **Generated artifacts**: none yet

## Language & Tooling

- **Language**: Python (3.12 preferred; confirm compatibility with LLM tooling)
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

- Easy way to use several common local models (LLAMA, DeepSeek, etc.).
- Assume 16 GB GPU.
- Avoid Python version conflicts with LLM tooling.
