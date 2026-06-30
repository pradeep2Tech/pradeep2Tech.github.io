---
title: "Garbage Collection"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Go GC tri-color mark-sweep, GOGC, pacing, and allocation tuning."
tags: ["golang", "go", "golang-cheatsheet", "cheatsheet", "handbook"]
categories: ["Go Cheat Sheet"]
shortTitle: "GC"
module: 8
moduleTitle: "Runtime"
sectionRef: "8.2"
ShowToc: true
cheatSheet: true
---

## At a Glance

- Go uses a **non-generational, concurrent tri-color mark-sweep** collector. Tuning via **`GOGC`** (default 100). **STW** pauses are short but exist.

---

## Reference Tables

```mermaid
flowchart LR
  alloc[Allocation] --> heap[Heap]
  heap --> mark[Concurrent mark]
  mark --> sweep[Sweep]
```

| Knob | Effect |
| :--- | :--- |
| `GOGC=100` | Heap doubles before next GC cycle |
| `GOGC=off` | Disable GC (debug only) |
| `GODEBUG=gctrace=1` | Log GC events |
| `runtime.GC()` | Force GC — rarely in prod |

| Goal | Approach |
| :--- | :--- |
| Less GC CPU | Reduce allocations — pools, reuse buffers |
| Lower latency | Fewer pointers, smaller heap |
| Profile | `pprof` heap/allocs |

---

## Snippets

```go
// prefer sync.Pool for short-lived buffers
// prefer value semantics for hot structs
// preallocate slices: make([]T, 0, n)
```

---

## Internals & Gotchas

- Finalizers (`runtime.SetFinalizer`) run unpredictably — don't rely for cleanup.
- Large heap = longer mark phase — allocation rate matters more than live set alone.
- `uintptr` is not a GC root — keep pointer alive.

---

## Production Notes

- See [Effective Go](https://go.dev/doc/effective_go) for idioms.

---

## See Also

- [Previous: Memory Model](/golang-cheatsheet/memory-model/)
- [Next: Modules](/golang-cheatsheet/go-modules/)
- [Go Cheat Sheet Index](/golang-cheatsheet/)
