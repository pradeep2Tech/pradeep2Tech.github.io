---
title: "Exceptions Quick Reference"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Checked vs unchecked, try-with-resources, suppression, and API design rules."
tags: ["java", "java-engineering", "handbook"]
categories: ["Java Engineering Handbook"]
shortTitle: "Exceptions"
module: 4
moduleTitle: "Exceptions & Generics"
sectionRef: "4.1"
ShowToc: true
cheatSheet: true
---

## At a Glance

- Checked: must handle or declare — `IOException`, `SQLException`.
- Unchecked: `RuntimeException` — programming bugs, optional handling.
- `Error`: serious JVM issues — generally don't catch.
- try-with-resources (7+): auto-close `AutoCloseable` in LIFO order.

---

## Reference Tables

| Type | Examples | Handle? |
| :--- | :--- | :--- |
| Checked | `IOException` | Compile-time |
| Unchecked | `IllegalArgumentException` | Optional |
| Error | `OutOfMemoryError` | Usually propagate |
| `Throwable` | Root | Catch only at boundary |

| Pattern | Use |
| :--- | :--- |
| Fail fast | Validate early, throw unchecked |
| Wrap + cause | `new ServiceException("msg", e)` preserve stack |
| Suppressed | try-with-resources multiple close failures |
| Multi-catch | `catch (IOException | SQLException e)` |

| Anti-pattern | Fix |
| :--- | :--- |
| Swallow empty catch | Log or rethrow |
| Catch `Exception` everywhere | Catch specific at low level |
| Control flow via exceptions | Use return codes/Optional |

---

## Snippets

```java
try (var in = Files.newInputStream(path);
     var out = Files.newOutputStream(target)) {
    in.transferTo(out);
} catch (IOException e) {
    throw new UncheckedIOException(e);
}
```

---

## Internals & Gotchas

- Exception creation captures stack trace — expensive in hot path.
- `fillInStackTrace` can be overridden for lightweight exceptions (rare).
- `addSuppressed` links close exceptions from TWR.

---

## Production Notes

- Global handler at service boundary maps to HTTP/gRPC codes.
- Never log and swallow security/auth failures.
- Use domain unchecked exceptions for invariant violations.

---

## Interview Probes


{< interview-answer >}
**Q:** Checked exceptions controversy?

**A:** Forces handling but encourages empty catches and wrapping layers. Modern APIs (Spring, NIO streams) lean unchecked + wrap.
{< /interview-answer >}

{< interview-answer >}
**Q:** try-with-resources order?

**A:** Resources closed reverse declaration order; primary exception wins, others suppressed.
{< /interview-answer >}

---

## See Also

- [Previous: CHM Internals](/java-engineering/concurrenthashmap-internals/)
- [Next: Generics](/java-engineering/generics-quick-ref/)
- [Java Engineering Handbook Index](/java-engineering/)
