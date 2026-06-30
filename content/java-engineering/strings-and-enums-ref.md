---
title: "Strings & Enums Reference"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Immutability, interning, text blocks, StringBuilder vs concat, enum patterns."
tags: ["java", "java-engineering", "handbook"]
categories: ["Java Engineering Handbook"]
shortTitle: "Strings & Enums"
module: 1
moduleTitle: "Language Essentials"
sectionRef: "1.2"
ShowToc: true
cheatSheet: true
---

## At a Glance

- `String` is immutable, UTF-16 `char` sequence; Java 21+ also has compact strings / UTF-8 byte backing internally.
- Literal pooling: compile-time constants interned; `intern()` costly — avoid in hot paths.
- Text blocks (15+) for multiline; `formatted`/`String.format` for templates.
- Enums: singleton-like, serializable, can implement interfaces; prefer over int constants.

---

## Reference Tables

| Operation | API | Complexity / note |
| :--- | :--- | :--- |
| Concat in loop | `StringBuilder` | O(n) total vs O(n²) for `+` in loop |
| Comparison | `equals` / `equalsIgnoreCase` | Never `==` unless interned literal |
| Search | `indexOf`, `contains` | Mind surrogate pairs for emoji |
| Split | `split(regex)` | Trailing empty strings dropped unless limit |
| Join | `String.join`, `Collectors.joining` | Prefer over manual builder for lists |

| Enum pattern | Use when |
| :--- | :--- |
| Simple constants | `enum Status { OPEN, CLOSED }` |
| Fields + ctor | Each constant carries data |
| Strategy enum | `enum Op { PLUS { int apply(int a,int b){...} } }` |
| `EnumSet` / `EnumMap` | Bitset/array-backed — fast, compact |

| Builder | Thread-safe | When |
| :--- | :---: | :--- |
| `StringBuilder` | No | Single-thread concat |
| `StringBuffer` | Yes | Legacy only |
| `String` concat `+` | N/A | OK for few operands; compiler may use builder |

---

## Snippets

```java
// Text block + formatted (21+) — multiline string literal in source
String json = String.format("{\"id\": %d, \"name\": \"%s\"}", id, name);

EnumSet<Day> weekend = EnumSet.of(Day.SATURDAY, Day.SUNDAY);
EnumMap<Day, Integer> hours = new EnumMap<>(Day.class);
```

---

## Internals & Gotchas

- `hashCode` caches after first compute (field `hash` in OpenJDK).
- `substring` (pre-7) copied; modern JDK shares array/compact representation.
- `enum` values(): clone each call — cache if hot.
- Switch on enum: compiler synthesizes ordinal map — don't rely on ordinal in persisted data.

---

## Production Notes

- Log user input with length cap; avoid logging full payloads in prod.
- Locale: use `toLowerCase(Locale.ROOT)` for identifiers.
- Persist enums by name (`name()`), never `ordinal()`.

---

## Interview Probes


{< interview-answer >}
**Q:** `String` immutability — why?

**A:** Thread-safe sharing, safe as map keys, hash caching, security (can't mutate URL/credential strings). Trade-off: many intermediate objects on concat.
{< /interview-answer >}

{< interview-answer >}
**Q:** When `EnumSet` over `HashSet<Enum>`?

**A:** `EnumSet` is bit vector — O(1) ops, no boxing, compact. Use for flag sets over enum universe.
{< /interview-answer >}

---

## See Also

- [Previous: Core Java](/java-engineering/core-java-quick-ref/)
- [Next: OOP](/java-engineering/oop-quick-ref/)
- [Java Engineering Handbook Index](/java-engineering/)
