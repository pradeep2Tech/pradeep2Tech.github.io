---
title: "Microservices Architecture Playbook — Mermaid Diagram Plan"
date: 2026-07-03T15:00:00+00:00
draft: true
description: "Diagram opportunities by topic — Phase B/C implementation backlog."
tags: ["microservices", "meta", "planning"]
---

# Mermaid Diagram Plan

**Principle:** Diagrams on **canonical pages only**. Non-canonical pages link to diagram section (`#architecture-diagram`).

**Existing diagrams:** 29 topic files contain at least one Mermaid block (legacy flat structure). `circuit-breaker-pattern.md` has **3** diagrams (state, flowchart, sequence) — best reference quality.

**Phase B:** Consolidate duplicate diagrams; do not copy outbox sequence to 5 pages.

---

## 01 Architecture Styles

| Page | Diagram type | Purpose | Priority | Status |
| :--- | :--- | :--- | :---: | :--- |
| `monolith.md` | `flowchart TB` | Single process + shared DB | P1 | Planned |
| `modular-monolith.md` | `flowchart LR` | Package boundaries in one deployable | P1 | Planned |
| `microservices.md` | `flowchart TB` | Network boundaries per service | P0 | **Exists** (migrate from comparison page) |
| `microservices.md` | `quadrantChart` or table | Monolith vs microservices tradeoff axes | P2 | Planned |
| `soa.md` | `flowchart LR` | ESB hub vs point-to-point microservices | P1 | Planned |

---

## 02 Service Communication

| Page | Diagram type | Purpose | Priority | Status |
| :--- | :--- | :--- | :---: | :--- |
| `api-gateway.md` | `sequenceDiagram` | TLS → JWT → fan-out aggregation | P0 | **Exists** (migrate from combined page) |
| `bff.md` | `flowchart TB` | Gateway → Mobile BFF / Web BFF → services | P1 | **Exists** (text diagram in combined page) |
| `service-discovery.md` | `sequenceDiagram` | Client-side lookup vs server-side LB | P1 | **Exists** |
| `service-discovery.md` | `flowchart LR` | K8s DNS + Endpoints slice | P2 | Planned |
| `communication-topologies.md` | `flowchart TB` | Sync query path vs async command path | P0 | **Exists** |
| `communication-topologies.md` | `sequenceDiagram` | Trace context injection on gRPC | P2 | Planned |

---

## 03 Data Management

| Page | Diagram type | Purpose | Priority | Status |
| :--- | :--- | :--- | :---: | :--- |
| `database-per-service.md` | `flowchart LR` | Service → private DB; async reference sync | P0 | **Exists** |
| `cqrs.md` | `flowchart LR` | Command → write model; query → read model | P0 | **Exists** (partial in combined page) |
| `event-sourcing.md` | `flowchart TB` | Append log → replay → snapshot anchor | P1 | Planned |
| `saga.md` | `sequenceDiagram` | Orchestration: steps + compensations | P0 | **Exists** |
| `saga.md` | `sequenceDiagram` | Choreography: event chain | P1 | Planned |
| `outbox.md` | `sequenceDiagram` | TX: domain write + outbox row → relay | P0 | **Exists** (currently on EDA page — **move here only**) |
| `cdc.md` | `sequenceDiagram` | WAL → Debezium → broker → consumer | P0 | Planned |

---

## 04 Distributed Systems

| Page | Diagram type | Purpose | Priority | Status |
| :--- | :--- | :--- | :---: | :--- |
| `cap-theorem.md` | `flowchart TB` | CP partition: quorum reject vs AP accept | P0 | **Exists** |
| `pacelc.md` | `flowchart LR` | Normal ops: latency vs consistency fork | P1 | Planned |
| `consistent-hashing.md` | `flowchart LR` | Hash ring + vnode distribution | P0 | **Exists** |
| `consistent-hashing.md` | `flowchart TB` | Node add: minimal key migration | P2 | Planned |
| `concurrency-control.md` | `sequenceDiagram` | Optimistic version conflict vs `SELECT FOR UPDATE` | P1 | **Exists** |

---

## 05 Resilience Patterns

| Page | Diagram type | Purpose | Priority | Status |
| :--- | :--- | :--- | :---: | :--- |
| `circuit-breaker.md` | `stateDiagram-v2` | CLOSED / OPEN / HALF-OPEN | P0 | **Exists** |
| `circuit-breaker.md` | `sequenceDiagram` | Checkout with breaker + payment | P0 | **Exists** |
| `bulkhead.md` | `flowchart TB` | Thread pools per dependency | P0 | **Exists** |
| `retry.md` | `sequenceDiagram` | Exponential backoff + jitter timeline | P1 | Planned |
| `timeout.md` | `sequenceDiagram` | Deadline propagation across gRPC hops | P1 | Planned |
| `fallback.md` | `flowchart LR` | Read: cache fallback vs write: structured 503 | P1 | Planned |

---

## 06 Event-Driven

