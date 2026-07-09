---
title: "Architecture Styles"
date: 2026-07-03T15:00:00+00:00
draft: false
description: "Monolith, modular monolith, microservices, and SOA — architect tradeoffs and decomposition triggers."
tags: ["microservices", "architecture-playbook", "distributed-systems"]
categories: ["Microservices Architecture Playbook"]
shortTitle: "Architecture Styles"
module: 1
moduleTitle: "Architecture Styles"
sectionRef: "1.1"
weight: 101
playbookVersion: 3
aliases:
  - "/microservices/architectural-pragmatist-monolith-vs-microservices/"
---

## Executive Summary

Compare deployment styles by team structure, consistency model, and operational tax — not hype.


## Problem It Solves

Teams default to microservices for hype — not organizational need. Architecture styles exist to **match deployment granularity to team structure, consistency requirements, and operational maturity**.

| Style | Core problem addressed |
| :--- | :--- |
| **Monolith** | Fast iteration; single-team ACID |
| **Modular monolith** | Code boundaries without network tax |
| **Microservices** | Independent deploy per autonomous team |
| **SOA** | Enterprise integration via shared services bus (legacy) vs modern decentralized events |

### SOA vs Modern Microservices

| Dimension | Classic SOA | Modern Microservices |
| :--- | :--- | :--- |
| Integration | Central ESB orchestration | Smart endpoints, dumb pipes (events/APIs) |
| Data | Shared enterprise data models | Database per service |
| Governance | Central integration team | Federated teams + platform guild |
| Best era | 2000s enterprise ERP | Cloud-native product orgs |

SOA is not wrong historically — but **ESB-as-brain** anti-patterns map to today's distributed monolith. Prefer decentralized choreography with clear bounded contexts.

---

## Where It Fits

First module for any architecture review, greenfield ADR, or migration planning.

---

## Security Considerations

Apply zero-trust between services, mTLS in mesh, and least-privilege credentials per service identity. See [Kubernetes RBAC](/kubernetes-handbook/rbac/) and service mesh policies.

---

## Observability

Export RED metrics, structured logs with `trace_id`, and distributed traces on every cross-service hop. See [Observability](/microservices/08-observability/observability/).

---

## Architect Notes

Canonical page for **Architecture Styles**. Cross-handbook depth: link out, do not duplicate broker/DB/cache engine internals.
