---
title: "Monolith Decomposition"
date: 2026-07-03T15:00:00+00:00
draft: false
description: "Domain-driven extraction of bounded contexts from a modular monolith."
tags: ["microservices", "architecture-playbook", "distributed-systems"]
categories: ["Microservices Architecture Playbook"]
shortTitle: "Monolith Decomposition"
module: 9
moduleTitle: "Migration & Modernization"
sectionRef: "9.2"
weight: 902
playbookVersion: 3
---

## Executive Summary

Monolith decomposition splits a single deployable by **bounded context** and team ownership — before or in parallel with database and traffic migration.

---

## Problem It Solves

Teams blocked on shared release cadence; unclear ownership; modules coupled through shared packages and DB.

---

## Where It Fits

After strangler identifies target capability; before database-per-service cutover.

---

## Internal Working

1. Identify bounded contexts (DDD event storming).
2. Extract module boundaries in monolith (package/module seams).
3. Define public API per context.
4. Assign team per context.
5. Extract hottest or most isolated context first.

---

## Design Decisions

Decompose by **organizational bottleneck** (Conway's Law), not CPU metrics alone.

---

## Tradeoffs

Premature decomposition adds network tax without team autonomy benefit.

---

## Scalability

Extract services that need independent scale first (e.g., notifications).

---

## Reliability

Each extraction adds failure domains — invest in observability before split.

---

## Security Considerations

Define service-to-service auth as contexts split.

---

## Observability

Distributed tracing mandatory before second extracted service goes live.

---

## Production Lessons

Keep anti-corruption layers at legacy boundaries.

---

## Common Failures

Distributed monolith — many services, one shared database.

---

## Common Mistakes

Big-bang rewrite; extracting without stable APIs.

---

## Interview Questions

1. How do you choose the first service to extract?
2. What is a distributed monolith?

---

## Architect Notes

Pairs with [Strangler Pattern](/microservices/09-migration-modernization/strangler-pattern/) and [Database Decomposition](/microservices/09-migration-modernization/database-decomposition/).
