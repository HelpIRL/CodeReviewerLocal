"""CLI entry point for local LLM code review."""

from __future__ import annotations

import argparse
from pathlib import Path

from src.repo_scanner import scan_repo
from src.context_builder import build_context_bundle
from src.llm_adapter import resolve_adapter
from src.review_orchestrator import review_bundle
from src.report_generator import generate_report_base_name, write_reports
from src.vscode_hook import open_report


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Local LLM code reviewer")
    parser.add_argument("target_path", help="Folder to review")
    parser.add_argument("--model", default="llama-3", help="Model identifier")
    parser.add_argument(
        "--backend",
        default="auto",
        choices=["auto", "mock", "ollama", "llama_cpp", "vllm"],
        help="Backend driver",
    )
    parser.add_argument("--max-depth", type=int, default=6, help="Max recursion depth")
    parser.add_argument("--report-dir", default="./reports", help="Report output directory")
    parser.add_argument(
        "--context-dir",
        default="./.codereview",
        help="Context/state directory",
    )
    parser.add_argument(
        "--state-file",
        default=None,
        help="Override state file path (default: {context-dir}/state.json)",
    )
    parser.add_argument("--resume", action="store_true", help="Resume from saved state")
    parser.add_argument(
        "--format",
        default="md,json",
        help="Report formats (comma-separated). Supported: md,json",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    target = Path(args.target_path).resolve()
    report_dir = Path(args.report_dir)
    adapter = resolve_adapter(args.backend, args.model)

    scan_result = scan_repo(target, max_depth=args.max_depth)
    bundle = build_context_bundle(scan_result.files)
    review_result = review_bundle(bundle, adapter)

    base_name = generate_report_base_name("report")
    paths = write_reports(report_dir, base_name, bundle=bundle, review_result=review_result)

    if args.format:
        formats = {fmt.strip().lower() for fmt in args.format.split(",") if fmt.strip()}
        if "md" not in formats and paths.markdown.exists():
            paths.markdown.unlink(missing_ok=True)
        if "json" not in formats and paths.json.exists():
            paths.json.unlink(missing_ok=True)

    open_report(paths.markdown)
    print(f"Report: {paths.markdown}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
