"""Spring Boot Handbook content — interview-focused pages for senior engineers."""
from __future__ import annotations

DATE = "2026-06-30T10:00:00+00:00"
SECTION = "spring-boot"
SECTION_TITLE = "Spring Boot Handbook"


def fm(
    title: str,
    desc: str,
    short: str,
    module: int,
    module_title: str,
    section: str,
    aliases: list[str] | None = None,
) -> str:
    lines = [
        "---",
        f'title: "{title}"',
        f"date: {DATE}",
        "draft: false",
        f'description: "{desc}"',
        'tags: ["spring-boot", "spring", "handbook", "interview"]',
        f'categories: ["{SECTION_TITLE}"]',
        f'shortTitle: "{short}"',
        f"module: {module}",
        f'moduleTitle: "{module_title}"',
        f'sectionRef: "{section}"',
        "ShowToc: true",
        "interviewHandbook: true",
    ]
    if aliases:
        lines.append("aliases:")
        for a in aliases:
            lines.append(f"  - {a}")
    lines.append("---")
    return "\n".join(lines) + "\n\n"


def q(
    title: str,
    difficulty: str,
    time: str,
    short: str,
    detail: str,
    internal: str = "",
    production: str = "",
    mistakes: str = "",
    followups: list[str] | None = None,
) -> str:
    parts = [
        f"## {title}",
        "",
        f"**Difficulty:** {difficulty}  ",
        f"**Expected Answer Time:** {time}",
        "",
        "### Short Answer",
        "",
        short,
        "",
        "### Detailed Explanation",
        "",
        detail,
    ]
    if internal:
        parts.extend(["", "### Internal Working", "", internal])
    if production:
        parts.extend(["", "### Production Notes", "", production])
    if mistakes:
        parts.extend(["", "### Common Mistakes", "", mistakes])
    if followups:
        parts.extend(["", "### Follow-up Questions", ""])
        parts.extend(f"- {f}" for f in followups)
    parts.extend(["", "---", ""])
    return "\n".join(parts)


PAGES: dict[str, str] = {}

# =============================================================================
# 1. STARTUP & INTERNALS
# =============================================================================
PAGES["startup-and-internals"] = fm(
    "Startup & Internals",
    "SpringApplication.run, auto-configuration, component scan, bean lifecycle, IoC, and DI — architect deep dive.",
    "Startup",
    1, "Startup & Internals", "1.1",
    aliases=["spring-boot-quick-ref", "annotations-stereotypes", "dependency-injection-ref", "spring-boot-interview-ref"],
) + q(
    "How does Spring Boot startup work?",
    "Hard", "3 min",
    "`SpringApplication.run` builds an `ApplicationContext`, loads environment, applies auto-configuration, refreshes beans, starts embedded web server, then runs `ApplicationRunner`/`CommandLineRunner`.",
    "Phases: (1) create `SpringApplication` — infer web app type, load `ApplicationContextInitializer` and `ApplicationListener`; (2) `prepareEnvironment` — property sources, profiles; (3) `printBanner`; (4) `createApplicationContext`; (5) `prepareContext` — post-processors, `ApplicationArguments` bean; (6) `refresh` — bean definition loading, `BeanFactoryPostProcessor`, bean instantiation; (7) `callRunners`; (8) publish `ApplicationReadyEvent`. Fail-fast on missing beans or circular dependencies.",
    "```mermaid\nflowchart TD\n  run[SpringApplication.run] --> env[prepareEnvironment]\n  env --> ctx[createApplicationContext]\n  ctx --> refresh[context.refresh]\n  refresh --> ac[AutoConfiguration]\n  refresh --> beans[Bean instantiation]\n  beans --> web[Start embedded server]\n  web --> ready[ApplicationReadyEvent]\n```\n\nAuto-config classes load from `META-INF/spring/org.springframework.boot.autoconfigure.AutoConfiguration.imports` (Boot 3). Each `@AutoConfiguration` class uses `@ConditionalOnClass`, `@ConditionalOnProperty`, `@ConditionalOnMissingBean` to register beans only when classpath and config match.",
    "Use `spring-boot-starter-actuator` + `startup` endpoint to profile slow auto-config. Exclude unused auto-config (`@SpringBootApplication(exclude = ...)`) to cut startup time in lambdas/scale-to-zero.",
    "Assuming startup is instant — cold start matters for K8s HPA and serverless. Ignoring `ApplicationContext` refresh failures buried in nested causes.",
    followups=["What runs first — `@PostConstruct` or `ApplicationRunner`?", "How does lazy initialization affect startup?"],
) + q(
    "How does auto-configuration work?",
    "Hard", "3 min",
    "Classpath-triggered conditional `@Configuration` classes register beans when `@Conditional*` predicates pass; user `@Bean` wins via `@ConditionalOnMissingBean`.",
    "Spring Boot imports hundreds of auto-config entries. Each class is a `@Configuration` guarded by conditions: e.g. `DataSourceAutoConfiguration` requires JDBC on classpath and no existing `DataSource` bean. Ordering uses `@AutoConfigureBefore` / `@AutoConfigureAfter`. Debugging: `--debug` logs positive/negative matches. Custom starters ship their own `AutoConfiguration.imports`.",
    "Boot 2 used `META-INF/spring.factories`; Boot 3 uses `AutoConfiguration.imports` — faster, no duplicate parsing. `spring.autoconfigure.exclude` property disables entries globally.",
    "Trim starters — each pulls transitive auto-config. Use `spring-context-indexer` for large apps.",
    "Thinking auto-config replaces understanding bean wiring. Using `@ComponentScan` on wrong package and wondering why beans missing.",
    followups=["Difference between `@Import` and auto-config?", "How to write a custom starter?"],
) + q(
    "Explain the Spring bean lifecycle.",
    "Medium", "1 min",
    "Instantiation → dependency injection → `BeanPostProcessor` before → `@PostConstruct` / `InitializingBean` → BPP after → bean ready → `@PreDestroy` / `DisposableBean` on shutdown.",
    "Singleton beans created during context refresh (unless `@Lazy`). Prototype beans created per `getBean` / injection point. `BeanPostProcessor` can wrap beans in proxies (AOP, `@Transactional`). `SmartLifecycle` beans start/stop with context. Graceful shutdown invokes destroy callbacks in reverse dependency order.",
    "CGLIB subclasses for `@Configuration` class enhancement — `@Bean` methods intercepted for singleton semantics. `@Scope(\"request\")` beans need scoped proxy when injected into singleton.",
    "Long `@PostConstruct` blocks startup — defer to `ApplicationRunner` or async init. Always implement destroy for resources holding native handles.",
    "Using `@PostConstruct` for remote calls without timeout. Assuming prototype beans are destroyed by container (they are not, except scoped).",
    followups=["When is CGLIB vs JDK proxy used?", "What is `BeanFactoryPostProcessor`?"],
) + q(
    "IoC vs Dependency Injection?",
    "Easy", "30 sec",
    "IoC: container controls object creation and wiring. DI: specific pattern where dependencies are supplied (constructor preferred) rather than looked up.",
    "Inversion of Control means your code doesn't `new` collaborators — the `ApplicationContext` manages lifecycle and graph. DI is how IoC is implemented in Spring: constructor, setter, or field injection. Constructor injection makes dependencies explicit, enables `final` fields, and simplifies unit tests without Spring.",
    "`DefaultListableBeanFactory` holds bean definitions; `AutowiredAnnotationBeanPostProcessor` resolves `@Autowired` / constructor injection points.",
    "Prefer constructor injection; use `@RequiredArgsConstructor` (Lombok) or explicit constructor. One constructor = no `@Autowired` needed.",
    "Field injection in services — untestable without reflection. Service locator anti-pattern inside domain code.",
    followups=["Why does Spring prefer constructor injection since 4.3?", "Circular dependency — how does Spring resolve it?"],
) + q(
    "Constructor vs field injection?",
    "Easy", "30 sec",
    "Constructor: immutable, required deps, testable. Field: legacy, hides dependencies, needs Spring test context or reflection.",
    "Constructor injection documents required dependencies in the signature. Optional dependencies: `@Autowired(required = false)` on setter or `ObjectProvider<T>`. For many optional deps, constructor with `ObjectProvider` avoids null checks.",
    "Single constructor auto-wired since Spring 4.3. Kotlin primary constructor supported.",
    "Never `@Autowired` fields in new code. Use package-private constructor + `@Test` direct instantiation.",
    "Mixing field and constructor injection on same class.",
    followups=["What is `ObjectProvider`?", "How to inject `List<Strategy>` of all implementations?"],
) + q(
    "@Primary vs @Qualifier?",
    "Medium", "1 min",
    "`@Primary`: default bean when multiple candidates share a type. `@Qualifier`: select by name or custom qualifier annotation.",
    "When two `PaymentGateway` beans exist, injection point without qualifier fails unless one is `@Primary`. `@Qualifier(\"stripe\")` or custom `@interface StripeGateway` disambiguates. Prefer qualifier annotations over string names for refactor safety.",
    "Resolution order: exact type match → `@Qualifier` → `@Primary` → bean name match by parameter name (with `-parameters` compiler flag).",
    "Document `@Primary` usage — surprising default in large codebases. Prefer interface segregation over many qualifiers.",
    "Two `@Primary` beans of same type — startup failure.",
    followups=["What is `@Resource`?", "How does `@ConditionalOnMissingBean` interact with custom beans?"],
) + q(
    "How does component scan work?",
    "Medium", "1 min",
    "`@ComponentScan` registers `@Component`, `@Service`, `@Repository`, `@Controller`, `@Configuration` in base packages; `@SpringBootApplication` scans the declaring class package by default.",
    "Classpath scanning uses ASM to read class metadata without loading classes. Filters: `@ComponentScan(excludeFilters = ...)`. `@SpringBootApplication` = `@Configuration` + `@EnableAutoConfiguration` + `@ComponentScan` on self package — moving main class changes scan root.",
    "`@Indexed` + `spring-context-indexer` generates `META-INF/spring.components` for faster startup.",
    "Explicit `@ComponentScan(\"com.acme.app\")` when main class is in parent package. Don't scan entire corporate root — pulls accidental beans.",
    "Placing `@SpringBootApplication` in `com.acme` but code in `com.acme.orders` — beans not found.",
    followups=["Difference between `@Bean` and `@Component`?", "Can you scan without annotations?"],
)

