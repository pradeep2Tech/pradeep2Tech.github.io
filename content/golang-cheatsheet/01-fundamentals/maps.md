---
title: "Maps"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "Map operations, iteration order, nil maps, and concurrency safety."
tags: ["golang", "golang-cheatsheet", "golang-handbook", "go", "interview"]
categories: ["Go Handbook"]
shortTitle: "Maps"
module: 1
moduleTitle: "Fundamentals"
sectionRef: "1.6"
weight: 116
ShowToc: true
cheatSheet: true
interviewHandbook: true
aliases:
  - "/golang-cheatsheet/maps/"
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
| Concurrent | Not safe concurrent — use mutex or [sync.Map](/golang-cheatsheet/04-concurrency/sync-package/) |

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

- Apply patterns from this page in code review and incident postmortems.

---

## How do map concurrent write panics manifest and what is the permanent fix?

### Short Answer
Slices are views (ptr,len,cap); subslices alias backing arrays. Maps are not safe for concurrent use without sync.

### Detailed Explanation
append may reallocate and copy when cap exhausted. Subslices of large arrays can leak memory if a small slice is retained. Map growth and iteration have defined but subtle semantics.

### Internal Working
Map writes are not atomic across goroutines — runtime detects concurrent map writes and panics. Slice headers are small but point to shared storage.

### Production Notes
Preallocate slices when size is known. Copy or reslice with full slice expression to detach from large backing arrays. Protect maps with mutex or sync.Map.

### Common Mistakes
Assuming append never mutates other slices sharing backing array. Using maps from multiple goroutines without synchronization.

### Follow-up Questions
How would you prove a memory leak is slice aliasing versus a true goroutine leak?

---
## Why can't you take the address of a map element?

### Short Answer
Slices are views (ptr,len,cap); subslices alias backing arrays. Maps are not safe for concurrent use without sync.

### Detailed Explanation
append may reallocate and copy when cap exhausted. Subslices of large arrays can leak memory if a small slice is retained. Map growth and iteration have defined but subtle semantics.

### Internal Working
Map writes are not atomic across goroutines — runtime detects concurrent map writes and panics. Slice headers are small but point to shared storage.

### Production Notes
Preallocate slices when size is known. Copy or reslice with full slice expression to detach from large backing arrays. Protect maps with mutex or sync.Map.

### Common Mistakes
Assuming append never mutates other slices sharing backing array. Using maps from multiple goroutines without synchronization.

### Follow-up Questions
How would you prove a memory leak is slice aliasing versus a true goroutine leak?

---
<!-- interview-answers:end -->

---

## How do map concurrent write panics manifest and what is the permanent fix?

### Short Answer
In production Go, the decisive factor is maps are not safe concurrent; iteration order is random; nil map write panics — for: How do map concurrent write panics manifest and what is the permanent fix.

### Detailed Explanation
Use mutex+map or sync.Map with clear criteria; never &m[k] — for: How do map concurrent write panics manifest and what is the permanent fix.

### Internal Working
Map growth may move buckets; concurrent write detected at runtime — internal note for: How do map concurrent write panics manifest and what is the permanent fix.

### Production Notes
Guard shared maps; document ownership in reviews covering: How do map concurrent write panics manifest and what is the permanent fix.

### Common Mistakes
Ranging maps while mutating without sync or assuming stable order fails: How do map concurrent write panics manifest and what is the permanent fix.

### Follow-up Questions
When is sync.Map worth it vs RWMutex+map for: How do map concurrent write panics manifest and what is the permanent fix?

---
## Why can't you take the address of a map element?

### Short Answer
The senior-level answer is maps are not safe concurrent; iteration order is random; nil map write panics — for: Why can't you take the address of a map element.

### Detailed Explanation
Use mutex+map or sync.Map with clear criteria; never &m[k] — for: Why can't you take the address of a map element.

### Internal Working
Map growth may move buckets; concurrent write detected at runtime — internal note for: Why can't you take the address of a map element.

### Production Notes
Guard shared maps; document ownership in reviews covering: Why can't you take the address of a map element.

### Common Mistakes
Ranging maps while mutating without sync or assuming stable order fails: Why can't you take the address of a map element.

### Follow-up Questions
When is sync.Map worth it vs RWMutex+map for: Why can't you take the address of a map element?

---
<!-- interview-answers:end -->

---

## See Also

- [Previous: Slices](/golang-cheatsheet/01-fundamentals/slices/)
- [Next: Methods](/golang-cheatsheet/01-fundamentals/methods/)
- [Go Handbook Index](/golang-cheatsheet/)
- [Top 150 Interview Questions](/golang-cheatsheet/08-interview-guide/top-150-interview-questions/)
