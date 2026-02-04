# Project Recap

Summarize the current project state to re-establish context.

## Instructions

Run these checks and present a concise summary:

1. **Git State**
   - Current branch
   - Clean or uncommitted changes?
   - Last 3 commits (oneline)

2. **Project Context**
   - Read `CONTEXT.md` for project structure and constraints
   - Note the build/test commands

3. **Active Tasks**
   - Check `Tasks/` for any in-progress work
   - Find the most recently modified task folder
   - If a `Status.md` exists, report current task status

4. **Open Questions**
   - Any blockers or decisions noted in task files?

## Output Format

```
## Project Recap

**Branch:** {branch} ({clean/uncommitted changes})
**Recent commits:**
- {hash} {message}
- {hash} {message}
- {hash} {message}

**Project:** {brief description from CONTEXT.md}
**Build:** `{command}` | **Test:** `{command}`

**Active Work:**
- {Task folder}: {current task or "no tasks started"}
- Status: {from Status.md or "unknown"}

**Notes:**
- {any blockers, decisions, or open questions}
```

---

> **Usage notes:** Run when starting a new session, after context gets long, before making significant changes, or when you've lost track of where things stand.

$ARGUMENTS
