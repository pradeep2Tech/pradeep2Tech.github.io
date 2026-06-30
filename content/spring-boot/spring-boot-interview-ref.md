---
title: "Spring Boot Interview Reference"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Startup flow, auto-config, DispatcherServlet, common probes."
tags: ["spring-boot", "spring", "cheatsheet", "handbook"]
categories: ["Spring Boot Cheat Sheet"]
shortTitle: "Interview"
module: 9
moduleTitle: "Interview"
sectionRef: "9.1"
ShowToc: true
cheatSheet: true
---

## At a Glance

- Startup: `SpringApplication.run` → env → context refresh → auto-config → runners → ready.
- DispatcherServlet: mapping → adapter → controller → message converter.
- Auto-config: `@ConditionalOnClass` + `@ConditionalOnProperty`.

---

## Reference Tables

| Question | Short answer |
| :--- | :--- |
| What is Spring Boot? | Opinionated Spring — auto-config, starters, embedded server |
| Auto-config mechanism? | Conditional beans from classpath via `AutoConfiguration.imports` |
| Default bean scope? | Singleton |
| `@Transactional` self-call? | Bypasses proxy — won't start new tx |
| Actuator purpose? | Prod ops: health, metrics |
| Boot 2 → 3? | Java 17, jakarta.*, SecurityFilterChain |

| Startup phase | What happens |
| :--- | :--- |
| Environment | Load properties, profiles |
| refresh() | Register bean definitions |
| Auto-config | Conditional beans |
| Web server | Start embedded container |

---

## Snippets

_See linked cheat sheets for snippets._

---

## Internals & Gotchas

- Answer with trade-offs in interviews, not definitions only.

---

## Production Notes

- Link bean lifecycle to `@PostConstruct` vs `ApplicationRunner` order.

---

## Interview Probes


{< interview-answer >}
**Q:** How does auto-configuration work?

**A:** Classpath triggers `@Conditional*` classes listed in AutoConfiguration.imports; beans register if conditions match.
{< /interview-answer >}

{< interview-answer >}
**Q:** DispatcherServlet role?

**A:** Front controller — maps URL to handler, invokes controller, resolves view/JSON.
{< /interview-answer >}

{< interview-answer >}
**Q:** Why constructor injection?

**A:** Immutable deps, testable, explicit contract.
{< /interview-answer >}

---

## See Also

- [Previous: Messaging](/spring-boot/messaging-ref/)
- [Spring Boot Cheat Sheet Index](/spring-boot/)
- [Java Engineering](/java-engineering/)
- [Microservices Playbook](/microservices/)
