# Local LLM Code Reviewer

> Owner: John  ·  Created: 2026-02-04

## Begin (raw)
<!-- 3-minute brain dump. Do not edit or reinterpret. -->
Local LLM code reviewer. Expect to run `CodeReview.py {folderName}` with a few parameters (LLM to use, recursion depth, where to store report and CONTEXT so we can continue on failure). Possibly automate in the future and add it to an MCP via some linkage.

## Refine (scope)
- **Goal**: Review code for clear logic violations, security risks, and highlight `//HACK` and `//TODO` statements.
- **In / Out of scope**: In scope: scan code and produce a report; include suggested fix guidance in the report. Nice-to-have: build a list of URLs or markdown files for issues found so future runs can build better context and improve over time.
- **Definition of Done**: Code is scanned and a report is created.
- **Constraints**: Local LLM on 16 GB GPU; Python version must be compatible with common local LLM stacks (Llama/DeepSeek/HuggingFace).
- **Risks**: (optional)
- **Resources**: (optional)
- **Dependencies**: Keep open; use whatever enables Llama, DeepSeek, and other local code-capable models.
