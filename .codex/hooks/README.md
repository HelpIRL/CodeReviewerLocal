# Codex Hooks (Future-Facing)

Codex does not yet support hooks. These scripts are included so the template can
adopt hooks quickly when the feature arrives.

## Hook Types

| Hook | When it runs |
|------|--------------|
| `PreToolUse` | Before a tool executes (can block) |
| `PostToolUse` | After a tool completes |
| `UserPromptSubmit` | When user submits a prompt |

## Configuration

Hooks are configured in `.codex/settings.json`:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": ".codex/hooks/pre-edit.sh",
            "timeout": 5
          }
        ]
      }
    ]
  }
}
```

## Example: Block edits on main branch

Create `.codex/hooks/pre-edit.sh`:

```bash
#!/bin/bash
# Block edits on protected branches
branch=$(git branch --show-current 2>/dev/null)
if [[ "$branch" == "main" || "$branch" == "master" ]]; then
  echo '{"block": true, "message": "Cannot edit on protected branch. Create a feature branch first."}' >&2
  exit 2
fi
```

Make it executable: `chmod +x .codex/hooks/pre-edit.sh`

## Hook Response Format

Hooks can return JSON to control behavior:

```json
{"block": true, "message": "Reason for blocking"}
{"feedback": "Message shown to Codex"}
{"suppressOutput": true}
```

## Included Hooks

### pre-edit.sh
Blocks edits on protected branches (main/master). Enabled by default.

### post-edit-reminder.sh
Reminds about uncommitted changes after edits. **Disabled by default.**

To enable, add to `.codex/settings.json`:

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": ".codex/hooks/post-edit-reminder.sh"
          }
        ]
      }
    ]
  }
}
```

Adjust the `THRESHOLD` variable in the script to control when reminders appear (default: 5 files).

### pre-commit-test.sh
Runs tests before allowing commits. Blocks commit if tests fail. **Disabled by default.**

- Reads test command from `CONTEXT.md` (looks for `Test: \`command\`` pattern)
- If no test command defined, shows helpful feedback
- If tests fail, blocks the commit

To enable, add to `.codex/settings.json`:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash(git commit*)",
        "hooks": [
          {
            "type": "command",
            "command": ".codex/hooks/pre-commit-test.sh",
            "timeout": 120
          }
        ]
      }
    ]
  }
}
```
