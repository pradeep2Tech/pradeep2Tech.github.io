---
title: "Transactions Reference"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Propagation, isolation, rollback rules, readOnly."
tags: ["spring-boot", "spring", "cheatsheet", "handbook"]
categories: ["Spring Boot Cheat Sheet"]
shortTitle: "Transactions"
module: 4
moduleTitle: "Data & Transactions"
sectionRef: "4.3"
ShowToc: true
cheatSheet: true
---

## At a Glance

- `@Transactional` on service layer — not controllers.
- Default propagation: `REQUIRED`.
- Unchecked exceptions rollback; checked exceptions don't by default.

---

## Reference Tables

| Propagation | Behavior |
| :--- | :--- |
| REQUIRED | Join or create (default) |
| REQUIRES_NEW | Suspend, new transaction |
| NESTED | Savepoint nested |
| SUPPORTS | Join if exists, else non-tx |

| Isolation | Trade-off |
| :--- | :--- |
| READ_COMMITTED | Default on many DBs |
| REPEATABLE_READ | Phantom protection varies |
| SERIALIZABLE | Strongest, slowest |

| Attribute | Note |
| :--- | :--- |
| `readOnly=true` | Hint for optimizations |
| `rollbackFor` | Include checked exceptions |

---

## Snippets

```java
@Transactional
public OrderDto placeOrder(CreateOrderRequest req) {
  // single transaction boundary
}
```

---

## Internals & Gotchas

- Self-invocation bypasses proxy — inject self or refactor.
- Keep transactions short — no remote HTTP inside.

---

## Production Notes

- Use `REQUIRES_NEW` for audit logs that must commit independently.

---

## Interview Probes


{< interview-answer >}
**Q:** Why rollback on RuntimeException?

**A:** Default policy — declare `rollbackFor` for checked business exceptions.
{< /interview-answer >}

---

## See Also

- [Previous: JPA Queries](/spring-boot/jpa-queries-ref/)
- [Next: Security](/spring-boot/security-quick-ref/)
- [Spring Boot Cheat Sheet Index](/spring-boot/)
- [Java Engineering](/java-engineering/)
- [Microservices Playbook](/microservices/)
