---
title: "Arrays"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "Fixed-size arrays, array vs slice, and when arrays appear in APIs."
tags: ["golang", "golang-cheatsheet", "golang-handbook", "go", "interview"]
categories: ["Go Handbook"]
shortTitle: "Arrays"
module: 1
moduleTitle: "Fundamentals"
sectionRef: "1.4"
weight: 114
ShowToc: true
cheatSheet: true
interviewHandbook: true
aliases:
  - "/golang-cheatsheet/arrays/"
---

## Quick Revision

- Arrays are **values** (`[N]T`); size is part of the type.
- Prefer **slices** in APIs; arrays appear for crypto keys, fixed buffers, stack arrays.
- Large array parameters **copy** — pass `*[N]T` or slice instead.
- Converting array to slice: `a[:]` — see [Slices](/golang-cheatsheet/01-fundamentals/slices/) for aliasing rules.

## At a Glance

- Arrays have **fixed size** — part of the type (`[3]int` ≠ `[4]int`). Rare in APIs; prefer slices. Arrays are **values** (copied on assignment).

---

## Reference Tables

| Array | Slice |
| :--- | :--- |
| `[N]T` fixed | `[]T` dynamic length |
| Value semantics | Header + backing array |
| Comparable | Not comparable if element not comparable |

```go
var a [3]int = [3]int{1, 2, 3}
b := [...]int{1, 2, 3} // compiler counts

// array to slice
s := a[:] // slice view of array
```

---

## Snippets

```go
// crypto keys, fixed buffers
var key [32]byte
copy(key[:], seed)
```

---

## Internals & Gotchas

- Large arrays as parameters copy entire value — pass pointer or slice.
- `[ ]` in function param is slice, not array.

---

## Production Notes

- Apply patterns from this page in code review and incident postmortems.

---

---

---

## See Also

- [Previous: Structs](/golang-cheatsheet/01-fundamentals/structs/)
- [Next: Slices](/golang-cheatsheet/01-fundamentals/slices/)
- [Go Handbook Index](/golang-cheatsheet/)
- [Top 150 Interview Questions](/golang-cheatsheet/08-interview-guide/top-150-interview-questions/)
