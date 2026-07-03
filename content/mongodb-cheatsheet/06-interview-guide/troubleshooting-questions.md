---
title: "Troubleshooting Questions"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "Production troubleshooting interview questions for MongoDB."
tags: ["mongodb-cheatsheet", "mongodb-handbook", "mongodb", "interview"]
categories: ["MongoDB Handbook"]
shortTitle: "Troubleshooting Q"
module: 6
moduleTitle: "Interview Guide"
sectionRef: "6.3"
weight: 603
ShowToc: true
interviewHandbook: true
---

Questions only — no answers.

# Troubleshooting Questions

1. How do you triage sustained replication lag on one secondary while others stay current?
2. What steps isolate application slowness from database slowness in a replica set?
3. How would you debug a query that regressed after a deployment with no index change?
4. What causes jumbo chunks and how do they block the balancer?
5. How do you remediate a hot shard created by a monotonic timestamp shard key?
6. What symptoms indicate the oplog is too small for maintenance catch-up?
7. How would you handle a secondary that fell off the oplog and needs resync?
8. What is rollback after failover and how do clients detect rolled-back writes?
9. How do you kill a runaway aggregation without impacting unrelated workloads?
10. What `currentOp` fields identify a long-running transaction blocking others?
11. How would you troubleshoot elections flapping during network instability?
12. What disk I/O patterns suggest checkpoint storms on WiredTiger?
13. How do page faults manifest in latency and which metrics confirm cache pressure?
14. What explains COLLSCAN on a collection you believed was indexed?
15. How do you troubleshoot `$lookup` performing COLLSCAN on the foreign collection?
16. What shard metadata issues cause mongos to return stale routing?
17. How would you diagnose connection storms from misconfigured connection pools?
18. What TTL index misconfigurations cause documents to never expire?
19. How do you troubleshoot Atlas `mongodb+srv` DNS resolution failures in corporate networks?
20. What runbook steps recover from accidental `dropDatabase` in production?
21. How do you detect and fix index builds stuck in background on large collections?
22. What causes `$text` queries to return unexpected stems or misses on SKUs?
23. How would you debug geospatial queries returning empty results for valid coordinates?
24. What transaction errors appear when collections don't exist before commit?
25. How do you troubleshoot write concern timeouts under cross-region replication?
26. What signs indicate the balancer is disabled or stuck?
27. How would you investigate memory climbing until mongod is OOM-killed?
28. What profiler settings are safe for intermittent slow-query capture in production?
29. How do you validate a restored backup before cutting traffic over?
30. What is your first-hour incident checklist for a primary that won't rejoin the replica set?
