---
title: "Messaging & Streaming Patterns"
date: 2026-07-03T15:00:00+00:00
draft: false
description: "Point-to-point queues, pub/sub vs log streaming, idempotent consumers, DLQ."
tags: ["microservices", "architecture-playbook", "distributed-systems"]
categories: ["Microservices Architecture Playbook"]
shortTitle: "Messaging"
module: 6
moduleTitle: "Event-Driven Architecture"
sectionRef: "6.2"
weight: 602
playbookVersion: 3
aliases:
  - "/microservices/point-to-point-message-queues/"
---

## Executive Summary

Choose queue vs log by replay, ordering, and throughput needs.

---

## Where It Fits

Links to [Kafka Handbook](/kafka-handbook/) for broker internals.

---

## Security Considerations

Apply zero-trust between services, mTLS in mesh, and least-privilege credentials per service identity. See [Kubernetes RBAC](/kubernetes-handbook/rbac/) and service mesh policies.

---

## Observability

Export RED metrics, structured logs with `trace_id`, and distributed traces on every cross-service hop. See [Observability](/microservices/08-observability/observability/).

---

## Architect Notes

Canonical page for **Messaging & Streaming Patterns**. Cross-handbook depth: link out, do not duplicate broker/DB/cache engine internals.
