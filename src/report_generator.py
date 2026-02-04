"""Generate markdown and JSON reports."""

from __future__ import annotations

from dataclasses import dataclass, asdict
from datetime import datetime
from pathlib import Path
import json

from .context_builder import ContextBundle
from .review_orchestrator import ReviewResult, ReviewFinding


@dataclass(frozen=True)
class ReportPaths:
    markdown: Path
    json: Path


def _finding_to_dict(finding: ReviewFinding) -> dict:
    return {
        "kind": finding.kind,
        "file": str(finding.file),
        "line_no": finding.line_no,
        "message": finding.message,
        "suggestion": finding.suggestion,
    }


def generate_report_base_name(prefix: str = "report") -> str:
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    return f"{prefix}-{timestamp}"


def write_reports(
    report_dir: Path,
    base_name: str,
    *,
    bundle: ContextBundle,
    review_result: ReviewResult,
) -> ReportPaths:
    report_dir.mkdir(parents=True, exist_ok=True)
    md_path = report_dir / f"{base_name}.md"
    json_path = report_dir / f"{base_name}.json"

    findings = [_finding_to_dict(f) for f in review_result.findings]
    context_files = [str(fc.file) for fc in bundle.files]

    payload = {
        "summary": {
            "files_reviewed": len(bundle.files),
            "total_chunks": bundle.total_chunks,
            "total_annotations": bundle.total_annotations,
            "findings": len(findings),
        },
        "context_files": context_files,
        "findings": findings,
        "responses": [
            {
                "file": str(resp.file),
                "chunk_index": resp.chunk_index,
                "response_text": resp.response_text,
            }
            for resp in review_result.responses
        ],
    }

    json_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    lines: list[str] = []
    lines.append(f"# Code Review Report: {base_name}")
    lines.append("")
    lines.append("## Summary")
    lines.append(f"- Files reviewed: {payload['summary']['files_reviewed']}")
    lines.append(f"- Total chunks: {payload['summary']['total_chunks']}")
    lines.append(f"- TODO/HACK annotations: {payload['summary']['total_annotations']}")
    lines.append(f"- Findings: {payload['summary']['findings']}")
    lines.append("")
    lines.append("## Context Files")
    for path in context_files:
        lines.append(f"- {path}")
    lines.append("")
    lines.append("## Findings")
    if findings:
        for finding in findings:
            line_info = f" (line {finding['line_no']})" if finding["line_no"] else ""
            lines.append(
                f"- [{finding['kind'].upper()}] {finding['file']}{line_info}: {finding['message']}"
            )
            if finding["suggestion"]:
                lines.append(f"  Suggestion: {finding['suggestion']}")
    else:
        lines.append("- None")
    lines.append("")
    lines.append("## Model Responses")
    if review_result.responses:
        for response in review_result.responses:
            lines.append(f"- {response.file} (chunk {response.chunk_index})")
            lines.append(f"  {response.response_text}")
    else:
        lines.append("- None")

    md_path.write_text("\n".join(lines), encoding="utf-8")

    return ReportPaths(markdown=md_path, json=json_path)
