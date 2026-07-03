---
title: "Zero-Downtime Deployments"
date: 2026-07-03T15:00:00+00:00
draft: false
description: "Blue-green, canary, expand-contract schema migrations, automated rollback."
tags: ["microservices", "architecture-playbook", "distributed-systems"]
categories: ["Microservices Architecture Playbook"]
shortTitle: "Zero Downtime"
module: 9
moduleTitle: "Migration & Modernization"
sectionRef: "9.3"
weight: 903
ShowToc: true
playbookVersion: 3
aliases:
  - "/microservices/zero-downtime-deployment-topologies/"
---

## Executive Summary

Ship without user-visible outage.

---

## Where It Fits

Migration cutover and ongoing releases.

---

## Security Considerations

Apply zero-trust between services, mTLS in mesh, and least-privilege credentials per service identity. See [Kubernetes RBAC](/kubernetes-handbook/rbac/) and service mesh policies.

---

## Observability

Export RED metrics, structured logs with `trace_id`, and distributed traces on every cross-service hop. See [Observability](/microservices/08-observability/observability/).

---

## Architect Notes

Canonical page for **Zero-Downtime Deployments**. Cross-handbook depth: link out, do not duplicate broker/DB/cache engine internals.
