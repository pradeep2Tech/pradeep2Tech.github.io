---
title: "Failure Scenarios"
date: 2026-07-03T15:00:00+00:00
draft: false
description: "Database, broker, cache, mesh, partition, and cascade failure recovery."
tags: ["microservices", "architecture-playbook", "distributed-systems"]
categories: ["Microservices Architecture Playbook"]
shortTitle: "Failures"
module: 10
moduleTitle: "Production Playbook"
sectionRef: "10.6"
weight: 1006
playbookVersion: 3
---

## Executive Summary

Production failure scenarios for microservices: database, broker, cache, mesh, network partition, region loss, dependency cascade — with recovery strategies.

---

## Problem It Solves

On-call needs runbook-level scenario playbooks, not generic 'restart the pod'.

---

## Where It Fits

Incident response, game days, and architecture review.

---

## Internal Working

### Database failure
Primary down → failover to replica; watch replication lag and split-brain.

### Broker failure
Consumer lag spikes; extend retention; scale consumers; DLQ poison pills.

### Cache failure
Fail-open vs fail-closed for rate limits; cache-aside falls through to DB.

### Service mesh failure
Control plane outage — data plane may continue; know your degradation mode.

### Network partition
CAP choice manifests; CP systems reject writes; AP systems diverge.

### Region failure
Active-passive DNS; multi-region Kafka mirroring — see Kafka HB.

### Cascading failure
Timeouts → pool exhaustion → retry storm → [Resilience Patterns](/microservices/05-resilience-patterns/resilience-patterns/).

---

## Design Decisions

Design for **graceful degradation** per dependency criticality.

---

## Tradeoffs

Fail-open improves availability; fail-closed protects data integrity.

---

## Scalability

Load shed at gateway when downstream unhealthy.

---

## Reliability

Error budgets gate releases after repeated incidents.

---

## Security Considerations

Failover must not bypass authz or expose stale tokens.

---

## Observability

Golden signals per scenario; SLO burn alerts.

---

## Production Lessons

Run game days for broker partition and AZ failure quarterly.

---

## Common Failures

Retry storm during partial outage.

---

## Common Mistakes

No bulkhead before Black Friday traffic.

---

## Interview Questions

1. Walk through payment DB failover with in-flight sagas.
2. What happens when Redis rate limiter dies?

---

## Architect Notes

Broker recovery details: [Kafka Troubleshooting](/kafka-handbook/02-kafka/kafka-troubleshooting/).
