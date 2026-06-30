---
title: "Pointers"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Address-of, dereference, new vs make, and when pointers matter in Go."
tags: ["golang", "go", "golang-cheatsheet", "cheatsheet", "handbook"]
categories: ["Go Cheat Sheet"]
shortTitle: "Pointers"
module: 2
moduleTitle: "Types & Structs"
sectionRef: "2.3"
ShowToc: true
cheatSheet: true
---

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
- Taking address of map element is **illegal** (may move on grow).
- `nil` pointer dereference panics.

---

## Production Notes

- See [Effective Go](https://go.dev/doc/effective_go) for idioms.

---

## See Also

- [Previous: Interfaces](/golang-cheatsheet/interfaces/)
- [Next: Methods](/golang-cheatsheet/methods/)
- [Go Cheat Sheet Index](/golang-cheatsheet/)
