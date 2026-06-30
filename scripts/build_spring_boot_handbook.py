"""Build Spring Boot Cheat Sheet pages from data/spring_boot_modules.yaml."""
from __future__ import annotations

import re
import textwrap
from pathlib import Path
from typing import NamedTuple

import yaml

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
CONTENT = ROOT / "content" / "spring-boot"
DATE = "2026-06-30T10:00:00+00:00"
SECTION = "spring-boot"
SECTION_TITLE = "Spring Boot Cheat Sheet"

BOOT23 = """| Area | Boot 2.x | Boot 3.x |
| :--- | :--- | :--- |
| **Java** | 8+ | **17+** required |
| **Namespace** | `javax.*` | **`jakarta.*`** |
| **Security** | `WebSecurityConfigurerAdapter` | `@Bean SecurityFilterChain` |
| **Auto-config index** | `META-INF/spring.factories` | `META-INF/spring/...AutoConfiguration.imports` |"""

TOPIC_META: dict[str, tuple[str, str, str]] = {
    "spring-boot-quick-ref": (
        "Spring Boot Quick Reference",
        "Quick Ref",
        "Starters, bootstrap, run commands, and Boot 2 vs 3 — one-page recap.",
    ),
    "annotations-stereotypes": (
        "Annotations & Stereotypes",
        "Annotations",
        "@SpringBootApplication, stereotypes, mapping, and common Spring annotations table.",
    ),
    "dependency-injection-ref": (
        "Dependency Injection Reference",
        "DI",
        "Constructor injection, scopes, @Bean, lifecycle callbacks — recap only.",
    ),
    "configuration-ref": (
        "Configuration Reference",
        "Config",
        "application.yml, profiles, @ConfigurationProperties, @Value, external config.",
    ),
    "rest-api-ref": (
        "REST API Reference",
        "REST",
        "RestController, HTTP mappings, RequestBody, PathVariable, ResponseEntity.",
    ),
    "validation-ref": (
        "Validation Reference",
        "Validation",
        "Jakarta Bean Validation constraints, @Valid, groups.",
    ),
    "exception-handling-ref": (
        "Exception Handling Reference",
        "Exceptions",
        "@ControllerAdvice, ProblemDetail, HTTP status mapping.",
    ),
    "jpa-quick-ref": (
        "Spring Data JPA Quick Reference",
        "JPA",
        "Entity, repository hierarchy, paging, sorting.",
    ),
    "jpa-queries-ref": (
        "JPA Queries Reference",
        "JPA Queries",
        "Derived queries, @Query, JPQL, native SQL.",
    ),
    "transactions-ref": (
        "Transactions Reference",
        "Transactions",
        "Propagation, isolation, rollback rules, readOnly.",
    ),
    "security-quick-ref": (
        "Spring Security Quick Reference",
        "Security",
        "SecurityFilterChain, authn vs authz, method security.",
    ),
    "jwt-oauth-ref": (
        "JWT & OAuth2 Reference",
        "JWT/OAuth",
        "Resource server, JWT validation, OAuth2 grant types.",
    ),
    "caching-ref": (
        "Caching Reference",
        "Caching",
        "@Cacheable, CacheManager, Redis, eviction.",
    ),
    "scheduling-async-ref": (
        "Scheduling & Async Reference",
        "Schedule/Async",
        "@Scheduled, cron, @Async, TaskExecutor.",
    ),
    "events-ref": (
        "Spring Events Reference",
        "Events",
        "ApplicationEvent, @EventListener, @TransactionalEventListener.",
    ),
    "actuator-ref": (
        "Actuator Reference",
        "Actuator",
        "Health, metrics, info, Prometheus, K8s probes.",
    ),
    "observability-ref": (
        "Observability Reference",
        "Observability",
        "Logging, MDC, Micrometer, OpenTelemetry, tracing hooks.",
    ),
    "testing-ref": (
        "Testing Reference",
        "Testing",
        "MockMvc, @MockBean, slice tests, Testcontainers.",
    ),
    "production-deployment-ref": (
        "Production & Deployment Reference",
        "Production",
        "Fat JAR, Docker, graceful shutdown, externalized config.",
    ),
    "spring-cloud-ref": (
        "Spring Cloud Reference",
        "Spring Cloud",
        "Config, discovery, Gateway, OpenFeign, Resilience4j.",
    ),
    "messaging-ref": (
        "Messaging Reference",
        "Messaging",
        "Kafka and RabbitMQ listener/producer snippets.",
    ),
    "spring-boot-interview-ref": (
        "Spring Boot Interview Reference",
        "Interview",
        "Startup flow, auto-config, DispatcherServlet, common probes.",
    ),
}

