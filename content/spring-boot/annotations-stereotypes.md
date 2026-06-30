---
title: "Annotations & Stereotypes"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "@SpringBootApplication, stereotypes, mapping, and common Spring annotations table."
tags: ["spring-boot", "spring", "cheatsheet", "handbook"]
categories: ["Spring Boot Cheat Sheet"]
shortTitle: "Annotations"
module: 1
moduleTitle: "Bootstrap & Core"
sectionRef: "1.2"
ShowToc: true
cheatSheet: true
---

## At a Glance

- Stereotypes are meta-annotated with `@Component`.
- Prefer constructor injection on all stereotype classes.
- Mapping annotations compose on `@RestController`.

---

## Reference Tables

| Annotation | Layer / purpose |
| :--- | :--- |
| `@Component` | Generic bean |
| `@Service` | Business logic |
| `@Repository` | Persistence (+ exception translation) |
| `@Controller` | MVC views |
| `@RestController` | `@Controller` + `@ResponseBody` |
| `@Configuration` | `@Bean` definitions |
| `@Bean` | Explicit factory method bean |
| `@Primary` | Win type conflict |
| `@Qualifier` | Disambiguate by name |
| `@Scope` | singleton (default), prototype, request, session |
| `@ConditionalOn*` | Auto-config guards |

| Web mapping | HTTP |
| :--- | :--- |
| `@GetMapping` | GET |
| `@PostMapping` | POST |
| `@PutMapping` | PUT |
| `@DeleteMapping` | DELETE |
| `@PatchMapping` | PATCH |
| `@RequestMapping` | Base path + method/consumes/produces |

| Other common | Use |
| :--- | :--- |
| `@Transactional` | Declarative TX (service layer) |
| `@Valid` / `@Validated` | Bean Validation trigger |
| `@Scheduled` / `@Async` | Background work |
| `@Cacheable` | Method result cache |

---

## Snippets

```java
@RestController
@RequestMapping("/api/orders")
public class OrderController {
  private final OrderService service;
  public OrderController(OrderService service) { this.service = service; }

  @GetMapping("/{id}")
  public OrderDto get(@PathVariable Long id) { return service.find(id); }
}
```

---

## Internals & Gotchas

- `@RestController` on class — methods return body directly.
- Don't annotate DTOs with `@Component`.

---

## Production Notes

- Keep controllers thin.
- One stereotype per class.

---

## Interview Probes


{< interview-answer >}
**Q:** @Service vs @Component?

**A:** Same container behavior — `@Service` documents intent.
{< /interview-answer >}

---

## See Also

- [Previous: Quick Ref](/spring-boot/spring-boot-quick-ref/)
- [Next: DI](/spring-boot/dependency-injection-ref/)
- [Spring Boot Cheat Sheet Index](/spring-boot/)
- [Java Engineering](/java-engineering/)
- [Microservices Playbook](/microservices/)