# =============================================================================
# 2. CONFIGURATION
# =============================================================================
PAGES["configuration"] = fm(
    "Configuration",
    "Property resolution order, profiles, @Value vs @ConfigurationProperties — production config patterns.",
    "Config",
    2, "Configuration", "2.1",
    aliases=["configuration-ref"],
) + q(
    "What is the Spring Boot property resolution order?",
    "Medium", "1 min",
    "Later sources override earlier: default properties → `@PropertySource` → config data (application.yml) → profile-specific files → env vars → system properties → command-line args.",
    "Spring Boot 2.4+ uses `configtree:` and `spring.config.import` for optional remote config. Relaxed binding maps `my.service-url` ↔ `MY_SERVICE_URL` ↔ `my.serviceUrl`. `spring.application.json` env var injects JSON tree. Kubernetes downward API mounts as env or files.",
    "`ConfigDataEnvironment` loads `application.properties|yml`, then `application-{profile}.*`, then imports. `@ConfigurationProperties` beans bind after environment prepared.",
    "Document required env vars in README/runbook. Validate at startup with `@Validated` + JSR-303 on properties class — fail fast.",
    "Secrets in `application-prod.yml` in git. Assuming profile-specific file overrides env (env wins over files).",
    followups=["What is `spring.config.import`?", "How does Cloud Config Server fit?"],
) + q(
    "How do Spring profiles work?",
    "Easy", "30 sec",
    "Profiles tag beans and config; activate via `spring.profiles.active`, env, or `@ActiveProfiles` in tests.",
    "`application-dev.yml` loads when `dev` profile active. `@Profile(\"dev\")` on `@Bean` or `@Configuration` registers conditionally. Multiple profiles: `prod,metrics`. Default profile via `spring.profiles.default`. Profile groups (Boot 2.4+): `spring.profiles.group.prod=proddb,prodcache`.",
    "`Environment.acceptsProfiles` / `@Profile` use `Profiles` API. Inactive profile beans are not registered — not just disabled.",
    "Use `prod` not `production` consistently across fleet. Never enable `dev` profile in production images.",
    "`@Profile` on `@Entity` — causes subtle missing table errors.",
    followups=["Profile vs property `app.feature.enabled`?", "How to test multiple profiles?"],
) + q(
    "@Value vs @ConfigurationProperties?",
    "Medium", "1 min",
    "`@Value`: single SpEL property, good for one-offs. `@ConfigurationProperties`: type-safe prefix binding, validation, lists, nested objects.",
    "`@Value(\"${app.timeout:30}\")` embeds in fields — hard to test, no bulk validation. `@ConfigurationProperties(prefix = \"app\")` on record/class binds tree; supports `ignoreUnknownFields`, `conversionService`. Enable via `@EnableConfigurationProperties` or `@ConfigurationPropertiesScan`.",
    "Binding uses JavaBeans conventions or constructor binding (immutable records). `Binder` API under the hood.",
    "Use records for immutable config. `@Validated` + `@NotNull` on properties class.",
    "Dozens of `@Value` scattered — unmaintainable. SpEL in `@Value` executing arbitrary code in prod config.",
    followups=["Relaxed binding examples?", "How to bind `Map<String, Duration>`?"],
)

