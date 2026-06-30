---
title: "Reflection"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "reflect.Type, reflect.Value, Kind, and when to avoid reflection."
tags: ["golang", "go", "golang-cheatsheet", "cheatsheet", "handbook"]
categories: ["Go Cheat Sheet"]
shortTitle: "Reflection"
module: 7
moduleTitle: "Testing & Reflection"
sectionRef: "7.2"
ShowToc: true
cheatSheet: true
---

## At a Glance

- **Reflection** inspects types at runtime via `reflect.Type` and `reflect.Value`. Powerful for serializers and DI — **avoid** on hot paths; loses compile-time safety.

---

## Reference Tables

| API | Role |
| :--- | :--- |
| `reflect.TypeOf(v)` | Static type |
| `reflect.ValueOf(v)` | Runtime value |
| `Kind()` | Underlying kind — `Struct`, `Ptr`, `Slice` |
| `Field` / `Set` | Struct field access — need addressable value to Set |

```go
v := reflect.ValueOf(x)
if v.Kind() == reflect.Ptr {
    v = v.Elem()
}
for i := 0; i < v.NumField(); i++ {
    f := v.Type().Field(i)
    _ = f.Name
}
```

---

## Snippets

```go
func deepEqual(a, b any) bool {
    return reflect.DeepEqual(a, b)
}
```

---

## Internals & Gotchas

- `reflect.Value` must be **addressable** to modify.
- Breaking refactor won't compile-check reflection-based field access.
- Prefer generics (1.18+) over reflection when possible.

---

## Production Notes

- See [Effective Go](https://go.dev/doc/effective_go) for idioms.

---

## See Also

- [Previous: Testing](/golang-cheatsheet/testing/)
- [Next: Memory Model](/golang-cheatsheet/memory-model/)
- [Go Cheat Sheet Index](/golang-cheatsheet/)
