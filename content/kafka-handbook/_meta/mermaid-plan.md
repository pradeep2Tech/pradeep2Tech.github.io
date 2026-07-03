---
title: "Kafka Handbook Mermaid Diagram Plan"
date: 2026-07-03T12:00:00+00:00
draft: true
description: "Diagram opportunities by topic — Phase B/C implementation backlog."
tags: ["kafka-handbook", "meta", "planning"]
---

# Mermaid Diagram Plan

**Principle:** Diagrams on **canonical pages only**. Non-canonical pages link to diagram section.

**Existing diagrams:** 3 (`messaging-patterns`, `kafka-core`, `kafka-vs-rabbitmq`, `broker-selection-guide` flowchart).

---

## 01 Fundamentals

| Page | Diagram type | Purpose | Priority | Status |
| :--- | :--- | :--- | :---: | :--- |
| `messaging-patterns.md` | `flowchart LR` | Fan-out via consumer groups | — | **Exists** |
| `messaging-models.md` | `flowchart TB` | Queue vs log consumer progress | P2 | Planned |
| `queue-vs-stream.md` | `quadrantChart` or table | Already has comparison table | P3 | Optional |
| `broker-selection-guide.md` | `flowchart TD` | Selection decision tree | — | **Exists** |

---

## 02 Kafka — Core & Groups

| Page | Diagram type | Purpose | Priority |
| :--- | :--- | :--- | :---: |
| `kafka-core.md` | `flowchart LR` | Producer → topic → groups | — | **Exists** |
| `kafka-core.md` | `sequenceDiagram` | Produce path with acks=0/1/all | P1 | Planned |
| `kafka-consumer-groups.md` | `sequenceDiagram` | Rebalance lifecycle | P0 | Planned |
| `kafka-consumer-groups.md` | `flowchart TB` | Partition assignment per group | P0 | Planned |
| `kafka-delivery-semantics.md` | `sequenceDiagram` | Idempotent producer sequence | P1 | Planned |
| `kafka-delivery-semantics.md` | `flowchart LR` | Outbox → Kafka → consumer | P1 | Planned |

---

## 02 Kafka — Internals & Storage

| Page | Diagram type | Purpose | Priority |
| :--- | :--- | :--- | :---: |
| `kafka-internals.md` | `flowchart TB` | Leader + ISR replication | P0 | Planned |
| `kafka-internals.md` | `sequenceDiagram` | Write path: append → replicate → HW | P0 | Planned |
| `kafka-internals.md` | `flowchart LR` | Log segment rolling | P1 | Planned |
| `kafka-internals.md` | `sequenceDiagram` | Unclean leader election failure | P1 | Planned |
| `kafka-internals.md` | `erDiagram` | Topic → Partition → Segment | P2 | Planned |

---

## 02 Kafka — Performance

| Page | Diagram type | Purpose | Priority |
| :--- | :--- | :--- | :---: |
| `kafka-performance.md` | `flowchart LR` | Hot partition vs balanced keys | P1 | Planned |
| `kafka-performance.md` | `sequenceDiagram` | Batch + linger pipeline | P2 | Planned |
| `kafka-performance.md` | `flowchart TB` | Capacity: RPS → disk → bandwidth | P2 | Planned |

---

## 02 Kafka — Security

| Page | Diagram type | Purpose | Priority |
| :--- | :--- | :--- | :---: |
| `kafka-security.md` | `flowchart TB` | mTLS client ↔ broker ↔ broker | P1 | Planned |
| `kafka-security.md` | `sequenceDiagram` | SASL handshake + ACL check | P2 | Planned |

---

## 02 Kafka — Operations

| Page | Diagram type | Purpose | Priority |
| :--- | :--- | :--- | :---: |
| `kafka-operations.md` | `flowchart TB` | KRaft quorum (controllers) | P1 | Planned |
| `kafka-operations.md` | `sequenceDiagram` | Rolling broker restart / leader move | P1 | Planned |
| `kafka-operations.md` | `flowchart LR` | K8s: StatefulSet + PV + operator | P2 | Planned |
| `kafka-multi-region.md` | `flowchart LR` | MirrorMaker 2 active-passive | P1 | Planned |

---

## 02 Kafka — Troubleshooting

| Page | Diagram type | Purpose | Priority |
| :--- | :--- | :--- | :---: |
| `kafka-troubleshooting.md` | `flowchart TD` | Lag isolation decision tree | P0 | Planned |
| `kafka-troubleshooting.md` | `flowchart TD` | Poison message → DLT → replay | P1 | Planned |
| `kafka-troubleshooting.md` | `sequenceDiagram` | Rebalance loop failure scenario | P1 | Planned |

---

## 03 Broker Comparisons

| Page | Diagram type | Purpose | Priority |
| :--- | :--- | :--- | :---: |
| `kafka-vs-rabbitmq.md` | `flowchart LR` | Hybrid streaming + task queue | — | **Exists** |
| `kafka-vs-pulsar.md` | `flowchart TB` | Broker + BookKeeper separation | P1 | Planned |
| `kafka-vs-nats.md` | `flowchart LR` | Edge NATS → central Kafka | P2 | Planned |
| `cloud-messaging-services.md` | `flowchart LR` | SNS → SQS vs Kafka consumer groups | P1 | Planned |

---

## Diagram Standards

| Rule | Detail |
| :--- | :--- |
| Syntax | Hugo fenced ` ```mermaid ` blocks |
| Labels | Quote edge labels; use `participant X as Name` in sequences |
| Placement | Under **Architecture** or **Internal Working** section |
| Avoid | Duplicate same diagram on comparison + core pages |
| System design posts | Use `sequenceDiagram` for request paths per repo rules |

---

## Implementation Phases

| Phase | Diagrams |
| :--- | :--- |
| **B** | Fix existing; add rebalance + ISR + lag decision tree (P0) |
| **C** | Delivery semantics, security mTLS, KRaft, MirrorMaker |
| **D** | erDiagram, capacity flowcharts |

---

**STOP — Implement diagrams during Phase C content depth work.**