# =============================================================================
# 3. REST API DESIGN
# =============================================================================
PAGES["rest-api-design"] = fm(
    "REST API Design",
    "Validation, exception handling, versioning, idempotency, pagination — senior API design.",
    "REST API",
    3, "REST API Design", "3.1",
    aliases=["rest-api-ref", "validation-ref", "exception-handling-ref"],
) + q(
    "PUT vs PATCH?",
    "Easy", "30 sec",
    "PUT replaces entire resource (idempotent). PATCH applies partial update (idempotent if designed with replace semantics).",
    "PUT missing fields may null out columns if mapped naively. PATCH with JSON Merge Patch or JSON Patch — document contract. Spring: `@PutMapping` full DTO; `@PatchMapping` with `Map` or dedicated patch DTO + validation groups.",
    "`HttpMessageConverter` deserializes body; partial update often needs custom service logic or `@DynamicUpdate` on entity.",
    "Expose PATCH only with clear schema. Use ETags for optimistic concurrency on both.",
    "Using entity as `@RequestBody` — leaks persistence model.",
    followups=["Idempotency keys for POST?", "How to implement conditional updates?"],
) + q(
    "API versioning strategies?",
    "Medium", "1 min",
    "URI path (`/v1/`), header (`Accept-Version`), query param, or content negotiation — pick one and stick to it.",
    "URI versioning is most visible and cache-friendly. Header versioning keeps URLs clean but harder to test in browser. Deprecation: `Sunset` header + metrics on old version traffic. Spring: separate controller packages or `@RequestMapping(\"/api/v1\")`.",
    "DispatcherServlet maps to handler via `RequestMappingHandlerMapping`. Version rarely needs separate DispatcherServlet.",
    "Never break v1 silently. Maintain N-1 version minimum for public APIs.",
    "Mixing versioning styles across teams.",
    followups=["How to deprecate an endpoint?", "OpenAPI multi-version docs?"],
) + q(
    "Validation best practices?",
    "Medium", "1 min",
    "Validate at API boundary with Jakarta Bean Validation on DTOs; domain invariants in service layer; never trust client-only validation.",
    "`@Valid` on `@RequestBody` triggers `MethodArgumentNotValidException`. Groups: `@Validated(Update.class)` for PATCH vs POST rules. Custom: `@Constraint` + `ConstraintValidator`. Method-level: `@Validated` on service + `@NotNull` on params.",
    "Hibernate Validator runs constraints via metadata; Boot auto-configures `LocalValidatorFactoryBean`.",
    "Return field-level errors in RFC 7807 `ProblemDetail` extensions. Don't expose stack traces.",
    "Missing `@Valid` — constraints silently skipped. Validating entities with lazy associations — triggers N+1.",
    followups=["Programmatic validation without annotations?", "Cross-field validation?"],
) + q(
    "Global exception handling?",
    "Medium", "1 min",
    "`@RestControllerAdvice` + `@ExceptionHandler` centralizes error mapping to stable HTTP status + body.",
    "Boot 3 `ProblemDetail` implements RFC 7807. Map `MethodArgumentNotValidException` → 400 with field errors; business `NotFoundException` → 404; `AccessDeniedException` → 403. Order matters — most specific handler wins. `@ControllerAdvice` without `ResponseBody` needs `@ResponseBody` per method.",
    "Exception handlers resolved by `ExceptionHandlerExceptionResolver`. Can use `@Hidden` on handlers for OpenAPI.",
    "Include correlation ID from MDC in response `instance` or custom property. Log full detail server-side only.",
    "Catch-all `Exception` → 500 with message leaking internals. Returning 200 with error envelope.",
    followups=["ProblemDetail vs custom error DTO?", "How to handle validation on `@RequestParam`?"],
) + q(
    "Pagination and error response design?",
    "Medium", "1 min",
    "Use `Pageable` + `Page<T>`; return consistent envelope with `content`, `totalElements`, `links`; errors use stable machine-readable codes.",
    "Spring Data: `PageRequest.of(page, size, Sort)`. HATEOAS optional. Error body: `type`, `title`, `status`, `detail`, `code`, `traceId`. Never expose SQL or stack in prod.",
    "`PageableHandlerMethodArgumentResolver` binds query params `page`, `size`, `sort`.",
    "Cap `size` max (e.g. 100) to prevent abuse. Index-friendly sort columns.",
    "Unbounded `findAll()` on large tables.",
    followups=["Cursor-based vs offset pagination?", "How to add HATEOAS links?"],
)

