# Tasks

This folder contains structured task breakdowns for project work.

## Structure

```
Tasks/
  {FeatureName}/
    CONTEXT.md        # Goal, scope, and requirements
    Status.md         # Progress tracking
    01.TaskName.md    # Individual task files
    02.TaskName.md
    ...
```

## Conventions

- **One folder per feature or initiative**
- **Tasks are numbered** (`01.`, `02.`, etc.) and executed in order
- **Each task has a clear Definition of Done**
- **Git commits occur at task boundaries**

## Creating Tasks

Use the `/brain` command to scaffold a new feature:

```
/brain "My Feature Name"
```

This creates the folder structure and guides you through the BRAIN workflow.

## Task States

| Status | Meaning |
|--------|---------|
| Todo | Not started |
| In Progress | Currently being worked on |
| Blocked | Waiting on something external |
| Done | Completed and committed |

See [AGENTS.md](../AGENTS.md) for task execution rules.
