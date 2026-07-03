---
title: "Testing"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Unit, slice, integration testing, MockMvc, Testcontainers — production testing strategy."
tags: ["spring-boot", "spring", "handbook", "interview"]
categories: ["Spring Boot Handbook"]
shortTitle: "Testing"
module: 10
moduleTitle: "Testing"
sectionRef: "10.1"
ShowToc: true
interviewHandbook: true
aliases:
  - testing-ref
---

## Unit vs slice vs integration tests?

**Difficulty:** Medium  
**Expected Answer Time:** 1 min

### Short Answer

Unit: plain JUnit + Mockito, no Spring. Slice: partial context (`@WebMvcTest`, `@DataJpaTest`). Integration: `@SpringBootTest` + Testcontainers for real infra.

### Detailed Explanation

Slice tests fast — mock collaborators with `@MockBean`. Full integration catches wiring and config errors. Test pyramid: many unit, fewer integration.

### Internal Working

`@MockBean` replaces bean in test `ApplicationContext`.

### Production Notes

CI: unit on every commit; Testcontainers on merge/main. Reuse containers where possible.

### Common Mistakes

`@SpringBootTest` for everything — slow suite. `@MockBean` on class under test.

### Follow-up Questions

- @MockBean vs @Mock?
- Testcontainers reuse?

---
## MockMvc testing strategy?

**Difficulty:** Medium  
**Expected Answer Time:** 1 min

### Short Answer

`@WebMvcTest(Controller.class)` loads MVC slice; `MockMvc` performs HTTP without socket — verify status, JSON, security.

### Detailed Explanation

`@AutoConfigureMockMvc` on integration test. `SecurityMockMvcRequestPostProcessors.jwt()` for OAuth2. Assert problem detail structure matches production.

### Internal Working

Standalone `MockMvcBuilders.standaloneSetup` for pure unit of controller with mocked deps.

### Production Notes

Test validation failures (400) and auth (401/403) paths.

### Common Mistakes

Only testing happy path 200.

### Follow-up Questions

- WebTestClient for WebFlux?
- Contract testing?

---
## Testcontainers in Spring Boot?

**Difficulty:** Medium  
**Expected Answer Time:** 1 min

### Short Answer

`@Testcontainers` + `@Container static PostgreSQLContainer` — dynamic property source wires JDBC URL into Spring context.

### Detailed Explanation

`@DynamicPropertySource` registers container host/port. `@ServiceConnection` (Boot 3.1+) auto-configures datasource from container.

### Internal Working

Ryuk container manages lifecycle.

### Production Notes

Pin image digests in CI. Parallel test classes need isolated containers or shared singleton with care.

### Common Mistakes

Hardcoded localhost ports conflicting.

### Follow-up Questions

- Embedded DB vs Testcontainers?
- Kafka Testcontainers?

---

## See Also

- [Previous: Production](/spring-boot/production-deployment/)
- [Next: Interview](/spring-boot/interview-questions/)
- [REST API](/spring-boot/rest-api-design/)
- [Data & TX](/spring-boot/data-and-transactions/)
- [100+ Interview Questions](/spring-boot/interview-questions/)
- [Spring Boot Handbook Index](/spring-boot/)
- [Java Engineering](/java-engineering/)
- [Microservices Playbook](/microservices/) — Saga, Outbox, CQRS, API Gateway
- [Kafka Handbook](/kafka-handbook/)
- [Security Architecture](/security-architecture/)
