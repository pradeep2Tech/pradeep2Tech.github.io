---
title: "Java Recent Features Rollup"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Post-17 language and API highlights through current JDK — records to virtual threads."
tags: ["java", "java-engineering", "handbook"]
categories: ["Java Engineering Handbook"]
shortTitle: "Recent Features"
module: 9
moduleTitle: "Modern Java"
sectionRef: "9.2"
ShowToc: true
cheatSheet: true
---

## At a Glance

- Rollup of post-8 language/API wins architects actually adopt in production.
- Records, sealed, pattern matching reduce boilerplate and enable exhaustiveness.
- Virtual threads + structured concurrency change blocking service economics.
- Collections: `SequencedCollection`, `getFirst`/`getLast` (21+).

---

## Reference Tables

| Area | Feature | Since |
| :--- | :--- | :---: |
| Language | `var` local inference | 10 |
| Language | Text blocks | 15 |
| Language | Records | 16 |
| Language | Sealed classes | 17 |
| Language | Pattern matching `instanceof` | 16 |
| Language | Switch patterns | 21 |
| Language | String templates (preview) | 21+ |
| Concurrency | Virtual threads | 21 |
| API | `HttpClient` | 11 |
| API | `List.of`, `Map.of` immutable factories | 9 |
| API | `Optional.isEmpty`, `stream.toList` | 11 / 16 |

| Adopt now (17/21 LTS) | Defer / preview |
| :--- | :--- |
| Records for DTOs | String templates until final |
| Sealed domain ADTs | Foreign API without need |
| Virtual threads for IO services | Structured concurrency until standardized |
| `switch` expressions | |

| Removed / deprecated watch | |
| :--- | :--- |
| Security manager | Deprecated 17, removal planned |
| Finalization | Deprecated 9 |
| Applet API | Removed |

---

## Snippets

```java
record AuditEvent(Instant at, String actor, String action) {}

if (obj instanceof String s && !s.isBlank()) {
    process(s);
}

switch (day) {
    case MONDAY, FRIDAY -> scheduleReview();
    case SATURDAY, SUNDAY -> rest();
    default -> work();
}
```

---

## Internals & Gotchas

- Records are final — frameworks use bytecode enhancement for JPA (discouraged) or mapping layers.
- Virtual threads change thread-per-request without reactive rewrite.
- Pattern switches compile to tableswitch/lookupswitch + type tests.

---

## Production Notes

- Enable features via toolchain not reflection hacks.
- Track JEP status for previews in use.
- Library ecosystem (Lombok overlap) — align team standards.

---

## Interview Probes


{< interview-answer >}
**Q:** Record vs Lombok `@Value`?

**A:** Record is language-native, serialization-friendly, pattern matching ready. Lombok more flexible but external processor dependency.
{< /interview-answer >}

{< interview-answer >}
**Q:** Biggest 21 production win?

**A:** Virtual threads for blocking microservices — simpler than reactive for many teams; still requires JDBC/driver and pool review.
{< /interview-answer >}

---

## See Also

- [Previous: LTS Matrix](/java-engineering/java-lts-release-matrix/)
- [Next: IO & NIO](/java-engineering/java-io-nio-ref/)
- [Java Engineering Handbook Index](/java-engineering/)
