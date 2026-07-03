---
title: "Configuration"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Property resolution order, profiles, @Value vs @ConfigurationProperties — production config patterns."
tags: ["spring-boot", "spring", "handbook", "interview"]
categories: ["Spring Boot Handbook"]
shortTitle: "Config"
module: 2
moduleTitle: "Configuration"
sectionRef: "2.1"
ShowToc: true
interviewHandbook: true
aliases:
  - configuration-ref
---

## What is the Spring Boot property resolution order?

**Difficulty:** Medium  
**Expected Answer Time:** 1 min

### Short Answer

Later sources override earlier: default properties → `@PropertySource` → config data (application.yml) → profile-specific files → env vars → system properties → command-line args.

### Detailed Explanation

Spring Boot 2.4+ uses `configtree:` and `spring.config.import` for optional remote config. Relaxed binding maps `my.service-url` ↔ `MY_SERVICE_URL` ↔ `my.serviceUrl`. `spring.application.json` env var injects JSON tree. Kubernetes downward API mounts as env or files.

### Internal Working

`ConfigDataEnvironment` loads `application.properties|yml`, then `application-{profile}.*`, then imports. `@ConfigurationProperties` beans bind after environment prepared.

### Production Notes

Document required env vars in README/runbook. Validate at startup with `@Validated` + JSR-303 on properties class — fail fast.

### Common Mistakes

Secrets in `application-prod.yml` in git. Assuming profile-specific file overrides env (env wins over files).

### Follow-up Questions

- What is `spring.config.import`?
- How does Cloud Config Server fit?

---
## How do Spring profiles work?

**Difficulty:** Easy  
**Expected Answer Time:** 30 sec

### Short Answer

Profiles tag beans and config; activate via `spring.profiles.active`, env, or `@ActiveProfiles` in tests.

### Detailed Explanation

`application-dev.yml` loads when `dev` profile active. `@Profile("dev")` on `@Bean` or `@Configuration` registers conditionally. Multiple profiles: `prod,metrics`. Default profile via `spring.profiles.default`. Profile groups (Boot 2.4+): `spring.profiles.group.prod=proddb,prodcache`.

### Internal Working

`Environment.acceptsProfiles` / `@Profile` use `Profiles` API. Inactive profile beans are not registered — not just disabled.

### Production Notes

Use `prod` not `production` consistently across fleet. Never enable `dev` profile in production images.

### Common Mistakes

`@Profile` on `@Entity` — causes subtle missing table errors.

### Follow-up Questions

- Profile vs property `app.feature.enabled`?
- How to test multiple profiles?

---
## @Value vs @ConfigurationProperties?

**Difficulty:** Medium  
**Expected Answer Time:** 1 min

### Short Answer

`@Value`: single SpEL property, good for one-offs. `@ConfigurationProperties`: type-safe prefix binding, validation, lists, nested objects.

### Detailed Explanation

`@Value("${app.timeout:30}")` embeds in fields — hard to test, no bulk validation. `@ConfigurationProperties(prefix = "app")` on record/class binds tree; supports `ignoreUnknownFields`, `conversionService`. Enable via `@EnableConfigurationProperties` or `@ConfigurationPropertiesScan`.

### Internal Working

Binding uses JavaBeans conventions or constructor binding (immutable records). `Binder` API under the hood.

### Production Notes

Use records for immutable config. `@Validated` + `@NotNull` on properties class.

### Common Mistakes

Dozens of `@Value` scattered — unmaintainable. SpEL in `@Value` executing arbitrary code in prod config.

### Follow-up Questions

- Relaxed binding examples?
- How to bind `Map<String, Duration>`?

---

## See Also

- [Previous: Startup](/spring-boot/startup-and-internals/)
- [Next: REST API](/spring-boot/rest-api-design/)
- [100+ Interview Questions](/spring-boot/interview-questions/)
- [Spring Boot Handbook Index](/spring-boot/)
- [Java Engineering](/java-engineering/)
- [Microservices Playbook](/microservices/) — Saga, Outbox, CQRS, API Gateway
- [Kafka Handbook](/kafka-handbook/)
- [Security Architecture](/security-architecture/)
