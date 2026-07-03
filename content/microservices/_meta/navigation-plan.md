---
title: "Microservices Architecture Playbook — Navigation Plan"
date: 2026-07-03T15:00:00+00:00
draft: true
description: "Hugo sidebar, yaml, aliases, and cross-link strategy for Phase B."
tags: ["microservices", "meta", "planning"]
---

# Navigation Plan

**Target:** GitHub Pages / Hugo curriculum sidebar via `data/microservices_modules.yaml` and `data/microservices_order.yaml`.

**Constraint:** Preserve Hugo section slug `microservices` (registered in `data/curriculum_sections.yaml`). Restructure content into 12 numbered modules inside `content/microservices/`.

---

## Current Navigation State

| Module | ID | Topics in yaml | In repo |
| :--- | :---: | :---: | :---: |
| Event-Driven Messaging | 1 | 5 | 5 |
| API Boundaries & Fault Tolerance | 2 | 4 | 4 |
| Data Ownership & Persistence | 3 | 5 | 5 |
| Runtime Infrastructure | 4 | 5 | 5 |
| Observability & Mesh | 5 | 6 | 6 |
| Distributed Theory & Quality | 6 | 5 | 5 |

**Sidebar resolution:** `site.GetPage "microservices/<slug>"` — today flat slugs; Phase B uses nested paths (e.g. `05-resilience-patterns/circuit-breaker`).

**Orphan files:** `code-tabs-example.md` (not in yaml).

---

## Proposed Module Structure (Phase B)

```yaml
modules:
  - id: 1
    focus: "Architecture Styles"
    path: "01-architecture-styles"
    topics:
      - 01-architecture-styles/monolith
      - 01-architecture-styles/modular-monolith
      - 01-architecture-styles/microservices
      - 01-architecture-styles/soa

  - id: 2
    focus: "Service Communication"
    path: "02-service-communication"
    topics:
      - 02-service-communication/api-gateway
      - 02-service-communication/bff
      - 02-service-communication/service-discovery
      - 02-service-communication/communication-topologies

  - id: 3
    focus: "Data Management"
    path: "03-data-management"
    topics:
      - 03-data-management/database-per-service
      - 03-data-management/cqrs
      - 03-data-management/event-sourcing
      - 03-data-management/saga
      - 03-data-management/outbox
      - 03-data-management/cdc

  - id: 4
    focus: "Distributed Systems"
    path: "04-distributed-systems"
    topics:
      - 04-distributed-systems/cap-theorem
      - 04-distributed-systems/pacelc
      - 04-distributed-systems/consistent-hashing
      - 04-distributed-systems/concurrency-control

  - id: 5
    focus: "Resilience Patterns"
    path: "05-resilience-patterns"
    topics:
      - 05-resilience-patterns/circuit-breaker
      - 05-resilience-patterns/bulkhead
      - 05-resilience-patterns/retry
      - 05-resilience-patterns/timeout
      - 05-resilience-patterns/fallback

  - id: 6
    focus: "Event-Driven Architecture"
    path: "06-event-driven"
    topics:
      - 06-event-driven/event-driven-architecture
      - 06-event-driven/messaging-patterns
      - 06-event-driven/event-streaming

  - id: 7
    focus: "Platform Patterns"
    path: "07-platform-patterns"
    topics:
      - 07-platform-patterns/sidecar
      - 07-platform-patterns/service-mesh
      - 07-platform-patterns/kubernetes-patterns

  - id: 8
    focus: "Observability"
    path: "08-observability"
    topics:
      - 08-observability/three-pillars-observability
      - 08-observability/metrics
      - 08-observability/logging
      - 08-observability/distributed-tracing

  - id: 9
    focus: "Migration & Modernization"
    path: "09-migration-modernization"
    topics:
      - 09-migration-modernization/strangler-pattern
      - 09-migration-modernization/monolith-decomposition
      - 09-migration-modernization/database-decomposition
      - 09-migration-modernization/zero-downtime-deployments

  - id: 10
    focus: "Production Playbook"
    path: "10-production-playbook"
    topics:
      - 10-production-playbook/scalability-patterns
      - 10-production-playbook/caching-patterns
      - 10-production-playbook/deployment-strategies
      - 10-production-playbook/reliability-engineering

  - id: 11
    focus: "Interview Guide"
    path: "11-interview-guide"
    topics:
      - 11-interview-guide/top-200-microservices-questions
      - 11-interview-guide/architect-questions
      - 11-interview-guide/troubleshooting-questions
      - 11-interview-guide/scalability-questions

  - id: 12
    focus: "Learning Paths"
    path: "12-learning-paths"
    topics:
      - 12-learning-paths/senior-engineer-path
      - 12-learning-paths/lead-engineer-path
      - 12-learning-paths/architect-path
      - 12-learning-paths/interview-revision-path
```

