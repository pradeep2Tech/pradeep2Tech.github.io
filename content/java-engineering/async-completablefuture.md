---
title: "Async & CompletableFuture"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Composition, async supply/run, exceptionally, orTimeout, and executor choice."
tags: ["java", "java-engineering", "handbook"]
categories: ["Java Engineering Handbook"]
shortTitle: "CompletableFuture"
module: 6
moduleTitle: "Concurrency"
sectionRef: "6.2"
ShowToc: true
cheatSheet: true
---

## At a Glance

- Composable async pipeline — `thenApply`, `thenCompose`, `allOf`, `anyOf`.
- Always pass explicit `Executor` for application work — don't rely on `ForkJoinPool.commonPool()` in services.
- `orTimeout` / `completeOnTimeout` (9+) for SLA bounds.
- Exception handling: `handle`, `exceptionally`, `whenComplete`.

---

## Reference Tables

| Method | Use |
| :--- | :--- |
| `supplyAsync` | Async value |
| `runAsync` | Async void |
| `thenApply` | Map result sync |
| `thenCompose` | FlatMap future |
| `thenCombine` | Merge two futures |
| `allOf` | Wait all — void aggregate |
| `anyOf` | First complete wins |

| Composition trap | Fix |
| :--- | :--- |
| Nested `get()` | `thenCompose` chain |
| Blocking on common pool | Dedicated executor |
| Lost exception | `handle` / `whenComplete` log |
| No timeout | `orTimeout`, `completeOnTimeout` |

---

## Snippets

```java
CompletableFuture<Order> order = validate(cart)
    .thenCompose(v -> reserveInventory(cart))
    .thenCompose(v -> chargePayment(cart))
    .orTimeout(10, TimeUnit.SECONDS);

order.whenComplete((o, ex) -> { if (ex != null) audit.fail(ex); });
```

---

## Internals & Gotchas

- `CompletableFuture` stored in `AltResult` for completion — CAS completion stack.
- `async` stages run on executor; non-async run on completing thread.

---

## Production Notes

- Propagate tracing context manually or via OpenTelemetry context wrappers.
- Bulkhead: separate executors per dependency.
- Don't block in `thenApply` on event loop threads.

---

## Interview Probes


{< interview-answer >}
**Q:** thenApply vs thenCompose?

**A:** `thenApply` maps value to value; `thenCompose` maps value to another Future — avoids nested futures.
{< /interview-answer >}

{< interview-answer >}
**Q:** Default executor risk?

**A:** Common pool shared with parallel streams — starvation/cross-talk. Use named executor per domain.
{< /interview-answer >}

---

## See Also

- [Previous: Threads & Executors](/java-engineering/threads-and-executors/)
- [Next: Locks & Atomics](/java-engineering/locks-and-atomics/)
- [Java Engineering Handbook Index](/java-engineering/)
