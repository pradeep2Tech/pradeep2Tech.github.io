---
title: "{{ replace .File.ContentBaseName "-" " " | title }}"
date: {{ .Date }}
draft: true
description: ""
tags: ["architecture-discovery", "architecture-pattern"]
categories: ["Architecture Discovery"]
shortTitle: ""
contentType: "architecture-pattern"
difficulty: "advanced"
estimatedReadingTime: 25
interviewImportance: "high"
enterpriseImportance: "critical"
prerequisites: []
dependencies: []
---

<!-- Use only for a repeatable discovery or governance pattern, not an implementation pattern owned elsewhere. -->

## Problem and Forces

## Applicability

| Use when | Avoid when |
|---|---|
| | |

## Pattern Structure

```mermaid
flowchart LR
    Trigger[Trigger] --> Roles[Roles and responsibilities]
    Roles --> Process[Pattern workflow]
    Process --> Artifacts[Governed artifacts]
    Artifacts --> Decision[Decision or review]
```

## Participants and Responsibilities

## Workflow

## Evidence and Artifacts

## Enterprise Example

## Variants

## Tradeoffs

| Benefit | Cost or risk | Mitigation |
|---|---|---|
| | | |

## Failure Modes and Anti-Patterns

## Architecture Review Notes

## Interview Questions

## Summary

## Related Patterns and Canonical Guidance

