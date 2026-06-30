---
title: "Spring Events Reference"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "ApplicationEvent, @EventListener, @TransactionalEventListener."
tags: ["spring-boot", "spring", "cheatsheet", "handbook"]
categories: ["Spring Boot Cheat Sheet"]
shortTitle: "Events"
module: 6
moduleTitle: "Cross-Cutting"
sectionRef: "6.3"
ShowToc: true
cheatSheet: true
---

## At a Glance

- Extend `ApplicationEvent` or use record events (Boot 2.2+).
- `ApplicationEventPublisher.publishEvent`.
- `@TransactionalEventListener(phase = AFTER_COMMIT)` for post-commit side effects.

---

## Reference Tables

| Listener | Timing |
| :--- | :--- |
| `@EventListener` | Synchronous default |
| `@Async` + `@EventListener` | Async handler |
| `@TransactionalEventListener` | After commit / rollback |

---

## Snippets

```java
@Service
public class OrderService {
  private final ApplicationEventPublisher events;
  public void complete(Order o) {
    repo.save(o);
    events.publishEvent(new OrderCompletedEvent(o.getId()));
  }
}
```

---

## Internals & Gotchas

- Domain events ≠ Kafka events — use outbox for cross-service.

---

## Production Notes

- Keep listeners idempotent.

---

## Interview Probes


{< interview-answer >}
**Q:** Sync vs async listener?

**A:** Sync in same thread/tx unless @Async — know your transaction boundary.
{< /interview-answer >}

---

## See Also

- [Previous: Schedule/Async](/spring-boot/scheduling-async-ref/)
- [Next: Actuator](/spring-boot/actuator-ref/)
- [Spring Boot Cheat Sheet Index](/spring-boot/)
- [Java Engineering](/java-engineering/)
- [Microservices Playbook](/microservices/)
