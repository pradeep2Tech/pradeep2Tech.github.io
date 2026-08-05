---
title: "Functional Discovery Cheat Sheet"
date: 2026-08-05T00:00:00+05:30
draft: true
description: "One-page reference for actors, journeys, use cases, scenarios, exceptions, functional rules, state, and acceptance."
tags: ["architecture-discovery", "cheat-sheet", "functional-discovery"]
categories: ["Architecture Discovery"]
shortTitle: "Functional Discovery"
module: 4
moduleTitle: "Applied Resources"
contentType: "cheat-sheet"
difficulty: "intermediate"
estimatedReadingTime: 5
interviewImportance: "high"
enterpriseImportance: "high"
prerequisites: ["Functional Discovery"]
dependencies: ["functional-discovery", "functional-discovery/use-cases-scenarios-and-scope", "functional-discovery/functional-rules-and-acceptance-boundaries"]
---

## Flow

Actor goal → journey stage → use case → scenario → rule/state → acceptance evidence.

## Actor Record

- goal and success;
- authority and delegation;
- channel, context, frequency, volume;
- accessibility and assistance needs;
- knowledge, incentives, and evidence.

## Scenario Set

For every priority goal include:

- normal success;
- valid alternate path;
- missing/invalid/duplicate input;
- unauthorized or delegated action;
- dependency timeout or ambiguous outcome;
- concurrency and late arrival;
- retry, resume, compensate, reconcile, escalate, abandon;
- acceptance and operational evidence.

## Use-Case Minimum

| Field | Content |
|---|---|
| Goal/actors | Actor-valued result and participants |
| Trigger | Observable start |
| Preconditions | Verified required state |
| Success guarantee | State after success |
| Minimal guarantee | State preserved after failure |
| Boundary | In scope, dependency, constraint, exclusion |
| Rules/quality | Referenced, owned, measurable |

## Rule Types

Validation, authorization, eligibility, calculation, state transition, temporal, exception, evidence, and retention. Record source, owner, effective date, version, exception, and examples.

## Acceptance Pattern

Given context and authoritative state, when an authorized actor performs an action, then observable outcome/state occurs within a measurable boundary and required evidence is produced.

## Red Flags

- requirements organized around screens;
- only happy-path steps;
- vague “manage/support/process” verbs;
- hidden manual work or asynchronous state;
- solution technology embedded without authority;
- acceptance that omits failure and recovery.

Detailed guide: [Personas, Actors, and User Journeys](/architecture-discovery/functional-discovery/).
