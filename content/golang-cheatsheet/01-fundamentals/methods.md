---
title: "Methods"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "Value vs pointer receivers, method sets, and interface satisfaction."
tags: ["golang", "golang-cheatsheet", "golang-handbook", "go", "interview"]
categories: ["Go Handbook"]
shortTitle: "Methods"
module: 1
moduleTitle: "Fundamentals"
sectionRef: "1.7"
weight: 117
ShowToc: true
cheatSheet: true
interviewHandbook: true
aliases:
  - "/golang-cheatsheet/methods/"
---

## Quick Revision

- **Pointer receiver** when mutating or struct contains `sync.Mutex`.
- **Value receiver** for small immutable types.
- Method set rules drive [interface satisfaction](/golang-cheatsheet/02-core-go/interfaces/).

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

- Apply patterns from this page in code review and incident postmortems.

---

## How do value versus pointer receivers affect interface satisfaction?

### Short Answer
Interfaces are implicit (type, data) pairs; typed nil breaks `== nil`. Errors use wrapping with `%w` and `errors.Is/As`.

### Detailed Explanation
An interface value is nil only when both type and data are nil. A nil pointer inside a non-nil interface type is a classic API bug. Error chains preserve cause for inspection.

### Internal Working
Method sets determine satisfaction — pointer vs value receivers matter. Error wrapping builds an unwrap chain inspected by Is/As.

### Production Notes
Keep interfaces small at boundaries. Never log and return the same error. Use sentinel errors sparingly with documented semantics.

### Common Mistakes
Comparing wrapped errors with `==`. Returning typed nil pointers in interfaces. Giant interfaces that hinder testing.

### Follow-up Questions
How would you test `errors.Is` through three layers of `%w` wrapping?

---
<!-- interview-answers:end -->

---

## How do value versus pointer receivers affect interface satisfaction?

### Short Answer
In production Go, the decisive factor is interfaces are implicit (type,data) pairs; typed nil breaks `== nil` — for: How do value versus pointer receivers affect interface satisfaction.

### Detailed Explanation
Tie method sets (value vs pointer receivers) to satisfaction and API design for: How do value versus pointer receivers affect interface satisfaction.

### Internal Working
Small interfaces at boundaries; empty interface boxes values and may allocate — internal angle on: How do value versus pointer receivers affect interface satisfaction.

### Production Notes
Use compile-time `var _ IF = (*T)(nil)` checks; test JSON nil edge cases for: How do value versus pointer receivers affect interface satisfaction.

### Common Mistakes
Returning typed nil pointers in interface-typed APIs is a classic bug in: How do value versus pointer receivers affect interface satisfaction.

### Follow-up Questions
How would you refactor a fat interface exposed by: How do value versus pointer receivers affect interface satisfaction?

---
<!-- interview-answers:end -->

---

## See Also

- [Previous: Maps](/golang-cheatsheet/01-fundamentals/maps/)
- [Next: Interfaces](/golang-cheatsheet/02-core-go/interfaces/)
- [Go Handbook Index](/golang-cheatsheet/)
- [Top 150 Interview Questions](/golang-cheatsheet/08-interview-guide/top-150-interview-questions/)
