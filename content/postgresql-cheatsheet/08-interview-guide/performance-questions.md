---
title: "Top 25 Performance Questions"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "Top 25 Performance Questions from the PostgreSQL handbook."
tags: ["postgresql-cheatsheet", "postgresql", "handbook", "interview"]
categories: ["PostgreSQL Handbook"]
shortTitle: "Top"
module: 8
moduleTitle: "Interview Guide"
sectionRef: "8.4"
weight: 804
interviewHandbook: true
---

Questions only — no answers. Sourced from [Top 150](/postgresql-cheatsheet/08-interview-guide/top-150-interview-questions/).

# Top 25 Performance Questions

1. When would you choose a partial index over a full B-tree index?
2. How does a covering index with INCLUDE enable index-only scans?
3. When does GIN outperform B-tree for jsonb queries?
4. What is BRIN appropriate for and when is it wrong?
5. How do you identify and drop unused indexes safely?
6. What does EXPLAIN BUFFERS reveal about cache efficiency?
7. How does increasing default_statistics_target affect plan quality and ANALYZE cost?
8. When does the planner choose hash join versus nested loop?
9. What parameters enable parallel sequential scan and when is parallel harmful?
10. How should work_mem be sized given concurrent connections?
11. What is the tradeoff of raising shared_buffers on a 128 GB host?
12. Why set random_page_cost lower on NVMe-backed instances?
13. How does effective_cache_size influence index versus seq scan choices?
14. What CTE materialization hints affect planner inlining in PostgreSQL 12+?
15. How does partition pruning fail when queries omit partition key predicates?
16. What index strategy supports keyset pagination at scale?
17. How do you reduce write amplification from too many secondary indexes?
18. What role does fillfactor play in update-heavy tables?
19. How would you benchmark a configuration change without production risk?
20. What OS-level tuning complements PostgreSQL on Linux for OLTP?
21. How do materialized views trade freshness for read performance?
22. When should REFRESH MATERIALIZED VIEW CONCURRENTLY be avoided?
23. How does jsonb_path_ops differ from default jsonb GIN ops?
24. What is the cost of functional indexes on lower(email)?
25. How do you capacity-plan WAL disk throughput for peak write bursts?
