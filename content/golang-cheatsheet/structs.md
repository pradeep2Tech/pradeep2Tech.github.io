---
title: "Structs"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Struct types, embedding, tags, and JSON marshaling patterns."
tags: ["golang", "go", "golang-cheatsheet", "cheatsheet", "handbook"]
categories: ["Go Cheat Sheet"]
shortTitle: "Structs"
module: 2
moduleTitle: "Types & Structs"
sectionRef: "2.1"
ShowToc: true
cheatSheet: true
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

- See [Effective Go](https://go.dev/doc/effective_go) for idioms.

---

## See Also

- [Previous: Functions](/golang-cheatsheet/functions/)
- [Next: Interfaces](/golang-cheatsheet/interfaces/)
- [Go Cheat Sheet Index](/golang-cheatsheet/)
