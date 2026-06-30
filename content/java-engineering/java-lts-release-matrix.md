---
title: "Java LTS Release Matrix"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Java 8/11/17/21/25 support timeline, migration checkpoints, and vendor builds."
tags: ["java", "java-engineering", "handbook"]
categories: ["Java Engineering Handbook"]
shortTitle: "LTS Matrix"
module: 9
moduleTitle: "Modern Java"
sectionRef: "9.1"
ShowToc: true
cheatSheet: true
---

## At a Glance

- LTS releases: 8, 11, 17, 21, 25 — extended vendor support windows.
- Non-LTS (6-month): feature releases — production only if you own upgrade cadence.
- Migration path: bytecode usually forward-compatible; watch removed APIs and strong encapsulation.
- Vendor builds (Temurin, Corretto, Oracle) share OpenJDK core with support deltas.

---

## Reference Tables

| LTS | GA | Highlights | Typical EOL (vendor-dependent) |
| :---: | :--- | :--- | :--- |
| 8 | 2014 | Lambdas, streams, Optional | Extended support offerings |
| 11 | 2018 | HTTP client, var in lambda, removal of JavaEE modules | 2026+ depending vendor |
| 17 | 2021 | Sealed, records, strong encapsulation | Long-term |
| 21 | 2023 | Virtual threads, sequenced collections, pattern matching mature | Long-term |
| 25 | 2025 | Next LTS baseline features | TBD |

| Migration checkpoint | Action |
| :--- | :--- |
| 8 → 11 | Remove JAXB/JAX-WS if on classpath; `var` optional |
| 11 → 17 | Strong encapsulation — `--add-opens` audit; records/sealed |
| 17 → 21 | Virtual threads pilot; prepare pinning monitors |
| Any | Run `jdeps`, `jdeprscan`, integration tests on target JDK |

| Build tool | JDK support |
| :--- | :--- |
| Maven compiler release | `-release 17` |
| Gradle toolchain | `java.toolchain.languageVersion` |
| Runtime vs compile | CI matrix both |

---

## Snippets

```xml
<!-- Maven -->
<release>21</release>
```
```gradle
java { toolchain { languageVersion = JavaLanguageVersion.of(21) } }
```

---

## Internals & Gotchas

- LTS cadence shifted: 21 LTS after 17; 25 continues 3-year pattern post-Oracle announcement.
- Preview features require `--enable-preview` — not for prod without plan.
- `javac --release` sets API and bytecode level.

---

## Production Notes

- Pin CI and prod to same major LTS; automate CVE image rebuilds.
- Maintain SBOM with JDK distribution provenance.
- Test on target JDK in staging minimum 2 weeks before prod cutover.

---

## Interview Probes


{< interview-answer >}
**Q:** Why LTS for enterprises?

**A:** Predictable support, vendor patches, slower change absorption — aligns with compliance and long maintenance contracts.
{< /interview-answer >}

{< interview-answer >}
**Q:** release vs target vs source?

**A:** `--release N` sets bytecode + API surface; `target` alone doesn't limit APIs; prefer `release` for reproducible builds.
{< /interview-answer >}

---

## See Also

- [Previous: JVM Flags](/java-engineering/jvm-flags-and-tuning/)
- [Next: Recent Features](/java-engineering/java-recent-features/)
- [Recent Features](/java-engineering/java-recent-features/)
- [Version Features](/java-engineering/java-version-features-interview/)
- [Java Engineering Handbook Index](/java-engineering/)
