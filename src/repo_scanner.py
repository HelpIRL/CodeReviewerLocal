"""Repository scanning and indexing utilities."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


DEFAULT_IGNORE_DIRS = {
    ".git",
    ".hg",
    ".svn",
    ".idea",
    ".vscode",
    ".venv",
    "venv",
    "node_modules",
    "dist",
    "build",
    "__pycache__",
    ".mypy_cache",
    ".pytest_cache",
    ".ruff_cache",
}

DEFAULT_IGNORE_FILES = {
    ".DS_Store",
    "Thumbs.db",
}

DEFAULT_MAX_FILE_BYTES = 2_000_000


@dataclass(frozen=True)
class ScanStats:
    total_files: int
    included_files: int
    skipped_binaries: int
    skipped_too_large: int
    skipped_ignored: int


@dataclass(frozen=True)
class ScanResult:
    files: list[Path]
    stats: ScanStats


def _is_binary_file(path: Path, sample_size: int = 2048) -> bool:
    try:
        with path.open("rb") as handle:
            chunk = handle.read(sample_size)
        return b"\x00" in chunk
    except OSError:
        return True


def _is_ignored(path: Path, ignore_dirs: set[str], ignore_files: set[str]) -> bool:
    if path.name in ignore_files:
        return True
    for part in path.parts:
        if part in ignore_dirs:
            return True
    return False


def _iter_files(root: Path, max_depth: int) -> Iterable[Path]:
    root = root.resolve()
    base_depth = len(root.parts)
    for path in root.rglob("*"):
        if len(path.parts) - base_depth > max_depth:
            continue
        if path.is_file():
            yield path


def scan_repo(
    root: Path,
    *,
    max_depth: int = 6,
    include_extensions: set[str] | None = None,
    ignore_dirs: set[str] | None = None,
    ignore_files: set[str] | None = None,
    max_file_bytes: int = DEFAULT_MAX_FILE_BYTES,
) -> ScanResult:
    """Scan a repository for reviewable files.

    Args:
        root: Root folder to scan.
        max_depth: Maximum recursion depth relative to root.
        include_extensions: Optional set of file extensions (".py", ".js").
        ignore_dirs: Directory names to skip.
        ignore_files: File names to skip.
        max_file_bytes: Max size for individual files.
    """
    root = root.resolve()
    ignore_dirs = set(ignore_dirs or DEFAULT_IGNORE_DIRS)
    ignore_files = set(ignore_files or DEFAULT_IGNORE_FILES)

    files: list[Path] = []
    skipped_binaries = 0
    skipped_too_large = 0
    skipped_ignored = 0

    for path in _iter_files(root, max_depth=max_depth):
        if _is_ignored(path, ignore_dirs, ignore_files):
            skipped_ignored += 1
            continue
        if include_extensions and path.suffix.lower() not in include_extensions:
            skipped_ignored += 1
            continue
        try:
            size = path.stat().st_size
        except OSError:
            skipped_ignored += 1
            continue
        if size > max_file_bytes:
            skipped_too_large += 1
            continue
        if _is_binary_file(path):
            skipped_binaries += 1
            continue
        files.append(path)

    files.sort(key=lambda p: str(p).lower())
    stats = ScanStats(
        total_files=len(files) + skipped_binaries + skipped_too_large + skipped_ignored,
        included_files=len(files),
        skipped_binaries=skipped_binaries,
        skipped_too_large=skipped_too_large,
        skipped_ignored=skipped_ignored,
    )
    return ScanResult(files=files, stats=stats)
