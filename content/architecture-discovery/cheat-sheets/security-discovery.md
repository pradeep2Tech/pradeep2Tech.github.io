---
title: "Security Discovery Cheat Sheet"
date: 2026-08-05T00:00:00+05:30
draft: true
description: "One-page reference for assets, actors, trust, abuse cases, obligations, control evidence, gaps, treatment, and risk acceptance."
tags: ["architecture-discovery", "cheat-sheet", "security"]
categories: ["Architecture Discovery"]
shortTitle: "Security Discovery"
module: 4
moduleTitle: "Applied Resources"
contentType: "cheat-sheet"
difficulty: "advanced"
estimatedReadingTime: 6
interviewImportance: "critical"
enterpriseImportance: "critical"
prerequisites: ["Security Discovery"]
dependencies: ["security", "security/compliance-controls-and-evidence", "security/security-gaps-and-risk-acceptance"]
---

## Discovery Chain

Asset/outcome → actor/capability → trust boundary → abuse path → current control evidence → gap → requirement/treatment → residual acceptance.

## Asset and Actor

Capture business harm to money, safety, continuity, identity, data, code/configuration, evidence, recovery, and reputation. Include customers, staff, administrators, support, workloads, devices, partners, suppliers, and attackers.

## Trust-Boundary Record

- parties and ownership;
- identity assurance and credentials;
- permitted actions and data;
- authorization and validation point;
- protection, replay/abuse controls;
- monitoring, failure, revocation, recovery;
- evidence and lifecycle owner.

## Abuse Cases

Impersonate, elevate, delegate improperly, repeat/reorder, alter state, enumerate, exfiltrate, poison, destroy, exhaust, compromise supply chain, abuse recovery/support, or conceal evidence.

## Obligation-to-Evidence

Source → applicability → obligation → control intent → implementation → design/operating evidence → validation → finding/exception.

## Risk Acceptance

Specify exact scope, residual scenario, current/compensating controls, evidence, consequence, monitoring, remediation owner, authorized acceptor, effective/expiry dates, and reassessment triggers.

## Red Flags

- generic checklist before assets and harm;
- trusted network or managed service assumed safe;
- privileged/support paths omitted;
- policy/certification treated as operating proof;
- exception without expiry or independent compensation;
- security team accepting business risk.

Detailed guide: [Security Discovery: Assets, Actors, and Trust](/architecture-discovery/security/). Implementation patterns: [Security Architecture](/security-architecture/).
