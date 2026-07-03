---
title: "CAP & PACELC"
date: 2026-07-03T15:00:00+00:00
draft: false
description: "Consistency vs availability under partition; latency vs consistency in normal operation."
tags: ["microservices", "architecture-playbook", "distributed-systems"]
categories: ["Microservices Architecture Playbook"]
shortTitle: "CAP & PACELC"
module: 4
moduleTitle: "Distributed Systems"
sectionRef: "4.1"
weight: 401
ShowToc: true
playbookVersion: 3
aliases:
  - "/microservices/cap-theorem-pacelc-framework/"
---

## Executive Summary

CAP applies during partition; PACELC during normal ops.

---

## Where It Fits

Every datastore and consistency decision.

---

## Security Considerations

Apply zero-trust between services, mTLS in mesh, and least-privilege credentials per service identity. See [Kubernetes RBAC](/kubernetes-handbook/rbac/) and service mesh policies.

---

## Observability

Export RED metrics, structured logs with `trace_id`, and distributed traces on every cross-service hop. See [Observability](/microservices/08-observability/observability/).

---

## Architect Notes

Canonical page for **CAP & PACELC**. Cross-handbook depth: link out, do not duplicate broker/DB/cache engine internals.
