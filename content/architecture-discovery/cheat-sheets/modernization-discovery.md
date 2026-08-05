---
title: "Modernization Discovery Cheat Sheet"
date: 2026-08-05T00:00:00+05:30
draft: true
description: "Compact reference for modernization drivers, assessment, dispositions, coexistence, waves, readiness, retirement, and fitness."
tags: ["architecture-discovery", "cheat-sheet", "modernization"]
categories: ["Architecture Discovery"]
shortTitle: "Modernization Discovery"
module: 4
moduleTitle: "Applied Resources"
contentType: "cheat-sheet"
difficulty: "advanced"
estimatedReadingTime: 6
interviewImportance: "critical"
enterpriseImportance: "critical"
prerequisites: ["Modernization Discovery"]
dependencies: ["modernization", "modernization/application-and-component-assessment", "modernization/modernization-disposition-decisions", "modernization/transition-and-coexistence-architecture", "modernization/migration-waves-and-dependency-sequencing", "modernization/modernization-readiness-and-fitness-measures"]
---

## Outcome First

Driver → baseline → measurable outcome → capability/process change → assessment scope → disposition → transition → wave → fitness/benefit.

## Assess

Business value, functional fit, architecture/changeability, technology lifecycle, data, integration, security/control, operations, delivery, economics, dependencies, readiness, and confidence. Preserve decisive dimensions; do not average them away.

## Dispositions

Retain, retire, consolidate, replace/repurchase, rehost, replatform, refactor, or rebuild. Apply at the assessment-unit level, not automatically to an entire application.

## Transition State

| Concern | Decide |
|---|---|
| Routing | Cohort, authority, affinity, fallback |
| Data | Attribute authority, sync, conflict, correction |
| Compatibility | Versions, adapters, consumer migration |
| Control | Identity, audit, privacy, reconciliation |
| Operations | Ownership, telemetry, capacity, incident |
| Recovery | Rollback window, forward repair, validation |
| Exit | Traffic/consumer/data/control retirement proof |

## Wave

Deliver a bounded outcome; respect hard dependencies; test high-consequence assumptions early; limit coexistence; include operations/adoption; pair migration with retirement; define entry and exit evidence.

## Readiness

Outcome/governance, domain/product, engineering, platform, data, integration, security, operations, commercial, and organizational change.

## Fitness

Measure outcome, quality, boundary conformance, delivery, operations, transition debt, legacy traffic, control, recovery, and unit cost. Every threshold needs an owner and response.

## Red Flags

- cloud or microservices used as outcome;
- application age used as assessment;
- rehost promised to remove architecture coupling;
- dual write without authority and reconciliation;
- waves that start everything and retire nothing;
- readiness self-attested without evidence.

Detailed guide: [Modernization Drivers and Scope](/architecture-discovery/modernization/).
