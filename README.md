# Code Reviewer Local

A local-first CLI that reviews a codebase with a local LLM, produces a report, and scales to larger repos via chunking and persisted context. Designed for 16 GB GPUs and offline workflows.

## Features

- Scan a repo and chunk files for small local models
- Highlight logic risks, security risks, and TODO/HACK markers
- Generate Markdown + JSON reports
- Resume from persisted state (work in progress)
- Optional VS Code report auto-open

## Quick Start

1. Install and run a local model backend and pull a model (Ollama recommended). See `docs/LOCAL_MODELS.md`.
2. Run the review:
   ```bash
   python CodeReview.py src/ --backend ollama --model llama3 --max-depth 6 --report-dir reports --format md
   ```

## CLI Usage

```bash
python CodeReview.py <target_path> [options]
```

Options:
- `--model <name>`: Model identifier (default: `llama-3`)
- `--backend <name>`: `ollama` (default), `llama_cpp`, `vllm` (future), `mock` (dev only with `--allow-mock`)
- `--max-depth <int>`: Max recursion depth (default: `6`)
- `--report-dir <path>`: Output directory (default: `./reports`)
- `--format <list>`: Report formats (comma-separated). Supported: `md,json`
- `--allow-mock`: Allow mock backend for local dev only

## Reports

Reports are written to the configured directory with a timestamped name:
- `report-YYYYMMDD-HHMMSS.md`
- `report-YYYYMMDD-HHMMSS.json`

## Local Models

See `docs/LOCAL_MODELS.md` for install and model pull steps (including Ollama).

## Development

- Language: Python 3.11/3.12
- Tests: `python -m pytest` (when tests are added)

## License

MIT License. See `LICENSE`.
