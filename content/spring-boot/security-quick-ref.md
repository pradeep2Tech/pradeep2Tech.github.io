---
title: "Spring Security Quick Reference"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "SecurityFilterChain, authn vs authz, method security."
tags: ["spring-boot", "spring", "cheatsheet", "handbook"]
categories: ["Spring Boot Cheat Sheet"]
shortTitle: "Security"
module: 5
moduleTitle: "Security"
sectionRef: "5.1"
ShowToc: true
cheatSheet: true
---

## At a Glance

- Boot 3: `@Bean SecurityFilterChain` — no `WebSecurityConfigurerAdapter`.
- Authentication = who; Authorization = what allowed.
- `SecurityContextHolder` holds `Authentication` per thread.

---

## Reference Tables

| Area | Boot 2.x | Boot 3.x |
| :--- | :--- | :--- |
| **Java** | 8+ | **17+** required |
| **Namespace** | `javax.*` | **`jakarta.*`** |
| **Security** | `WebSecurityConfigurerAdapter` | `@Bean SecurityFilterChain` |
| **Auto-config index** | `META-INF/spring.factories` | `META-INF/spring/...AutoConfiguration.imports` |

| Config | Purpose |
| :--- | :--- |
| `authorizeHttpRequests` | URL access rules |
| `formLogin` / `httpBasic` | Built-in auth |
| `oauth2ResourceServer` | JWT bearer APIs |
| `csrf` | Disable only for stateless APIs |
| `@PreAuthorize` | Method-level SpEL |

---

## Snippets

```java
@Bean
SecurityFilterChain api(HttpSecurity http) throws Exception {
  return http
    .authorizeHttpRequests(a -> a
      .requestMatchers("/actuator/health").permitAll()
      .anyRequest().authenticated())
    .oauth2ResourceServer(o -> o.jwt(Customizer.withDefaults()))
    .build();
}
```

---

## Internals & Gotchas

- Permit health/prometheus explicitly.
- CSRF off ≠ security off — still need authz.

---

## Production Notes

- Use `PasswordEncoder` bean (BCrypt) for stored passwords.

---

## Interview Probes


{< interview-answer >}
**Q:** Filter chain vs DispatcherServlet?

**A:** Security filters run before Spring MVC.
{< /interview-answer >}

---

## See Also

- [Previous: Transactions](/spring-boot/transactions-ref/)
- [Next: JWT/OAuth](/spring-boot/jwt-oauth-ref/)
- [JWT/OAuth](/spring-boot/jwt-oauth-ref/)
- [Spring Boot Cheat Sheet Index](/spring-boot/)
- [Java Engineering](/java-engineering/)
- [Microservices Playbook](/microservices/)
