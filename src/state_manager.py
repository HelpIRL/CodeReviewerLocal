"""Persist and resume review state."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import json


@dataclass(frozen=True)
class ReviewState:
    pending_files: list[str]
    completed_files: list[str]
    report_base_name: str | None = None


def initialize_state(files: list[Path], report_base_name: str | None = None) -> ReviewState:
    return ReviewState(
        pending_files=[str(path) for path in files],
        completed_files=[],
        report_base_name=report_base_name,
    )


def mark_completed(state: ReviewState, file: Path) -> ReviewState:
    file_str = str(file)
    pending = [path for path in state.pending_files if path != file_str]
    completed = list(state.completed_files)
    if file_str not in completed:
        completed.append(file_str)
    return ReviewState(pending_files=pending, completed_files=completed, report_base_name=state.report_base_name)


def save_state(state: ReviewState, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "pending_files": state.pending_files,
        "completed_files": state.completed_files,
        "report_base_name": state.report_base_name,
    }
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def load_state(path: Path) -> ReviewState:
    payload = json.loads(path.read_text(encoding="utf-8"))
    return ReviewState(
        pending_files=payload.get("pending_files", []),
        completed_files=payload.get("completed_files", []),
        report_base_name=payload.get("report_base_name"),
    )
