---
title: "Reflection & Annotations Reference"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Core reflection APIs, annotation retention, processors, and module boundaries."
tags: ["java", "java-engineering", "handbook"]
categories: ["Java Engineering Handbook"]
shortTitle: "Reflection"
module: 10
moduleTitle: "Platform APIs"
sectionRef: "10.2"
ShowToc: true
cheatSheet: true
---

## At a Glance

- Reflection: inspect/instantiate at runtime — breaks encapsulation, bypasses compile checks.
- Annotations: metadata — retention `SOURCE`/`CLASS`/`RUNTIME`.
- Modules (9+): `opens` packages for deep reflection to frameworks.
- Prefer compile-time annotation processing over runtime reflection scans.

---

## Reference Tables

| Retention | Visible |
| :--- | :--- |
| `SOURCE` | Compiler only (`@Override`) |
| `CLASS` | Bytecode, not runtime |
| `RUNTIME` | Reflection |

| Meta-annotation | Purpose |
| :--- | :--- |
| `@Target` | Where applicable |
| `@Retention` | Lifetime |
| `@Documented` | Javadoc |
| `@Inherited` | Subclass inherits |

| Reflection cost | Mitigation |
| :--- | :--- |
| Method lookup | Cache `MethodHandle` |
| setAccessible | `trySetAccessible` + module opens |
| Startup scan | Index at build time (Spring AOT) |

| Built-in | Role |
| :--- | :--- |
| `@Deprecated` | API lifecycle |
| `@FunctionalInterface` | SAM check |
| `@SuppressWarnings` | Compiler noise |

---

## Snippets

```java
@Target(ElementType.METHOD)
@Retention(RetentionPolicy.RUNTIME)
public @interface Audited {
    String action();
}

Method m = clazz.getDeclaredMethod("save", Order.class);
m.setAccessible(true); // may fail on module encapsulation
```

---

## Internals & Gotchas

- `MethodHandles` + `VarHandles` faster than raw `Method.invoke` after warmup.
- GraalVM native image requires reachability metadata for reflection.
- Annotation proxies implement `Annotation` interface at runtime.

---

## Production Notes

- Minimize reflection in hot paths — generate bytecode or use records.
- Document `--add-opens` requirements for JDK 17+.
- Security: don't reflect on user-supplied class names.

---

## Interview Probes


{< interview-answer >}
**Q:** Why modules hurt reflection?

**A:** Strong encapsulation — internal packages not open by default; frameworks need explicit `opens` or command-line flags.
{< /interview-answer >}

{< interview-answer >}
**Q:** SOURCE vs RUNTIME annotations?

**A:** SOURCE for compile-time checks/generation; RUNTIME for DI/mapping frameworks scanning at startup.
{< /interview-answer >}

---

## See Also

- [Previous: IO & NIO](/java-engineering/java-io-nio-ref/)
- [Next: Serialization](/java-engineering/serialization-quick-ref/)
- [Java Engineering Handbook Index](/java-engineering/)
