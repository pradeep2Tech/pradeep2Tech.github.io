---
title: "Go Interview Questions"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "High-signal Go interview probes — concurrency, interfaces, slices, and GC."
tags: ["golang", "go", "golang-cheatsheet", "cheatsheet", "handbook"]
categories: ["Go Cheat Sheet"]
shortTitle: "Interview"
module: 10
moduleTitle: "Interview"
sectionRef: "10.1"
ShowToc: true
cheatSheet: true
---

## At a Glance

- High-signal **Go interview** topics: interface nil semantics, slice internals, concurrency patterns, error handling, and GC/allocation trade-offs.

---

## Reference Tables

| Topic | Classic question |
| :--- | :--- |
| Interfaces | Why `interface == nil` is false with typed nil |
| Slices | What `append` does to cap/len and aliasing |
| Concurrency | Buffered vs unbuffered; when to use mutex vs channel |
| Errors | `%w` vs `%v`; `errors.Is` |
| Runtime | What GOGC does; how to reduce GC pressure |

| Probe | Strong answer shape |
| :--- | :--- |
| Goroutine vs thread | M:N scheduling, smaller stacks, cooperative points |
| Map concurrency | Not safe — mutex or sync.Map |
| Context | Cancellation tree; first param; defer cancel |
| defer order | LIFO; args evaluated at defer statement |

---

## Snippets

```go
// Q: What prints?
var w io.Writer
var buf *bytes.Buffer
w = buf
fmt.Println(w == nil) // false

// Q: slice after append
x := []int{1, 2, 3}
y := append(x[:2], 99)
// know shared backing array effects
```

---

## Internals & Gotchas

- Memorize **nil interface** and **slice header** — most common loops.
- "Share memory by communicating" — but know when mutex is simpler.
- Read [Effective Go](https://go.dev/doc/effective_go) and Go FAQ for phrasing.

---

## Production Notes

- See [Effective Go](https://go.dev/doc/effective_go) for idioms.

---

## See Also

- [Previous: Dependencies](/golang-cheatsheet/dependency-management/)
- [Go Cheat Sheet Index](/golang-cheatsheet/)
