---
title: "Reliability Engineering"
date: 2026-07-03T15:00:00+00:00
draft: false
description: "SLOs, error budgets, contract testing, chaos practices, incident response."
tags: ["microservices", "architecture-playbook", "distributed-systems"]
categories: ["Microservices Architecture Playbook"]
shortTitle: "Reliability"
module: 10
moduleTitle: "Production Playbook"
sectionRef: "10.4"
weight: 1004
playbookVersion: 3
aliases:
  - "/microservices/consumer-driven-contract-testing-cdct/"
---

## Executive Summary

Reliability is designed — not accidental.

---

## Where It Fits

SRE partnership with product teams.

---

## Security Considerations

Apply zero-trust between services, mTLS in mesh, and least-privilege credentials per service identity. See [Kubernetes RBAC](/kubernetes-handbook/rbac/) and service mesh policies.

---

## Observability

Export RED metrics, structured logs with `trace_id`, and distributed traces on every cross-service hop. See [Observability](/microservices/08-observability/observability/).

---

## Architect Notes

Canonical page for **Reliability Engineering**. Cross-handbook depth: link out, do not duplicate broker/DB/cache engine internals.