# =============================================================================
# 4. DATA & TRANSACTIONS
# =============================================================================
PAGES["data-and-transactions"] = fm(
    "Data & Transactions",
    "@Transactional internals, JPA, N+1, locking, caches — production data layer.",
    "Data & TX",
    4, "Data & Transactions", "4.1",
    aliases=["jpa-quick-ref", "jpa-queries-ref", "transactions-ref"],
) + q(
    "How does @Transactional work?",
    "Hard", "3 min",
    "Spring creates a JDK or CGLIB proxy around the bean; `TransactionInterceptor` opens/commits/rolls back a `PlatformTransactionManager` transaction around the method.",
    "At startup, `InfrastructureAdvisorAutoProxyCreator` wraps `@Transactional` beans. On invoke: `TransactionAspectSupport` gets transaction attribute (propagation, isolation, timeout), calls `transactionManager.getTransaction()`, proceeds, commits or rolls back on exception policy. Default: `PROPAGATION_REQUIRED`, rollback on unchecked exceptions only.",
    "```mermaid\nsequenceDiagram\n  Client->>Proxy: call service.method()\n  Proxy->>TxInterceptor: invoke\n  TxInterceptor->>TxManager: begin\n  TxInterceptor->>Target: method()\n  TxInterceptor->>TxManager: commit/rollback\n```\n\nSelf-invocation (`this.method()`) bypasses proxy — no transaction. Fix: inject self, move to another bean, or `AopContext.currentProxy()`.",
    "Keep transactions short — no HTTP calls inside. Use `readOnly=true` on queries for Hibernate optimization hint.",
    "`@Transactional` on controller — wrong layer. `@Transactional` on private method — ignored (proxy doesn't intercept).",
    followups=["Which TransactionManager for JPA?", "How does rollbackFor work?"],
) + q(
    "What is the N+1 problem?",
    "Hard", "3 min",
    "One query loads N parent rows; lazy loading triggers N additional queries when accessing each child collection.",
    "Occurs with `FetchType.LAZY` and iterating associations in service or (worse) open session in view. Fixes: `JOIN FETCH` in JPQL, `@EntityGraph`, DTO projection (`@Query` constructor expression), `batch_size` hint, or `hibernate.default_batch_fetch_size`.",
    "Hibernate Session first-level cache deduplicates within persistence context. Second-level cache (EhCache, Redis via Hibernate) caches entity data across sessions — requires careful invalidation.",
    "Set `spring.jpa.open-in-view=false` in production. Use `@Transactional(readOnly=true)` on read services.",
    "Enabling OSIV to 'fix' LazyInitializationException in controllers. Eager fetch everything — cartesian product explosions.",
    followups=["Explain first-level vs second-level cache?", "When is `@Modifying` required?"],
) + q(
    "Lazy vs Eager loading?",
    "Medium", "1 min",
    "Lazy (default for collections): load on access within session. Eager: load immediately with parent — risks over-fetching.",
    "`@ManyToOne` defaults EAGER in JPA spec (Hibernate same) — often change to LAZY explicitly. Lazy requires active persistence context or join fetch in query.",
    "Lazy collections use bytecode enhancement or `PersistentBag` placeholders.",
    "Default LAZY on `@OneToMany`. Fetch joins in repository for known access paths.",
    "Serializing lazy entities to JSON — triggers lazy load or `LazyInitializationException`.",
    followups=["Bytecode enhancement?", "DTO vs entity in API?"],
) + q(
    "Optimistic vs pessimistic locking?",
    "Medium", "1 min",
    "Optimistic: `@Version` column — detect conflict at flush. Pessimistic: DB row/page lock via `@Lock(LockModeType.PESSIMISTIC_WRITE)`.",
    "Optimistic suits low contention — `OptimisticLockException` on stale version. Pessimistic: `SELECT FOR UPDATE` — deadlocks possible, holds DB connections. `PESSIMISTIC_READ` vs `WRITE` depends on DB.",
    "Spring Data: `@Lock` on query method. Timeout via `javax.persistence.lock.timeout` hint.",
    "Retry optimistic conflicts with exponential backoff. Use pessimistic for financial debit/credit short transactions.",
    "No version field on hot concurrent entity. Long-held pessimistic locks under load.",
    followups=["What is SKIP LOCKED?", "Saga vs local transaction?"],
) + q(
    "Transaction propagation and isolation?",
    "Hard", "3 min",
    "Propagation defines how methods join existing TX (`REQUIRED`, `REQUIRES_NEW`, `NESTED`, etc.). Isolation maps to JDBC isolation levels.",
    "`REQUIRES_NEW` suspends outer TX — use for audit log that must commit independently. `NESTED` uses savepoints — not all drivers support. Isolation: `READ_COMMITTED` default on PostgreSQL; `REPEATABLE_READ` prevents non-repeatable reads; `SERIALIZABLE` strongest, most contention.",
    "`AbstractPlatformTransactionManager` delegates to `Connection.setTransactionIsolation`.",
    "Match isolation to business — don't default SERIALIZABLE. `readOnly=true` doesn't guarantee read replica routing without extra config.",
    "Nested `@Transactional` with wrong propagation causing partial commits. Remote calls inside REQUIRED transaction.",
    followups=["Does `@Transactional` work on self call?", "Distributed transactions without 2PC?"],
) + q(
    "Query optimization in Spring Data JPA?",
    "Medium", "1 min",
    "Derived queries for simple paths; `@Query` JPQL for explicit joins; projections for read models; pagination at DB; indexes on filter/sort columns.",
    "Native SQL for CTEs/window functions — bypasses change tracking. `@EntityGraph` on `findById`. Specifications for dynamic predicates. Hibernate statistics or `datasource-proxy` for slow query detection.",
    "Query derivation parsed into `PartTreeJpaQuery`.",
    "Explain analyze in staging. Avoid `select *` entity loads when 2 columns needed.",
    "`findAll()` without pagination. Native query returning entities with wrong column order.",
    followups=["Blaze Persistence?", "When native over JPQL?"],
)

# =============================================================================
# 5. SECURITY
# =============================================================================
PAGES["security"] = fm(
    "Security",
    "SecurityFilterChain, JWT validation, method security, RBAC — Boot 3 security architecture.",
    "Security",
    5, "Security", "5.1",
    aliases=["security-quick-ref", "jwt-oauth-ref"],
) + q(
    "Explain the Spring Security filter chain.",
    "Hard", "3 min",
    "A chain of `Filter` beans runs before `DispatcherServlet`; `SecurityFilterChain` `@Bean` configures `HttpSecurity` — authn, authz, CSRF, headers, OAuth2 resource server.",
    "Boot 3: no `WebSecurityConfigurerAdapter`. Multiple chains possible with `@Order`. Key filters: `SecurityContextHolderFilter`, `LogoutFilter`, `BearerTokenAuthenticationFilter` (JWT), `AuthorizationFilter`. `SecurityContext` stored in `ThreadLocal` (or `SecurityContextHolderStrategy` for reactive).",
    "```mermaid\nflowchart LR\n  req[HTTP Request] --> sec[Security Filters]\n  sec --> auth[Authentication]\n  auth --> authz[Authorization]\n  authz --> mvc[DispatcherServlet]\n```",
    "Permit `/actuator/health` explicitly. Separate chain for actuator with mTLS or IP allowlist.",
    "Disabling CSRF on session cookies without understanding risk. `permitAll()` on `/**` by mistake.",
    followups=["Filter order customization?", "SecurityContext in async threads?"],
) + q(
    "Authentication vs Authorization?",
    "Easy", "30 sec",
    "Authentication: who you are (`Authentication` principal). Authorization: what you're allowed (`AccessDecisionManager`, `@PreAuthorize`).",
    "Authn produces `Authentication` with credentials and authorities. Authz checks roles/scopes before method or URL access. 401 unauthenticated; 403 authenticated but denied.",
    "`ProviderManager` delegates to `AuthenticationProvider` list.",
    "Don't leak 404 for unauthorized resources if policy requires hiding existence.",
    "Confusing 401 vs 403 in API clients.",
    followups=["How are roles mapped from JWT?", "Method security vs URL security?"],
) + q(
    "JWT validation flow in Spring Boot?",
    "Hard", "3 min",
    "Resource server receives Bearer token → `NimbusJwtDecoder` fetches JWK set from issuer → validates signature, `exp`, `iss`, `aud` → builds `JwtAuthenticationToken`.",
    "Configure `spring.security.oauth2.resourceserver.jwt.issuer-uri` or `jwk-set-uri`. Custom `JwtAuthenticationConverter` maps `scope`/`roles` claims to `GrantedAuthority`. For local validation without network: static public key PEM.",
    "`BearerTokenAuthenticationFilter` extracts token from `Authorization` header.",
    "Short access token TTL; rotate refresh tokens. Validate audience for multi-tenant IdPs. Clock skew tolerance.",
    "Trusting unsigned JWTs. Parsing without signature verification. Logging full token.",
    followups=["Opaque token vs JWT?", "How to propagate JWT to downstream calls?"],
) + q(
    "Method security and RBAC?",
    "Medium", "1 min",
    "`@EnableMethodSecurity` + `@PreAuthorize(\"hasRole('ADMIN')\")` or `@PostAuthorize` enforces fine-grained authz on service methods.",
    "SpEL in annotations — `hasAuthority`, `hasPermission` with custom `PermissionEvaluator`. RBAC: roles in JWT → `ROLE_*` prefix convention. Prefer permission-based over role explosion.",
    "AOP proxy around secured methods — same self-invocation caveat as `@Transactional`.",
    "Deny by default. Centralize role constants. Test security with `@WithMockUser` / `@WithJwt`.",
    "Securing only controllers — service layer callable internally bypasses URL security.",
    followups=["`@PreFilter` for collections?", "OAuth2 scopes vs roles?"],
)

