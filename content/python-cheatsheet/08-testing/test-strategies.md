---
title: "Test Strategies"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "CI stages: lint → typecheck → unit → integration. Coverage targets on critical paths; `hypothesis` for property tests."
tags: ["python", "python-cheatsheet", "handbook", "interview"]
categories: ["Python Handbook"]
shortTitle: "Test Strategy"
module: 8
moduleTitle: "Testing"
sectionRef: "8.4"
weight: 804
ShowToc: true
interviewHandbook: true
---

## Quick Revision

- CI gates: ruff/mypy → unit → integration.
- Property-based (`hypothesis`) for parsers and serializers.
- Record/replay fixtures for external APIs — scrub secrets.

## Core Concepts

| Strategy | Purpose |
| :--- | :--- |
| Contract tests | API schema stability |
| Property-based | Edge case discovery |
| Snapshot tests | Careful — avoid brittle JSON dumps |
| Load tests | Separate pipeline, not every PR |

## Production Usage

- Mark slow tests; run nightly if needed.
- Flaky test policy: fix or quarantine — never ignore.
- Test minimum Python version from `requires-python`.

## Common Mistakes

- Chasing 100% coverage on UI glue code.
- Parallel integration tests on shared DB without isolation.



## Interview Questions

See [Top 150](/python-cheatsheet/09-interview-guide/top-150-interview-questions/).

---

## See Also

- [Previous: Mocking](/python-cheatsheet/08-testing/mocking/)
- [Python Handbook Index](/python-cheatsheet/)
- [Top 150 Interview Questions](/python-cheatsheet/09-interview-guide/top-150-interview-questions/)
