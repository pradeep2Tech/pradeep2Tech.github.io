---
title: "Outbox & CDC Patterns"
date: 2026-07-03T15:00:00+00:00
draft: false
description: "Transactional outbox and change data capture for reliable event publication."
tags: ["microservices", "architecture-playbook", "distributed-systems", "outbox", "cdc"]
categories: ["Microservices Architecture Playbook"]
shortTitle: "Outbox & CDC"
module: 3
moduleTitle: "Data Management"
sectionRef: "3.4"
weight: 304
ShowToc: true
playbookVersion: 3
---

## Executive Summary

The **transactional outbox** and **CDC** patterns solve the dual-write problem: reliably publishing events when domain state changes in a local database. Outbox writes the event in the same ACID transaction as the domain row; CDC streams WAL changes to the broker without application-thread overhead.

---

## Problem It Solves

Without outbox/CDC, services either lose events or corrupt state when DB commit succeeds but broker publish fails.

---

## Where It Fits

Every service that mutates local state and must notify other bounded contexts asynchronously.

---

## Internal Working

**Outbox:** INSERT domain row + INSERT outbox row in one transaction → relay polls or tails outbox → publish → mark processed.

**CDC:** Debezium reads database WAL → transforms row changes → publishes to Kafka topic.

Schema and relay tuning: [Transactional Outbox Pattern](/database-handbook/transactional-outbox-pattern/).

---

## Design Decisions

| Pattern | When | Trade-off |
| Outbox table | Full control, any DB | Relay component to operate |
| CDC | Minimal app code | Coupled to WAL format |

---

## Tradeoffs

At-least-once delivery requires idempotent consumers. Ordering per aggregate key via partition routing.

---

## Scalability

Outbox relay must keep pace with write rate; monitor relay lag.

---

## Reliability

Never dual-write to DB and broker from application code without outbox or CDC.

---

## Security Considerations

Encrypt outbox payloads containing PII; restrict relay service credentials.

---

## Observability

Metrics: `outbox_pending_count`, `cdc_lag_seconds`, publish error rate.

---

## Production Lessons

Use idempotent `event_id` deduplication on consumers.

---

## Common Failures

| Relay stopped | Events never published | Alert on pending outbox age |
| CDC lag at cutover | Split brain | Lag gate before flip |

---

## Common Mistakes

Publishing before DB commit; deleting outbox rows before broker ack.

---

## Interview Questions

1. Why is dual-write an anti-pattern?
2. Compare outbox polling vs CDC.
3. How do you guarantee ordering for one order ID?

---

## Architect Notes

Canonical architect page for outbox/CDC. Database Handbook owns relay schema details.
