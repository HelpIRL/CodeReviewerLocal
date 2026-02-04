# Template Update

Update this project's Codex template files from the upstream source.

## Source Repository

```
https://github.com/HelpIRL/CodexTemplateV1
Branch: main
```

## First: Check for Uncommitted Changes

Before proceeding, check for uncommitted changes:

```bash
git status --porcelain
```

If output is **not empty**, ask the user:

> **You have uncommitted changes.**
>
> It's easier to review or revert template updates when starting from a clean state.
>
> Would you like to commit your changes first before pulling in updates?
> 1. Yes, commit first (runs `/commit`)
> 2. No, continue anyway

If user chooses to commit first, run the `/commit` command, then continue with the update.

## Then: Ask What to Update

Present this menu to the user:

> **What would you like to add/update?**
>
> 1. **Commands** — AI behavior rules + slash commands
> 2. **Skills** — Behavioral patterns (e.g., systematic-debugging)
> 3. **Hooks** — Workflow scripts (pre-commit, post-edit, etc.)
> 4. **All** — Everything above
>
> Press Esc to cancel without making changes.

Wait for user selection before proceeding.

## What Each Selection Includes

| Selection | Files Updated |
|-----------|---------------|
| **Commands** | `AGENTS.md`, `.codex/README.md`, `.codex/commands/*.md` |
| **Skills** | `.codex/skills/*.md` |
| **Hooks** | `.codex/hooks/README.md`, `.codex/hooks/*.sh` |
| **All** | All of the above |

## What is NEVER Updated

These files are **project-specific** and will NOT be modified regardless of selection:

- `README.md` — Your project documentation
- `CONTEXT.md` — Your project structure and constraints
- `.codex/settings.json` — Your permission and hook configuration
- `.codex/settings.local.json` — Your local settings
- `.github/*` — Your issue templates and workflows

## Instructions

### 1. Get file lists from template repo

```bash
# Commands
gh api repos/HelpIRL/CodexTemplateV1/contents/.codex/commands --jq '.[].name'

# Skills
gh api repos/HelpIRL/CodexTemplateV1/contents/.codex/skills --jq '.[].name'

# Hooks (only .md and .sh files)
gh api repos/HelpIRL/CodexTemplateV1/contents/.codex/hooks --jq '.[] | select(.name | test("\\.(md|sh)$")) | .name'
```

### 2. Fetch files using raw GitHub URLs

```
https://raw.githubusercontent.com/HelpIRL/CodexTemplateV1/main/<path>
```

Examples:
- `https://raw.githubusercontent.com/HelpIRL/CodexTemplateV1/main/AGENTS.md`
- `https://raw.githubusercontent.com/HelpIRL/CodexTemplateV1/main/.codex/README.md`
- `https://raw.githubusercontent.com/HelpIRL/CodexTemplateV1/main/.codex/commands/brain.md`

### 3. For each file in the selected categories

- Create parent directories if needed (`mkdir -p`)
- Fetch the latest version from template repo
- Compare with local version (if exists)
- If different or new, update the file
- For `.sh` files, ensure they are executable (`chmod +x`)

### 4. Important rules

- Do NOT delete local files missing from template (user may have custom files)
- Do NOT update `template-update.md` during execution (this file)
- Do NOT modify `.codex/settings.json` (user's permissions)

### 5. Report summary

After completion, show:
- Files updated (with change indicator)
- New files added
- Files unchanged (skipped)

Example output:
```
Template Update Complete

Updated:
  ✓ AGENTS.md
  ✓ .codex/commands/brain.md
  + .codex/skills/systematic-debugging.md (new)

Unchanged:
  - .codex/commands/commit.md (no changes)

Run /template-update again anytime to check for updates.
```
