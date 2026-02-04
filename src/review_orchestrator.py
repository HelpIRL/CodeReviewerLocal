"""Orchestrate local LLM review across chunks."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from .context_builder import ContextBundle, Annotation
from .llm_adapter import LlmAdapter, LlmRequest


@dataclass(frozen=True)
class ReviewFinding:
    kind: str
    file: Path
    line_no: int | None
    message: str
    suggestion: str | None = None


@dataclass(frozen=True)
class ReviewResponse:
    file: Path
    chunk_index: int
    response_text: str


@dataclass(frozen=True)
class ReviewResult:
    findings: list[ReviewFinding]
    responses: list[ReviewResponse]


def _annotation_to_finding(annotation: Annotation) -> ReviewFinding:
    return ReviewFinding(
        kind=annotation.kind.lower(),
        file=annotation.file,
        line_no=annotation.line_no,
        message=annotation.text,
    )


def review_bundle(
    bundle: ContextBundle,
    adapter: LlmAdapter,
    *,
    system_prompt: str | None = None,
) -> ReviewResult:
    findings: list[ReviewFinding] = []
    responses: list[ReviewResponse] = []

    for file_context in bundle.files:
        for annotation in file_context.annotations:
            findings.append(_annotation_to_finding(annotation))

        for chunk in file_context.chunks:
            prompt = (
                "Review the following code chunk for logic issues, security risks, "
                "and risky TODO/HACK comments. Return concise bullet points.\n\n"
                f"File: {chunk.file}\nChunk {chunk.index}\n\n{chunk.text}"
            )
            response = adapter.generate(LlmRequest(prompt=prompt, system=system_prompt))
            responses.append(
                ReviewResponse(
                    file=file_context.file,
                    chunk_index=chunk.index,
                    response_text=response.text,
                )
            )

    return ReviewResult(findings=findings, responses=responses)
