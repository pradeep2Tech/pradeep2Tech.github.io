---
title: "100+ Spring Boot Interview Questions"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Categorized Spring Boot interview questions for senior engineers and architects."
tags: ["spring-boot", "spring", "handbook", "interview"]
categories: ["Spring Boot Handbook"]
shortTitle: "Interview"
module: 11
moduleTitle: "Interview"
sectionRef: "11.1"
ShowToc: true
interviewHandbook: true
aliases:
  - spring-boot-interview-ref
---

Curated questions for **6+ year** engineers, tech leads, and architects. Each links to a deep-dive page.

## Easy

| # | Question | Topic | Deep Dive |
| --: | :--- | :--- | :--- |
| 1 | What does @SpringBootApplication combine? | Startup | [Startup & Internals](/spring-boot/startup-and-internals/) |
| 2 | Default bean scope in Spring? | Startup | [Startup & Internals](/spring-boot/startup-and-internals/) |
| 3 | Constructor vs field injection? | Startup | [Startup & Internals](/spring-boot/startup-and-internals/) |
| 4 | IoC vs DI? | Startup | [Startup & Internals](/spring-boot/startup-and-internals/) |
| 5 | Authentication vs authorization? | Security | [Security](/spring-boot/security/) |
| 6 | PUT vs PATCH? | REST | [REST API Design](/spring-boot/rest-api-design/) |
| 7 | What is a Spring profile? | Config | [Configuration](/spring-boot/configuration/) |
| 8 | @Value vs @ConfigurationProperties? | Config | [Configuration](/spring-boot/configuration/) |
| 9 | Lazy vs eager JPA loading? | Data | [Data & Transactions](/spring-boot/data-and-transactions/) |
| 10 | What is MockMvc? | Testing | [Testing](/spring-boot/testing/) |
| 11 | Actuator health endpoint purpose? | Observability | [Observability](/spring-boot/observability/) |
| 12 | Liveness vs readiness probe? | Observability | [Observability](/spring-boot/observability/) |
| 13 | Minimum Java for Boot 3? | Startup | [Startup & Internals](/spring-boot/startup-and-internals/) |
| 14 | javax vs jakarta in Boot 3? | Startup | [Startup & Internals](/spring-boot/startup-and-internals/) |
| 15 | What is a starter? | Startup | [Startup & Internals](/spring-boot/startup-and-internals/) |
| 16 | @Service vs @Component? | Startup | [Startup & Internals](/spring-boot/startup-and-internals/) |
| 17 | HTTP 401 vs 403? | Security | [Security](/spring-boot/security/) |
| 18 | What is CSRF? | Security | [Security](/spring-boot/security/) |
| 19 | Cache Aside pattern? | Performance | [Caching & Performance](/spring-boot/caching-performance/) |
| 20 | @Scheduled fixedDelay vs fixedRate? | Performance | [Caching & Performance](/spring-boot/caching-performance/) |

## Medium

