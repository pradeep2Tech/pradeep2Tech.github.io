---
title: "Validation Reference"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Jakarta Bean Validation constraints, @Valid, groups."
tags: ["spring-boot", "spring", "cheatsheet", "handbook"]
categories: ["Spring Boot Cheat Sheet"]
shortTitle: "Validation"
module: 3
moduleTitle: "REST & Validation"
sectionRef: "3.2"
ShowToc: true
cheatSheet: true
---

## At a Glance

- Boot 3 uses `jakarta.validation.*`.
- Trigger with `@Valid` on `@RequestBody` or `@Validated` on class.
- Custom: `@Constraint` + `ConstraintValidator`.

---

## Reference Tables

| Constraint | Checks |
| :--- | :--- |
| `@NotNull` / `@NotBlank` / `@NotEmpty` | Presence |
| `@Size` | String/collection length |
| `@Min` / `@Max` | Numeric bounds |
| `@Email` | Email format |
| `@Pattern` | Regex |
| `@Past` / `@Future` | Date/time |

| Groups | Use |
| :--- | :--- |
| `Create.class` | POST rules |
| `Update.class` | PATCH rules — `@Validated(Update.class)` |

---

## Snippets

```java
public record CreateOrderRequest(
    @NotBlank String sku,
    @Min(1) int quantity,
    @Email String contactEmail
) {}
```

---

## Internals & Gotchas

- Import `javax.validation` on Boot 3 → compile error.

---

## Production Notes

- Validate at API boundary; don't rely only on DB constraints.

---

## Interview Probes


{< interview-answer >}
**Q:** Where to validate?

**A:** Controller DTOs at boundary; domain invariants in service layer.
{< /interview-answer >}

---

## See Also

- [Previous: REST](/spring-boot/rest-api-ref/)
- [Next: Exceptions](/spring-boot/exception-handling-ref/)
- [Spring Boot Cheat Sheet Index](/spring-boot/)
- [Java Engineering](/java-engineering/)
- [Microservices Playbook](/microservices/)
