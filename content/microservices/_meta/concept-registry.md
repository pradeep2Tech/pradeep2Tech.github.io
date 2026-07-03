---
title: "Microservices Concept Registry"
date: 2026-07-03T15:00:00+00:00
draft: true
description: "Canonical source mapping — one authoritative page per microservices architecture concept."
tags: ["microservices", "meta", "planning"]
---

# Microservices Concept Registry

**Rule:** Full explanation lives on the canonical page only. All other pages: **≤ 2 sentences** + link.

**Status:** Phase A — registry defined; enforcement in Phase B/C.

**Cross-handbook rule:** Technology selection and broker/DB/cache engine internals are **not** duplicated here — link only.

---

## Architecture Styles

| Concept | Canonical Page | Status | Notes |
| :--- | :--- | :--- | :--- |
| Monolith (single deployable) | `01-architecture-styles/monolith.md` | **Planned** | Split from `architectural-pragmatist-monolith-vs-microservices` |
| Modular monolith | `01-architecture-styles/modular-monolith.md` | **Planned** | Package boundaries, in-process calls |
| Microservices | `01-architecture-styles/microservices.md` | **Planned** | Network boundaries, team autonomy |
| SOA | `01-architecture-styles/soa.md` | **Planned** | ESB era vs modern microservices |
| Monolith vs microservices comparison | `01-architecture-styles/microservices.md` §Tradeoffs | **Planned** | Comparison template sections |
| Conway's Law | `01-architecture-styles/microservices.md` | **Planned** | Move from comparison page |
| When to decompose checklist | `01-architecture-styles/microservices.md` | **Planned** | |

---

## Service Communication

| Concept | Canonical Page | Status | Notes |
| :--- | :--- | :--- | :--- |
| API Gateway | `02-service-communication/api-gateway.md` | **Planned** | Split from `api-gateway-bff-pattern` |
| BFF (Backend for Frontend) | `02-service-communication/bff.md` | **Planned** | Split from `api-gateway-bff-pattern` |
| Service discovery (client-side) | `02-service-communication/service-discovery.md` | **Planned** | From `dynamic-service-discovery-registry` |
| Service discovery (server-side / K8s DNS) | `02-service-communication/service-discovery.md` | **Planned** | Link [K8s Services](/kubernetes-handbook/services/) |
| Sync vs async communication topologies | `02-service-communication/communication-topologies.md` | **Planned** | From `microservices-communication-topologies` |
| gRPC vs REST boundary choice | `02-service-communication/communication-topologies.md` | **Planned** | |
| "Sync for queries, async for commands" | `02-service-communication/communication-topologies.md` | **Planned** | |
| Trace context propagation (HTTP/gRPC) | `02-service-communication/communication-topologies.md` | **Planned** | Link `08-observability/distributed-tracing.md` |

---

## Data Management

| Concept | Canonical Page | Status | Notes |
| :--- | :--- | :--- | :--- |
| Database per service | `03-data-management/database-per-service.md` | **Planned** | From `database-per-microservice` |
| Polyglot persistence (architect view) | `03-data-management/database-per-service.md` | **Planned** | Selection → [Technology Playbook](/technology-playbook/how-to-choose-database/) |
| CQRS | `03-data-management/cqrs.md` | **Planned** | Split from `cqrs-event-sourcing` |
| Event sourcing | `03-data-management/event-sourcing.md` | **Planned** | Split from `cqrs-event-sourcing` |
| Event snapshots & upcasters | `03-data-management/event-sourcing.md` | **Planned** | |
| Saga (orchestration) | `03-data-management/saga.md` | **Planned** | From `saga-pattern-distributed-transactions` |
| Saga (choreography) | `03-data-management/saga.md` | **Planned** | |
| Compensating transactions | `03-data-management/saga.md` | **Planned** | |
| Transactional outbox (architect pattern) | `03-data-management/outbox.md` | **Planned** | Schema/relay → [DB Handbook](/database-handbook/transactional-outbox-pattern/) |
| Change Data Capture (CDC) | `03-data-management/cdc.md` | **Planned** | Extract from EDA + decomposition pages |
| Cross-service reference data replication | `03-data-management/database-per-service.md` | **Planned** | ≤2 sentences; CDC link |
| Reporting / analytics boundary | `03-data-management/database-per-service.md` | **Planned** | Warehouse offload |

---

## Distributed Systems