# =============================================================================
# 6. CACHING & PERFORMANCE
# =============================================================================
PAGES["caching-performance"] = fm(
    "Caching & Performance",
    "Cache strategies, Redis, @Async, thread pools, connection pools — performance tuning.",
    "Cache & Perf",
    6, "Caching & Performance", "6.1",
    aliases=["caching-ref", "scheduling-async-ref"],
) + q(
    "Cache Aside vs Write Through?",
    "Medium", "1 min",
    "Cache Aside: app reads cache, on miss loads DB and populates cache; writes go to DB then invalidate cache. Write Through: write to cache and cache synchronously writes to DB.",
    "Spring `@Cacheable` is cache-aside on reads. `@CachePut` updates cache after method. `@CacheEvict` on mutations. Write-through needs custom `CacheWriter` or application logic. Write-behind: async DB write — consistency risk.",
    "AOP proxy intercepts `@Cacheable` — self-invocation bypasses cache.",
    "Redis for distributed; Caffeine for local L1. TTL + jitter against stampede. Don't cache nulls without `unless`.",
    "Caching mutable objects — stale references. No TTL on config data.",
    followups=["Cache stampede mitigation?", "Redis vs Caffeine two-tier?"],
) + q(
    "How does @Async work internally?",
    "Hard", "3 min",
    "`@EnableAsync` registers `AsyncAnnotationBeanPostProcessor` which wraps `@Async` methods to submit `Runnable`/`Callable` to `TaskExecutor` instead of running on caller thread.",
    "Default executor: `SimpleAsyncTaskExecutor` (new thread per task — dangerous in prod). Provide `@Bean TaskExecutor` with bounded pool. Return `CompletableFuture` for composition. Exception handling: `AsyncUncaughtExceptionHandler`.",
    "Proxy-based — public methods only. `SecurityContext` and `MDC` don't propagate unless `TaskDecorator` configured.",
    "Size pool from metrics: queue depth, rejection count. Use virtual threads (Boot 3.2+) for IO-bound `@Async` with caution on pinning.",
    "Unbounded thread creation. Missing `TaskDecorator` — lost trace IDs.",
    followups=["@Async vs CompletableFuture supplyAsync?", "Virtual thread executor for @Async?"],
) + q(
    "Thread pool sizing for Spring Boot?",
    "Medium", "1 min",
    "Separate pools for HTTP (Tomcat threads), `@Async`, and `@Scheduled`; size from load testing — CPU-bound ≈ cores; blocking IO needs higher or virtual threads.",
    "Tomcat: `server.tomcat.threads.max`. Custom `ThreadPoolTaskExecutor` with `corePoolSize`, `maxPoolSize`, `queueCapacity`, named threads. RejectedExecutionPolicy: `CallerRunsPolicy` for backpressure.",
    "HikariCP pool separate from thread pool — don't conflate.",
    "Monitor pool saturation via Micrometer. Graceful shutdown: `waitForTasksToCompleteOnShutdown`.",
    "One giant pool for everything. `queueCapacity` Integer.MAX_VALUE hiding overload.",
    followups=["Tomcat vs reactive Netty thread model?", "HikariCP pool size formula?"],
) + q(
    "@Scheduled and connection pool tuning?",
    "Medium", "1 min",
    "`@Scheduled` uses single-threaded executor by default — configure `TaskScheduler` pool for parallel jobs. HikariCP: `maximumPoolSize` ≈ concurrent DB users, not thread count.",
    "`fixedDelay` waits after completion; `fixedRate` can overlap. Clustered schedules need ShedLock or Quartz. Hikari: `connectionTimeout`, `maxLifetime` < DB idle timeout, `leakDetectionThreshold` in dev.",
    "Spring Boot auto-configures Hikari when JDBC on classpath.",
    "Don't schedule long jobs on default single thread. Align `maxLifetime` with DB/proxy timeouts.",
    "Pool size = thread count myth. `@Scheduled` blocking all cron jobs.",
    followups=["ShedLock pattern?", "Read replica routing?"],
)

# =============================================================================
# 7. MESSAGING & EVENTS
# =============================================================================
PAGES["messaging-events"] = fm(
    "Messaging & Events",
    "Spring Events, Kafka, RabbitMQ, retry, DLQ, idempotency — integration patterns.",
    "Messaging",
    7, "Messaging & Events", "7.1",
    aliases=["events-ref", "messaging-ref"],
) + q(
    "Spring Application Events vs message broker?",
    "Medium", "1 min",
    "In-process `ApplicationEventPublisher` is synchronous by default within same JVM. Broker (Kafka/RabbitMQ) is cross-service, durable, at-least-once.",
    "`@EventListener` runs in publisher thread unless `@Async`. `@TransactionalEventListener(AFTER_COMMIT)` ensures handlers see committed data. Domain events stay in-process; integration events go to broker.",
    "Events published via `ApplicationEventMulticaster`.",
    "For reliable cross-service publish with DB write, use transactional outbox — see [Microservices Playbook](/microservices/).",
    "Treating in-process events as delivery guarantee across pods.",
    followups=["Outbox pattern?", "Event sourcing vs events?"],
) + q(
    "Kafka vs RabbitMQ in Spring Boot?",
    "Medium", "1 min",
    "Kafka: log, partitioned, replay, high throughput — `spring-kafka`, `@KafkaListener`. RabbitMQ: queue routing, flexible exchanges — `spring-amqp`, `@RabbitListener`.",
    "Kafka consumer groups scale with partitions. Rabbit competing consumers on queue. Spring abstracts template/listener containers; ack mode manual for at-least-once.",
    "`ConcurrentKafkaListenerContainerFactory` sets concurrency ≤ partitions.",
    "Idempotent consumers with business key dedup. DLQ for poison messages. Schema registry for evolution.",
    "Auto-commit before processing completes. No retry backoff — hammering downstream.",
    followups=["Exactly-once semantics?", "When Kafka vs Rabbit?"],
) + q(
    "Retry patterns and DLQ?",
    "Medium", "1 min",
    "Spring Retry / `@Retryable` for transient failures; after max attempts route to DLQ topic/queue for manual inspection.",
    "Kafka: `SeekToCurrentErrorHandler` + `DeadLetterPublishingRecoverer`. Rabbit: `RepublishMessageRecoverer`. Exponential backoff with jitter. Distinguish retryable vs non-retryable exceptions.",
    "Listener container ack after successful processing when manual ack enabled.",
    "Monitor DLQ depth alert. Include original headers + failure reason in DLQ message.",
    "Infinite retry on bad payload. DLQ without replay tooling.",
    followups=["Idempotency key storage?", "Saga vs retry?"],
)

