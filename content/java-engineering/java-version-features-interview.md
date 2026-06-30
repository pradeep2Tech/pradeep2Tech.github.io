---
title: "Java Version Features (Interview)"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "What shipped in each LTS and recent releases — whiteboard facts."
tags: ["java", "java-engineering", "handbook"]
categories: ["Java Engineering Handbook"]
shortTitle: "Version Features"
module: 11
moduleTitle: "Interview Cheat Sheets"
sectionRef: "11.5"
ShowToc: true
cheatSheet: true
---

## At a Glance

- Whiteboard LTS deltas — 8→11→17→21.
- Records/sealed/patterns = 16–21 story.
- Modules strong encapsulation = 9/17 enforcement.
- Virtual threads = 21 headline.

---

## Reference Tables

| Release | Headline features |
| :---: | :--- |
| 8 | Lambdas, streams, `Optional`, `java.time` |
| 11 | HTTP client, `var` in lambda, removed JavaEE modules |
| 17 | Records, sealed, pattern `instanceof` |
| 21 | Virtual threads, sequenced collections, pattern switch |
| 25 | LTS rollup — check release notes for GA |

| Question angle | Answer shape |
| :--- | :--- |
| Why upgrade? | Security, support, performance, language productivity |
| Risk | Removed APIs, reflection, dependencies |
| Preview features | Not in prod without flag plan |

---

## Snippets

```java
// 17+ style
public sealed interface Result permits Ok, Err {}
public record Ok<T>(T value) implements Result {}
```

---

## Internals & Gotchas

- `-release` flag ties bytecode to API.
- LTS support timelines vendor-specific.

---

## Production Notes

- Automate dependency compatibility scans on JDK bump.
- Run canary with new JDK before fleet.

---

## Interview Probes


{< interview-answer >}
**Q:** Top 3 Java 17 features for teams?

**A:** Records (DTOs), sealed (domain), pattern matching (cleaner code paths) — plus strong encapsulation forcing dependency updates.
{< /interview-answer >}

{< interview-answer >}
**Q:** 8 to 21 biggest infra change?

**A:** Module encapsulation + remove illegal reflective access; thread model option with virtual threads.
{< /interview-answer >}

---

## See Also

- [Previous: GC Interview](/java-engineering/gc-summary-interview/)
- [Next: Memory Diagram](/java-engineering/memory-diagram-interview/)
- [Java Engineering Handbook Index](/java-engineering/)
