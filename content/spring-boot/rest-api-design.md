---
title: "REST API Design"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Validation, exception handling, versioning, idempotency, pagination — senior API design."
tags: ["spring-boot", "spring", "handbook", "interview"]
categories: ["Spring Boot Handbook"]
shortTitle: "REST API"
module: 3
moduleTitle: "REST API Design"
sectionRef: "3.1"
interviewHandbook: true
aliases:
  - rest-api-ref
  - validation-ref
  - exception-handling-ref
---

## PUT vs PATCH?

**Difficulty:** Easy  
**Expected Answer Time:** 30 sec

### Short Answer

PUT replaces entire resource (idempotent). PATCH applies partial update (idempotent if designed with replace semantics).

### Detailed Explanation

PUT missing fields may null out columns if mapped naively. PATCH with JSON Merge Patch or JSON Patch — document contract. Spring: `@PutMapping` full DTO; `@PatchMapping` with `Map` or dedicated patch DTO + validation groups.

### Internal Working

`HttpMessageConverter` deserializes body; partial update often needs custom service logic or `@DynamicUpdate` on entity.

### Production Notes

Expose PATCH only with clear schema. Use ETags for optimistic concurrency on both.

### Common Mistakes

Using entity as `@RequestBody` — leaks persistence model.

### Follow-up Questions

- Idempotency keys for POST?
- How to implement conditional updates?

---
## API versioning strategies?

**Difficulty:** Medium  
**Expected Answer Time:** 1 min

### Short Answer

URI path (`/v1/`), header (`Accept-Version`), query param, or content negotiation — pick one and stick to it.

### Detailed Explanation

URI versioning is most visible and cache-friendly. Header versioning keeps URLs clean but harder to test in browser. Deprecation: `Sunset` header + metrics on old version traffic. Spring: separate controller packages or `@RequestMapping("/api/v1")`.

### Internal Working

DispatcherServlet maps to handler via `RequestMappingHandlerMapping`. Version rarely needs separate DispatcherServlet.

### Production Notes

Never break v1 silently. Maintain N-1 version minimum for public APIs.

### Common Mistakes

Mixing versioning styles across teams.

### Follow-up Questions

- How to deprecate an endpoint?
- OpenAPI multi-version docs?

---
## Validation best practices?

**Difficulty:** Medium  
**Expected Answer Time:** 1 min

### Short Answer

Validate at API boundary with Jakarta Bean Validation on DTOs; domain invariants in service layer; never trust client-only validation.

### Detailed Explanation

`@Valid` on `@RequestBody` triggers `MethodArgumentNotValidException`. Groups: `@Validated(Update.class)` for PATCH vs POST rules. Custom: `@Constraint` + `ConstraintValidator`. Method-level: `@Validated` on service + `@NotNull` on params.

### Internal Working

Hibernate Validator runs constraints via metadata; Boot auto-configures `LocalValidatorFactoryBean`.

### Production Notes

Return field-level errors in RFC 7807 `ProblemDetail` extensions. Don't expose stack traces.

### Common Mistakes

Missing `@Valid` — constraints silently skipped. Validating entities with lazy associations — triggers N+1.

### Follow-up Questions

- Programmatic validation without annotations?
- Cross-field validation?

---
## Global exception handling?

**Difficulty:** Medium  
**Expected Answer Time:** 1 min

### Short Answer

`@RestControllerAdvice` + `@ExceptionHandler` centralizes error mapping to stable HTTP status + body.

### Detailed Explanation

Boot 3 `ProblemDetail` implements RFC 7807. Map `MethodArgumentNotValidException` → 400 with field errors; business `NotFoundException` → 404; `AccessDeniedException` → 403. Order matters — most specific handler wins. `@ControllerAdvice` without `ResponseBody` needs `@ResponseBody` per method.

### Internal Working

Exception handlers resolved by `ExceptionHandlerExceptionResolver`. Can use `@Hidden` on handlers for OpenAPI.

### Production Notes

Include correlation ID from MDC in response `instance` or custom property. Log full detail server-side only.

### Common Mistakes

Catch-all `Exception` → 500 with message leaking internals. Returning 200 with error envelope.

### Follow-up Questions

- ProblemDetail vs custom error DTO?
- How to handle validation on `@RequestParam`?

---
## Pagination and error response design?

**Difficulty:** Medium  
**Expected Answer Time:** 1 min

### Short Answer

Use `Pageable` + `Page<T>`; return consistent envelope with `content`, `totalElements`, `links`; errors use stable machine-readable codes.

### Detailed Explanation

Spring Data: `PageRequest.of(page, size, Sort)`. HATEOAS optional. Error body: `type`, `title`, `status`, `detail`, `code`, `traceId`. Never expose SQL or stack in prod.

### Internal Working

`PageableHandlerMethodArgumentResolver` binds query params `page`, `size`, `sort`.

### Production Notes

Cap `size` max (e.g. 100) to prevent abuse. Index-friendly sort columns.

### Common Mistakes

Unbounded `findAll()` on large tables.

### Follow-up Questions

- Cursor-based vs offset pagination?
- How to add HATEOAS links?

---

## See Also

- [Previous: Config](/spring-boot/configuration/)
- [Next: Data & TX](/spring-boot/data-and-transactions/)
- [Data & TX](/spring-boot/data-and-transactions/)
- [100+ Interview Questions](/spring-boot/interview-questions/)
- [Spring Boot Handbook Index](/spring-boot/)
- [Java Engineering](/java-engineering/)
- [Microservices Playbook](/microservices/) — Saga, Outbox, CQRS, API Gateway
- [Kafka Handbook](/kafka-handbook/)
- [Security Architecture](/security-architecture/)
