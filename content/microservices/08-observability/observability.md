---
title: "Observability"
date: 2026-07-03T15:00:00+00:00
draft: false
description: "Metrics, logs, traces, RED/USE, sampling, and correlated telemetry."
tags: ["microservices", "architecture-playbook", "distributed-systems"]
categories: ["Microservices Architecture Playbook"]
shortTitle: "Observability"
module: 8
moduleTitle: "Observability"
sectionRef: "8.1"
weight: 801
ShowToc: true
playbookVersion: 3
aliases:
  - "/microservices/three-pillars-observability/"
  - "/microservices/distributed-tracing-log-aggregation/"
---

## Executive Summary

Three pillars plus correlation IDs on every hop.

---

## Where It Fits

SRE and on-call foundation.

---

## Security Considerations

Apply zero-trust between services, mTLS in mesh, and least-privilege credentials per service identity. See [Kubernetes RBAC](/kubernetes-handbook/rbac/) and service mesh policies.

---

## Observability

Export RED metrics, structured logs with `trace_id`, and distributed traces on every cross-service hop. See [Observability](/microservices/08-observability/observability/).

---

## Architect Notes

Canonical page for **Observability**. Cross-handbook depth: link out, do not duplicate broker/DB/cache engine internals.
