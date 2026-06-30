---
title: "Dependency Management"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "go get, versioning, minimal version selection, and vendoring."
tags: ["golang", "go", "golang-cheatsheet", "cheatsheet", "handbook"]
categories: ["Go Cheat Sheet"]
shortTitle: "Dependencies"
module: 9
moduleTitle: "Modules & Tooling"
sectionRef: "9.2"
ShowToc: true
cheatSheet: true
---

## At a Glance

- Go uses **Minimal Version Selection (MVS)** — `go.mod` lists minimum versions; build picks lowest compatible set. Upgrade with **`go get pkg@version`**.

---

## Reference Tables

| Command | Action |
| :--- | :--- |
| `go get pkg@latest` | Upgrade to latest |
| `go get pkg@v1.2.3` | Pin version |
| `go get pkg@none` | Remove dependency |
| `go mod vendor` | Copy deps to `vendor/` |
| `go list -m all` | Resolved module list |

```bash
go get -u ./...
go get github.com/foo/bar@v1.5.0
go mod tidy   # add missing, drop unused
```

---

## Snippets

```bash
# private module
GOPRIVATE=github.com/myorg/*
go env -w GOPRIVATE=github.com/myorg/*
```

---

## Internals & Gotchas

- `go get -u` in library repos — bump carefully; consumers resolve MVS.
- Vendoring: `-mod=vendor` in CI for hermetic builds.
- Pseudo-versions for untagged commits: `v0.0.0-20240101120000-abcdef`.

---

## Production Notes

- See [Effective Go](https://go.dev/doc/effective_go) for idioms.

---

## See Also

- [Previous: Modules](/golang-cheatsheet/go-modules/)
- [Next: Interview](/golang-cheatsheet/interview-questions/)
- [Go Cheat Sheet Index](/golang-cheatsheet/)
