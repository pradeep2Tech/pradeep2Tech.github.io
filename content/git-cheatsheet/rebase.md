---
title: "Rebase"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "git rebase — replay commits, update feature branch, and golden rules for shared branches."
tags: ["git-cheatsheet", "git", "cheatsheet", "handbook"]
categories: ["Git Cheatsheet"]
shortTitle: "Rebase"
module: 2
moduleTitle: "Branching & Integration"
sectionRef: "2.3"
ShowToc: true
---

## Executive Summary

`git rebase` **replays** commits from one branch onto another tip, producing a linear history. Use it to refresh a feature branch on latest `main`. **Never rebase commits already pushed and shared** without explicit team agreement — SHAs change.

---

## Core Concepts

```mermaid
gitGraph
  commit id: "A"
  branch main
  commit id: "B"
  branch feature
  checkout feature
  commit id: "C"
  commit id: "D"
  checkout main
  commit id: "E"
  checkout feature
  commit id: "C'"
  commit id: "D'"
```

| Operation | Effect |
| :--- | :--- |
| `git rebase main` | Replay current branch commits on top of `main` |
| `git pull --rebase` | Fetch + rebase local commits on remote |
| `git rebase -i` | Interactive — squash, reorder, edit (see Interactive Rebase) |

| Safe | Risky |
| :--- | :--- |
| Rebase local-only feature branch | Rebase `main` or shared branch |
| Before first push | After others based work on your commits |

---

## Quick Reference

| Task | Command |
| :--- | :--- |
| Rebase onto main | `git switch feature && git rebase main` |
| Rebase onto remote main | `git fetch && git rebase origin/main` |
| Abort | `git rebase --abort` |
| Continue | `git rebase --continue` |
| Skip commit | `git rebase --skip` |
| Pull with rebase | `git pull --rebase` |
| Autostash | `git rebase --autostash main` |

```bash
git switch feature/oauth
git fetch origin
git rebase origin/main
# fix conflicts → git add . → git rebase --continue
git push --force-with-lease origin feature/oauth
```

---

## Examples

### Keep feature branch current (daily)

```bash
git switch feature/payments
git fetch origin
git rebase origin/main
```

### Rebase after PR feedback (local commits only)

```bash
git commit --amend -m "fix: address review"
git rebase -i HEAD~3          # squash WIP commits
```

### `pull.rebase` default for cleaner history

```bash
git config --global pull.rebase true
git config --global rebase.autoStash true
```

### Recovery after bad rebase

```bash
git reflog
git reset --hard HEAD@{3}     # point before rebase started
```

---

## Best Practices

- **Golden rule:** do not rebase public/shared history.
- After rebase + push, use `--force-with-lease` not `--force` (safety check).
- Rebase **before** PR review, not after merge to main.
- For merge commits in feature branch, use `git rebase --rebase-merges` (advanced).
- Communicate when force-pushing shared feature branches.

---

## Common Interview Questions

{{< interview-answer >}}
**Q:** Why does rebase rewrite history?

**A:** Each replayed commit gets a **new parent** and **new SHA** even if the diff is identical. Old commits become unreachable (until reflog expires).
{{< /interview-answer >}}

{{< interview-answer >}}
**Q:** `git pull --rebase` vs `git pull` (merge)?

**A:** **Rebase pull** puts your local commits on top of fetched remote — linear history. **Merge pull** creates a merge commit when both sides diverged. Team should pick one default.
{{< /interview-answer >}}

---

## Related Topics

- [Interactive Rebase](/git-cheatsheet/interactive-rebase/) — squash, edit, reorder
- [Merge](/git-cheatsheet/merge/) — non-rewriting integration
- [Reset](/git-cheatsheet/reset/) — recover from rebase mistakes
- [Conflict Resolution](/git-cheatsheet/conflict-resolution/)
