---
title: "Memory Leaks & OOM"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Reference types, common leak patterns, Metaspace, direct memory, diagnosis."
tags: ["java", "java-engineering", "handbook"]
categories: ["Java Engineering Handbook"]
shortTitle: "Leaks & OOM"
module: 7
moduleTitle: "Memory & GC"
sectionRef: "7.2"
ShowToc: true
cheatSheet: true
---

## At a Glance

- Java leak = reachable but unused objects — GC cannot reclaim.
- Common: static collections, listeners, ThreadLocal, classloader leaks in containers.
- OOM types: heap, Metaspace, direct memory, unable to create native thread.
- Diagnose: heap dump, MAT/VisualVM, async profiler, JFR.

---

## Reference Tables

| Reference | GC behavior | Use |
| :--- | :--- | :--- |
| Strong | Never if reachable | Default |
| Soft | Cleared before OOM | Memory-sensitive cache |
| Weak | Next GC | Canonical mappings |
| Phantom | After finalize/enqueue | Post-mortem cleanup |

| Leak pattern | Fix |
| :--- | :--- |
| Static `Map` cache no eviction | Bounded cache + TTL |
| Listener not removed | Weak refs or explicit remove |
| `ThreadLocal` in pool threads | `remove()` in finally |
| Reloaded WAR classloader | Undeploy hook, avoid static refs to app classes |

| OOM message | Likely cause |
| :--- | :--- |
| Java heap space | Object retention |
| Metaspace | Class explosion / reload |
| Direct buffer memory | NIO leak |
| unable to create native thread | Thread spawn storm |

---

## Snippets

```java
try {
    threadLocal.set(ctx);
    process();
} finally {
    threadLocal.remove(); // critical in pooled threads
}
```

---

## Internals & Gotchas

- Finalization deprecated (9+) — prefer `Cleaner`/`PhantomReference`.
- `String` deduplication (G1 option) saves heap for duplicate char arrays.
- Off-heap leaks won't trigger heap GC — monitor `BufferPoolMXBean`.

---

## Production Notes

- Cap caches; expose size metrics.
- Automate heap dump on OOM in prod (with disk guard).
- Review reactive/Netty direct buffer allocators.

---

## Interview Probes


{< interview-answer >}
**Q:** Can you leak memory with GC?

**A:** Yes — logical leaks keep strong references (static, singleton registries, class loaders).
{< /interview-answer >}

{< interview-answer >}
**Q:** Soft vs weak cache?

**A:** Soft survives until memory pressure — good for image caches. Weak disappears aggressively — canonical keys.
{< /interview-answer >}

---

## See Also

- [Previous: Memory & GC](/java-engineering/jvm-memory-and-gc/)
- [Next: JVM Internals](/java-engineering/jvm-internals-quick-ref/)
- [Java Engineering Handbook Index](/java-engineering/)
