---
title: "Testing Reference"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "MockMvc, @MockBean, slice tests, Testcontainers."
tags: ["spring-boot", "spring", "cheatsheet", "handbook"]
categories: ["Spring Boot Cheat Sheet"]
shortTitle: "Testing"
module: 7
moduleTitle: "Production"
sectionRef: "7.3"
ShowToc: true
cheatSheet: true
---

## At a Glance

- Slice tests load partial context — faster than full `@SpringBootTest`.
- `@MockBean` replaces bean in test context.
- Testcontainers for real Postgres/Kafka.

---

## Reference Tables

| Annotation | Loads |
| :--- | :--- |
| `@WebMvcTest` | MVC layer only |
| `@DataJpaTest` | JPA + in-memory or Testcontainers |
| `@SpringBootTest` | Full application |
| `@MockMvc` | Mock HTTP without server |

| Tool | Use |
| :--- | :--- |
| Mockito | Mock collaborators |
| AssertJ | Fluent assertions |
| Testcontainers | Real infra |

---

## Snippets

```java
@WebMvcTest(OrderController.class)
class OrderControllerTest {
  @Autowired MockMvc mvc;
  @MockBean OrderService service;

  @Test void getReturns200() throws Exception {
    when(service.find(1L)).thenReturn(dto);
    mvc.perform(get("/api/orders/1")).andExpect(status().isOk());
  }
}
```

---

## Internals & Gotchas

- `@SpringBootTest(webEnvironment = RANDOM_PORT)` for integration.
- Don't `@MockBean` the class under test.

---

## Production Notes

- CI: slice tests on every commit; Testcontainers on merge.

---

## Interview Probes


{< interview-answer >}
**Q:** @MockBean vs @Mock?

**A:** @MockBean in Spring context; @Mock in plain unit test.
{< /interview-answer >}

---

## See Also

- [Previous: Observability](/spring-boot/observability-ref/)
- [Next: Production](/spring-boot/production-deployment-ref/)
- [Spring Boot Cheat Sheet Index](/spring-boot/)
- [Java Engineering](/java-engineering/)
- [Microservices Playbook](/microservices/)
