---
title: "Performance Questions"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "MongoDB performance and tuning interview questions."
tags: ["mongodb-cheatsheet", "mongodb-handbook", "mongodb", "interview"]
categories: ["MongoDB Handbook"]
shortTitle: "Performance Q"
module: 6
moduleTitle: "Interview Guide"
sectionRef: "6.4"
weight: 604
ShowToc: true
interviewHandbook: true
---

Questions only — no answers.

# Performance Questions

1. How do you use explain output to decide between a new compound index and a covered query rewrite?
2. What ESR ordering would you use for `{ status, createdAt, amount }` filters?
3. When does index intersection help and when should you avoid relying on it?
4. How do partial indexes reduce write amplification for status-filtered queries?
5. What projection changes turn an IXSCAN+FETCH into a covered query?
6. How does large `skip` pagination degrade performance and what pattern replaces it?
7. How do you tune aggregation `$lookup` pipeline order for index use?
8. When is `allowDiskUse: true` acceptable versus a design smell?
9. How does WiredTiger cache sizing affect p99 read latency?
10. What compression settings trade CPU for disk I/O on write-heavy workloads?
11. How do you right-size `maxPoolSize` across 50 application pods?
12. What bulk write patterns maximize insert throughput on sharded collections?
13. How do hashed shard keys affect range query performance?
14. What index hygiene process prevents unbounded index growth over years?
15. How would you load-test shard key distribution before production cutover?
16. What regex patterns can use indexes and which force COLLSCAN?
17. How does read preference nearest reduce latency at consistency cost?
18. What Atlas Performance Advisor suggestions do you auto-apply versus review?
19. How do write-heavy indexes on high-cardinality fields impact checkpoint I/O?
20. When does embedding outperform `$lookup` for read latency at scale?
21. How do you benchmark working set size before hardware procurement?
22. What `$facet` patterns reduce round trips without exploding memory?
23. How does collation-aware indexing affect sort stage elimination?
24. What pre-split strategy avoids hot chunks during initial bulk load?
25. How do you tune oplog size for write bursts without wasting disk?
