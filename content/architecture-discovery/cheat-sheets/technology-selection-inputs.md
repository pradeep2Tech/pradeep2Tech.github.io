---
title: "Technology Selection Inputs Cheat Sheet"
date: 2026-08-05T00:00:00+05:30
draft: true
description: "Compact reference for estate evidence, workload, constraints, criteria, experiments, economics, operations, transition, and ADR inputs."
tags: ["architecture-discovery", "cheat-sheet", "technology-selection"]
categories: ["Architecture Discovery"]
shortTitle: "Technology Selection Inputs"
module: 4
moduleTitle: "Applied Resources"
contentType: "cheat-sheet"
difficulty: "advanced"
estimatedReadingTime: 5
interviewImportance: "critical"
enterpriseImportance: "high"
prerequisites: ["Technology Discovery"]
dependencies: ["technology", "technology/standards-constraints-and-technical-debt", "technology/technology-decision-inputs"]
---

## Decision Order

Outcome → workload → governing quality scenarios → obligations/constraints → viable architecture → criteria → experiments → technology → ADR.

## Workload Profile

- interaction and state model;
- request mix, rate, concurrency, burst, seasonality;
- data size, growth, hot keys, locality, history;
- latency, consistency, availability, recovery;
- security, tenancy, residency, audit;
- change rate, compatibility, operations, and skills.

## Classify Inputs

| Input | Treatment |
|---|---|
| Obligation | Mandatory source and scope |
| Constraint | Verify owner, consequence, trigger |
| Standard | Applicability, version, exception |
| Paved road | Supported fit and SLO |
| Preference | Low-priority default |
| Assumption | Validate before sensitive decision |
| Debt | Condition, consequence, trajectory |

## Evaluation

- Gate: option is viable or eliminated.
- Weighted criterion: ranks viable options.
- Risk: scenario and treatment, not feature score.
- Uncertainty: evidence confidence and sensitivity.
- Portfolio effect: concentration, reuse, capacity, exit.

## Good Experiment

Hypothesis, representative conditions, predefined threshold, compared options, owner/timebox, evidence, limitations, and decision impact. Test consequential uncertainty such as saturation, recovery, compatibility, isolation, change effort, or cost.

## Total Cost

Include license, infrastructure, transfer, environments, support, operations, controls, observability, skills, migration, coexistence, downtime, and exit.

## Red Flags

- criteria written after choosing a product;
- feature count unrelated to workload;
- benchmark treated as end-to-end proof;
- product compared without operating model and transition;
- no portability, supplier, or exit analysis.

Detailed guide: [Technology Decision Inputs](/architecture-discovery/technology/technology-decision-inputs/).