EXTRA_RELATED: dict[str, list[str]] = {
    "rest-api-ref": ["validation-ref", "exception-handling-ref"],
    "jpa-quick-ref": ["jpa-queries-ref", "transactions-ref"],
    "security-quick-ref": ["jwt-oauth-ref"],
    "actuator-ref": ["observability-ref", "production-deployment-ref"],
}


class TopicSpec(NamedTuple):
    glance: list[str]
    tables: str
    snippets: str
    internals: str
    production: str
    interviews: list[tuple[str, str]] | None


def flatten_topics(modules: list) -> list[str]:
    topics: list[str] = []
    for mod in modules:
        if mod.get("groups"):
            for group in mod["groups"]:
                topics.extend(group["topics"])
        else:
            topics.extend(mod["topics"])
    return topics


def iter_module_topics(modules: list) -> list[tuple[int, str, str, int]]:
    result: list[tuple[int, str, str, int]] = []
    for mod in modules:
        mod_id = mod["id"]
        mod_title = mod["focus"]
        slugs = flatten_topics([mod])
        for idx, slug in enumerate(slugs, start=1):
            result.append((mod_id, mod_title, slug, idx))
    return result


def write_order_yaml(topics: list[str], path: Path) -> None:
    header = (
        "# Flat topic order — derived from spring_boot_modules.yaml.\n"
        "# Prefer editing data/spring_boot_modules.yaml for module structure.\n"
        "topics:\n"
    )
    path.write_text(header + "".join(f"  - {s}\n" for s in topics), encoding="utf-8")


def interview_block(q: str, a: str) -> str:
    return f"""{{< interview-answer >}}
**Q:** {q}

**A:** {a}
{{< /interview-answer >}}"""


def see_also_links(slug: str, ordered: list[str]) -> str:
    links: list[str] = []
    idx = ordered.index(slug)
    if idx > 0:
        prev = ordered[idx - 1]
        links.append(f"- [Previous: {TOPIC_META[prev][1]}](/{SECTION}/{prev}/)")
    if idx < len(ordered) - 1:
        nxt = ordered[idx + 1]
        links.append(f"- [Next: {TOPIC_META[nxt][1]}](/{SECTION}/{nxt}/)")
    for rel in EXTRA_RELATED.get(slug, []):
        if rel in TOPIC_META:
            links.append(f"- [{TOPIC_META[rel][1]}](/{SECTION}/{rel}/)")
    links.append(f"- [{SECTION_TITLE} Index](/{SECTION}/)")
    links.append("- [Java Engineering](/java-engineering/)")
    links.append("- [Microservices Playbook](/microservices/)")
    return "\n".join(links)


def front_matter(slug: str, mod_id: int, mod_title: str, topic_idx: int) -> str:
    title, short, desc = TOPIC_META[slug]
    return f"""---
title: "{title}"
date: {DATE}
draft: false
description: "{desc}"
tags: ["spring-boot", "spring", "cheatsheet", "handbook"]
categories: ["{SECTION_TITLE}"]
shortTitle: "{short}"
module: {mod_id}
moduleTitle: "{mod_title}"
sectionRef: "{mod_id}.{topic_idx}"
ShowToc: true
cheatSheet: true
---

"""


def page_body(spec: TopicSpec, see_also: str) -> str:
    sections = [
        "## At a Glance",
        "",
        "\n".join(f"- {b}" for b in spec.glance),
        "",
        "---",
        "",
        "## Reference Tables",
        "",
        spec.tables.strip(),
        "",
        "---",
        "",
        "## Snippets",
        "",
        spec.snippets.strip(),
        "",
        "---",
        "",
        "## Internals & Gotchas",
        "",
        spec.internals.strip(),
        "",
        "---",
        "",
        "## Production Notes",
        "",
        spec.production.strip(),
    ]
    if spec.interviews:
        sections.extend(["", "---", "", "## Interview Probes", ""])
        for q, a in spec.interviews:
            sections.extend(["", interview_block(q, a)])
    sections.extend(["", "---", "", "## See Also", "", see_also.strip()])
    return "\n".join(sections) + "\n"