| # | Question | Topic | Deep Dive |
| --: | :--- | :--- | :--- |
| 21 | How does Spring Boot startup work? | Startup | [Startup & Internals](/spring-boot/startup-and-internals/) |
| 22 | How does auto-configuration work? | Startup | [Startup & Internals](/spring-boot/startup-and-internals/) |
| 23 | Bean lifecycle phases? | Startup | [Startup & Internals](/spring-boot/startup-and-internals/) |
| 24 | @Primary vs @Qualifier? | Startup | [Startup & Internals](/spring-boot/startup-and-internals/) |
| 25 | Component scan mechanics? | Startup | [Startup & Internals](/spring-boot/startup-and-internals/) |
| 26 | Property resolution order? | Config | [Configuration](/spring-boot/configuration/) |
| 27 | Profile groups in Boot? | Config | [Configuration](/spring-boot/configuration/) |
| 28 | Relaxed binding examples? | Config | [Configuration](/spring-boot/configuration/) |
| 29 | API versioning strategies? | REST | [REST API Design](/spring-boot/rest-api-design/) |
| 30 | Global exception handling? | REST | [REST API Design](/spring-boot/rest-api-design/) |
| 31 | Validation best practices? | REST | [REST API Design](/spring-boot/rest-api-design/) |
| 32 | Pagination in Spring Data? | REST | [REST API Design](/spring-boot/rest-api-design/) |
| 33 | Idempotency for POST? | REST | [REST API Design](/spring-boot/rest-api-design/) |
| 34 | How does @Transactional work? | Data | [Data & Transactions](/spring-boot/data-and-transactions/) |
| 35 | Transaction propagation types? | Data | [Data & Transactions](/spring-boot/data-and-transactions/) |
| 36 | Self-invocation transaction bug? | Data | [Data & Transactions](/spring-boot/data-and-transactions/) |
| 37 | N+1 problem and fixes? | Data | [Data & Transactions](/spring-boot/data-and-transactions/) |
| 38 | Optimistic vs pessimistic locking? | Data | [Data & Transactions](/spring-boot/data-and-transactions/) |
| 39 | First-level vs second-level cache? | Data | [Data & Transactions](/spring-boot/data-and-transactions/) |
| 40 | open-in-view true or false? | Data | [Data & Transactions](/spring-boot/data-and-transactions/) |
| 41 | SecurityFilterChain in Boot 3? | Security | [Security](/spring-boot/security/) |
| 42 | JWT validation flow? | Security | [Security](/spring-boot/security/) |
| 43 | Method security @PreAuthorize? | Security | [Security](/spring-boot/security/) |
| 44 | Session vs JWT for APIs? | Security | [Security](/spring-boot/security/) |
| 45 | @Cacheable internals? | Performance | [Caching & Performance](/spring-boot/caching-performance/) |
| 46 | @Async internals? | Performance | [Caching & Performance](/spring-boot/caching-performance/) |
| 47 | Thread pool sizing? | Performance | [Caching & Performance](/spring-boot/caching-performance/) |
| 48 | HikariCP pool sizing? | Performance | [Caching & Performance](/spring-boot/caching-performance/) |
| 49 | Spring Events vs Kafka? | Messaging | [Messaging & Events](/spring-boot/messaging-events/) |
| 50 | Kafka vs RabbitMQ? | Messaging | [Messaging & Events](/spring-boot/messaging-events/) |
| 51 | Retry and DLQ patterns? | Messaging | [Messaging & Events](/spring-boot/messaging-events/) |
| 52 | Correlation IDs and MDC? | Observability | [Observability](/spring-boot/observability/) |
| 53 | Micrometer vs Actuator? | Observability | [Observability](/spring-boot/observability/) |
| 54 | Graceful shutdown config? | Production | [Production Deployment](/spring-boot/production-deployment/) |
| 55 | Unit vs slice vs integration test? | Testing | [Testing](/spring-boot/testing/) |
| 56 | @MockBean vs @Mock? | Testing | [Testing](/spring-boot/testing/) |
| 57 | Testcontainers with Spring Boot? | Testing | [Testing](/spring-boot/testing/) |
| 58 | DispatcherServlet role? | Startup | [Startup & Internals](/spring-boot/startup-and-internals/) |
| 59 | ProblemDetail RFC 7807? | REST | [REST API Design](/spring-boot/rest-api-design/) |
| 60 | Derived query method naming? | Data | [Data & Transactions](/spring-boot/data-and-transactions/) |
| 61 | @Query JPQL vs native? | Data | [Data & Transactions](/spring-boot/data-and-transactions/) |
| 62 | @EntityGraph purpose? | Data | [Data & Transactions](/spring-boot/data-and-transactions/) |
| 63 | PasswordEncoder best practice? | Security | [Security](/spring-boot/security/) |
| 64 | OAuth2 resource server setup? | Security | [Security](/spring-boot/security/) |
| 65 | Redis cache manager? | Performance | [Caching & Performance](/spring-boot/caching-performance/) |
| 66 | Cache stampede mitigation? | Performance | [Caching & Performance](/spring-boot/caching-performance/) |
| 67 | @TransactionalEventListener? | Messaging | [Messaging & Events](/spring-boot/messaging-events/) |
| 68 | Kafka listener concurrency? | Messaging | [Messaging & Events](/spring-boot/messaging-events/) |
| 69 | Prometheus scrape config? | Observability | [Observability](/spring-boot/observability/) |
| 70 | Layered JAR for Docker? | Production | [Production Deployment](/spring-boot/production-deployment/) |
| 71 | @WebMvcTest scope? | Testing | [Testing](/spring-boot/testing/) |
| 72 | @DataJpaTest scope? | Testing | [Testing](/spring-boot/testing/) |

## Hard

