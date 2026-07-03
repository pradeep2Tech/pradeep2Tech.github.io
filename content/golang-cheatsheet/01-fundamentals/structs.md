---
title: "Structs"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "Struct types, embedding, tags, and JSON marshaling patterns."
tags: ["golang", "golang-cheatsheet", "golang-handbook", "go", "interview"]
categories: ["Go Handbook"]
shortTitle: "Structs"
module: 1
moduleTitle: "Fundamentals"
sectionRef: "1.3"
weight: 113
ShowToc: true
cheatSheet: true
interviewHandbook: true
aliases:
  - "/golang-cheatsheet/structs/"
---

## At a Glance

- **Structs** group fields. Go uses **composition over inheritance** via **embedded** anonymous fields. Struct tags drive JSON/XML encoding.

---

## Reference Tables

| Concept | Recap |
| :--- | :--- |
| Literal | `Point{X: 1, Y: 2}` or `Point{1, 2}` |
| Embedding | Anonymous field promotes methods/fields |
| Tags | `` `json:"name,omitempty"` `` |
| Comparable | Struct comparable if all fields comparable |
| Zero value | All fields zeroed |

| Operation | Syntax |
| :--- | :--- |
| Pointer to struct | `&User{Name: "a"}` or `new(User)` |
| Embedded access | `s.Field` promoted from embed |
| Copy | Assignment copies all fields (shallow) |

---

## Snippets

```go
type User struct {
    ID   int    `json:"id"`
    Name string `json:"name,omitempty"`
}

type Admin struct {
    User            // embedded
    Permissions []string
}

func (u User) String() string {
    return fmt.Sprintf("User(%d)", u.ID)
}
```

---

## Internals & Gotchas

- Embedded pointer fields: `nil` embed → promoted methods may panic.
- Comparing structs with slices/maps inside is **invalid**.
- JSON `omitempty` skips zero values — `false`, `0`, `""`, `nil`.

---

## Production Notes

- Apply patterns from this page in code review and incident postmortems.

---

## How does embedding promote methods and what happens with nil embedded pointers?

### Short Answer
Anchor the answer in Go runtime semantics, observable behavior, and production tradeoffs for structs.

### Detailed Explanation
Senior interviews expect mechanism-first reasoning: what the language/runtime guarantees, what it does not, and how that shows up under load or failure.

### Internal Working
Go couples language rules (types, interfaces, concurrency primitives) with a runtime scheduler, GC, and memory model. Correct answers connect API behavior to these subsystems.

### Production Notes
Validate assumptions with `go test -race`, benchmarks, and pprof before changing architecture. Pin Go versions and document SLO impact of concurrency/GC choices.

### Common Mistakes
Hand-waving 'Go is fast' without allocation, scheduling, or cancellation analysis. Copying patterns without bounding goroutines or defining shutdown behavior.

### Follow-up Questions
What observable metric or test would prove your design handles this structs concern in production?

---
<!-- interview-answers:end -->

---

## How does embedding promote methods and what happens with nil embedded pointers?

### Short Answer
The mechanism-first explanation is interfaces are implicit (type,data) pairs; typed nil breaks `== nil` — for: How does embedding promote methods and what happens with nil embedded pointers.

### Detailed Explanation
Tie method sets (value vs pointer receivers) to satisfaction and API design for: How does embedding promote methods and what happens with nil embedded pointers.

### Internal Working
Small interfaces at boundaries; empty interface boxes values and may allocate — internal angle on: How does embedding promote methods and what happens with nil embedded pointers.

### Production Notes
Use compile-time `var _ IF = (*T)(nil)` checks; test JSON nil edge cases for: How does embedding promote methods and what happens with nil embedded pointers.

### Common Mistakes
Returning typed nil pointers in interface-typed APIs is a classic bug in: How does embedding promote methods and what happens with nil embedded pointers.

### Follow-up Questions
How would you refactor a fat interface exposed by: How does embedding promote methods and what happens with nil embedded pointers?

---
<!-- interview-answers:end -->

---

## See Also

- [Previous: Functions](/golang-cheatsheet/01-fundamentals/functions/)
- [Next: Arrays](/golang-cheatsheet/01-fundamentals/arrays/)
- [Go Handbook Index](/golang-cheatsheet/)
- [Top 150 Interview Questions](/golang-cheatsheet/08-interview-guide/top-150-interview-questions/)