def t(
    glance: list[str],
    tables: str,
    snippets: str = "",
    internals: str = "",
    production: str = "",
    interviews: list[tuple[str, str]] | None = None,
) -> TopicSpec:
    return TopicSpec(glance, tables, snippets, internals, production, interviews)


PAGE_BODIES: dict[str, TopicSpec] = {
    "spring-boot-quick-ref": t(
        [
            "`@SpringBootApplication` = `@Configuration` + `@EnableAutoConfiguration` + `@ComponentScan`.",
            "Starters pull aligned transitive deps; BOM locks versions.",
            "Boot 3 requires Java 17 and `jakarta.*`.",
        ],
        BOOT23
        + """

| Starter | Pulls |
| :--- | :--- |
| `spring-boot-starter-web` | MVC, Jackson, Tomcat |
| `spring-boot-starter-data-jpa` | Hibernate, JDBC, transactions |
| `spring-boot-starter-security` | Security filter chain |
| `spring-boot-starter-actuator` | Health, metrics |
| `spring-boot-starter-test` | JUnit 5, Mockito, MockMvc |

| Run | Command |
| :--- | :--- |
| JAR | `java -jar app.jar --spring.profiles.active=prod` |
| Maven | `./mvnw spring-boot:run` |
| Gradle | `./gradlew bootRun` |""",
        """```java
@SpringBootApplication
public class App {
  public static void main(String[] args) {
    SpringApplication.run(App.class, args);
  }
}
```""",
        "- Auto-config is conditional — exclude with `@SpringBootApplication(exclude = ...)`.\n- DevTools restart only for dev classpath scope.",
        "- Pin Boot version in parent BOM.\n- Add actuator from day one.\n- Never commit secrets — use env / vault.",
        [
            ("Minimum Java for Boot 3?", "Java 17."),
            ("What is a starter?", "Curated dependency descriptor + optional auto-config — not one fat library."),
        ],
    ),
    "annotations-stereotypes": t(
        [
            "Stereotypes are meta-annotated with `@Component`.",
            "Prefer constructor injection on all stereotype classes.",
            "Mapping annotations compose on `@RestController`.",
        ],
        """| Annotation | Layer / purpose |
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
| `@Cacheable` | Method result cache |""",
        """```java
@RestController
@RequestMapping("/api/orders")
public class OrderController {
  private final OrderService service;
  public OrderController(OrderService service) { this.service = service; }

  @GetMapping("/{id}")
  public OrderDto get(@PathVariable Long id) { return service.find(id); }
}
```""",
        "- `@RestController` on class — methods return body directly.\n- Don't annotate DTOs with `@Component`.",
        "- Keep controllers thin.\n- One stereotype per class.",
        [("@Service vs @Component?", "Same container behavior — `@Service` documents intent.")],
    ),
    "dependency-injection-ref": t(
        [
            "Constructor injection is default when one constructor exists.",
            "Singleton scope unless `@Scope` specified.",
            "Avoid field `@Autowired` in new code.",
        ],
        """| Injection | When |
| :--- | :--- |
| Constructor | **Preferred** — required deps, immutable |
| Setter | Rare — optional deps |
| Field | Legacy — hard to test |

| Scope | Instances |
| :--- | :--- |
| singleton | One per context (default) |
| prototype | New per injection / getBean |
| request / session | Web-scoped (needs proxy into singleton) |

| Lifecycle | Hook |
| :--- | :--- |
| After inject | `@PostConstruct` |
| Before destroy | `@PreDestroy` |
| Programmatic | `InitializingBean` / `DisposableBean` |""",
        """```java
@Service
public class OrderService {
  private final OrderRepository repo;
  public OrderService(OrderRepository repo) { this.repo = repo; }
}
```""",
        "- Circular deps fail at startup — refactor or `@Lazy` (last resort).\n- Prototype into singleton needs scoped proxy.",
        "- No request state in singleton beans.",
        [("Why constructor injection?", "Explicit, immutable, unit-testable without Spring.")],
    ),
    "configuration-ref": t(
        [
            "Load order: command line → env → application-{profile}.yml → application.yml.",
            "Relaxed binding: `my.service-url` ↔ `MY_SERVICE_URL`.",
            "`@ConfigurationProperties` for typed prefix binding.",
        ],
        """| Mechanism | Example |
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
| `@Profile("dev")` on `@Bean` | Same |""",
        """```yaml
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
```""",
        "- `@Value` scattered keys don't scale — prefer `@ConfigurationProperties` records.\n- Secrets via env / K8s Secret / Vault — never in git.",
        "- Validate config with `@Validated` on properties class.\n- Document required env vars in README.",
        [("Property precedence?", "Command line args override env override profile files override default application.yml.")],
    ),
    "rest-api-ref": t(
        [
            "`@RestController` returns JSON via HttpMessageConverter.",
            "Use DTOs — never expose JPA entities directly.",
            "`ResponseEntity` for status + headers control.",
        ],
        """| Annotation | Binds |
| :--- | :--- |
| `@RequestBody` | HTTP body → object |
| `@RequestParam` | Query / form param |
| `@PathVariable` | URI `{id}` segment |
| `@RequestHeader` | Header value |
| `@ResponseStatus` | Fixed status on method |

| Status | Typical use |
| :--- | :--- |
| 200 | GET success |
| 201 | POST create (+ Location header) |
| 204 | DELETE success |
| 400 | Validation failure |
| 404 | Not found |
| 409 | Conflict |""",
        """```java
@PostMapping
public ResponseEntity<OrderDto> create(@Valid @RequestBody CreateOrderRequest req) {
  OrderDto created = service.create(req);
  URI location = URI.create("/api/orders/" + created.id());
  return ResponseEntity.created(location).body(created);
}
```""",
        "- Wrong `Content-Type` → 415.\n- Missing `@Valid` → constraints not enforced.",
        "- Version APIs (`/api/v1`).\n- Enable `spring.jackson.deserialization.fail-on-unknown-properties` for public APIs.",
        [("@PathVariable vs @RequestParam?", "Path = resource id; query = filters/pagination.")],
    ),
    "validation-ref": t(
        [
            "Boot 3 uses `jakarta.validation.*`.",
            "Trigger with `@Valid` on `@RequestBody` or `@Validated` on class.",
            "Custom: `@Constraint` + `ConstraintValidator`.",
        ],
        """| Constraint | Checks |
| :--- | :--- |
| `@NotNull` / `@NotBlank` / `@NotEmpty` | Presence |
| `@Size` | String/collection length |
| `@Min` / `@Max` | Numeric bounds |
| `@Email` | Email format |
| `@Pattern` | Regex |
| `@Past` / `@Future` | Date/time |

| Groups | Use |
| :--- | :--- |
| `Create.class` | POST rules |
| `Update.class` | PATCH rules — `@Validated(Update.class)` |""",
        """```java
public record CreateOrderRequest(
    @NotBlank String sku,
    @Min(1) int quantity,
    @Email String contactEmail
) {}
```""",
        "- Import `javax.validation` on Boot 3 → compile error.",
        "- Validate at API boundary; don't rely only on DB constraints.",
        [("Where to validate?", "Controller DTOs at boundary; domain invariants in service layer.")],
    ),
    "exception-handling-ref": t(
        [
            "`@RestControllerAdvice` + `@ExceptionHandler` for global JSON errors.",
            "Boot 3 has `ProblemDetail` (RFC 7807).",
            "Log server detail; return safe client message.",
        ],
        """| Exception type | HTTP |
| :--- | :--- |
| Validation (`MethodArgumentNotValidException`) | 400 |
| Not found (custom) | 404 |
| Conflict | 409 |
| Unauthorized | 401 |
| Forbidden | 403 |""",
        """```java
@RestControllerAdvice
public class ApiErrors {
  @ExceptionHandler(NotFoundException.class)
  public ProblemDetail notFound(NotFoundException ex) {
    return ProblemDetail.forStatusAndDetail(HttpStatus.NOT_FOUND, ex.getMessage());
  }
}
```""",
        "- Don't catch broad `Exception` and return 200.\n- Include correlation id from MDC in body.",
        "- Map vendor errors to stable API error codes.",
        [("@ControllerAdvice vs @RestControllerAdvice?", "后者 adds @ResponseBody on handlers.")],
    ),
    "jpa-quick-ref": t(
        [
            "Repositories are interfaces — Spring implements at runtime.",
            "`JpaRepository` adds flush + batch delete.",
            "Use `Pageable` for large result sets.",
        ],
        """| Interface | Provides |
| :--- | :--- |
| `CrudRepository` | basic CRUD |
| `PagingAndSortingRepository` | `Pageable`, `Sort` |
| `JpaRepository` | JPA flush, `deleteAllInBatch` |

| Entity | Annotation |
| :--- | :--- |
| Table | `@Entity` `@Table(name="orders")` |
| PK | `@Id` `@GeneratedValue` |
| Version | `@Version` optimistic lock |
| Relations | `@OneToMany`, `@ManyToOne`, etc. |""",
        """```java
@Entity
public class Order {
  @Id @GeneratedValue private Long id;
  @Version private Long version;
}

public interface OrderRepository extends JpaRepository<Order, Long> {}
```""",
        "- `open-in-view=false` in prod — avoid lazy load in controllers.\n- equals/hashCode on entities: use business key or id only.",
        "- DTO projection for reads; don't return entities from REST.",
        [("Derived query method naming?", "Spring parses `findByStatusAndCreatedAtAfter` → query.")],
    ),
    "jpa-queries-ref": t(
        [
            "Derived method names for simple queries.",
            "`@Query` for JPQL; `nativeQuery=true` for SQL.",
            "Named parameters: `@Param(\"status\")`.",
        ],
        """| Style | When |
| :--- | :--- |
| Derived | Simple property paths |
| JPQL | Portable object queries |
| Native | DB-specific SQL, hints, CTEs |
| Specification | Dynamic predicates (Criteria API) |

| JPQL example | |
| :--- | :--- |
| `SELECT o FROM Order o WHERE o.status = :s` | entity name, not table |""",
        """```java
@Query("select o from Order o where o.status = :status")
List<Order> findByStatus(@Param("status") OrderStatus status);

@Query(value = "SELECT * FROM orders WHERE id = ?1", nativeQuery = true)
Optional<Order> findRaw(Long id);
```""",
        "- Native queries bypass change tracking semantics.\n- `@Modifying` for UPDATE/DELETE — clear persistence context.",
        "- Prefer JPQL unless you need SQL features.",
        [("N+1 problem?", "Fetch join or `@EntityGraph` or DTO projection.")],
    ),
    "transactions-ref": t(
        [
            "`@Transactional` on service layer — not controllers.",
            "Default propagation: `REQUIRED`.",
            "Unchecked exceptions rollback; checked exceptions don't by default.",
        ],
        """| Propagation | Behavior |
| :--- | :--- |
| REQUIRED | Join or create (default) |
| REQUIRES_NEW | Suspend, new transaction |
| NESTED | Savepoint nested |
| SUPPORTS | Join if exists, else non-tx |

| Isolation | Trade-off |
| :--- | :--- |
| READ_COMMITTED | Default on many DBs |
| REPEATABLE_READ | Phantom protection varies |
| SERIALIZABLE | Strongest, slowest |

| Attribute | Note |
| :--- | :--- |
| `readOnly=true` | Hint for optimizations |
| `rollbackFor` | Include checked exceptions |""",
        """```java
@Transactional
public OrderDto placeOrder(CreateOrderRequest req) {
  // single transaction boundary
}
```""",
        "- Self-invocation bypasses proxy — inject self or refactor.\n- Keep transactions short — no remote HTTP inside.",
        "- Use `REQUIRES_NEW` for audit logs that must commit independently.",
        [("Why rollback on RuntimeException?", "Default policy — declare `rollbackFor` for checked business exceptions.")],
    ),
    "security-quick-ref": t(
        [
            "Boot 3: `@Bean SecurityFilterChain` — no `WebSecurityConfigurerAdapter`.",
            "Authentication = who; Authorization = what allowed.",
            "`SecurityContextHolder` holds `Authentication` per thread.",
        ],
        BOOT23
        + """

| Config | Purpose |
| :--- | :--- |
| `authorizeHttpRequests` | URL access rules |
| `formLogin` / `httpBasic` | Built-in auth |
| `oauth2ResourceServer` | JWT bearer APIs |
| `csrf` | Disable only for stateless APIs |
| `@PreAuthorize` | Method-level SpEL |""",
        """```java
@Bean
SecurityFilterChain api(HttpSecurity http) throws Exception {
  return http
    .authorizeHttpRequests(a -> a
      .requestMatchers("/actuator/health").permitAll()
      .anyRequest().authenticated())
    .oauth2ResourceServer(o -> o.jwt(Customizer.withDefaults()))
    .build();
}
```""",
        "- Permit health/prometheus explicitly.\n- CSRF off ≠ security off — still need authz.",
        "- Use `PasswordEncoder` bean (BCrypt) for stored passwords.",
        [("Filter chain vs DispatcherServlet?", "Security filters run before Spring MVC.")],
    ),
    "jwt-oauth-ref": t(
        [
            "Resource server validates JWT signature/issuer/audience.",
            "Scopes/roles map to `GrantedAuthority`.",
            "OAuth2 authorization code for user login; client credentials for service-to-service.",
        ],
        """| Grant | Use |
| :--- | :--- |
| Authorization code | User-facing apps |
| Client credentials | Machine-to-machine |
| Refresh token | Renew access token |

| JWT claim | Maps to |
| :--- | :--- |
| `sub` | Principal name |
| `scope` / `roles` | Authorities |""",
        """```yaml
spring:
  security:
    oauth2:
      resourceserver:
        jwt:
          issuer-uri: https://auth.example.com/realms/app
```""",
        "- Validate issuer and audience — don't trust unsigned tokens.\n- Short access token TTL + refresh rotation.",
        "- Use Spring Authorization Server or external IdP (Keycloak, Entra ID).",
        [("Session vs JWT?", "JWT stateless for APIs; sessions for server-rendered forms.")],
    ),
    "caching-ref": t(
        [
            "`@EnableCaching` + `CacheManager` bean.",
            "`@Cacheable` on method — key from SpEL.",
            "Redis for distributed cache.",
        ],
        """| Annotation | Effect |
| :--- | :--- |
| `@Cacheable` | Return cached value on hit |
| `@CachePut` | Always run + update cache |
| `@CacheEvict` | Remove entries |

| Manager | Backend |
| :--- | :--- |
| `CaffeineCacheManager` | In-process |
| `RedisCacheManager` | Distributed |""",
        """```java
@Cacheable(value = "orders", key = "#id")
public OrderDto findById(Long id) { ... }

@CacheEvict(value = "orders", key = "#id")
public void invalidate(Long id) { ... }
```""",
        "- Cache nulls carefully (`unless`).\n- TTL + key design prevents stale reads.",
        "- `@Cacheable` on self-call doesn't work — proxy issue.",
        [("Cache stampede?", "Sync cache load, random TTL jitter, or single-flight pattern.")],
    ),
    "scheduling-async-ref": t(
        [
            "`@EnableScheduling` + `@Scheduled` on methods.",
            "`fixedDelay` waits after completion; `fixedRate` between starts.",
            "`@Async` needs `@EnableAsync` + `TaskExecutor` bean.",
        ],
        """| `@Scheduled` | Meaning |
| :--- | :--- |
| `fixedDelay` | ms after previous **finish** |
| `fixedRate` | ms between **starts** |
| `cron` | 6-field Spring cron |

| Cron field | Order |
| :--- | :--- |
| sec min hour day month weekday | |""",
        """```java
@Scheduled(cron = "0 0 2 * * *", zone = "UTC")
public void nightlyReconcile() { ... }

@Async
public CompletableFuture<Report> buildReport() { ... }
```""",
        "- `@Scheduled` is single-threaded by default — long jobs block others.\n- `@Async` return type: `void`, `Future`, or `CompletableFuture`.",
        "- Use ShedLock or Quartz for clustered schedules.\n- Size thread pools for `@Async`.",
        [("fixedDelay vs fixedRate?", "Delay = backpressure friendly; rate can overlap if job slower than interval.")],
    ),
    "events-ref": t(
        [
            "Extend `ApplicationEvent` or use record events (Boot 2.2+).",
            "`ApplicationEventPublisher.publishEvent`.",
            "`@TransactionalEventListener(phase = AFTER_COMMIT)` for post-commit side effects.",
        ],
        """| Listener | Timing |
| :--- | :--- |
| `@EventListener` | Synchronous default |
| `@Async` + `@EventListener` | Async handler |
| `@TransactionalEventListener` | After commit / rollback |""",
        """```java
@Service
public class OrderService {
  private final ApplicationEventPublisher events;
  public void complete(Order o) {
    repo.save(o);
    events.publishEvent(new OrderCompletedEvent(o.getId()));
  }
}
```""",
        "- Domain events ≠ Kafka events — use outbox for cross-service.",
        "- Keep listeners idempotent.",
        [("Sync vs async listener?", "Sync in same thread/tx unless @Async — know your transaction boundary.")],
    ),
    "actuator-ref": t(
        [
            "Add `spring-boot-starter-actuator`.",
            "Expose endpoints via `management.endpoints.web.exposure.include`.",
            "K8s: separate liveness vs readiness.",
        ],
        """| Endpoint | Path |
| :--- | :--- |
| health | `/actuator/health` |
| metrics | `/actuator/metrics` |
| prometheus | `/actuator/prometheus` |
| info | `/actuator/info` |

| Probe | Checks |
| :--- | :--- |
| liveness | JVM up — restart if fail |
| readiness | DB/upstream OK — remove from LB |""",
        """```yaml
management:
  endpoints:
    web:
      exposure:
        include: health,info,prometheus
  endpoint:
    health:
      probes:
        enabled: true
```""",
        "- Don't expose all actuator endpoints publicly.\n- Secure with Spring Security or network policy.",
        "- Custom `HealthIndicator` for DB, broker, downstream HTTP.",
        [("Liveness vs readiness?", "Liveness = process alive; readiness = can serve traffic.")],
    ),
    "observability-ref": t(
        [
            "SLF4J + Logback default; config via `logback-spring.xml`.",
            "MDC for trace/correlation IDs.",
            "Micrometer → Prometheus / OTLP.",
        ],
        """| Concern | Tool |
| :--- | :--- |
| Logs | Logback JSON appenders |
| Correlation | MDC `traceId` |
| Metrics | Micrometer counters/timers |
| Traces | Micrometer tracing / OTel |
| Dashboards | Grafana + Prometheus |""",
        """```java
// MDC in filter
MDC.put("traceId", traceId);
try { chain.doFilter(req, res); }
finally { MDC.clear(); }
```""",
        "- Clear MDC in `finally` — thread pool leaks context.\n- Don't log PII/secrets.",
        "- Structured JSON logs in prod.\n- RED/USE metrics for services.",
        [("Metrics vs logs vs traces?", "Metrics = aggregates; logs = events; traces = request path across services.")],
    ),
    "testing-ref": t(
        [
            "Slice tests load partial context — faster than full `@SpringBootTest`.",
            "`@MockBean` replaces bean in test context.",
            "Testcontainers for real Postgres/Kafka.",
        ],
        """| Annotation | Loads |
| :--- | :--- |
| `@WebMvcTest` | MVC layer only |
| `@DataJpaTest` | JPA + in-memory or Testcontainers |
| `@SpringBootTest` | Full application |
| `@MockMvc` | Mock HTTP without server |

| Tool | Use |
| :--- | :--- |
| Mockito | Mock collaborators |
| AssertJ | Fluent assertions |
| Testcontainers | Real infra |""",
        """```java
@WebMvcTest(OrderController.class)
class OrderControllerTest {
  @Autowired MockMvc mvc;
  @MockBean OrderService service;

  @Test void getReturns200() throws Exception {
    when(service.find(1L)).thenReturn(dto);
    mvc.perform(get("/api/orders/1")).andExpect(status().isOk());
  }
}
```""",
        "- `@SpringBootTest(webEnvironment = RANDOM_PORT)` for integration.\n- Don't `@MockBean` the class under test.",
        "- CI: slice tests on every commit; Testcontainers on merge.",
        [("@MockBean vs @Mock?", "@MockBean in Spring context; @Mock in plain unit test.")],
    ),
    "production-deployment-ref": t(
        [
            "Fat JAR via `spring-boot-maven-plugin` / `bootJar`.",
            "Layered JAR for Docker cache.",
            "`server.shutdown=graceful` for K8s preStop.",
        ],
        """| Topic | Setting / pattern |
| :--- | :--- |
| Graceful shutdown | `server.shutdown=graceful` |
| External config | env, ConfigMap, Spring Cloud Config |
| Health probes | actuator health groups |
| JVM in container | respect cgroup memory |
| DevTools | dev scope only |""",
        """```dockerfile
FROM eclipse-temurin:17-jre AS run
COPY target/app.jar /app.jar
ENTRYPOINT ["java","-jar","/app.jar"]
```""",
        "- Thin JAR without repackage won't run.\n- DevTools in prod image causes unexpected restarts.",
        "- 12-factor config: store in environment.\n- Set resource limits matching JVM heap.",
        [("Why layered JAR?", "Docker layer cache — dependencies change less often than app code.")],
    ),
    "spring-cloud-ref": t(
        [
            "Spring Cloud — config, discovery, gateway, resilience on top of Boot.",
            "OpenFeign for declarative HTTP clients.",
            "Resilience4j for circuit breaker / retry / bulkhead.",
        ],
        """| Component | Role |
| :--- | :--- |
| Config Server | Central Git-backed config |
| Eureka / Consul | Service discovery |
| Spring Cloud Gateway | Edge routing, filters |
| OpenFeign | `@FeignClient` REST |
| Resilience4j | `@CircuitBreaker`, `@Retry` |

| Pattern | Annotation |
| :--- | :--- |
| Circuit breaker | `@CircuitBreaker(name, fallbackMethod)` |
| Retry | `@Retry(name)` |
| Bulkhead | `@Bulkhead(name)` |""",
        """```java
@FeignClient(name = "inventory")
public interface InventoryClient {
  @GetMapping("/api/stock/{sku}")
  StockDto getStock(@PathVariable String sku);
}
```""",
        "- Deep distributed patterns → [Microservices Playbook](/microservices/).",
        "- Timeouts on every Feign client.",
        [("Gateway vs BFF?", "Gateway = platform edge; BFF = per-client API aggregation.")],
    ),
    "messaging-ref": t(
        [
            "Kafka: `spring-kafka` + `@KafkaListener`.",
            "RabbitMQ: `spring-amqp` + `@RabbitListener`.",
            "Idempotent consumers + dead-letter for failures.",
        ],
        """| Broker | Send | Receive |
| :--- | :--- | :--- |
| Kafka | `KafkaTemplate.send` | `@KafkaListener` |
| RabbitMQ | `RabbitTemplate` | `@RabbitListener` |

| Setting | Why |
| :--- | :--- |
| `enable.auto.commit=false` | Manual ack after processing |
| consumer group | Horizontal scale |""",
        """```java
@KafkaListener(topics = "orders", groupId = "billing")
public void onOrder(OrderEvent event) { ... }
```""",
        "- Broker internals → [Kafka Handbook](/kafka-handbook/).\n- This page is Spring integration only.",
        "- Serialize with schema registry or versioned JSON.\n- Outbox for reliable publish with DB.",
        [("@KafkaListener concurrency?", "Container concurrency threads per topic partition cap.")],
    ),
    "spring-boot-interview-ref": t(
        [
            "Startup: `SpringApplication.run` → env → context refresh → auto-config → runners → ready.",
            "DispatcherServlet: mapping → adapter → controller → message converter.",
            "Auto-config: `@ConditionalOnClass` + `@ConditionalOnProperty`.",
        ],
        """| Question | Short answer |
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
| Web server | Start embedded container |""",
        "_See linked cheat sheets for snippets._",
        "- Answer with trade-offs in interviews, not definitions only.",
        "- Link bean lifecycle to `@PostConstruct` vs `ApplicationRunner` order.",
        [
            ("How does auto-configuration work?", "Classpath triggers `@Conditional*` classes listed in AutoConfiguration.imports; beans register if conditions match."),
            ("DispatcherServlet role?", "Front controller — maps URL to handler, invokes controller, resolves view/JSON."),
            ("Why constructor injection?", "Immutable deps, testable, explicit contract."),
        ],
    ),
}