**Total topic pages:** 52 (+ 12 section `_index.md` + handbook `_index.md`)

---

## Recommended Reading Orders

### Architect path (breadth → depth)

1. `01-architecture-styles` → `02-service-communication` → `03-data-management`
2. `04-distributed-systems` → `05-resilience-patterns` → `06-event-driven`
3. `07-platform-patterns` → `08-observability` → `09-migration-modernization`
4. `10-production-playbook` → `11-interview-guide` (revision)

### Interview revision (2-week)

| Week | Modules | Focus sections |
| :--- | :--- | :--- |
| 1 | 01, 03, 04, 05 | Tradeoffs, failure modes, interview questions |
| 2 | 06, 08, 09, 10, 11 | EDA, observability, migration, top-200 drill |

### Troubleshooting on-call

`05-resilience-patterns` → `08-observability` → `10-production-playbook/reliability-engineering` → `11-interview-guide/troubleshooting-questions`

---

## Landing Page (`_index.md`) — Phase B Updates

| Section | Update |
| :--- | :--- |
| Title / positioning | "Microservices Architecture Playbook" — architect handbook, not tutorial |
| Remove | "What is microservices?" beginner table (or compress to 3 bullets) |
| Add | 12-module curriculum table with topic counts |
| Add | Links to `12-learning-paths/*` |
| Add | Cross-handbook map (Kafka, K8s, DB, Technology Playbook) |
| Add | Maintainer link to `_meta/concept-registry.md` (draft) |
| Update | `microservicesTocPageSize` if topic count > 30 |

---

## Section Index Pages (`01-*/\_index.md` … `12-*/\_index.md`)

Each section landing includes:

- Module purpose (2–3 sentences for architects)
- Reading order within module
- Concept map table (topic → one-line outcome)
- Links to canonical pages only
- "See also" cross-module links (≤ 3)

---

## Hugo Aliases (Preserve Existing URLs)

Add to front matter of each migrated page:

```yaml
aliases:
  - /microservices/<legacy-slug>/
```