# =============================================================================
# 8. OBSERVABILITY
# =============================================================================
PAGES["observability"] = fm(
    "Observability",
    "Actuator, MDC, correlation IDs, metrics, tracing, Prometheus — production observability.",
    "Observability",
    8, "Observability", "8.1",
    aliases=["actuator-ref", "observability-ref"],
) + q(
    "Correlation IDs and MDC?",
    "Medium", "1 min",
    "Propagate unique request ID in header; store in SLF4J MDC so every log line includes `traceId`/`correlationId`.",
    "Servlet `Filter` or WebMvc `HandlerInterceptor` reads/generates ID, puts in MDC, adds to response header. Clear MDC in `finally` — thread pool reuse leaks context without clear.",
    "Micrometer Tracing (Boot 3) bridges to OpenTelemetry; trace ID aligns with MDC when configured.",
    "Structured JSON logging in prod. Pass correlation ID to `RestTemplate`/`WebClient` downstream headers.",
    "Forgetting MDC clear in async — wrong ID on next request. Logging PII in MDC.",
    followups=["W3C traceparent?", "How does Micrometer Tracing work?"],
) + q(
    "Actuator endpoints and K8s probes?",
    "Medium", "1 min",
    "Actuator exposes `health`, `metrics`, `prometheus`; enable probes via `management.endpoint.health.probes.enabled=true` for separate liveness/readiness.",
    "Liveness: JVM up — restart pod if fails. Readiness: DB/broker checks — remove from service endpoints. Expose only needed endpoints; secure `/actuator` with Security or network policy.",
    "Custom `HealthIndicator` beans contribute to composite health.",
    "Don't put slow external checks on liveness — causes restart loops. Readiness for dependency failures.",
    "Exposing `env` and `beans` publicly.",
    followups=["Custom health groups?", "Startup probe for slow Boot apps?"],
) + q(
    "Metrics and distributed tracing?",
    "Hard", "3 min",
    "Micrometer registers meters → Prometheus scrape or OTLP export. Tracing: spans across HTTP, JDBC, Kafka with trace context propagation.",
    "RED metrics: Rate, Errors, Duration per endpoint. USE for resources. `@Timed` or `Observation` API (Boot 3). Grafana dashboards + alerts on SLO burn rate.",
    "`MeterRegistry` auto-configured; `ObservationRegistry` unifies metrics + traces.",
    "Sample traces in prod (tail sampling). Cardinality control on tags — don't tag userId on metrics.",
    "High-cardinality labels crashing Prometheus. No tracing on async without context propagation.",
    followups=["Which metrics to alert on?", "OpenTelemetry agent vs starter?"],
)

# =============================================================================
# 9. PRODUCTION DEPLOYMENT
# =============================================================================
PAGES["production-deployment"] = fm(
    "Production Deployment",
    "Fat JAR, Docker layers, graceful shutdown, externalized config — production deployment.",
    "Production",
    9, "Production", "9.1",
    aliases=["production-deployment-ref"],
) + q(
    "Graceful shutdown in Spring Boot?",
    "Medium", "1 min",
    "`server.shutdown=graceful` + `spring.lifecycle.timeout-per-shutdown-phase` stops accepting new requests, completes in-flight, then closes context.",
    "K8s `preStop` hook + adequate `terminationGracePeriodSeconds`. Tomcat pauses connector; reactive Netty drains connections. `@PreDestroy` and `SmartLifecycle.stop()` run during shutdown phase.",
    "Shutdown hook registered by `SpringApplication`.",
    "Align K8s probe timeouts with shutdown duration. Drain message listeners before kill.",
    "Immediate SIGKILL without grace — truncated transactions. DevTools in prod image.",
    followups=["Kubernetes preStop sleep?", "How to drain Kafka consumers?"],
) + q(
    "Layered JAR and Docker best practices?",
    "Medium", "1 min",
    "Spring Boot layered JAR splits dependencies, resources, and app code for Docker layer cache; use JRE not JDK in runtime image.",
    "`spring-boot-maven-plugin` `layers.enabled=true`. Dockerfile copies layers separately. Set JVM container flags: `-XX:MaxRAMPercentage`, respect cgroup limits.",
    "Layertools extract in build pipeline.",
    "Multi-stage build; non-root user; read-only root FS where possible.",
    "Fat JAR COPY without layers — slow deploys. JDK image bloat.",
    followups=["CDS/AppCDS for faster startup?", "Native image trade-offs?"],
)

# =============================================================================
# 10. TESTING
# =============================================================================
PAGES["testing"] = fm(
    "Testing",
    "Unit, slice, integration testing, MockMvc, Testcontainers — production testing strategy.",
    "Testing",
    10, "Testing", "10.1",
    aliases=["testing-ref"],
) + q(
    "Unit vs slice vs integration tests?",
    "Medium", "1 min",
    "Unit: plain JUnit + Mockito, no Spring. Slice: partial context (`@WebMvcTest`, `@DataJpaTest`). Integration: `@SpringBootTest` + Testcontainers for real infra.",
    "Slice tests fast — mock collaborators with `@MockBean`. Full integration catches wiring and config errors. Test pyramid: many unit, fewer integration.",
    "`@MockBean` replaces bean in test `ApplicationContext`.",
    "CI: unit on every commit; Testcontainers on merge/main. Reuse containers where possible.",
    "`@SpringBootTest` for everything — slow suite. `@MockBean` on class under test.",
    followups=["@MockBean vs @Mock?", "Testcontainers reuse?"],
) + q(
    "MockMvc testing strategy?",
    "Medium", "1 min",
    "`@WebMvcTest(Controller.class)` loads MVC slice; `MockMvc` performs HTTP without socket — verify status, JSON, security.",
    "`@AutoConfigureMockMvc` on integration test. `SecurityMockMvcRequestPostProcessors.jwt()` for OAuth2. Assert problem detail structure matches production.",
    "Standalone `MockMvcBuilders.standaloneSetup` for pure unit of controller with mocked deps.",
    "Test validation failures (400) and auth (401/403) paths.",
    "Only testing happy path 200.",
    followups=["WebTestClient for WebFlux?", "Contract testing?"],
) + q(
    "Testcontainers in Spring Boot?",
    "Medium", "1 min",
    "`@Testcontainers` + `@Container static PostgreSQLContainer` — dynamic property source wires JDBC URL into Spring context.",
    "`@DynamicPropertySource` registers container host/port. `@ServiceConnection` (Boot 3.1+) auto-configures datasource from container.",
    "Ryuk container manages lifecycle.",
    "Pin image digests in CI. Parallel test classes need isolated containers or shared singleton with care.",
    "Hardcoded localhost ports conflicting.",
    followups=["Embedded DB vs Testcontainers?", "Kafka Testcontainers?"],
)