| Concept | Canonical Page | Status | Notes |
| :--- | :--- | :--- | :--- |
| CAP theorem | `04-distributed-systems/cap-theorem.md` | **Planned** | Split from `cap-theorem-pacelc-framework` |
| PACELC | `04-distributed-systems/pacelc.md` | **Planned** | Split from combined page |
| CP vs AP under partition | `04-distributed-systems/cap-theorem.md` | **Planned** | |
| PC vs EL under normal operation | `04-distributed-systems/pacelc.md` | **Planned** | |
| Domain-driven consistency selection | `04-distributed-systems/pacelc.md` | **Planned** | Ledger vs feed mapping |
| Consistent hashing | `04-distributed-systems/consistent-hashing.md` | **Planned** | From `consistent-hashing-rings-virtual-nodes` |
| Virtual nodes | `04-distributed-systems/consistent-hashing.md` | **Planned** | |
| Sloppy quorum / hinted handoff | `04-distributed-systems/consistent-hashing.md` | **Planned** | |
| MVCC / isolation levels | `04-distributed-systems/concurrency-control.md` | **Planned** | From `database-isolation-levels-concurrency-control` |
| Optimistic vs pessimistic locking | `04-distributed-systems/concurrency-control.md` | **Planned** | |
| Distributed deadlock | `04-distributed-systems/concurrency-control.md` | **Planned** | |
| CRDT / conflict resolution | `04-distributed-systems/cap-theorem.md` | **Planned** | Brief; deep dive → [system-design CRDTs](/system-design/crdts-and-multi-master-conflict-resolution/) |

---

## Resilience Patterns

| Concept | Canonical Page | Status | Notes |
| :--- | :--- | :--- | :--- |
| Circuit breaker | `05-resilience-patterns/circuit-breaker.md` | **Exists** | Migrate from `circuit-breaker-pattern`; template reference |
| Bulkhead | `05-resilience-patterns/bulkhead.md` | **Planned** | From `bulkhead-isolation-pattern` |
| Retry (exponential backoff, jitter) | `05-resilience-patterns/retry.md` | **Planned** | Split from `transient-fault-handling-timeouts-retries` |
| Retry budget | `05-resilience-patterns/retry.md` | **Planned** | |
| Timeout / deadline propagation | `05-resilience-patterns/timeout.md` | **Planned** | Split from combined page |
| Fallback / graceful degradation | `05-resilience-patterns/fallback.md` | **Planned** | **New** — extract from circuit-breaker |
| Idempotent retries (write safety) | `05-resilience-patterns/retry.md` | **Planned** | |
| Resilience stack (breaker + bulkhead + retry) | `05-resilience-patterns/circuit-breaker.md` | **Planned** | Link siblings only |

---

## Event-Driven Architecture

| Concept | Canonical Page | Status | Notes |
| :--- | :--- | :--- | :--- |
| Event-driven architecture (EDA) | `06-event-driven/event-driven-architecture.md` | **Planned** | Trim from `event-driven-architecture-log-streaming` |
| Pub/Sub vs log-based streaming (architect) | `06-event-driven/messaging-patterns.md` | **Planned** | Merge EDA table + point-to-point page |
| Point-to-point / competing consumers | `06-event-driven/messaging-patterns.md` | **Planned** | Broker detail → Kafka HB |
| Idempotent consumer | `06-event-driven/messaging-patterns.md` | **Planned** | |
| Poison message / DLQ | `06-event-driven/messaging-patterns.md` | **Planned** | |
| Consumer lag / backpressure | `06-event-driven/event-streaming.md` | **Planned** | |
| Event streaming patterns (log, replay, ordering) | `06-event-driven/event-streaming.md` | **Planned** | **New**; Kafka internals → Kafka HB |
| Partition key / ordering scope | `06-event-driven/event-streaming.md` | **Planned** | Link [Kafka partitions](/kafka-handbook/02-kafka/kafka-core/) |
| Event-carried state transfer | `06-event-driven/event-driven-architecture.md` | **Planned** | |

---

## Platform Patterns

| Concept | Canonical Page | Status | Notes |
| :--- | :--- | :--- | :--- |
| Sidecar pattern | `07-platform-patterns/sidecar.md` | **Planned** | From `sidecar-integration-pattern` |
| Service mesh (data + control plane) | `07-platform-patterns/service-mesh.md` | **Planned** | From `service-mesh-architecture` |
| mTLS mesh traffic | `07-platform-patterns/service-mesh.md` | **Planned** | Link [Istio](/kubernetes-handbook/istio/) |
| Ambient / eBPF mesh | `07-platform-patterns/service-mesh.md` | **Planned** | |
| Kubernetes patterns for microservices | `07-platform-patterns/kubernetes-patterns.md` | **Planned** | **New** — replaces docker+k8s tutorial pages |
| Externalized configuration | `07-platform-patterns/kubernetes-patterns.md` §Config | **Planned** | Trim from `externalized-configuration-management` |
| Container basics | **External:** [Kubernetes Handbook / Docker](/kubernetes-handbook/docker/) | N/A | Not owned here |

---

## Observability

