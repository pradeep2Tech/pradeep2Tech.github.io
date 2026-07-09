---
title: "API Gateway & BFF"
date: 2026-07-03T15:00:00+00:00
draft: false
description: "Unified ingress — TLS, JWT, routing, rate limits, and client-specific BFF aggregation."
tags: ["microservices", "architecture-playbook", "distributed-systems"]
categories: ["Microservices Architecture Playbook"]
shortTitle: "API Gateway & BFF"
module: 2
moduleTitle: "Service Communication"
sectionRef: "2.1"
weight: 201
playbookVersion: 3
aliases:
  - "/microservices/api-gateway-bff-pattern/"
---

## Executive Summary

Gateway handles cross-cutting ingress; BFF shapes payloads per client surface.

---

## Where It Fits

Edge of every external client integration.

---

## Security Considerations

Apply zero-trust between services, mTLS in mesh, and least-privilege credentials per service identity. See [Kubernetes RBAC](/kubernetes-handbook/rbac/) and service mesh policies.

---

## Observability

Export RED metrics, structured logs with `trace_id`, and distributed traces on every cross-service hop. See [Observability](/microservices/08-observability/observability/).

---

## Architect Notes

Canonical page for **API Gateway & BFF**. Cross-handbook depth: link out, do not duplicate broker/DB/cache engine internals.
