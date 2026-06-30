---
title: "JPA Queries Reference"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Derived queries, @Query, JPQL, native SQL."
tags: ["spring-boot", "spring", "cheatsheet", "handbook"]
categories: ["Spring Boot Cheat Sheet"]
shortTitle: "JPA Queries"
module: 4
moduleTitle: "Data & Transactions"
sectionRef: "4.2"
ShowToc: true
cheatSheet: true
---

## At a Glance

- Derived method names for simple queries.
- `@Query` for JPQL; `nativeQuery=true` for SQL.
- Named parameters: `@Param("status")`.

---

## Reference Tables

| Style | When |
| :--- | :--- |
| Derived | Simple property paths |
| JPQL | Portable object queries |
| Native | DB-specific SQL, hints, CTEs |
| Specification | Dynamic predicates (Criteria API) |

| JPQL example | |
| :--- | :--- |
| `SELECT o FROM Order o WHERE o.status = :s` | entity name, not table |

---

## Snippets

```java
@Query("select o from Order o where o.status = :status")
List<Order> findByStatus(@Param("status") OrderStatus status);

@Query(value = "SELECT * FROM orders WHERE id = ?1", nativeQuery = true)
Optional<Order> findRaw(Long id);
```

---

## Internals & Gotchas

- Native queries bypass change tracking semantics.
- `@Modifying` for UPDATE/DELETE — clear persistence context.

---

## Production Notes

- Prefer JPQL unless you need SQL features.

---

## Interview Probes


{< interview-answer >}
**Q:** N+1 problem?

**A:** Fetch join or `@EntityGraph` or DTO projection.
{< /interview-answer >}

---

## See Also

- [Previous: JPA](/spring-boot/jpa-quick-ref/)
- [Next: Transactions](/spring-boot/transactions-ref/)
- [Spring Boot Cheat Sheet Index](/spring-boot/)
- [Java Engineering](/java-engineering/)
- [Microservices Playbook](/microservices/)
