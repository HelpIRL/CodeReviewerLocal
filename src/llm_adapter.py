"""Pluggable adapter layer for local LLM backends."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True)
class LlmRequest:
    prompt: str
    system: str | None = None
    max_tokens: int | None = None


@dataclass(frozen=True)
class LlmResponse:
    text: str
    model: str
    backend: str


class LlmAdapter(Protocol):
    """Minimal adapter protocol."""

    def generate(self, request: LlmRequest) -> LlmResponse:
        raise NotImplementedError


@dataclass
class MockAdapter:
    """Simple adapter for local testing."""

    model: str = "mock"
    backend: str = "mock"

    def generate(self, request: LlmRequest) -> LlmResponse:
        return LlmResponse(text=request.prompt[:200], model=self.model, backend=self.backend)


def resolve_adapter(backend: str, model: str) -> LlmAdapter:
    """Resolve adapter by backend name.

    Supported: auto, mock. Other backends should be implemented later.
    """
    backend = backend.lower()
    if backend in {"auto", "mock"}:
        return MockAdapter(model=model, backend="mock")
    raise ValueError(f"Unsupported backend: {backend}")
