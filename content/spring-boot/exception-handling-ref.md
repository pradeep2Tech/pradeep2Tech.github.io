---
title: "Exception Handling Reference"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "@ControllerAdvice, ProblemDetail, HTTP status mapping."
tags: ["spring-boot", "spring", "cheatsheet", "handbook"]
categories: ["Spring Boot Cheat Sheet"]
shortTitle: "Exceptions"
module: 3
moduleTitle: "REST & Validation"
sectionRef: "3.3"
ShowToc: true
cheatSheet: true
---

## At a Glance

- `@RestControllerAdvice` + `@ExceptionHandler` for global JSON errors.
- Boot 3 has `ProblemDetail` (RFC 7807).
- Log server detail; return safe client message.

---

## Reference Tables

| Exception type | HTTP |
| :--- | :--- |
| Validation (`MethodArgumentNotValidException`) | 400 |
| Not found (custom) | 404 |
| Conflict | 409 |
| Unauthorized | 401 |
| Forbidden | 403 |

---

## Snippets

```java
@RestControllerAdvice
public class ApiErrors {
  @ExceptionHandler(NotFoundException.class)
  public ProblemDetail notFound(NotFoundException ex) {
    return ProblemDetail.forStatusAndDetail(HttpStatus.NOT_FOUND, ex.getMessage());
  }
}
```

---

## Internals & Gotchas

- Don't catch broad `Exception` and return 200.
- Include correlation id from MDC in body.

---

## Production Notes

- Map vendor errors to stable API error codes.

---

## Interview Probes


{< interview-answer >}
**Q:** @ControllerAdvice vs @RestControllerAdvice?

**A:** 后者 adds @ResponseBody on handlers.
{< /interview-answer >}

---

## See Also

- [Previous: Validation](/spring-boot/validation-ref/)
- [Next: JPA](/spring-boot/jpa-quick-ref/)
- [Spring Boot Cheat Sheet Index](/spring-boot/)
- [Java Engineering](/java-engineering/)
- [Microservices Playbook](/microservices/)