| # | Question | Topic | Deep Dive |
| --: | :--- | :--- | :--- |
| 73 | Auto-config conditional annotations? | Startup | [Startup & Internals](/spring-boot/startup-and-internals/) |
| 74 | BeanPostProcessor vs BeanFactoryPostProcessor? | Startup | [Startup & Internals](/spring-boot/startup-and-internals/) |
| 75 | CGLIB vs JDK dynamic proxy? | Startup | [Startup & Internals](/spring-boot/startup-and-internals/) |
| 76 | Circular dependency resolution? | Startup | [Startup & Internals](/spring-boot/startup-and-internals/) |
| 77 | Transaction isolation levels? | Data | [Data & Transactions](/spring-boot/data-and-transactions/) |
| 78 | REQUIRES_NEW vs NESTED? | Data | [Data & Transactions](/spring-boot/data-and-transactions/) |
| 79 | Hibernate session flush timing? | Data | [Data & Transactions](/spring-boot/data-and-transactions/) |
| 80 | @Modifying query pitfalls? | Data | [Data & Transactions](/spring-boot/data-and-transactions/) |
| 81 | Filter chain order customization? | Security | [Security](/spring-boot/security/) |
| 82 | JWT JWK rotation? | Security | [Security](/spring-boot/security/) |
| 83 | SecurityContext in async? | Security | [Security](/spring-boot/security/) |
| 84 | TaskDecorator for MDC propagation? | Performance | [Caching & Performance](/spring-boot/caching-performance/) |
| 85 | Virtual threads with @Async? | Performance | [Caching & Performance](/spring-boot/caching-performance/) |
| 86 | Exactly-once Kafka consumption? | Messaging | [Messaging & Events](/spring-boot/messaging-events/) |
| 87 | Idempotent message consumer design? | Messaging | [Messaging & Events](/spring-boot/messaging-events/) |
| 88 | Distributed tracing propagation? | Observability | [Observability](/spring-boot/observability/) |
| 89 | Tail sampling for traces? | Observability | [Observability](/spring-boot/observability/) |
| 90 | Startup actuator profiling? | Startup | [Startup & Internals](/spring-boot/startup-and-internals/) |
| 91 | ConditionalOnMissingBean semantics? | Startup | [Startup & Internals](/spring-boot/startup-and-internals/) |
| 92 | Multiple SecurityFilterChain beans? | Security | [Security](/spring-boot/security/) |
| 93 | SpEL in @PreAuthorize risks? | Security | [Security](/spring-boot/security/) |
| 94 | Two-phase cache invalidation? | Performance | [Caching & Performance](/spring-boot/caching-performance/) |
| 95 | Connection leak detection? | Data | [Data & Transactions](/spring-boot/data-and-transactions/) |
| 96 | Specification API dynamic queries? | Data | [Data & Transactions](/spring-boot/data-and-transactions/) |
| 97 | ShedLock for clustered cron? | Performance | [Caching & Performance](/spring-boot/caching-performance/) |
| 98 | Consumer ack modes Kafka? | Messaging | [Messaging & Events](/spring-boot/messaging-events/) |
| 99 | Custom HealthIndicator? | Observability | [Observability](/spring-boot/observability/) |
| 100 | Observation API Boot 3? | Observability | [Observability](/spring-boot/observability/) |
| 101 | Native image GraalVM trade-offs? | Production | [Production Deployment](/spring-boot/production-deployment/) |

## Architect

| # | Question | Topic | Deep Dive |
| --: | :--- | :--- | :--- |
| 102 | Design idempotent REST API? | REST | [REST API Design](/spring-boot/rest-api-design/) |
| 103 | When local TX vs saga? | Data | [Data & Transactions](/spring-boot/data-and-transactions/) |
| 104 | Multi-tenant config isolation? | Config | [Configuration](/spring-boot/configuration/) |
| 105 | Zero-downtime schema migration? | Data | [Data & Transactions](/spring-boot/data-and-transactions/) |
| 106 | API gateway vs BFF? | REST | [REST API Design](/spring-boot/rest-api-design/) |
| 107 | Outbox pattern placement? | Messaging | [Messaging & Events](/spring-boot/messaging-events/) |
| 108 | Event-driven vs request-driven? | Messaging | [Messaging & Events](/spring-boot/messaging-events/) |
| 109 | SLO-driven alerting stack? | Observability | [Observability](/spring-boot/observability/) |
| 110 | Blue/green vs rolling K8s deploy? | Production | [Production Deployment](/spring-boot/production-deployment/) |
| 111 | Secrets rotation without restart? | Config | [Configuration](/spring-boot/configuration/) |
| 112 | Rate limiting in Boot service? | REST | [REST API Design](/spring-boot/rest-api-design/) |
| 113 | Multi-region active-active data? | Data | [Data & Transactions](/spring-boot/data-and-transactions/) |
| 114 | Service mesh vs library resilience? | Production | [Production Deployment](/spring-boot/production-deployment/) |
| 115 | CQRS when worth it? | Data | [Data & Transactions](/spring-boot/data-and-transactions/) |
| 116 | Platform logging standard? | Observability | [Observability](/spring-boot/observability/) |
| 117 | Boot cold start at scale? | Startup | [Startup & Internals](/spring-boot/startup-and-internals/) |
| 118 | Custom starter design? | Startup | [Startup & Internals](/spring-boot/startup-and-internals/) |
| 119 | AuthZ model RBAC vs ABAC? | Security | [Security](/spring-boot/security/) |
| 120 | Token propagation service mesh? | Security | [Security](/spring-boot/security/) |
| 121 | Cache coherence across pods? | Performance | [Caching & Performance](/spring-boot/caching-performance/) |

---

## See Also

- [Startup & Internals](/spring-boot/startup-and-internals/)
- [Microservices Playbook](/microservices/)
- [Java Engineering](/java-engineering/)
- [Spring Boot Handbook Index](/spring-boot/)