| Page | Diagram type | Purpose | Priority | Status |
| :--- | :--- | :--- | :---: | :--- |
| `event-driven-architecture.md` | `flowchart TB` | Producer → broker → N consumers | P1 | Planned |
| `messaging-patterns.md` | `sequenceDiagram` | Point-to-point competing consumers | P0 | **Exists** |
| `messaging-patterns.md` | table | Pub/Sub vs log comparison | P0 | **Exists** (on EDA page) |
| `event-streaming.md` | `flowchart LR` | Partition log + consumer groups | P0 | Planned |
| `event-streaming.md` | `sequenceDiagram` | Ordering scope per partition key | P1 | Planned |

---

## 07 Platform Patterns

| Page | Diagram type | Purpose | Priority | Status |
| :--- | :--- | :--- | :---: | :--- |
| `sidecar.md` | `flowchart TB` | App container + Envoy sidecar per pod | P0 | **Exists** |
| `sidecar.md` | `sequenceDiagram` | iptables redirect request path | P2 | Planned |
| `service-mesh.md` | `flowchart TB` | Control plane (Istiod) → data plane (Envoy) | P0 | **Exists** |
| `service-mesh.md` | `flowchart LR` | Sidecar mesh vs ambient/eBPF | P1 | Planned |
| `kubernetes-patterns.md` | `flowchart TB` | Deployment → Service → Ingress → HPA | P0 | Planned |
| `kubernetes-patterns.md` | `sequenceDiagram` | Rolling update + readiness gate | P1 | Planned |

---

## 08 Observability

| Page | Diagram type | Purpose | Priority | Status |
| :--- | :--- | :--- | :---: | :--- |
| `three-pillars-observability.md` | `flowchart LR` | Metrics + logs + traces correlation | P0 | **Exists** |
| `metrics.md` | `flowchart TB` | RED method on service; USE on node | P1 | Planned |
| `logging.md` | `flowchart LR` | App → Fluent Bit → Loki/ELK | P1 | Planned |
| `distributed-tracing.md` | `sequenceDiagram` | traceparent across 3 services | P0 | **Exists** |
| `distributed-tracing.md` | `flowchart TB` | Head vs tail sampling decision | P1 | Planned |

---

## 09 Migration & Modernization

| Page | Diagram type | Purpose | Priority | Status |
| :--- | :--- | :--- | :---: | :--- |
| `strangler-pattern.md` | `flowchart LR` | Gateway routes: legacy vs new service | P0 | **Exists** |
| `monolith-decomposition.md` | `flowchart TB` | Bounded context extraction order | P1 | Planned |
| `database-decomposition.md` | `sequenceDiagram` | CDC mirror → cutover gate | P0 | **Exists** |
| `zero-downtime-deployments.md` | `flowchart LR` | Blue-green traffic switch | P0 | **Exists** |
| `zero-downtime-deployments.md` | `flowchart TB` | Canary % progression + rollback | P1 | Planned |

---

## 10 Production Playbook

| Page | Diagram type | Purpose | Priority | Status |
| :--- | :--- | :--- | :---: | :--- |
| `scalability-patterns.md` | `flowchart TB` | Scale axes: stateless, read replica, shard | P0 | Planned |
| `scalability-patterns.md` | `flowchart LR` | Tiered rate limit: edge → gateway → service | P1 | **Exists** (on rate-limit page) |
| `caching-patterns.md` | `sequenceDiagram` | Cache-aside read + write-invalidate | P1 | **Exists** (on caching page) |
| `deployment-strategies.md` | `flowchart TB` | Rolling vs blue-green vs canary matrix | P1 | Planned |
| `reliability-engineering.md` | `flowchart LR` | SLO → error budget → release gate | P1 | Planned |

---

## 11 Interview Guide

| Page | Diagram type | Purpose | Priority |
| :--- | :--- | :--- | :---: |
| Interview pages | None | Link to canonical diagram sections | — |

---

## 12 Learning Paths

| Page | Diagram type | Purpose | Priority |
| :--- | :--- | :--- | :---: |
| `architect-path.md` | `flowchart TD` | Module reading order decision tree | P2 |
| `interview-revision-path.md` | `gantt` or table | 2-week revision schedule | P3 |

---

## Diagram Deduplication Rules (Phase B)

| Remove duplicate from | Keep only on |
| :--- | :--- |
| `communication-topologies`, `saga`, `database-per-service` | `outbox.md` — outbox sequence |
| `cqrs-event-sourcing`, `distributed-caching-invalidation` | `cdc.md` — WAL pipeline |
| `sidecar`, `kubernetes-patterns` | `service-mesh.md` — control/data plane (sidecar page = pod layout only) |
| `three-pillars`, `distributed-tracing` | One sampling diagram on `distributed-tracing.md` |
| `database-sharding`, `scalability-patterns` | `consistent-hashing.md` — ring mechanics |

---

## Priority Legend

| Priority | Meaning |
| :---: | :--- |
| P0 | Required for architect comprehension — Phase B |
| P1 | High value — Phase B/C |
| P2 | Nice to have — Phase C |
| P3 | Optional polish |

**Estimated net new diagrams:** ~18 (after deduplication of ~12 moved/consolidated).

---

**Phase A complete. Implementation deferred to Phase B/C.**
