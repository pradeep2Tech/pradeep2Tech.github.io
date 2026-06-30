---
title: "JVM Flags & Tuning"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Production flag sets for heap, GC, diagnostics, and container awareness."
tags: ["java", "java-engineering", "handbook"]
categories: ["Java Engineering Handbook"]
shortTitle: "JVM Flags"
module: 8
moduleTitle: "JVM"
sectionRef: "8.2"
ShowToc: true
cheatSheet: true
---

## At a Glance

- Ergonomic defaults adapt to container cgroup memory (10+).
- Always set explicit max heap in K8s — `-XX:MaxRAMPercentage` or `-Xmx`.
- Diagnostic flags: `NativeMemoryTracking`, `HeapDumpOnOutOfMemoryError`.
- Unlock experimental GC only with vendor support and benchmarks.

---

## Reference Tables

| Category | Example flags |
| :--- | :--- |
| Heap | `-Xms`, `-Xmx`, `-XX:MaxRAMPercentage=75` |
| GC | `-XX:+UseG1GC`, `-XX:MaxGCPauseMillis=200` |
| Diagnostics | `-XX:+HeapDumpOnOutOfMemoryError`, `-XX:HeapDumpPath` |
| Logging | `-Xlog:gc*,safepoint:file=gc.log:time,level,tags` |
| JIT | `-XX:CICompilerCount`, `-XX:-TieredCompilation` (rare) |
| Container | `-XX:+UseContainerSupport` (default 10+) |

| Anti-pattern | Why |
| :--- | :--- |
| Huge `-Xms` == `-Xmx` always | Wastes K8s memory at idle |
| Copy-paste 8GB heap | OOMKill in 512Mi pod |
| Aggressive `-XX:MaxGCPauseMillis=10` | Throughput collapse |

| Prod starter (G1, container) | |
| :--- | :--- |
| `-XX:MaxRAMPercentage=75.0` | |
| `-XX:+UseG1GC` | if not default |
| `-XX:+HeapDumpOnOutOfMemoryError` | |
| `-Xlog:gc*:file=/logs/gc.log:time,uptime,level,tags` | |

---

## Snippets

```bash
# Print ergonomics decision
java -XX:+PrintFlagsFinal -version | grep Heap
java -XshowSettings:system -version
```

---

## Internals & Gotchas

- `-XX:+AlwaysPreTouch` touches pages at startup — longer start, fewer runtime faults.
- `-XX:ActiveProcessorCount` overrides CPU count for GC/worker sizing.
- Flag availability varies by vendor build (Oracle, Temurin, Corretto).

---

## Production Notes

- Document flag rationale in runbook — not tribal knowledge.
- Change one variable at a time when tuning.
- Test GC upgrades on canary with production-like allocation profile.

---

## Interview Probes


{< interview-answer >}
**Q:** MaxRAMPercentage vs Xmx?

**A:** Percentage of container-visible RAM — portable across pod sizes. `-Xmx` fixed — predictable absolute cap.
{< /interview-answer >}

{< interview-answer >}
**Q:** When disable explicit GC (`System.gc`)?

**A:** `-XX:+DisableExplicitGC` if libraries trigger full GC via `System.gc` — but may break DirectByteBuffer cleanup relying on `Cleaner`; evaluate NIO libs first.
{< /interview-answer >}

---

## See Also

- [Previous: JVM Internals](/java-engineering/jvm-internals-quick-ref/)
- [Next: LTS Matrix](/java-engineering/java-lts-release-matrix/)
- [Java Engineering Handbook Index](/java-engineering/)
