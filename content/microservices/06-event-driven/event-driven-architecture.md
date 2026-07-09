---
title: "Event-Driven Architecture"
date: 2026-07-03T15:00:00+00:00
draft: false
description: "Temporal decoupling, eventual consistency, and EDA failure modes at architect level."
tags: ["microservices", "architecture-playbook", "distributed-systems"]
categories: ["Microservices Architecture Playbook"]
shortTitle: "EDA"
module: 6
moduleTitle: "Event-Driven Architecture"
sectionRef: "6.1"
weight: 601
playbookVersion: 3
aliases:
  - "/microservices/event-driven-architecture-log-streaming/"
---

## Executive Summary

Decouple services via events instead of sync chains.

---

## Where It Fits

Async integration backbone — broker details in Kafka Handbook.

---

## Security Considerations

Apply zero-trust between services, mTLS in mesh, and least-privilege credentials per service identity. See [Kubernetes RBAC](/kubernetes-handbook/rbac/) and service mesh policies.

---

## Observability

Export RED metrics, structured logs with `trace_id`, and distributed traces on every cross-service hop. See [Observability](/microservices/08-observability/observability/).

---

## Architect Notes

Canonical page for **Event-Driven Architecture**. Cross-handbook depth: link out, do not duplicate broker/DB/cache engine internals.
