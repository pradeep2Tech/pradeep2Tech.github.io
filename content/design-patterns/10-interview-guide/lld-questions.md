---
title: "LLD Design Questions"
date: 2026-07-03T14:00:00+00:00
draft: false
description: "LLD Design Questions — interview question bank."
tags: ["design-patterns", "lld", "interview"]
categories: ["Design Patterns"]
shortTitle: "LLD"
module: 10
moduleTitle: "Interview Guide"
sectionRef: "10.5"
weight: 1005
interviewHandbook: true
---

Questions only — no answers. Sourced from [Top 150](/design-patterns/10-interview-guide/top-150-design-pattern-questions/).

# LLD Design Questions

1. What entities and relationships would you model for a multi-floor parking lot with concurrency?
2. How do you design spot allocation to avoid double-booking under concurrent entry?
3. What pricing strategies would you plug into a parking lot without changing allocation?
4. How do you model elevator state machines for idle, moving, and door-open phases?
5. What scheduling algorithm tradeoffs exist between SCAN and LOOK for elevator dispatch?
6. How would you design a token-bucket rate limiter for a sliding one-minute window?
7. What thread-safety approach would you use for in-memory rate limiting at high RPS?
8. How do you design multi-channel notification with retry and idempotency keys?
9. What domain boundaries separate template rendering from delivery in a notification service?
10. How would you model task priority and cancellation in a scheduler LLD?
11. What Command pattern role does a task scheduler play for undo and audit?
12. How do you design rider-driver matching with surge pricing in ride sharing?
13. What geospatial indexing concerns affect nearest-driver queries in ride sharing?
14. How would you model book copies, reservations, and fines in library management?
15. What concurrency rules apply when two members reserve the last copy of a book?
16. How do you present class diagrams in a 45-minute LLD interview without over-engineering?
17. What non-functional requirements would you elicit before designing a rate limiter?
18. How do you scope an LLD to in-memory versus distributed when the prompt is ambiguous?
19. What scalability follow-ups would you mention after completing parking lot LLD?
20. How would you extend elevator LLD to multiple shafts and floor requests?
21. What failure modes would you discuss for notification delivery at-least-once?
22. How do you justify entity design choices when the interviewer challenges your class count?
23. What patterns would you name-drop sparingly in ride-sharing matching design?
24. How do you trade off synchronous matching versus async dispatch in ride sharing LLD?
25. What common LLD mistakes do candidates make on parking lot pricing extensibility?
