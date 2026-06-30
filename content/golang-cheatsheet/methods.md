---
title: "Methods"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Value vs pointer receivers, method sets, and interface satisfaction."
tags: ["golang", "go", "golang-cheatsheet", "cheatsheet", "handbook"]
categories: ["Go Cheat Sheet"]
shortTitle: "Methods"
module: 2
moduleTitle: "Types & Structs"
sectionRef: "2.4"
ShowToc: true
cheatSheet: true
---

## At a Glance

- Methods are functions with a **receiver**. **Value receivers** copy; **pointer receivers** mutate and are required when the method modifies the receiver or the struct is large.

---

## Reference Tables

| Receiver | Method set includes |
| :--- | :--- |
| `(T)` | Methods with value receiver |
| `(*T)` | Methods with pointer **and** value receiver |

| Rule of thumb | Use |
| :--- | :--- |
| Mutates receiver | Pointer receiver |
| Contains sync.Mutex | Pointer receiver (don't copy mutex) |
| Small immutable type | Value receiver |

```go
type Counter struct{ n int }

func (c *Counter) Inc() { c.n++ }
func (c Counter) Value() int { return c.n }
```

---

## Snippets

```go
type Buffer struct {
    b []byte
}

func (b *Buffer) Write(p []byte) (int, error) {
    b.b = append(b.b, p...)
    return len(p), nil
}

func (b Buffer) Len() int { return len(b.b) }
```

---

## Internals & Gotchas

- Calling pointer method on addressable value auto-takes `&`.
- Interface satisfaction uses **method set** of the stored type.
- Don't mix value/pointer receivers on same type without reason.

---

## Production Notes

- See [Effective Go](https://go.dev/doc/effective_go) for idioms.

---

## See Also

- [Previous: Pointers](/golang-cheatsheet/pointers/)
- [Next: Packages](/golang-cheatsheet/packages/)
- [Go Cheat Sheet Index](/golang-cheatsheet/)
