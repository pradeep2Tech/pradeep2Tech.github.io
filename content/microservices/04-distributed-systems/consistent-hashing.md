---
title: "Consistent Hashing"
date: 2026-07-03T15:00:00+00:00
draft: false
description: "Hash rings, virtual nodes, minimal migration on scale, sloppy quorum."
tags: ["microservices", "architecture-playbook", "distributed-systems"]
categories: ["Microservices Architecture Playbook"]
shortTitle: "Consistent Hashing"
module: 4
moduleTitle: "Distributed Systems"
sectionRef: "4.2"
weight: 402
playbookVersion: 3
aliases:
  - "/microservices/consistent-hashing-rings-virtual-nodes/"
---

## Executive Summary

Route keys to shards with bounded movement on node churn.

---

## Where It Fits

Sharding gateways, caches, and distributed stores.

---

## Security Considerations

Apply zero-trust between services, mTLS in mesh, and least-privilege credentials per service identity. See [Kubernetes RBAC](/kubernetes-handbook/rbac/) and service mesh policies.

---

## Observability

Export RED metrics, structured logs with `trace_id`, and distributed traces on every cross-service hop. See [Observability](/microservices/08-observability/observability/).

---

## Architect Notes

Canonical page for **Consistent Hashing**. Cross-handbook depth: link out, do not duplicate broker/DB/cache engine internals.