def normalize(body: str) -> str:
    body = textwrap.dedent(body)
    body = re.sub(r"\n {8}", "\n", body)
    return body.strip() + "\n"


def main() -> None:
    modules_path = DATA / "spring_boot_modules.yaml"
    with open(modules_path, encoding="utf-8") as f:
        modules = yaml.safe_load(f)["modules"]

    ordered = flatten_topics(modules)
    write_order_yaml(ordered, DATA / "spring_boot_order.yaml")

    missing = [s for s in ordered if s not in TOPIC_META or s not in PAGE_BODIES]
    if missing:
        raise SystemExit(f"Missing meta or body for: {missing}")

    CONTENT.mkdir(parents=True, exist_ok=True)
    written = 0
    for mod_id, mod_title, slug, topic_idx in iter_module_topics(modules):
        see_also = see_also_links(slug, ordered)
        body = page_body(PAGE_BODIES[slug], see_also)
        path = CONTENT / f"{slug}.md"
        path.write_text(front_matter(slug, mod_id, mod_title, topic_idx) + body, encoding="utf-8")
        written += 1
        print(f"Wrote {path.relative_to(ROOT)}")

    keep = {"_index.md"} | {f"{s}.md" for s in ordered}
    deleted = 0
    for path in CONTENT.glob("*.md"):
        if path.name not in keep:
            path.unlink()
            deleted += 1
            print(f"Deleted {path.relative_to(ROOT)}")

    print(f"\nSummary: {written} pages written, {deleted} deleted, {len(ordered)} topics.")


if __name__ == "__main__":
    main()
