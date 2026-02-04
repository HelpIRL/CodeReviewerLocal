# Project Context (Template)

⚠️ **This file is a template.** Follow the bootstrap instructions below.

Codex (and other AI tools) rely on this file to understand the project.
When this bootstrap section is present, the project has not been configured yet.

---

## Bootstrap Instructions for Codex

When you read this file and see this section, help the user set up their project
using the BRAIN method. Read `.codex/commands/brain.md` for full BRAIN details.

### Welcome Message

Display this to the user:

> **Welcome to the HelpIRL Codex Template** 👋
>
> This repository is pre-wired with a practical, opinionated structure for working
> with Codex in a way that stays readable, repeatable, and team-friendly.
>
> **You'll find:**
> - A ready-to-use `.codex/` setup (commands, hooks, and skills)
> - `.github/` structure to encourage clean commits and reviews
> - A lightweight workflow designed to scale from solo work to teams
>
> This template uses the **BRAIN method** to establish shared context before any
> code is written.
>
> **Begin (B):**
> This is idea capture only — no design, no planning, no solutions yet.
>
> Once that's done, I'll guide you through:
> - **Refine (R):** clarifying goals and constraints
> - **Arrange (A):** identifying developer tasks and structure
>
> You can move fast or go deep — the structure is here to support either.
>
> ---
>
> **What is this project? Give me the elevator pitch in 2-3 sentences.**

### Bootstrap Flow

1. **Auto-detect values**:
   - OWNER/REPO from `git remote get-url origin`
   - Existing folder structure

2. **Begin Phase**:
   - Wait for user to describe their project (they were prompted in welcome message)
   - Acknowledge receipt only—no analysis, suggestions, or reframing
   - Commit: `chore(init): begin project definition`

3. **Refine Phase** — Ask targeted questions:
   - Primary language/framework?
   - Build command? (or "none yet")
   - Test command? (or "none yet")
   - Source code location? (e.g., `src/`, `lib/`, project root)
   - Any key constraints or considerations?
   - Commit: `chore(init): refine project context`

4. **Populate Files**:
   - Replace this CONTEXT.md with real values (use template in next section)
   - Update `.github/ISSUE_TEMPLATE/config.yml`—replace `OWNER/REPO` with detected values
   - Commit: `chore(init): populate project configuration`

5. **Explain Task Workflow**:
   - "Your project is configured. Features are broken into tasks under `Tasks/`."
   - "Standard practice: commit when each task is complete so work is captured
     and you have clean rollback points."
   - Explain the file structure that will be created:
     ```
     Tasks/
       {FeatureName}/
         CONTEXT.md        # Feature context (Begin + Refine)
         Status.md         # Progress tracking
         01-TaskName.md    # Individual task files
         02-TaskName.md
         ...
     ```
   - **Important:** Each task MUST be its own file. This provides:
     - Clear audit trail for what was done
     - Safe rollback points per task
     - Readable history even with auto-accept enabled

6. **Transition**:
   - Ask if ready to scaffold their first feature
   - If yes, follow `.codex/commands/brain.md` to create the task file structure
   - **Do not skip creating task files** — the Arrange phase must produce individual
     `##-TaskName.md` files, not just notes in CONTEXT.md

---

## CONTEXT.md Template (use this for replacement)

Once bootstrap is complete, replace this entire file with the following,
filled in with the user's answers:

```markdown
# Project Context

## Project Structure

- **Source code**: {location}
- **Tests**: {location or "none yet"}
- **Config files**: {list relevant files}
- **Generated artifacts**: {build outputs, or "none"}

## Language & Tooling

- **Language**: {language}
- **Framework**: {framework or "none"}
- **Build**: `{build command}` or "none yet"
- **Test**: `{test command}` or "none yet"
- **Package manager**: {npm, pip, cargo, etc. if applicable}

## Build & Test Entry Points

These are the approved commands. Do not invent alternatives.

- Build: `{command}`
- Test: `{command}`
- Lint: `{command}` (if applicable)

## Task Management

Tasks are stored under `Tasks/{FeatureName}/` with numbered task files.
See `.codex/commands/brain.md` for the BRAIN workflow.

## Constraints

{Any project-specific rules, limitations, or considerations the user mentioned}
```

---

End of bootstrap instructions. Once CONTEXT.md is replaced, this section is gone
and Codex will read the real project context instead.
