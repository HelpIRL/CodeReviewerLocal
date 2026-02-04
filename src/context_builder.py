"""Chunking and context-building utilities."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
from typing import Iterable


DEFAULT_MAX_CHARS = 4000
DEFAULT_OVERLAP = 200

_TODO_RE = re.compile(r"\b(TODO|HACK)\b", re.IGNORECASE)


@dataclass(frozen=True)
class Annotation:
    file: Path
    line_no: int
    kind: str
    text: str


@dataclass(frozen=True)
class Chunk:
    file: Path
    index: int
    start: int
    end: int
    text: str


@dataclass(frozen=True)
class FileContext:
    file: Path
    chunks: list[Chunk]
    annotations: list[Annotation]


@dataclass(frozen=True)
class ContextBundle:
    files: list[FileContext]
    total_chunks: int
    total_annotations: int


def _chunk_text(text: str, *, max_chars: int, overlap: int) -> Iterable[tuple[int, int, str]]:
    if max_chars <= 0:
        raise ValueError("max_chars must be positive")
    if overlap < 0:
        raise ValueError("overlap must be non-negative")
    start = 0
    length = len(text)
    while start < length:
        end = min(start + max_chars, length)
        yield start, end, text[start:end]
        if end == length:
            break
        start = max(0, end - overlap)


def _extract_annotations(file: Path, lines: list[str]) -> list[Annotation]:
    annotations: list[Annotation] = []
    for idx, line in enumerate(lines, start=1):
        match = _TODO_RE.search(line)
        if not match:
            continue
        kind = match.group(1).upper()
        annotations.append(
            Annotation(file=file, line_no=idx, kind=kind, text=line.strip())
        )
    return annotations


def build_context_bundle(
    files: Iterable[Path],
    *,
    max_chars: int = DEFAULT_MAX_CHARS,
    overlap: int = DEFAULT_OVERLAP,
) -> ContextBundle:
    """Build chunked context bundle for a list of files."""
    file_contexts: list[FileContext] = []
    total_chunks = 0
    total_annotations = 0

    for file in files:
        try:
            text = file.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        lines = text.splitlines()
        annotations = _extract_annotations(file, lines)
        chunks: list[Chunk] = []
        for index, (start, end, chunk_text) in enumerate(
            _chunk_text(text, max_chars=max_chars, overlap=overlap)
        ):
            chunks.append(
                Chunk(
                    file=file,
                    index=index,
                    start=start,
                    end=end,
                    text=chunk_text,
                )
            )
        total_chunks += len(chunks)
        total_annotations += len(annotations)
        file_contexts.append(FileContext(file=file, chunks=chunks, annotations=annotations))

    return ContextBundle(
        files=file_contexts,
        total_chunks=total_chunks,
        total_annotations=total_annotations,
    )
