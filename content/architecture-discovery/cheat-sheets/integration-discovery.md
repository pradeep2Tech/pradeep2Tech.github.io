---
title: "Integration Discovery Cheat Sheet"
date: 2026-08-05T00:00:00+05:30
draft: true
description: "One-page reference for integration landscape, contracts, dependencies, timing, failure semantics, recovery, security, and governance."
tags: ["architecture-discovery", "cheat-sheet", "integration"]
categories: ["Architecture Discovery"]
shortTitle: "Integration Discovery"
module: 4
moduleTitle: "Applied Resources"
contentType: "cheat-sheet"
difficulty: "advanced"
estimatedReadingTime: 6
interviewImportance: "critical"
enterpriseImportance: "critical"
prerequisites: ["Integration Discovery"]
dependencies: ["integration", "integration/integration-requirements-and-failure-semantics", "integration/integration-and-api-catalog-governance"]
---

## Integration Record

| Concern | Capture |
|---|---|
| Purpose | Outcome, scenario, intent: command/event/query/transfer |
| Parties | Provider, consumers, semantic and operational owners |
| Contract | Meaning, input/output, errors, version, policy |
| Data | Authority, classification, volume, lifecycle |
| Timing | Sync/async, deadline, frequency, latency |
| Guarantees | Delivery, ordering scope, idempotency, consistency |
| Failure | Timeout, ambiguity, retry, degradation, recovery |
| Security | Identity, authorization, trust, protection, audit |
| Operations | SLO, telemetry, support, incident, lifecycle |

## Failure Semantics

- Timeout means unknown, not necessarily failed.
- Use a stable business idempotency key.
- Define status query, pending visibility, retry deadline, and reconciliation.
- Specify loss, duplication, delay, replay, and late-event behavior.
- Coordinate retries across layers to avoid amplification.

## Dependency Mapping

Trace beyond the first hop: identity, network, DNS, certificates, secrets, brokers, shared data, telemetry, deployment, suppliers, and human support. Criticality is scenario-specific.

## Contract Evolution

Structural compatibility is not semantic compatibility. Govern meaning, behavior, timing, security, operational guarantees, known consumers, migration, deprecation, and retirement evidence.

## Catalogue Health

Measure observed coverage, owners, verification freshness, consumer registration, contract availability, deprecated traffic, orphan interfaces, and runbook/dashboard links.

## Red Flags

- protocol inventory without business purpose;
- global ordering or “exactly once” without business need;
- eventual consistency without convergence deadline;
- provider documentation without consumer validation;
- zero traffic used as sole retirement proof.

Detailed guide: [Integration Landscape and Dependency Mapping](/architecture-discovery/integration/).
