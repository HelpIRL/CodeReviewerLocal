"""Ollama backend adapter."""

from __future__ import annotations

from dataclasses import dataclass
import json
from typing import Any
from urllib import request, error

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .llm_adapter import LlmRequest, LlmResponse


DEFAULT_OLLAMA_URL = "http://localhost:11434/api/generate"
DEFAULT_TIMEOUT = 30


@dataclass(frozen=True)
class OllamaAdapter:
    model: str
    base_url: str = DEFAULT_OLLAMA_URL
    timeout: int = DEFAULT_TIMEOUT

    def generate(self, request_data: "LlmRequest") -> "LlmResponse":
        payload = {
            "model": self.model,
            "prompt": request_data.prompt,
            "stream": False,
        }
        if request_data.system:
            payload["system"] = request_data.system
        if request_data.max_tokens is not None:
            payload["num_predict"] = request_data.max_tokens

        data = json.dumps(payload).encode("utf-8")
        req = request.Request(
            self.base_url,
            data=data,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with request.urlopen(req, timeout=self.timeout) as resp:
                body = resp.read().decode("utf-8")
        except error.URLError as exc:
            raise RuntimeError(f"Failed to reach Ollama at {self.base_url}: {exc}") from exc

        try:
            decoded: dict[str, Any] = json.loads(body)
        except json.JSONDecodeError as exc:
            raise RuntimeError("Invalid JSON response from Ollama") from exc

        if "response" not in decoded:
            raise RuntimeError("Ollama response missing 'response' field")

        from .llm_adapter import LlmResponse

        return LlmResponse(text=decoded["response"], model=self.model, backend="ollama")