# =============================================================================
# TOPIC META for build script
# =============================================================================
TOPIC_META: dict[str, tuple[str, str, str]] = {
    "startup-and-internals": (
        "Startup & Internals",
        "Startup",
        "SpringApplication.run, auto-configuration, bean lifecycle, IoC, DI — architect deep dive.",
    ),
    "configuration": (
        "Configuration",
        "Config",
        "Property resolution, profiles, @Value vs @ConfigurationProperties.",
    ),
    "rest-api-design": (
        "REST API Design",
        "REST API",
        "Validation, exceptions, versioning, idempotency, pagination.",
    ),
    "data-and-transactions": (
        "Data & Transactions",
        "Data & TX",
        "@Transactional, JPA, N+1, locking, query optimization.",
    ),
    "security": (
        "Security",
        "Security",
        "SecurityFilterChain, JWT, method security, RBAC.",
    ),
    "caching-performance": (
        "Caching & Performance",
        "Cache & Perf",
        "Cache strategies, Redis, @Async, thread pools.",
    ),
    "messaging-events": (
        "Messaging & Events",
        "Messaging",
        "Spring Events, Kafka, RabbitMQ, retry, DLQ.",
    ),
    "observability": (
        "Observability",
        "Observability",
        "Actuator, MDC, metrics, tracing, Prometheus.",
    ),
    "production-deployment": (
        "Production Deployment",
        "Production",
        "Graceful shutdown, Docker layers, externalized config.",
    ),
    "testing": (
        "Testing",
        "Testing",
        "Slice tests, MockMvc, Testcontainers strategy.",
    ),
    "interview-questions": (
        "100+ Spring Boot Interview Questions",
        "Interview",
        "Categorized index of Spring Boot interview questions with deep-dive links.",
    ),
}

EXTRA_RELATED: dict[str, list[str]] = {
    "startup-and-internals": ["security"],
    "rest-api-design": ["data-and-transactions"],
    "data-and-transactions": ["caching-performance"],
    "security": ["observability"],
    "messaging-events": ["caching-performance"],
    "observability": ["production-deployment"],
    "testing": ["rest-api-design", "data-and-transactions"],
}

