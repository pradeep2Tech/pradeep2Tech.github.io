---
title: "Strangler Fig Pattern"
date: 2026-07-03T15:00:00+00:00
draft: false
description: "Incremental monolith retirement via gateway routing and anti-corruption layers."
tags: ["microservices", "architecture-playbook", "distributed-systems"]
categories: ["Microservices Architecture Playbook"]
shortTitle: "Strangler"
module: 9
moduleTitle: "Migration & Modernization"
sectionRef: "9.1"
weight: 901
playbookVersion: 3
aliases:
  - "/microservices/strangler-fig-application-pattern/"
---

## Executive Summary

The Strangler Fig Application Pattern systematically deconstructs a monolithic codebase by migrating bounded contexts into independent microservices one piece at a time, routing traffic away from legacy systems at the network edge until the monolith is safely phased out.

- **Video Reference:** [Strangler Fig Pattern Explained](https://www.youtube.com/watch?v=xuOJF3w4vQQ)

---

## Architecture Diagram

```mermaid
graph TD
    Client[Client Request] --> AG[API Gateway / Routing Layer]
    AG -->|Path: /api/v2/orders| MS[New Order Microservice]
    AG -->|Path: /api/v1/* Legacy| Mono[Monolith Application]
    MS -->|Anti-Corruption Layer| MonoDB[(Shared Database)]
    Mono --> MonoDB
```

## Internal Working

An API Gateway or reverse proxy (e.g., Envoy, Nginx) sits in front of both the legacy monolith and the new microservices. Traffic is migrated incrementally by updating **path-based routing rules** (e.g., redirecting `/api/v1/orders` to the new service).

When extracting data from a shared database, an **Anti-Corruption Layer (ACL)** is implemented in the new service to translate legacy data structures into clean domain models, protecting the new architecture from legacy tech debt.

### State & Migration Synchronization

If a shared database cannot be split immediately, database-level triggers or **dual-writing** techniques are used to keep data mirrored between old and new tables until the migration is validated.

See also: [API Gateway & BFF Pattern](/microservices/02-service-communication/api-gateway-and-bff/), [Database Per Microservice](/microservices/03-data-management/database-per-service/), and [Monolithic Database Decomposition](/microservices/monolithic-database-decomposition/).

---

### Strangler Migration Phases

| Phase | Routing | Data state | Risk profile |
| :--- | :--- | :--- | :--- |
| **1 — Facade only** | All traffic → monolith | Single shared DB | Low; gateway is pass-through |
| **2 — Read extraction** | New paths for read-heavy domains | Shared DB + ACL translation | LowΓÇômedium; no write split yet |
| **3 — Write extraction** | Writes routed to new service | Dual-write or trigger sync | High; race conditions possible |
| **4 — Data split** | Full domain on microservice | Dedicated per-service DB | Medium; cut over with validation |
| **5 — Decommission** | Monolith paths removed | Legacy DB archived | Low; monolith retired |

---

## Tradeoffs

### Network & Latency

During the migration phase, the system often experiences a **performance penalty**. The new service may need to call back into the monolith to fetch unmigrated data, adding network hops and serialization overhead to previously fast, in-memory function calls.

### Data Consistency

Running a split-state architecture where both the monolith and new services modify related data creates a high risk of **race conditions and data corruption**. This requires clear data ownership boundaries throughout the migration process.

## Common Failures

If the fallback connections between the new microservice and the monolith lack proper circuit breakers, performance degradations in the legacy monolith can easily cascade and bring down the newly migrated microservice.

| Failure Mode | Symptom | Mitigation |
| :--- | :--- | :--- |
| **Monolith callback cascade** | New service 503s when legacy slows | Circuit breakers on ACL/monolith calls |
| **Dual-write divergence** | Old and new tables disagree | Reconciliation job; idempotent sync |
| **Premature path cutover** | Missing data on new service | Feature flags; canary traffic percentage |
| **ACL leakage** | Legacy models pollute new domain | Strict translation boundary; no passthrough |
| **Big-bang rewrite** | Full outage on deploy | Incremental strangler phases only |

---

### Traffic Migration & Rollback Flow

```text
  Feature flag: orders_v2_enabled = 5% canary
        │
        ▼
  API Gateway ──5%──Γû║ Order Microservice (v2)
        │
        └──95%──Γû║ Monolith (v1 legacy)
        │
  Anomaly detected (error rate / latency)
        │
        ▼
  Flip flag → 0% ── instant rollback, no redeploy
```

---

## Interview Questions

### The "Junior" Mistake

Suggesting a **"big bang" migration** where the entire monolith is rewritten from scratch and deployed all at once, which carries an incredibly high risk of project failure in production environments.

### The "Senior" Counter-Measure

Advocate for a disciplined, domain-driven approach using the Strangler Fig Pattern. Start by extracting **simple, read-heavy, or non-critical domains** (such as a notification service) to validate the new infrastructure and CI/CD pipelines before tackling core transaction engines. Use **feature flags** to quickly roll back traffic if any performance anomalies appear.

```text
  Recommended extraction order:
    1. Notifications / email / audit logs     (read-heavy, low risk)
    2. User preferences / static config       (bounded, few dependencies)
    3. Catalog / search                       (read-heavy, cacheable)
    4. Core transactions (orders, payments) (last — highest blast radius)
```

---


---

## Where It Fits

Apply at service boundaries within the microservices fleet. Cross-link to domain handbooks for broker, database, and cache engine internals.

---

## Security Considerations

Apply zero-trust between services, mTLS in mesh, and least-privilege credentials per service identity.

---

## Observability

Export RED metrics, structured logs with `trace_id`, and distributed traces on every cross-service hop. See [Observability](/microservices/08-observability/observability/).

---

## Architect Notes

Expanded from legacy playbook content. See related modules in the curriculum sidebar for adjacent patterns.
