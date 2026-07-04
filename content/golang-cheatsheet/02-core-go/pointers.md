---
title: "Pointers"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "Address-of, dereference, new vs make, and when pointers matter in Go."
tags: ["golang", "golang-cheatsheet", "golang-handbook", "go", "interview"]
categories: ["Go Handbook"]
shortTitle: "Pointers"
module: 2
moduleTitle: "Core Go"
sectionRef: "2.2"
weight: 202
cheatSheet: true
interviewHandbook: true
aliases:
  - "/golang-cheatsheet/pointers/"
---

## Quick Revision

- `&` address-of, `*` dereference; no pointer arithmetic.
- `new(T)` allocates zeroed `*T`; `make` only for slice/map/chan.
- Stack vs heap: [Escape Analysis](/golang-cheatsheet/03-go-internals/escape-analysis/).

## At a Glance

- Pointers hold addresses. Go has **no pointer arithmetic**. Use pointers for mutation, large structs, or optional presence (`nil` pointer).

---

## Reference Tables

| Operator | Meaning |
| :--- | :--- |
| `&x` | Address of x |
| `*p` | Value at p |
| `new(T)` | `*T` allocated, zeroed |
| `make(T)` | Only slice, map, chan — not `new` |

| Prefer pointer when | Prefer value when |
| :--- | :--- |
| Mutate callee state | Small, immutable structs |
| Avoid copy | No mutation needed |
| `nil` means absent | Sync/copy semantics matter |

```go
p := new(int)   // *int, zero
*p = 42

type Node struct { Next *Node }

func (n *Node) SetNext(next *Node) { n.Next = next }
```

---

## Snippets

```go
func swap(a, b *int) {
    *a, *b = *b, *a
}

x, y := 1, 2
swap(&x, &y)
```

---

## Internals & Gotchas

- `new` returns pointer; `make` initializes slice/map/chan internals.
- Stack vs heap allocation is decided by [escape analysis](/golang-cheatsheet/03-go-internals/escape-analysis/).
- Taking address of map element is **illegal** (may move on grow).
- `nil` pointer dereference panics.

---

## Production Notes

- Apply patterns from this page in code review and incident postmortems.

---

---

---

## See Also

- [Previous: Interfaces](/golang-cheatsheet/02-core-go/interfaces/)
- [Next: Packages](/golang-cheatsheet/02-core-go/packages/)
- [Go Handbook Index](/golang-cheatsheet/)
- [Top 150 Interview Questions](/golang-cheatsheet/08-interview-guide/top-150-interview-questions/)