# (question, difficulty, topic, slug)
INTERVIEW_INDEX: list[tuple[str, str, str, str]] = [
    # Easy
    ("What does @SpringBootApplication combine?", "Easy", "Startup", "startup-and-internals"),
    ("Default bean scope in Spring?", "Easy", "Startup", "startup-and-internals"),
    ("Constructor vs field injection?", "Easy", "Startup", "startup-and-internals"),
    ("IoC vs DI?", "Easy", "Startup", "startup-and-internals"),
    ("Authentication vs authorization?", "Easy", "Security", "security"),
    ("PUT vs PATCH?", "Easy", "REST", "rest-api-design"),
    ("What is a Spring profile?", "Easy", "Config", "configuration"),
    ("@Value vs @ConfigurationProperties?", "Easy", "Config", "configuration"),
    ("Lazy vs eager JPA loading?", "Easy", "Data", "data-and-transactions"),
    ("What is MockMvc?", "Easy", "Testing", "testing"),
    ("Actuator health endpoint purpose?", "Easy", "Observability", "observability"),
    ("Liveness vs readiness probe?", "Easy", "Observability", "observability"),
    ("Minimum Java for Boot 3?", "Easy", "Startup", "startup-and-internals"),
    ("javax vs jakarta in Boot 3?", "Easy", "Startup", "startup-and-internals"),
    ("What is a starter?", "Easy", "Startup", "startup-and-internals"),
    ("@Service vs @Component?", "Easy", "Startup", "startup-and-internals"),
    ("HTTP 401 vs 403?", "Easy", "Security", "security"),
    ("What is CSRF?", "Easy", "Security", "security"),
    ("Cache Aside pattern?", "Easy", "Performance", "caching-performance"),
    ("@Scheduled fixedDelay vs fixedRate?", "Easy", "Performance", "caching-performance"),
    # Medium
    ("How does Spring Boot startup work?", "Medium", "Startup", "startup-and-internals"),
    ("How does auto-configuration work?", "Medium", "Startup", "startup-and-internals"),
    ("Bean lifecycle phases?", "Medium", "Startup", "startup-and-internals"),
    ("@Primary vs @Qualifier?", "Medium", "Startup", "startup-and-internals"),
    ("Component scan mechanics?", "Medium", "Startup", "startup-and-internals"),
    ("Property resolution order?", "Medium", "Config", "configuration"),
    ("Profile groups in Boot?", "Medium", "Config", "configuration"),
    ("Relaxed binding examples?", "Medium", "Config", "configuration"),
    ("API versioning strategies?", "Medium", "REST", "rest-api-design"),
    ("Global exception handling?", "Medium", "REST", "rest-api-design"),
    ("Validation best practices?", "Medium", "REST", "rest-api-design"),
    ("Pagination in Spring Data?", "Medium", "REST", "rest-api-design"),
    ("Idempotency for POST?", "Medium", "REST", "rest-api-design"),
    ("How does @Transactional work?", "Medium", "Data", "data-and-transactions"),
    ("Transaction propagation types?", "Medium", "Data", "data-and-transactions"),
    ("Self-invocation transaction bug?", "Medium", "Data", "data-and-transactions"),
    ("N+1 problem and fixes?", "Medium", "Data", "data-and-transactions"),
    ("Optimistic vs pessimistic locking?", "Medium", "Data", "data-and-transactions"),
    ("First-level vs second-level cache?", "Medium", "Data", "data-and-transactions"),
    ("open-in-view true or false?", "Medium", "Data", "data-and-transactions"),
    ("SecurityFilterChain in Boot 3?", "Medium", "Security", "security"),
    ("JWT validation flow?", "Medium", "Security", "security"),
    ("Method security @PreAuthorize?", "Medium", "Security", "security"),
    ("Session vs JWT for APIs?", "Medium", "Security", "security"),
    ("@Cacheable internals?", "Medium", "Performance", "caching-performance"),
    ("@Async internals?", "Medium", "Performance", "caching-performance"),
    ("Thread pool sizing?", "Medium", "Performance", "caching-performance"),
    ("HikariCP pool sizing?", "Medium", "Performance", "caching-performance"),
    ("Spring Events vs Kafka?", "Medium", "Messaging", "messaging-events"),
    ("Kafka vs RabbitMQ?", "Medium", "Messaging", "messaging-events"),
    ("Retry and DLQ patterns?", "Medium", "Messaging", "messaging-events"),
    ("Correlation IDs and MDC?", "Medium", "Observability", "observability"),
    ("Micrometer vs Actuator?", "Medium", "Observability", "observability"),
    ("Graceful shutdown config?", "Medium", "Production", "production-deployment"),
    ("Unit vs slice vs integration test?", "Medium", "Testing", "testing"),
    ("@MockBean vs @Mock?", "Medium", "Testing", "testing"),
    ("Testcontainers with Spring Boot?", "Medium", "Testing", "testing"),
    ("DispatcherServlet role?", "Medium", "Startup", "startup-and-internals"),
    ("ProblemDetail RFC 7807?", "Medium", "REST", "rest-api-design"),
    ("Derived query method naming?", "Medium", "Data", "data-and-transactions"),
    ("@Query JPQL vs native?", "Medium", "Data", "data-and-transactions"),
    ("@EntityGraph purpose?", "Medium", "Data", "data-and-transactions"),
    ("PasswordEncoder best practice?", "Medium", "Security", "security"),
    ("OAuth2 resource server setup?", "Medium", "Security", "security"),
    ("Redis cache manager?", "Medium", "Performance", "caching-performance"),
    ("Cache stampede mitigation?", "Medium", "Performance", "caching-performance"),
    ("@TransactionalEventListener?", "Medium", "Messaging", "messaging-events"),
    ("Kafka listener concurrency?", "Medium", "Messaging", "messaging-events"),
    ("Prometheus scrape config?", "Medium", "Observability", "observability"),
    ("Layered JAR for Docker?", "Medium", "Production", "production-deployment"),
    ("@WebMvcTest scope?", "Medium", "Testing", "testing"),
    ("@DataJpaTest scope?", "Medium", "Testing", "testing"),
    # Hard
    ("Auto-config conditional annotations?", "Hard", "Startup", "startup-and-internals"),
    ("BeanPostProcessor vs BeanFactoryPostProcessor?", "Hard", "Startup", "startup-and-internals"),
    ("CGLIB vs JDK dynamic proxy?", "Hard", "Startup", "startup-and-internals"),
    ("Circular dependency resolution?", "Hard", "Startup", "startup-and-internals"),
    ("Transaction isolation levels?", "Hard", "Data", "data-and-transactions"),
    ("REQUIRES_NEW vs NESTED?", "Hard", "Data", "data-and-transactions"),
    ("Hibernate session flush timing?", "Hard", "Data", "data-and-transactions"),
    ("@Modifying query pitfalls?", "Hard", "Data", "data-and-transactions"),
    ("Filter chain order customization?", "Hard", "Security", "security"),
    ("JWT JWK rotation?", "Hard", "Security", "security"),
    ("SecurityContext in async?", "Hard", "Security", "security"),
    ("TaskDecorator for MDC propagation?", "Hard", "Performance", "caching-performance"),
    ("Virtual threads with @Async?", "Hard", "Performance", "caching-performance"),
    ("Exactly-once Kafka consumption?", "Hard", "Messaging", "messaging-events"),
    ("Idempotent message consumer design?", "Hard", "Messaging", "messaging-events"),
    ("Distributed tracing propagation?", "Hard", "Observability", "observability"),
    ("Tail sampling for traces?", "Hard", "Observability", "observability"),
    ("Startup actuator profiling?", "Hard", "Startup", "startup-and-internals"),
    ("ConditionalOnMissingBean semantics?", "Hard", "Startup", "startup-and-internals"),
    ("Multiple SecurityFilterChain beans?", "Hard", "Security", "security"),
    ("SpEL in @PreAuthorize risks?", "Hard", "Security", "security"),
    ("Two-phase cache invalidation?", "Hard", "Performance", "caching-performance"),
    ("Connection leak detection?", "Hard", "Data", "data-and-transactions"),
    ("Specification API dynamic queries?", "Hard", "Data", "data-and-transactions"),
    ("ShedLock for clustered cron?", "Hard", "Performance", "caching-performance"),
    ("Consumer ack modes Kafka?", "Hard", "Messaging", "messaging-events"),
    ("Custom HealthIndicator?", "Hard", "Observability", "observability"),
    ("Observation API Boot 3?", "Hard", "Observability", "observability"),
    ("Native image GraalVM trade-offs?", "Hard", "Production", "production-deployment"),
    # Architect
    ("Design idempotent REST API?", "Architect", "REST", "rest-api-design"),
    ("When local TX vs saga?", "Architect", "Data", "data-and-transactions"),
    ("Multi-tenant config isolation?", "Architect", "Config", "configuration"),
    ("Zero-downtime schema migration?", "Architect", "Data", "data-and-transactions"),
    ("API gateway vs BFF?", "Architect", "REST", "rest-api-design"),
    ("Outbox pattern placement?", "Architect", "Messaging", "messaging-events"),
    ("Event-driven vs request-driven?", "Architect", "Messaging", "messaging-events"),
    ("SLO-driven alerting stack?", "Architect", "Observability", "observability"),
    ("Blue/green vs rolling K8s deploy?", "Architect", "Production", "production-deployment"),
    ("Secrets rotation without restart?", "Architect", "Config", "configuration"),
    ("Rate limiting in Boot service?", "Architect", "REST", "rest-api-design"),
    ("Multi-region active-active data?", "Architect", "Data", "data-and-transactions"),
    ("Service mesh vs library resilience?", "Architect", "Production", "production-deployment"),
    ("CQRS when worth it?", "Architect", "Data", "data-and-transactions"),
    ("Platform logging standard?", "Architect", "Observability", "observability"),
    ("Boot cold start at scale?", "Architect", "Startup", "startup-and-internals"),
    ("Custom starter design?", "Architect", "Startup", "startup-and-internals"),
    ("AuthZ model RBAC vs ABAC?", "Architect", "Security", "security"),
    ("Token propagation service mesh?", "Architect", "Security", "security"),
    ("Cache coherence across pods?", "Architect", "Performance", "caching-performance"),
]


def build_interview_questions_page() -> str:
    body = fm(
        "100+ Spring Boot Interview Questions",
        "Categorized Spring Boot interview questions for senior engineers and architects.",
        "Interview",
        11, "Interview", "11.1",
        aliases=["spring-boot-interview-ref"],
    )
    body += (
        "Curated questions for **6+ year** engineers, tech leads, and architects. "
        "Each links to a deep-dive page.\n\n"
    )
    for level in ("Easy", "Medium", "Hard", "Architect"):
        items = [q for q in INTERVIEW_INDEX if q[1] == level]
        if not items:
            continue
        body += f"## {level}\n\n"
        body += "| # | Question | Topic | Deep Dive |\n"
        body += "| --: | :--- | :--- | :--- |\n"
        for question, _, topic, slug in items:
            num = INTERVIEW_INDEX.index((question, _, topic, slug)) + 1
            title = TOPIC_META[slug][0]
            body += (
                f"| {num} | {question} | {topic} "
                f"| [{title}](/{SECTION}/{slug}/) |\n"
            )
        body += "\n"
    body += "---\n\n## See Also\n\n"
    body += "- [Startup & Internals](/spring-boot/startup-and-internals/)\n"
    body += "- [Microservices Playbook](/microservices/)\n"
    body += "- [Java Engineering](/java-engineering/)\n"
    body += "- [Spring Boot Handbook Index](/spring-boot/)\n"
    return body


PAGES["interview-questions"] = ""  # filled at import tail
PAGES["interview-questions"] = build_interview_questions_page()
