"""Best-effort report opener for VS Code terminals."""

from __future__ import annotations

from pathlib import Path
import os
import subprocess


def is_vscode_terminal() -> bool:
    return bool(os.environ.get("VSCODE_PID") or os.environ.get("TERM_PROGRAM") == "vscode")


def open_report(path: Path) -> bool:
    """Attempt to open the report in VS Code. Returns True if a command was launched."""
    if not is_vscode_terminal():
        return False

    # Prefer the `code` CLI if available.
    try:
        subprocess.run(["code", str(path)], check=False)
        return True
    except OSError:
        return False
