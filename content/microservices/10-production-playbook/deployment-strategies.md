---
title: "Deployment Strategies"
date: 2026-07-03T15:00:00+00:00
draft: false
description: "Rolling, blue-green, canary, feature flags, and contract-gated releases."
tags: ["microservices", "architecture-playbook", "distributed-systems"]
categories: ["Microservices Architecture Playbook"]
shortTitle: "Deployment"
module: 10
moduleTitle: "Production Playbook"
sectionRef: "10.3"
weight: 1003
playbookVersion: 3
---

## Executive Summary

Choose rollout strategy by blast radius and observability depth.

---

## Where It Fits

Platform and product release engineering.

---

## Security Considerations

Apply zero-trust between services, mTLS in mesh, and least-privilege credentials per service identity. See [Kubernetes RBAC](/kubernetes-handbook/rbac/) and service mesh policies.

---

## Observability

Export RED metrics, structured logs with `trace_id`, and distributed traces on every cross-service hop. See [Observability](/microservices/08-observability/observability/).

---

## Architect Notes

Canonical page for **Deployment Strategies**. Cross-handbook depth: link out, do not duplicate broker/DB/cache engine internals.
