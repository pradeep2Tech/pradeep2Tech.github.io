---
title: "Kafka Handbook Infographic Plan"
date: 2026-07-03T12:00:00+00:00
draft: true
description: "Visual asset backlog — revision sheets, decision trees, comparison one-pagers."
tags: ["kafka-handbook", "meta", "planning"]
---

# Infographic Plan

**Note:** This site is Markdown/Hugo-first. "Infographics" = **structured one-page visual tables**, Mermaid diagrams, and optional future static images — not separate image assets unless generated later.

**Meta file:** `draft: true` — planning backlog only.

---

## Format Strategy

| Asset type | Implementation | Location |
| :--- | :--- | :--- |
| Revision sheet | Markdown table + bullets | Page **Quick Revision** or `05-learning-paths/kafka-interview-revision-path.md` |
| Comparison one-pager | `comparison-table` Hugo shortcode | `03-broker-comparisons/*` |
| Decision tree | Mermaid `flowchart TD` | `broker-selection-guide`, `kafka-troubleshooting` |
| Troubleshooting flowchart | Mermaid | `kafka-troubleshooting.md` |
| Interview cheat sheet | Single-page table | `04-interview-guide/` or revision path |
| Architecture poster | Mermaid `flowchart LR` | `kafka-internals`, `kafka-core` |

---

## By Major Topic

### Fundamentals

| Topic | Infographic | Canonical page | Priority |
| :--- | :--- | :--- | :---: |
| Queue vs stream | Side-by-side comparison card | `queue-vs-stream.md` | — Exists (table) |
| Broker selection | Decision tree poster | `broker-selection-guide.md` | P1 |
| Messaging patterns | Fan-out illustration | `messaging-patterns.md` | — Exists (mermaid) |

### Kafka Core

| Topic | Infographic | Canonical page | Priority |
| :--- | :--- | :--- | :---: |
| Topic / partition / offset | Layered stack diagram | `kafka-core.md` | P1 |
| `acks` tradeoff | 3-column pros/cons card | `kafka-core.md` | P1 |
| Consumer group model | Assignment grid | `kafka-consumer-groups.md` | P0 |

### Internals & Replication

| Topic | Infographic | Canonical page | Priority |
| :--- | :--- | :--- | :---: |
| ISR + leader | Broker cluster status card | `kafka-internals.md` | P0 |
| Log segment files | On-disk layout ASCII/Mermaid | `kafka-internals.md` | P1 |
| HW vs LEO | Offset timeline | `kafka-internals.md` | P1 |
| Compaction | Before/after key retention | `kafka-internals.md` | P2 |

### Delivery & Transactions

| Topic | Infographic | Canonical page | Priority |
| :--- | :--- | :--- | :---: |
| Delivery semantics matrix | at-most / least / exactly-once | `kafka-delivery-semantics.md` | P0 |
| Idempotent producer | Sequence # diagram | `kafka-delivery-semantics.md` | P1 |
| Outbox pattern | Dual-write vs outbox | `kafka-delivery-semantics.md` | P1 |

### Performance

| Topic | Infographic | Canonical page | Priority |
| :--- | :--- | :--- | :---: |
| Tuning knobs | Producer vs consumer knob table | `kafka-performance.md` | P1 |
| Hot partition | Skew visualization | `kafka-performance.md` | P1 |
| Capacity planning | BOE formula card | `kafka-performance.md` | P2 |

### Security

| Topic | Infographic | Canonical page | Priority |
| :--- | :--- | :--- | :---: |
| Defense in depth | TLS + SASL + ACL layers | `kafka-security.md` | P1 |
| Shared responsibility (MSK) | Cloud vs customer matrix | `kafka-security.md` | P2 |

### Operations

| Topic | Infographic | Canonical page | Priority |
| :--- | :--- | :--- | :---: |
| KRaft vs ZK | Feature comparison card | `kafka-operations.md` | P1 |
| Upgrade runbook | Phase timeline | `kafka-operations.md` | P2 |
| K8s deployment | Pod / PV / operator stack | `kafka-operations.md` | P2 |

### Troubleshooting

| Topic | Infographic | Canonical page | Priority |
| :--- | :--- | :--- | :---: |
| Lag triage | Flowchart poster | `kafka-troubleshooting.md` | P0 |
| Symptom → cause matrix | Table | `kafka-troubleshooting.md` | — Partial |
| Incident severity | Runbook escalation card | `kafka-troubleshooting.md` | P2 |

### Broker Comparisons

| Topic | Infographic | Canonical page | Priority |
| :--- | :--- | :--- | :---: |
| 11-dimension matrix | comparison-table | Each `kafka-vs-*.md` | — Exists |
| Cloud messaging | AWS/Azure/GCP one-pager | `cloud-messaging-services.md` | P1 |
| Hybrid platform map | Kafka + queue flows | `kafka-vs-rabbitmq.md` | — Partial |

### Interview

| Topic | Infographic | Canonical page | Priority |
| :--- | :--- | :--- | :---: |
| Top 25 architect | Printable question list | `architect-questions.md` | — Exists |
| 30-minute revision | One-page cram sheet | `05-learning-paths/kafka-interview-revision-path.md` | P0 |
| Topic → page map | Concept registry visual | `_meta/concept-registry.md` | P2 |

---

## Cheat Sheet Module (`13-cheat-sheets` — Optional Future)

**Not in current IA.** If added later, consolidate:

| Cheat sheet | Source material |
| :--- | :--- |
| Kafka internals cram | `kafka-internals` Quick Revision |
| Producer/consumer knobs | `kafka-performance` tables |
| Troubleshooting triage | `kafka-troubleshooting` flowchart |
| Comparison at-a-glance | Broker comparison matrices |

Prefer **`05-learning-paths/kafka-interview-revision-path.md`** over new module to avoid IA sprawl.

---

## Production Checklist Infographics

Embed in **Checklists** section (Phase C):

| Checklist | Page |
| :--- | :--- |
| Pre-production go-live | `kafka-operations.md` |
| Consumer service readiness | `kafka-consumer-groups.md` |
| Security audit | `kafka-security.md` |
| Campaign / peak traffic | `kafka-performance.md` |
| Architect review ADR | `broker-selection-guide.md` |

---

## Priority Summary

| Priority | Deliverables |
| :---: | :--- |
| **P0** | Lag triage flowchart, ISR card, delivery semantics matrix, consumer group grid, 30-min revision path |
| **P1** | acks card, broker decision tree, mTLS layers, cloud one-pager, write path sequence |
| **P2** | KRaft card, capacity BOE, compaction visual, K8s stack |

---

## Asset Generation Notes

- **Phase B:** Markdown tables + fix broken `comparison-table` shortcode on RabbitMQ page
- **Phase C:** Mermaid per `mermaid-plan.md`
- **Future:** Optional PNG/SVG exports from Mermaid for social/print — out of scope Phase A–B

---

**STOP — Implement infographics during Phase C content depth work.**
