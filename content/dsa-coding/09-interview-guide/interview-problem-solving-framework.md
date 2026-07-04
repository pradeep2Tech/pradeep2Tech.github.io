---
title: "Interview Problem-Solving Framework"
date: 2026-07-04T00:00:00+00:00
draft: false
description: "Interview Framework"
tags: ["dsa-coding", "dsa", "algorithms", "interview"]
categories: ["DSA & Coding"]
shortTitle: "Interview Framework"
module: 9
moduleTitle: "DSA & Coding"
sectionRef: "9.0"
weight: 900
interviewHandbook: true
---

# Interview Problem-Solving Framework

Architect-grade flow for 45-minute coding rounds. Use with [Pattern Recognition Table](/dsa-coding/09-interview-guide/pattern-recognition-table/).

---

## Step 1 — Understand the Problem

Restate in your own words. Identify inputs, outputs, and implicit ordering.

---

## Step 2 — Clarify Requirements

- Empty input? Duplicates? Negative numbers?
- One answer or all? In-place?
- Time/space expectations?

---

## Step 3 — Analyze Constraints

Derive complexity budget: n ≤ 10⁵ → ~O(n log n); n ≤ 10³ → O(n²) may pass.

---

## Step 4 — Identify Pattern

Map signals to **one primary module** (never re-derive fundamentals on the problem page):

| Need | Primary reference |
| :--- | :--- |
| Fast lookup / frequency | [Module 1](/dsa-coding/01-arrays-hashmap-two-pointers/) |
| Contiguous window / prefix | [Module 2](/dsa-coding/02-sliding-window-prefix-sum/) |
| Sorted / feasibility | [Module 3](/dsa-coding/03-binary-search/) |
| Generate / search state space | [Module 4](/dsa-coding/04-recursion-backtracking/) |
| Tree structure | [Module 5](/dsa-coding/05-trees/) |
| Grid/graph connectivity | [Module 6](/dsa-coding/06-graphs/) |
| Ordering constraints | [Module 7](/dsa-coding/07-advanced-graphs/) |
| Optimal substructure | [Module 8](/dsa-coding/08-dynamic-programming/) |

---

## Step 5 — Build Brute Force

State naive approach and complexity — establishes optimization delta.

---

## Step 6 — Analyze Complexity

Compare brute vs target; name bottleneck (nested loop, resorting, etc.).

---

## Step 7 — Optimize

Apply one pattern from the canonical module. **Cross-link, don't re-teach.**

---

## Step 8 — Code

Java or Go per problem page; narrate invariant while writing.

---

## Step 9 — Dry Run

Walk smallest non-trivial example; hit one edge case.

---

## Step 10 — Discuss Tradeoffs

Time, space, alternative patterns, when approach fails.

---

## Step 11 — Handle Follow-Ups

See problem page **Interview Follow-ups**; extend pattern (k-sum, stream, memory limits).

---

## Quick Revision

Clarify → Pattern (link module) → Brute → Optimize → Code → Dry run → Tradeoffs.
