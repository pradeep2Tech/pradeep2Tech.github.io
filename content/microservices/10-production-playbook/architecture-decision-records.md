---
title: "Architecture Decision Records"
date: 2026-07-03T15:00:00+00:00
draft: false
description: "ADR process, tradeoff documentation, and architecture governance."
tags: ["microservices", "architecture-playbook", "distributed-systems"]
categories: ["Microservices Architecture Playbook"]
shortTitle: "ADRs"
module: 10
moduleTitle: "Production Playbook"
sectionRef: "10.5"
weight: 1005
ShowToc: true
playbookVersion: 3
---

## Executive Summary

Architecture Decision Records (ADRs) capture **context, decision, and consequences** for significant technical choices — essential when many teams share a microservices platform.

---

## Problem It Solves

Tribal knowledge loss; repeated debates; unclear why Kafka vs queue, mesh vs library, saga vs 2PC.

---

## Where It Fits

Platform guild, architecture review board, and service team onboarding.

---

## Internal Working

ADR template: Title · Status · Context · Decision · Consequences · Alternatives considered.

---

## Design Decisions

Immutable ADRs — supersede with new ADR rather than edit history.

---

## Tradeoffs

Lightweight Markdown ADRs vs heavy tooling (Architectural Decision Records in Confluence).

---

## Scalability

Index ADRs by tag: data, messaging, security, deployment.

---

## Reliability

Link ADRs to runbooks and failure scenarios.

---

## Security Considerations

Record threat model assumptions in security ADRs.

---

## Observability

ADR for tracing standard (OpenTelemetry) and log schema.

---

## Production Lessons

Review ADRs quarterly; mark superseded explicitly.

---

## Common Failures

ADRs written after decision — no alternative analysis.

---

## Common Mistakes

No consequences section; vague decision statement.

---

## Interview Questions

1. What belongs in an ADR vs a design doc?
2. How do you supersede a bad ADR?

---

## Architect Notes

Technology evaluation matrices live in [Technology Playbook](/technology-playbook/) — ADR references them.
