---
title: "Architecture Review Checklist"
date: 2026-07-03T15:00:00+00:00
draft: false
description: "PRR checklists for scalability, reliability, security, observability, cost, operability."
tags: ["microservices", "architecture-playbook", "distributed-systems"]
categories: ["Microservices Architecture Playbook"]
shortTitle: "Review Checklist"
module: 10
moduleTitle: "Production Playbook"
sectionRef: "10.7"
weight: 1007
playbookVersion: 3
---

## Executive Summary

Architecture review checklist before production launch: scalability, reliability, security, observability, cost, operability, and readiness gates.

---

## Problem It Solves

Services reach prod without SLOs, without idempotent consumers, without rollback plan.

---

## Where It Fits

Production readiness review (PRR) and quarterly architecture audits.

---

## Internal Working

**Scalability:** Stateless? HPA metrics? Shard key? Hot path identified?

**Reliability:** SLO defined? Breaker/timeout/bulkhead? Saga/outbox for cross-service writes?

**Security:** mTLS? Secret rotation? OWASP API top 10?

**Observability:** RED metrics? Trace propagation? Log correlation?

**Cost:** Right-sized instances? Cache hit ratio? Broker retention policy?

**Operability:** Runbook? On-call rotation? Feature flag rollback?

---

## Design Decisions

Block launch on P0 gaps; track P1 as debt with owner.

---

## Tradeoffs

Checklist weight vs team velocity — tier by tier-1 vs tier-3 service.

---

## Scalability

Load test at 2× expected peak.

---

## Reliability

Chaos test dependency failure monthly for tier-1.

---

## Security Considerations

Threat model sign-off for external-facing APIs.

---

## Observability

Dashboard + alert links in service catalog.

---

## Production Lessons

PRR once per service major version.

---

## Common Failures

Launch without consumer lag alerts.

---

## Common Mistakes

Checkbox exercise without owners.

---

## Interview Questions

1. What is in your PRR for a new payment microservice?

---

## Architect Notes

Pair with [ADRs](/microservices/10-production-playbook/architecture-decision-records/).