| Legacy slug | New path |
| :--- | :--- |
| `event-driven-architecture-log-streaming` | `06-event-driven/event-driven-architecture` |
| `point-to-point-message-queues` | `06-event-driven/messaging-patterns` |
| `saga-pattern-distributed-transactions` | `03-data-management/saga` |
| `cqrs-event-sourcing` | `03-data-management/cqrs` |
| `microservices-communication-topologies` | `02-service-communication/communication-topologies` |
| `api-gateway-bff-pattern` | `02-service-communication/api-gateway` |
| `dynamic-service-discovery-registry` | `02-service-communication/service-discovery` |
| `circuit-breaker-pattern` | `05-resilience-patterns/circuit-breaker` |
| `transient-fault-handling-timeouts-retries` | `05-resilience-patterns/retry` |
| `bulkhead-isolation-pattern` | `05-resilience-patterns/bulkhead` |
| `database-per-microservice` | `03-data-management/database-per-service` |
| `monolithic-database-decomposition` | `09-migration-modernization/database-decomposition` |
| `database-replication-scaling` | `10-production-playbook/scalability-patterns` |
| `database-sharding-horizontal-partitioning` | `10-production-playbook/scalability-patterns` |
| `database-isolation-levels-concurrency-control` | `04-distributed-systems/concurrency-control` |
| `application-containerization-docker` | `07-platform-patterns/kubernetes-patterns` |
| `declarative-container-orchestration-kubernetes` | `07-platform-patterns/kubernetes-patterns` |
| `externalized-configuration-management` | `07-platform-patterns/kubernetes-patterns` |
| `zero-downtime-deployment-topologies` | `09-migration-modernization/zero-downtime-deployments` |
| `strangler-fig-application-pattern` | `09-migration-modernization/strangler-pattern` |
| `distributed-tracing-log-aggregation` | `08-observability/distributed-tracing` |
| `three-pillars-observability` | `08-observability/three-pillars-observability` |
| `sidecar-integration-pattern` | `07-platform-patterns/sidecar` |
| `service-mesh-architecture` | `07-platform-patterns/service-mesh` |
| `distributed-rate-limiting-throttling` | `10-production-playbook/scalability-patterns` |
| `distributed-caching-invalidation` | `10-production-playbook/caching-patterns` |
| `consistent-hashing-rings-virtual-nodes` | `04-distributed-systems/consistent-hashing` |
| `consumer-driven-contract-testing-cdct` | `10-production-playbook/reliability-engineering` |
| `cap-theorem-pacelc-framework` | `04-distributed-systems/cap-theorem` |
| `architectural-pragmatist-monolith-vs-microservices` | `01-architecture-styles/microservices` |

**Split pages:** Secondary aliases on companion pages (e.g. `api-gateway-bff-pattern` → also `bff`).

---

## Cross-Link Strategy

### Outbound (from microservices)

| When page mentions… | Link to |
| :--- | :--- |
| Outbox schema, relay tuning | `/database-handbook/transactional-outbox-pattern/` |
| Kafka partitions, consumer groups | `/kafka-handbook/02-kafka/kafka-core/` |
| Broker selection ADR | `/technology-playbook/how-to-choose-message-broker/` or Kafka HB selection |
| Docker, Pods, Services | `/kubernetes-handbook/` |
| Cache implementation | `/system-design/` or Redis HB |
| CRDT deep dive | `/system-design/crdts-and-multi-master-conflict-resolution/` |

### Inbound (to microservices)

Update these handbooks' "See also" in Phase C (optional):

- `database-handbook/transactional-outbox-pattern.md` → link `03-data-management/outbox.md`
- `kafka-handbook/01-fundamentals/messaging-patterns.md` → link `06-event-driven/messaging-patterns.md`
- `technology-playbook/module-architecture-patterns.md` → link playbook `_index.md`

---

## Layout & TOC

| Setting | Value |
| :--- | :--- |
| Layout | Existing `layouts/microservices/` (`curriculum-module-list`, `section-nav`) |
| `ShowPageNums` | `true` on topic pages |
| `playbookVersion` | `3` after architect template migration |
| Collapsible sections | Yes — `.sd-collapsible-content` per `cheatsheet-template.mdc` playbook rules |
| Previous/Next | Driven by `microservices_order.yaml` flat topic list |

---

## `data/` File Changes (Phase B)

1. Replace `microservices_modules.yaml` with 12-module structure above
2. Regenerate `microservices_order.yaml` (~52 topics in reading order)
3. No change to `curriculum_sections.yaml` slug (`microservices` stays)

---

## GitHub Pages Considerations

- All internal links use Hugo paths (`/microservices/05-resilience-patterns/circuit-breaker/`)
- Aliases prevent 404s from bookmarks and external links
- `draft: true` on `_meta/*` — excluded from production build unless `buildDrafts: true`
- Interview pages: no collapsible answers (questions only)

---

**Phase A complete. Yaml and content moves deferred to Phase B.**
