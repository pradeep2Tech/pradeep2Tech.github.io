---
title: "GC Summary (Interview)"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Collector comparison, pause vs throughput, and tuning talking points."
tags: ["java", "java-engineering", "handbook"]
categories: ["Java Engineering Handbook"]
shortTitle: "GC Interview"
module: 11
moduleTitle: "Interview Cheat Sheets"
sectionRef: "11.4"
ShowToc: true
cheatSheet: true
---

## At a Glance

- Throughput vs latency collectors — no free lunch.
- Generational hypothesis: most objects die young.
- GC roots: stacks, statics, JNI, synchronized monitors.
- Tune with data: logs, JFR, pause percentiles.

---

## Reference Tables

| Collector | Goal |
| :--- | :--- |
| G1 | Balance, regional |
| ZGC | Low pause, colored pointers |
| Shenandoah | Concurrent compact |
| Parallel | Max throughput batch |

| Term | Meaning |
| :--- | :--- |
| Minor GC | Young collection |
| Full GC | Often whole heap STW — investigate if frequent |
| Promotion | Survivors → old |
| Mixed GC (G1) | Partial old regions |

| Red flag | Action |
| :--- | :--- |
| Frequent Full GC | Heap too small or leak |
| Long pause spikes | Tune or switch collector |
| High allocation rate | Object churn profiling |

---

## Snippets

```bash
-Xlog:gc*:file=gc.log:time,uptime,level,tags
```

---

## Internals & Gotchas

- STW phases: snapshot roots at safepoint.
- Concurrent collectors still brief pauses.
- Metaspace GC distinct from heap GC.

---

## Production Notes

- Alert on pause P99 and GC time %.
- Capacity plan includes GC overhead CPU.

---

## Interview Probes


{< interview-answer >}
**Q:** Generational hypothesis?

**A:** Most objects short-lived — collecting young gen frequently is cheap; few promote to old.
{< /interview-answer >}

{< interview-answer >}
**Q:** ZGC vs G1 trade-off?

**A:** ZGC targets low pauses on large heaps with more CPU/barrier cost — validate on workload.
{< /interview-answer >}

---

## See Also

- [Previous: Concurrent Collections](/java-engineering/concurrent-collections-interview/)
- [Next: Version Features](/java-engineering/java-version-features-interview/)
- [Java Engineering Handbook Index](/java-engineering/)
