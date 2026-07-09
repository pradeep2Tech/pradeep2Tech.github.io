---
title: "Saga Pattern"
date: 2026-07-03T15:00:00+00:00
draft: false
description: "Orchestration vs choreography, compensating transactions, and idempotent rollback."
tags: ["microservices", "architecture-playbook", "distributed-systems"]
categories: ["Microservices Architecture Playbook"]
shortTitle: "Saga"
module: 3
moduleTitle: "Data Management"
sectionRef: "3.3"
weight: 303
playbookVersion: 3
aliases:
  - "/microservices/saga-pattern-distributed-transactions/"
---

## Executive Summary

Replace 2PC with forward steps and compensations.

---

## Where It Fits

Cross-service business transactions without shared DB.

---

## Security Considerations

Apply zero-trust between services, mTLS in mesh, and least-privilege credentials per service identity. See [Kubernetes RBAC](/kubernetes-handbook/rbac/) and service mesh policies.

---

## Observability

Export RED metrics, structured logs with `trace_id`, and distributed traces on every cross-service hop. See [Observability](/microservices/08-observability/observability/).

---

## Architect Notes

Canonical page for **Saga Pattern**. Cross-handbook depth: link out, do not duplicate broker/DB/cache engine internals.
