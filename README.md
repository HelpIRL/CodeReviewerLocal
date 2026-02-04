# Codex Project Template

## Start Here (Required)

If this is a fresh repo, type **Begin** in the chat. Codex will read `CONTEXT.md`
and guide you through the full BRAIN onboarding flow before any work starts.

This repository is a **starter template** for projects that use AI-assisted development
with strong guardrails, repeatability, and auditability.

It is a **normal Git repository** with a small set of conventions that allow
AI tools (such as Codex) to work safely and predictably alongside humans.

---

## Table of Contents

- [Maintainer & Contact](#maintainer--contact)
- [License](#license)
- [What This Template Is](#what-this-template-is)
- [Template Behavior (important)](#template-behavior-important)
- [Key Files](#key-files)
- [Typical Workflow](#typical-workflow)
- [Adding to an Existing Project](#adding-to-an-existing-project)
- [Task Structure Example](#task-structure-example)

---

## Maintainer & Contact

This project is maintained by **HelpIRL LLC**.

- 🌐 Website: https://helpirl.com
- 📧 Email: john@helpirl.com
- 🧑‍💻 GitHub: https://github.com/helpirl

For questions about:
- using this template
- AI-safe development workflows
- training or consulting

please reach out via email or open an issue.

## License

This project is licensed under the **MIT License**.

You are free to use, modify, and distribute this template, including for
commercial purposes. See the `LICENSE` file for details.

## What This Template Is

- A **human-first project scaffold**
- A **safe starting point** for AI-assisted coding
- A way to standardize:
  - documentation
  - task breakdown
  - commits
  - AI behavior

Nothing in this repo is required for your code to run.
If you remove all AI-related files, the project still works.

---

## Template Behavior (important)

This repository serves **two purposes at once**:

- It is a **live public repository**
- It is a **template copied** when you click **Use this template**

Due to a GitHub limitation, files under `.github/` apply to **both** the template
repository itself *and* to any repositories created from it.

There is no separate "template-only" configuration.

### Pattern 1 — Placeholder configuration (used here)

Some GitHub configuration files (notably `.github/ISSUE_TEMPLATE/config.yml`)
intentionally contain **placeholders**, for example:

```yaml
url: https://github.com/OWNER/REPO/discussions
```

This is **by design**, not an oversight.

Why this pattern is used:

- Prevents forks and template-based projects from accidentally routing issues
  back to HelpIRL
- Forces each new project owner to consciously configure their own links
- Matches the approach used by GitHub's official templates

If you create a repository from this template:

> **You should update `.github/ISSUE_TEMPLATE/config.yml`**
> to point to your repository's Discussions or support channel.

The template repository itself relies on the contact information above
for questions and support.

---

## Key Files

| File | Purpose |
|---|---|
| `README.md` | Human onboarding and project overview |
| `CONTEXT.md` | Project-specific structure and constraints (AI-first) |
| `AGENTS.md` | AI behavior and guardrails |
| `.codex/commands/` | Human-invoked workflows (e.g., `/brain`, `/review`) |
| `.codex/settings.json` | Permissions, hooks, environment (shared via git) |
| `.mcp.json` | MCP server configuration (shared via git) |
| `Tasks/` | Structured task breakdowns, grouped by feature |

### Local Files (git-ignored)

| File | Purpose |
|---|---|
| `AGENTS.local.md` | Personal notes, memories, local context (not shared) |
| `.codex/settings.local.json` | Personal permissions and settings overrides |

Create `AGENTS.local.md` in the project root for personal notes that shouldn't be
committed. Codex reads it automatically but it stays out of version control.

---

## Typical Workflow

1. **Initialize a new project**
   - Use this repo as a template **or**
   - Run the initialization script in an existing repo

2. **Update `README.md`**
   - Replace this file with real project documentation
   - Describe what the project does and how humans use it

3. **Update `.github/ISSUE_TEMPLATE/config.yml`**
   - Replace `OWNER/REPO` with your GitHub username and repository name
   - This routes questions to your project's Discussions instead of Issues

4. **Update `CONTEXT.md`**
   - Describe the actual project structure
   - Define build/test entry points
   - Document constraints that AI should not guess

5. **Work using Tasks**
   - Break work into feature folders under `Tasks/`
   - Each task is a small, self-contained unit of work
   - Git commits occur at task boundaries

6. **Let AI assist safely**
   - AI follows the rules in `AGENTS.md`
   - Real-world actions go through approved tools
   - Humans review results, not shell commands

---

## Adding to an Existing Project

Already have a project and want to add these AI guardrails? You don't need to start from scratch.

### Quick Setup

1. **Copy the template-update command** into your project:
   ```bash
   mkdir -p .codex/commands
   curl -sL https://raw.githubusercontent.com/HelpIRL/CodexTemplateV1/main/.codex/commands/template-update.md \
     -o .codex/commands/template-update.md
   ```

2. **Run the command** in Codex:
   ```
   /template-update
   ```

3. **Choose what to install** when prompted:
   - **Commands** — AI behavior rules (`AGENTS.md`) + workflows
   - **Skills** — Behavioral patterns (e.g., systematic-debugging)
   - **Hooks** — Workflow scripts (pre-commit tests, edit reminders)
   - **All** — Everything above

4. **Create your project-specific files** (these are never overwritten):
   - `CONTEXT.md` — Your project structure, build commands, toolchain
   - `.codex/settings.json` — Your permissions and hook configuration

### What Gets Updated vs. What Stays Yours

| Your selection | Files updated |
|----------------|---------------|
| Commands | `AGENTS.md`, `.codex/README.md`, `.codex/commands/*.md` |
| Skills | `.codex/skills/*.md` |
| Hooks | `.codex/hooks/README.md`, `.codex/hooks/*.sh` |

| Never touched (yours to customize) |
|-----------------------------------|
| `README.md` |
| `CONTEXT.md` |
| `.codex/settings.json` |
| `.github/*` |

Run `/template-update` periodically to get improvements without affecting your project-specific configuration.

---

## Task Structure Example
