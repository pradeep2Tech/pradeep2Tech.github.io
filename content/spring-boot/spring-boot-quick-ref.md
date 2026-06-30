---
title: "Spring Boot Quick Reference"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Starters, bootstrap, run commands, and Boot 2 vs 3 — one-page recap."
tags: ["spring-boot", "spring", "cheatsheet", "handbook"]
categories: ["Spring Boot Cheat Sheet"]
shortTitle: "Quick Ref"
module: 1
moduleTitle: "Bootstrap & Core"
sectionRef: "1.1"
ShowToc: true
cheatSheet: true
---

## At a Glance

- `@SpringBootApplication` = `@Configuration` + `@EnableAutoConfiguration` + `@ComponentScan`.
- Starters pull aligned transitive deps; BOM locks versions.
- Boot 3 requires Java 17 and `jakarta.*`.

---

## Reference Tables

| Area | Boot 2.x | Boot 3.x |
| :--- | :--- | :--- |
| **Java** | 8+ | **17+** required |
| **Namespace** | `javax.*` | **`jakarta.*`** |
| **Security** | `WebSecurityConfigurerAdapter` | `@Bean SecurityFilterChain` |
| **Auto-config index** | `META-INF/spring.factories` | `META-INF/spring/...AutoConfiguration.imports` |

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
| Gradle | `./gradlew bootRun` |

---

## Snippets

```java
@SpringBootApplication
public class App {
  public static void main(String[] args) {
    SpringApplication.run(App.class, args);
  }
}
```

---

## Internals & Gotchas

- Auto-config is conditional — exclude with `@SpringBootApplication(exclude = ...)`.
- DevTools restart only for dev classpath scope.

---

## Production Notes

- Pin Boot version in parent BOM.
- Add actuator from day one.
- Never commit secrets — use env / vault.

---

## Interview Probes


{< interview-answer >}
**Q:** Minimum Java for Boot 3?

**A:** Java 17.
{< /interview-answer >}

{< interview-answer >}
**Q:** What is a starter?

**A:** Curated dependency descriptor + optional auto-config — not one fat library.
{< /interview-answer >}

---

## See Also

- [Next: Annotations](/spring-boot/annotations-stereotypes/)
- [Spring Boot Cheat Sheet Index](/spring-boot/)
- [Java Engineering](/java-engineering/)
- [Microservices Playbook](/microservices/)
