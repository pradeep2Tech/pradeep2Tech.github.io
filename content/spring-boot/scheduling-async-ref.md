---
title: "Scheduling & Async Reference"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "@Scheduled, cron, @Async, TaskExecutor."
tags: ["spring-boot", "spring", "cheatsheet", "handbook"]
categories: ["Spring Boot Cheat Sheet"]
shortTitle: "Schedule/Async"
module: 6
moduleTitle: "Cross-Cutting"
sectionRef: "6.2"
ShowToc: true
cheatSheet: true
---

## At a Glance

- `@EnableScheduling` + `@Scheduled` on methods.
- `fixedDelay` waits after completion; `fixedRate` between starts.
- `@Async` needs `@EnableAsync` + `TaskExecutor` bean.

---

## Reference Tables

| `@Scheduled` | Meaning |
| :--- | :--- |
| `fixedDelay` | ms after previous **finish** |
| `fixedRate` | ms between **starts** |
| `cron` | 6-field Spring cron |

| Cron field | Order |
| :--- | :--- |
| sec min hour day month weekday | |

---

## Snippets

```java
@Scheduled(cron = "0 0 2 * * *", zone = "UTC")
public void nightlyReconcile() { ... }

@Async
public CompletableFuture<Report> buildReport() { ... }
```

---

## Internals & Gotchas

- `@Scheduled` is single-threaded by default — long jobs block others.
- `@Async` return type: `void`, `Future`, or `CompletableFuture`.

---

## Production Notes

- Use ShedLock or Quartz for clustered schedules.
- Size thread pools for `@Async`.

---

## Interview Probes


{< interview-answer >}
**Q:** fixedDelay vs fixedRate?

**A:** Delay = backpressure friendly; rate can overlap if job slower than interval.
{< /interview-answer >}

---

## See Also

- [Previous: Caching](/spring-boot/caching-ref/)
- [Next: Events](/spring-boot/events-ref/)
- [Spring Boot Cheat Sheet Index](/spring-boot/)
- [Java Engineering](/java-engineering/)
- [Microservices Playbook](/microservices/)
