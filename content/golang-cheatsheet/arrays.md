---
title: "Arrays"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Fixed-size arrays, array vs slice, and when arrays appear in APIs."
tags: ["golang", "go", "golang-cheatsheet", "cheatsheet", "handbook"]
categories: ["Go Cheat Sheet"]
shortTitle: "Arrays"
module: 4
moduleTitle: "Collections"
sectionRef: "4.2"
ShowToc: true
cheatSheet: true
---

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

- See [Effective Go](https://go.dev/doc/effective_go) for idioms.

---

## See Also

- [Previous: Slices](/golang-cheatsheet/slices/)
- [Next: Maps](/golang-cheatsheet/maps/)
- [Go Cheat Sheet Index](/golang-cheatsheet/)
