---
title: "Maps"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "map operations, iteration order, nil maps, and sync.Map overview."
tags: ["golang", "go", "golang-cheatsheet", "cheatsheet", "handbook"]
categories: ["Go Cheat Sheet"]
shortTitle: "Maps"
module: 4
moduleTitle: "Collections"
sectionRef: "4.3"
ShowToc: true
cheatSheet: true
---

## At a Glance

- Maps are hash tables — **reference type** (like slices). Must be initialized with `make` or literal before write. **Iteration order is randomized**.

---

## Reference Tables

| Op | Code |
| :--- | :--- |
| Literal | `m := map[string]int{"a": 1}` |
| Make | `m := make(map[string]int, 100)` |
| Read | `v := m[k]` — zero value if missing |
| Check | `v, ok := m[k]` |
| Delete | `delete(m, k)` |

| Topic | Note |
| :--- | :--- |
| Nil map | Read OK; write panics |
| Not addressable elements | Can't `&m[k]` |
| Concurrent | Use `sync.Map` or mutex + map |

---

## Snippets

```go
counts := make(map[string]int)
counts["go"]++

if v, ok := counts["rust"]; ok {
    _ = v
}

for k, v := range counts {
    fmt.Println(k, v)
}
```

---

## Internals & Gotchas

- Never R/W same map from goroutines without sync.
- Taking pointer to value in map forbidden.
- Map keys must be comparable — no slices/maps/funcs as keys.

---

## Production Notes

- See [Effective Go](https://go.dev/doc/effective_go) for idioms.

---

## See Also

- [Previous: Arrays](/golang-cheatsheet/arrays/)
- [Next: Goroutines](/golang-cheatsheet/goroutines/)
- [Go Cheat Sheet Index](/golang-cheatsheet/)
