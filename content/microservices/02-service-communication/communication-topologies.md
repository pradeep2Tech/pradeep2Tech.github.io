---
title: "Communication Topologies"
date: 2026-07-03T15:00:00+00:00
draft: false
description: "Sync vs async boundaries, gRPC hot paths, trace propagation, and command/query routing."
tags: ["microservices", "architecture-playbook", "distributed-systems"]
categories: ["Microservices Architecture Playbook"]
shortTitle: "Comm Topologies"
module: 2
moduleTitle: "Service Communication"
sectionRef: "2.3"
weight: 203
ShowToc: true
playbookVersion: 3
aliases:
  - "/microservices/microservices-communication-topologies/"
---

## Executive Summary

Sync for queries; async for commands — the default hybrid topology.

---

## Where It Fits

Core integration decision for every cross-service interaction.

---

## Security Considerations

Apply zero-trust between services, mTLS in mesh, and least-privilege credentials per service identity. See [Kubernetes RBAC](/kubernetes-handbook/rbac/) and service mesh policies.

---

## Observability

Export RED metrics, structured logs with `trace_id`, and distributed traces on every cross-service hop. See [Observability](/microservices/08-observability/observability/).

---

## Architect Notes

Canonical page for **Communication Topologies**. Cross-handbook depth: link out, do not duplicate broker/DB/cache engine internals.
