---
title: "Configuration Reference"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "application.yml, profiles, @ConfigurationProperties, @Value, external config."
tags: ["spring-boot", "spring", "cheatsheet", "handbook"]
categories: ["Spring Boot Cheat Sheet"]
shortTitle: "Config"
module: 2
moduleTitle: "Configuration"
sectionRef: "2.1"
ShowToc: true
cheatSheet: true
---

## At a Glance

- Load order: command line → env → application-{profile}.yml → application.yml.
- Relaxed binding: `my.service-url` ↔ `MY_SERVICE_URL`.
- `@ConfigurationProperties` for typed prefix binding.

---

## Reference Tables

| Mechanism | Example |
| :--- | :--- |
| Properties | `server.port=8080` |
| YAML | nested keys under `spring:` |
| Profile | `spring.profiles.active=prod` |
| Env | `SPRING_APPLICATION_JSON`, `MY_APP_FEATURE=true` |
| `@Value` | `@Value("${app.timeout:30}")` |
| `@ConfigurationProperties` | `@ConfigurationProperties(prefix = "app")` |

| Profile file | Loads when |
| :--- | :--- |
| `application-dev.yml` | `spring.profiles.active=dev` |
| `@Profile("dev")` on `@Bean` | Same |

---

## Snippets

```yaml
spring:
  application:
    name: orders-api
  datasource:
    url: ${DB_URL}
app:
  feature-flags:
    new-checkout: true
```

```java
@ConfigurationProperties(prefix = "app.feature-flags")
public record FeatureFlags(boolean newCheckout) {}
```

---

## Internals & Gotchas

- `@Value` scattered keys don't scale — prefer `@ConfigurationProperties` records.
- Secrets via env / K8s Secret / Vault — never in git.

---

## Production Notes

- Validate config with `@Validated` on properties class.
- Document required env vars in README.

---

## Interview Probes


{< interview-answer >}
**Q:** Property precedence?

**A:** Command line args override env override profile files override default application.yml.
{< /interview-answer >}

---

## See Also

- [Previous: DI](/spring-boot/dependency-injection-ref/)
- [Next: REST](/spring-boot/rest-api-ref/)
- [Spring Boot Cheat Sheet Index](/spring-boot/)
- [Java Engineering](/java-engineering/)
- [Microservices Playbook](/microservices/)
