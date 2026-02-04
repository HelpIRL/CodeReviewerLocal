# Local Model Setup (16 GB GPU)

This guide covers recommended local runtimes and example commands for pulling
code-capable models. Choose one backend and start with a 7B–8B model to fit
comfortably on a 16 GB GPU.

## Recommended Runtimes

- Ollama (fastest to get started)
- llama.cpp (lightweight, flexible)
- vLLM (higher throughput, more setup)

## Ollama (Recommended)

1. Install Ollama from the official site.
   ```bash
   curl -fsSL https://ollama.com/install.sh | sh
   ```
2. Pull a code-capable model:
   ```bash
   ollama pull llama3
   # or a smaller code-focused model
   ollama pull deepseek-coder:7b
   ```
3. Run a quick test:
   ```bash
   ollama run llama3 "Explain this Python function"
   ```
4. Start the local server (if not already running):
   ```bash
   ollama serve
   ```
5. Verify the API is reachable:
   ```bash
   curl -s http://localhost:11434/api/tags
   ```

## llama.cpp

1. Build or install the `llama.cpp` binaries.
2. Download a GGUF model compatible with your GPU (7B–8B recommended).
3. Run a quick test:
   ```bash
   ./main -m /path/to/model.gguf -p "Explain this Python function"
   ```

## vLLM

1. Install vLLM in a Python environment.
2. Start a model server:
   ```bash
   vllm serve meta-llama/Llama-3-8B-Instruct
   ```
3. Send a test request using your preferred client.

## Hardware Notes

- Prefer 7B–8B models for 16 GB GPUs.
- If you hit OOM, use a smaller model or lower context length.
- Quantized models (4-bit/5-bit) are often the best fit locally.

## Next Steps

- Once a backend is chosen, wire it into `CodeReview.py`.
- Use `--backend ollama|llama_cpp|vllm` after the adapter is implemented.
