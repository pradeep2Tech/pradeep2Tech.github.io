---
title: "NFR Discovery Cheat Sheet"
date: 2026-08-05T00:00:00+05:30
draft: true
description: "Compact reference for quality scenarios, priorities, conflicts, budgets, acceptance, evidence, exceptions, and operational traceability."
tags: ["architecture-discovery", "cheat-sheet", "nfr"]
categories: ["Architecture Discovery"]
shortTitle: "NFR Discovery"
module: 4
moduleTitle: "Applied Resources"
contentType: "cheat-sheet"
difficulty: "advanced"
estimatedReadingTime: 6
interviewImportance: "critical"
enterpriseImportance: "critical"
prerequisites: ["Non-Functional Discovery"]
dependencies: ["non-functional-discovery", "non-functional-discovery/nfr-prioritization-and-conflict-resolution", "non-functional-discovery/nfr-acceptance-and-traceability"]
---

## Quality Scenario

**Source + stimulus + affected artifact + environment + response + measure + owner/evidence.**

Example: During peak, when 1,500 verified submissions arrive per second, accepted requests complete within 800 ms p99, no committed outcome is lost, and overload is visible before the recovery window is breached.

## Attribute Prompts

| Attribute | Ask |
|---|---|
| Availability | Which journey, failure, window, degradation, dependency? |
| Performance | Which workload, percentile, boundary, saturation? |
| Reliability | What loss, duplicate, ordering, integrity, convergence? |
| Recovery | Which capability, RTO/RPO, restore, reconciliation? |
| Security/privacy | Which asset, actor, trust, abuse, control response? |
| Operability | What must operators detect, diagnose, and change safely? |
| Modifiability | Which change, frequency, lead time, regression scope? |
| Accessibility | Which actor/context and equivalent task outcome? |
| Cost | Which workload driver, unit, range, quality constraint? |

## Priority

- Governing: option fails if unmet.
- Differentiating: materially ranks viable options.
- Necessary: standard baseline and evidence.
- Monitor: uncertain/low consequence; reassess on trigger.

## Common Tradeoffs

Availability–consistency, latency–control, resilience–cost, autonomy–standardization, delivery speed–assurance, observability–privacy, flexibility–simplicity.

## Acceptance

Define baseline, target, workload, environment, validation, evidence owner, production indicator, dependency budget, exception authority, and trigger. Test the end-to-end outcome, not only components.

## Red Flags

- adjectives without scenarios;
- averages without distributions;
- targets unsupported by dependency contracts;
- infrastructure recovery mistaken for business recovery;
- every NFR marked critical;
- waiver without expiry and monitoring.

Detailed guide: [Quality-Attribute Discovery](/architecture-discovery/non-functional-discovery/).
