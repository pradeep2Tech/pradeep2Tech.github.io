---
title: "Architecture Reviews Cheat Sheet"
date: 2026-08-05T00:00:00+05:30
draft: true
description: "Compact reference for evidence gates, review probes, authority, outcomes, conditions, waivers, actions, and reassessment triggers."
tags: ["architecture-discovery", "cheat-sheet", "architecture-review"]
categories: ["Architecture Discovery"]
shortTitle: "Architecture Reviews"
module: 4
moduleTitle: "Applied Resources"
contentType: "cheat-sheet"
difficulty: "advanced"
estimatedReadingTime: 5
interviewImportance: "critical"
enterpriseImportance: "critical"
prerequisites: ["Architecture Reviews and Reassessment Triggers", "Architecture Review Checklist"]
dependencies: ["risk/architecture-reviews-and-reassessment-triggers", "checklists/architecture-review-checklist"]
---

## Review the Decision

State decision, authority, scope, deadline, outcomes, reversibility, and permitted review results. Review evidence and tradeoffs—not document polish.

## Evidence Package

- current context and reason for change;
- findings and confidence;
- measurable requirements and quality scenarios;
- constraints, assumptions, dependencies, and risks;
- viable options and rejected alternatives;
- experiments, cost, transition, and operations;
- recommendation, conditions, residual risk, measures, triggers.

## Core Probes

1. Does each option pass mandatory obligations and invariants?
2. Are quality budgets feasible across dependencies?
3. Are domain/data authority and failure semantics explicit?
4. Are trust, controls, operations, recovery, and delivery credible?
5. Is transition viable, bounded, and reversible where claimed?
6. Which uncertainty is decision-sensitive?
7. Who accepts consequence and owns follow-up?

## Outcomes

- Approve.
- Approve with bounded conditions.
- Request targeted evidence/experiment.
- Reject or reframe.
- Confirm, amend, supersede, or retire an existing decision.

## Condition/Waiver Minimum

Scope, required evidence/control, owner, deadline, monitoring, residual consequence, acceptance authority, expiry, and failure response.

## Reassessment Triggers

Workload, criticality, geography, data class, obligation, dependency, provider, cost, lifecycle, incident, recovery result, assumption, quality threshold, transition duration, or ownership change.

## Red Flags

- board accepting risk outside its authority;
- unwritten preference enforced as standard;
- “address later” without owner and gate;
- same process for every risk level;
- review record missing dissent and triggers.

Full asset: [Architecture Review Checklist](/architecture-discovery/checklists/architecture-review-checklist/).
