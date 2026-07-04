---
title: "Top 25 Troubleshooting Questions"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "Top 25 Troubleshooting Questions from the PostgreSQL handbook."
tags: ["postgresql-cheatsheet", "postgresql", "handbook", "interview"]
categories: ["PostgreSQL Handbook"]
shortTitle: "Top"
module: 8
moduleTitle: "Interview Guide"
sectionRef: "8.3"
weight: 803
interviewHandbook: true
---

Questions only — no answers. Sourced from [Top 150](/postgresql-cheatsheet/08-interview-guide/top-150-interview-questions/).

# Top 25 Troubleshooting Questions

1. What is your first step when p99 query latency doubles after a deploy?
2. How do you identify blocking sessions and their root blockers?
3. When should you use pg_cancel_backend versus pg_terminate_backend?
4. How does transaction ID wraparound threaten cluster availability?
5. What symptoms indicate autovacuum cannot keep up on a hot table?
6. How do you tune per-table autovacuum settings for append-mostly versus churn-heavy tables?
7. What causes replication lag to grow on a standby during heavy write load?
8. How can an unused replication slot fill the primary disk with WAL?
9. What wait events suggest IO-bound queries versus lock contention?
10. How do you trace a deadlock from PostgreSQL logs?
11. What application patterns prevent deadlocks in fund-transfer workflows?
12. How does SKIP LOCKED support concurrent job queue workers?
13. Why do migrations with ACCESS EXCLUSIVE locks cause outages?
14. How do you detect connection leaks from application servers?
15. What metrics alert you before max_connections is exhausted?
16. How do prepared statements interact with PgBouncer transaction pooling?
17. What causes sort operations to spill to disk and how do you confirm?
18. What steps validate a backup before an incident requires restore?
19. How do you perform PITR to a timestamp before accidental DELETE?
20. What failures occur when archive_command stops shipping WAL?
21. How do logical replication conflicts manifest on subscribers?
22. What is your runbook when the primary runs out of disk on the WAL volume?
23. When would you choose a partial index over a full B-tree index?
24. How does declarative partitioning change planner behavior via partition pruning?
25. When would you choose Citus over native partitioning?
