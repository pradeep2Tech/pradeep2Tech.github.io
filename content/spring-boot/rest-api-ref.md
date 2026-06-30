---
title: "REST API Reference"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "RestController, HTTP mappings, RequestBody, PathVariable, ResponseEntity."
tags: ["spring-boot", "spring", "cheatsheet", "handbook"]
categories: ["Spring Boot Cheat Sheet"]
shortTitle: "REST"
module: 3
moduleTitle: "REST & Validation"
sectionRef: "3.1"
ShowToc: true
cheatSheet: true
---

## At a Glance

- `@RestController` returns JSON via HttpMessageConverter.
- Use DTOs — never expose JPA entities directly.
- `ResponseEntity` for status + headers control.

---

## Reference Tables

| Annotation | Binds |
| :--- | :--- |
| `@RequestBody` | HTTP body → object |
| `@RequestParam` | Query / form param |
| `@PathVariable` | URI `{id}` segment |
| `@RequestHeader` | Header value |
| `@ResponseStatus` | Fixed status on method |

| Status | Typical use |
| :--- | :--- |
| 200 | GET success |
| 201 | POST create (+ Location header) |
| 204 | DELETE success |
| 400 | Validation failure |
| 404 | Not found |
| 409 | Conflict |

---

## Snippets

```java
@PostMapping
public ResponseEntity<OrderDto> create(@Valid @RequestBody CreateOrderRequest req) {
  OrderDto created = service.create(req);
  URI location = URI.create("/api/orders/" + created.id());
  return ResponseEntity.created(location).body(created);
}
```

---

## Internals & Gotchas

- Wrong `Content-Type` → 415.
- Missing `@Valid` → constraints not enforced.

---

## Production Notes

- Version APIs (`/api/v1`).
- Enable `spring.jackson.deserialization.fail-on-unknown-properties` for public APIs.

---

## Interview Probes


{< interview-answer >}
**Q:** @PathVariable vs @RequestParam?

**A:** Path = resource id; query = filters/pagination.
{< /interview-answer >}

---

## See Also

- [Previous: Config](/spring-boot/configuration-ref/)
- [Next: Validation](/spring-boot/validation-ref/)
- [Validation](/spring-boot/validation-ref/)
- [Exceptions](/spring-boot/exception-handling-ref/)
- [Spring Boot Cheat Sheet Index](/spring-boot/)
- [Java Engineering](/java-engineering/)
- [Microservices Playbook](/microservices/)
