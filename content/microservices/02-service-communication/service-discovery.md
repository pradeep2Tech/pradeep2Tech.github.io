---
title: "Service Discovery"
date: 2026-07-03T15:00:00+00:00
draft: false
description: "Client-side vs server-side discovery, registry consensus, and Kubernetes DNS abstraction."
tags: ["microservices", "architecture-playbook", "distributed-systems"]
categories: ["Microservices Architecture Playbook"]
shortTitle: "Service Discovery"
module: 2
moduleTitle: "Service Communication"
sectionRef: "2.2"
weight: 202
ShowToc: true
playbookVersion: 3
aliases:
  - "/microservices/dynamic-service-discovery-registry/"
---

## Executive Summary

Services must find healthy instances without hardcoded endpoints.

---

## Where It Fits

Between gateway and internal service mesh routing.

---

## Security Considerations

Apply zero-trust between services, mTLS in mesh, and least-privilege credentials per service identity. See [Kubernetes RBAC](/kubernetes-handbook/rbac/) and service mesh policies.

---

## Observability

Export RED metrics, structured logs with `trace_id`, and distributed traces on every cross-service hop. See [Observability](/microservices/08-observability/observability/).

---

## Architect Notes

Canonical page for **Service Discovery**. Cross-handbook depth: link out, do not duplicate broker/DB/cache engine internals.
