---
title: "Database Per Service"
date: 2026-07-03T15:00:00+00:00
draft: false
description: "Domain-encapsulated persistence, reference data replication, and analytics boundaries."
tags: ["microservices", "architecture-playbook", "distributed-systems"]
categories: ["Microservices Architecture Playbook"]
shortTitle: "DB Per Service"
module: 3
moduleTitle: "Data Management"
sectionRef: "3.1"
weight: 301
playbookVersion: 3
aliases:
  - "/microservices/database-per-microservice/"
---

## Executive Summary

Each service owns its schema; no cross-service JOINs.

---

## Where It Fits

Foundation of loosely coupled data architecture.

---

## Security Considerations

Apply zero-trust between services, mTLS in mesh, and least-privilege credentials per service identity. See [Kubernetes RBAC](/kubernetes-handbook/rbac/) and service mesh policies.

---

## Observability

Export RED metrics, structured logs with `trace_id`, and distributed traces on every cross-service hop. See [Observability](/microservices/08-observability/observability/).

---

## Architect Notes

Canonical page for **Database Per Service**. Cross-handbook depth: link out, do not duplicate broker/DB/cache engine internals.
