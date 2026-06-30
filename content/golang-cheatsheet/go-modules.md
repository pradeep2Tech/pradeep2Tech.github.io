---
title: "Go Modules"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "go.mod, go.sum, module path, replace, and workspace mode."
tags: ["golang", "go", "golang-cheatsheet", "cheatsheet", "handbook"]
categories: ["Go Cheat Sheet"]
shortTitle: "Modules"
module: 9
moduleTitle: "Modules & Tooling"
sectionRef: "9.1"
ShowToc: true
cheatSheet: true
---

## At a Glance

- **Go modules** are the unit of dependency versioning since Go 1.16+. Defined by **`go.mod`** at module root; checksums in **`go.sum`**.

---

## Reference Tables

| File | Role |
| :--- | :--- |
| `go.mod` | Module path, Go version, require/replace/exclude |
| `go.sum` | Cryptographic checksums of module contents |
| `go.work` | Multi-module workspace (local dev) |

| Directive | Purpose |
| :--- | :--- |
| `module` | Import path prefix |
| `require` | Dependencies |
| `replace` | Local fork or vanity redirect |
| `retract` | Withdraw bad versions |

```bash
go mod init example.com/myapp
go mod tidy
go mod verify
go mod graph
```

---

## Snippets

```go
module github.com/org/project

go 1.22

require (
    github.com/lib/pq v1.10.9
)
```

---

## Internals & Gotchas

- Commit `go.sum` — required for reproducible builds.
- Major version `/v2` in module path for v2+ APIs.
- `replace` in go.mod is local-only — don't rely in published libraries.

---

## Production Notes

- See [Effective Go](https://go.dev/doc/effective_go) for idioms.

---

## See Also

- [Previous: GC](/golang-cheatsheet/garbage-collection/)
- [Next: Dependencies](/golang-cheatsheet/dependency-management/)
- [Go Cheat Sheet Index](/golang-cheatsheet/)
