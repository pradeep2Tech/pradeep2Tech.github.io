---
title: "JWT & OAuth2 Reference"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Resource server, JWT validation, OAuth2 grant types."
tags: ["spring-boot", "spring", "cheatsheet", "handbook"]
categories: ["Spring Boot Cheat Sheet"]
shortTitle: "JWT/OAuth"
module: 5
moduleTitle: "Security"
sectionRef: "5.2"
ShowToc: true
cheatSheet: true
---

## At a Glance

- Resource server validates JWT signature/issuer/audience.
- Scopes/roles map to `GrantedAuthority`.
- OAuth2 authorization code for user login; client credentials for service-to-service.

---

## Reference Tables

| Grant | Use |
| :--- | :--- |
| Authorization code | User-facing apps |
| Client credentials | Machine-to-machine |
| Refresh token | Renew access token |

| JWT claim | Maps to |
| :--- | :--- |
| `sub` | Principal name |
| `scope` / `roles` | Authorities |

---

## Snippets

```yaml
spring:
  security:
    oauth2:
      resourceserver:
        jwt:
          issuer-uri: https://auth.example.com/realms/app
```

---

## Internals & Gotchas

- Validate issuer and audience — don't trust unsigned tokens.
- Short access token TTL + refresh rotation.

---

## Production Notes

- Use Spring Authorization Server or external IdP (Keycloak, Entra ID).

---

## Interview Probes


{< interview-answer >}
**Q:** Session vs JWT?

**A:** JWT stateless for APIs; sessions for server-rendered forms.
{< /interview-answer >}

---

## See Also

- [Previous: Security](/spring-boot/security-quick-ref/)
- [Next: Caching](/spring-boot/caching-ref/)
- [Spring Boot Cheat Sheet Index](/spring-boot/)
- [Java Engineering](/java-engineering/)
- [Microservices Playbook](/microservices/)
