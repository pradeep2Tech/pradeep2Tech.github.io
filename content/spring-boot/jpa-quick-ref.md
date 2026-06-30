---
title: "Spring Data JPA Quick Reference"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Entity, repository hierarchy, paging, sorting."
tags: ["spring-boot", "spring", "cheatsheet", "handbook"]
categories: ["Spring Boot Cheat Sheet"]
shortTitle: "JPA"
module: 4
moduleTitle: "Data & Transactions"
sectionRef: "4.1"
ShowToc: true
cheatSheet: true
---

## At a Glance

- Repositories are interfaces — Spring implements at runtime.
- `JpaRepository` adds flush + batch delete.
- Use `Pageable` for large result sets.

---

## Reference Tables

| Interface | Provides |
| :--- | :--- |
| `CrudRepository` | basic CRUD |
| `PagingAndSortingRepository` | `Pageable`, `Sort` |
| `JpaRepository` | JPA flush, `deleteAllInBatch` |

| Entity | Annotation |
| :--- | :--- |
| Table | `@Entity` `@Table(name="orders")` |
| PK | `@Id` `@GeneratedValue` |
| Version | `@Version` optimistic lock |
| Relations | `@OneToMany`, `@ManyToOne`, etc. |

---

## Snippets

```java
@Entity
public class Order {
  @Id @GeneratedValue private Long id;
  @Version private Long version;
}

public interface OrderRepository extends JpaRepository<Order, Long> {}
```

---

## Internals & Gotchas

- `open-in-view=false` in prod — avoid lazy load in controllers.
- equals/hashCode on entities: use business key or id only.

---

## Production Notes

- DTO projection for reads; don't return entities from REST.

---

## Interview Probes


{< interview-answer >}
**Q:** Derived query method naming?

**A:** Spring parses `findByStatusAndCreatedAtAfter` → query.
{< /interview-answer >}

---

## See Also

- [Previous: Exceptions](/spring-boot/exception-handling-ref/)
- [Next: JPA Queries](/spring-boot/jpa-queries-ref/)
- [JPA Queries](/spring-boot/jpa-queries-ref/)
- [Transactions](/spring-boot/transactions-ref/)
- [Spring Boot Cheat Sheet Index](/spring-boot/)
- [Java Engineering](/java-engineering/)
- [Microservices Playbook](/microservices/)
