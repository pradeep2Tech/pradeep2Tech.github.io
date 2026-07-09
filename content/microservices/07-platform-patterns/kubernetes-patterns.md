---
title: "Kubernetes Patterns for Microservices"
date: 2026-07-03T15:00:00+00:00
draft: false
description: "Deployments, Services, HPA, PDB, probes, and config for service fleets."
tags: ["microservices", "architecture-playbook", "distributed-systems"]
categories: ["Microservices Architecture Playbook"]
shortTitle: "K8s Patterns"
module: 7
moduleTitle: "Platform Patterns"
sectionRef: "7.2"
weight: 702
playbookVersion: 3
aliases:
  - "/microservices/declarative-container-orchestration-kubernetes/"
  - "/microservices/application-containerization-docker/"
  - "/microservices/externalized-configuration-management/"
---

## Executive Summary

Run microservices on K8s with safe rollout and discovery.

---

## Where It Fits

Primitives: [Kubernetes Handbook](/kubernetes-handbook/).

---

## Security Considerations

Apply zero-trust between services, mTLS in mesh, and least-privilege credentials per service identity. See [Kubernetes RBAC](/kubernetes-handbook/rbac/) and service mesh policies.

---

## Observability

Export RED metrics, structured logs with `trace_id`, and distributed traces on every cross-service hop. See [Observability](/microservices/08-observability/observability/).

---

## Architect Notes

Canonical page for **Kubernetes Patterns for Microservices**. Cross-handbook depth: link out, do not duplicate broker/DB/cache engine internals.
