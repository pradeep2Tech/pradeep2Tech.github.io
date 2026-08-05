---
title: "Architecture Deliverables Cheat Sheet"
date: 2026-08-05T00:00:00+05:30
draft: true
description: "One-page map from decisions and audiences to the minimum useful architecture artifact and its quality criteria."
tags: ["architecture-discovery", "cheat-sheet", "deliverables"]
categories: ["Architecture Discovery"]
shortTitle: "Architecture Deliverables"
module: 4
moduleTitle: "Applied Resources"
contentType: "cheat-sheet"
difficulty: "advanced"
estimatedReadingTime: 6
interviewImportance: "high"
enterpriseImportance: "high"
prerequisites: ["Discovery Closure and Architecture Handoff"]
dependencies: ["risk/discovery-closure-and-architecture-handoff"]
---

## Choose by Decision

| Need | Minimum useful artifact |
|---|---|
| Outcomes/scope | Business requirements or decision brief |
| Observable behavior | Functional requirements/use-case catalogue |
| Quality commitments | NFR specification with scenarios/evidence |
| Language/ownership | Domain model |
| Scope/dependencies | System context diagram |
| User experience | User journey |
| Enterprise abilities | Capability model |
| Work/control flow | Business process model |
| Data meaning/lifecycle | Enterprise data model |
| Interfaces/contracts | Integration/API catalogue |
| Trust/controls | Security architecture |
| Runtime/operations | Deployment architecture |
| Whole solution decision | Solution architecture document |
| Transition/waves | Modernization roadmap |
| Exposure | Risk register |
| Decision history | Decision log and ADR index |

## Every Artifact Needs

Purpose, audience, scope, owner, status/version, evidence date, source links, decisions supported, assumptions, dependencies, quality check, review/expiry, and access classification.

## Quality Tests

- Decision-focused: content changes or validates a decision.
- Evidence-backed: facts cite sources and confidence.
- Traceable: identifiers connect outcomes, requirements, decisions, risks, and tests.
- Bounded: current, target, transition, and exclusions are clear.
- Owned: approval, update, and retirement responsibilities exist.
- Usable: intended audience can act without oral reconstruction.

## Avoid

- one document for every audience;
- duplicated requirements that drift;
- diagrams with unlabeled semantics;
- artifact completion used as discovery completion;
- workshop drafts presented as authoritative baselines;
- deliverables without lifecycle and review trigger.

Detailed guides begin at [Architecture Deliverables](/architecture-discovery/deliverables/).