| Concept | Canonical Page | Status | Notes |
| :--- | :--- | :--- | :--- |
| Three pillars (metrics, logs, traces) | `08-observability/three-pillars-observability.md` | **Planned** | From existing page |
| Distributed tracing | `08-observability/distributed-tracing.md` | **Planned** | Split from `distributed-tracing-log-aggregation` |
| W3C tracecontext / OpenTelemetry | `08-observability/distributed-tracing.md` | **Planned** | Link [OTel K8s](/kubernetes-handbook/opentelemetry/) |
| Structured logging | `08-observability/logging.md` | **Planned** | Split from combined page |
| Log aggregation pipelines | `08-observability/logging.md` | **Planned** | |
| Metrics (RED, USE, golden signals) | `08-observability/metrics.md` | **Planned** | **New** — extract from three-pillars |
| Head vs tail sampling | `08-observability/distributed-tracing.md` | **Planned** | |
| Correlated telemetry (trace_id in logs) | `08-observability/three-pillars-observability.md` | **Planned** | |

---

## Migration & Modernization

| Concept | Canonical Page | Status | Notes |
| :--- | :--- | :--- | :--- |
| Strangler fig pattern | `09-migration-modernization/strangler-pattern.md` | **Planned** | From `strangler-fig-application-pattern` |
| Monolith decomposition (domain) | `09-migration-modernization/monolith-decomposition.md` | **Planned** | **New** |
| Database decomposition | `09-migration-modernization/database-decomposition.md` | **Planned** | From `monolithic-database-decomposition` |
| Zero-downtime deployments | `09-migration-modernization/zero-downtime-deployments.md` | **Planned** | From `zero-downtime-deployment-topologies` |
| Expand-contract schema migration | `09-migration-modernization/zero-downtime-deployments.md` | **Planned** | |
| Anti-corruption layer | `09-migration-modernization/strangler-pattern.md` | **Planned** | |

---

## Production Playbook

| Concept | Canonical Page | Status | Notes |
| :--- | :--- | :--- | :--- |
| Scalability patterns (holistic) | `10-production-playbook/scalability-patterns.md` | **Planned** | **New** — absorb sharding/replication/rate-limit architect angles |
| Horizontal vs vertical scaling | `10-production-playbook/scalability-patterns.md` | **Planned** | |
| Database sharding (architect) | `10-production-playbook/scalability-patterns.md` | **Planned** | Link consistent-hashing + DB handbooks |
| Read replica scaling | `10-production-playbook/scalability-patterns.md` | **Planned** | Brief; link PostgreSQL/MongoDB HB |
| Caching patterns (architect) | `10-production-playbook/caching-patterns.md` | **Planned** | **New** — cache-aside, stampede; impl → Redis HB |
| Distributed rate limiting (ingress) | `10-production-playbook/scalability-patterns.md` | **Planned** | Trim from `distributed-rate-limiting-throttling` |
| Deployment strategies | `10-production-playbook/deployment-strategies.md` | **Planned** | Blue-green, canary, rolling |
| Reliability engineering | `10-production-playbook/reliability-engineering.md` | **Planned** | **New** — SLOs, error budgets, incident response |
| Consumer-driven contract testing | `10-production-playbook/` appendix | **Optional** | From `consumer-driven-contract-testing-cdct` |

---

## Explicitly NOT Owned (Link Only)

| Concept | Owner | Link from |
| :--- | :--- | :--- |
| How to choose database | Technology Playbook | `database-per-service.md` |
| How to choose cache | Technology Playbook | `caching-patterns.md` |
| How to choose message broker | Technology Playbook + Kafka HB | `messaging-patterns.md` |
| Kafka broker internals | Kafka Handbook | `event-streaming.md` |
| Redis implementation | Redis / system-design | `caching-patterns.md` |
| Docker / kubectl primitives | Kubernetes Handbook | `kubernetes-patterns.md` |
| Outbox relay schema tuning | Database Handbook | `outbox.md` |
| Design pattern catalog entries | Design Patterns HB | Optional cross-links |

---

## Legacy Slug → Canonical Mapping (Hugo Aliases)

| Legacy slug | New canonical path |
| :--- | :--- |
| `circuit-breaker-pattern` | `05-resilience-patterns/circuit-breaker` |
| `cap-theorem-pacelc-framework` | `04-distributed-systems/cap-theorem` (+ `pacelc`) |
| `api-gateway-bff-pattern` | `02-service-communication/api-gateway` (+ `bff`) |
| `cqrs-event-sourcing` | `03-data-management/cqrs` (+ `event-sourcing`) |
| `event-driven-architecture-log-streaming` | `06-event-driven/event-driven-architecture` |
| `architectural-pragmatist-monolith-vs-microservices` | `01-architecture-styles/microservices` |
| *(full alias table in navigation-plan.md)* | |

---

**Enforcement (Phase B):** Grep CI check or manual audit — any concept row marked **Planned** must not have >2 sentences of deep dive outside canonical page.
