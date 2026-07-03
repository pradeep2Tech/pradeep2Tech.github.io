---
title: "Backup & Recovery"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "mongodump, mongorestore, PITR, oplog recovery, disaster recovery."
tags: ["mongodb-cheatsheet", "mongodb-handbook", "mongodb", "interview"]
categories: ["MongoDB Handbook"]
shortTitle: "Backup"
module: 4
moduleTitle: "Production Operations"
sectionRef: "4.4"
weight: 404
ShowToc: true
interviewHandbook: true
---

## Quick Revision

- **mongodump/mongorestore** — logical backup; good for dev/migration.
- **Atlas snapshots + PITR** — production default on M10+.
- **Oplog** tail enables point-in-time between snapshots on self-managed RS.

## Core Concepts

| Method | RPO | Use |
| :--- | :--- | :--- |
| mongodump | Snapshot time | Dev, small DBs, selective restore |
| Atlas continuous backup | Minutes (PITR) | Production Atlas |
| Filesystem snapshot | Crash-consistent | Self-managed with care |
| Oplog replay | Between backups | PITR on replica sets |

## Production Patterns

```bash
mongodump --uri="mongodb://..." --out=/backup/$(date +%F)
mongorestore --uri="mongodb://..." /backup/2026-07-03
```

Atlas: enable backup on M10+; test restore to staging quarterly.

## Reliability

Test **restore drills** — backup without tested restore is worthless.

## Disaster Recovery

1. Identify target RPO/RTO.
2. Atlas: restore cluster or download snapshot.
3. Self-managed: restore dump + replay oplog to timestamp.
4. Validate application consistency after restore.

## Common Mistakes

- mongodump on huge sharded clusters without coordination — use per-shard or Atlas.
- No off-site copy of backups.

## Architect Notes

DR architecture must account for **sharded** topology — config server metadata and all shards.

<!-- interview-answers:start -->

# Interview Answers (Top 150)

## What runbook steps recover from accidental `dropDatabase` in production?

### Short Answer
For this question, the architecturally correct answer is defining recovery objectives first, then selecting backup granularity and restore validation for: What runbook steps recover from accidental `dropDatabase` in production.

### Detailed Explanation
Reliable MongoDB DR plans include PITR/window choices, immutable backups, and rehearsed restore cutover checks against application invariants for: What runbook steps recover from accidental `dropDatabase` in production.

### Internal Working
Backup correctness depends on consistent snapshots of replica-set or sharded metadata, not just collection files, for: What runbook steps recover from accidental `dropDatabase` in production.

### Production Notes
You justify it by proving p95/p99 behavior under realistic cardinality by regularly running restore drills, data-integrity checks, and rollback plans on isolated environments for: What runbook steps recover from accidental `dropDatabase` in production.

### Common Mistakes
A dangerous mistake is treating backup success logs as recovery proof without query-level validation for: What runbook steps recover from accidental `dropDatabase` in production.

### Follow-up Questions
How will you prove RPO/RTO and data correctness under: What runbook steps recover from accidental `dropDatabase` in production before declaring recovery complete?

---
## How do you validate a restored backup before cutting traffic over?

### Short Answer
The production-grade answer is defining recovery objectives first, then selecting backup granularity and restore validation for: How do you validate a restored backup before cutting traffic over.

### Detailed Explanation
Reliable MongoDB DR plans include PITR/window choices, immutable backups, and rehearsed restore cutover checks against application invariants for: How do you validate a restored backup before cutting traffic over.

### Internal Working
Backup correctness depends on consistent snapshots of replica-set or sharded metadata, not just collection files, for: How do you validate a restored backup before cutting traffic over.

### Production Notes
You justify it by minimizing cross-shard work and rollback risk by regularly running restore drills, data-integrity checks, and rollback plans on isolated environments for: How do you validate a restored backup before cutting traffic over.

### Common Mistakes
A dangerous mistake is treating backup success logs as recovery proof without query-level validation for: How do you validate a restored backup before cutting traffic over.

### Follow-up Questions
How will you prove RPO/RTO and data correctness under: How do you validate a restored backup before cutting traffic over before declaring recovery complete?

---
## What RPO/RTO targets are realistic with Atlas continuous backup?

### Short Answer
The senior-level decision is defining recovery objectives first, then selecting backup granularity and restore validation for: What RPO/RTO targets are realistic with Atlas continuous backup.

### Detailed Explanation
Reliable MongoDB DR plans include PITR/window choices, immutable backups, and rehearsed restore cutover checks against application invariants for: What RPO/RTO targets are realistic with Atlas continuous backup.

### Internal Working
Backup correctness depends on consistent snapshots of replica-set or sharded metadata, not just collection files, for: What RPO/RTO targets are realistic with Atlas continuous backup.

### Production Notes
You justify it by balancing latency, durability, and operational toil by regularly running restore drills, data-integrity checks, and rollback plans on isolated environments for: What RPO/RTO targets are realistic with Atlas continuous backup.

### Common Mistakes
A dangerous mistake is treating backup success logs as recovery proof without query-level validation for: What RPO/RTO targets are realistic with Atlas continuous backup.

### Follow-up Questions
How will you prove RPO/RTO and data correctness under: What RPO/RTO targets are realistic with Atlas continuous backup before declaring recovery complete?

---
## What backup strategy covers config servers in a sharded cluster DR plan?

### Short Answer
For this question, the architecturally correct answer is choosing a shard key that preserves query targeting and distributes writes, not just one that looks high-cardinality, for: What backup strategy covers config servers in a sharded cluster DR plan.

### Detailed Explanation
In MongoDB sharding, the wrong leading key creates hot chunks, scatter-gather queries, or jumbo chunks, so key choice must follow real filters and time-skew behavior for: What backup strategy covers config servers in a sharded cluster DR plan.

### Internal Working
`mongos` routes via config metadata and chunk ranges, so shard-key entropy and monotonicity directly control migration pressure and balancer load for: What backup strategy covers config servers in a sharded cluster DR plan.

### Production Notes
You justify it by proving p95/p99 behavior under realistic cardinality by load-testing chunk distribution, migration rate, and per-shard opcounters before production for: What backup strategy covers config servers in a sharded cluster DR plan.

### Common Mistakes
Teams often choose hashed keys that break range locality or ranged keys that hotspot writes because they skipped workload replay for: What backup strategy covers config servers in a sharded cluster DR plan.

### Follow-up Questions
How would you prove shard targeting percentage, not just throughput, for: What backup strategy covers config servers in a sharded cluster DR plan before launch?

---
## What Atlas backup window settings minimize impact on production I/O?

### Short Answer
For this question, the architecturally correct answer is defining recovery objectives first, then selecting backup granularity and restore validation for: What Atlas backup window settings minimize impact on production I/O.

### Detailed Explanation
Reliable MongoDB DR plans include PITR/window choices, immutable backups, and rehearsed restore cutover checks against application invariants for: What Atlas backup window settings minimize impact on production I/O.

### Internal Working
Backup correctness depends on consistent snapshots of replica-set or sharded metadata, not just collection files, for: What Atlas backup window settings minimize impact on production I/O.

### Production Notes
You justify it by proving p95/p99 behavior under realistic cardinality by regularly running restore drills, data-integrity checks, and rollback plans on isolated environments for: What Atlas backup window settings minimize impact on production I/O.

### Common Mistakes
A dangerous mistake is treating backup success logs as recovery proof without query-level validation for: What Atlas backup window settings minimize impact on production I/O.

### Follow-up Questions
How will you prove RPO/RTO and data correctness under: What Atlas backup window settings minimize impact on production I/O before declaring recovery complete?

---
<!-- interview-answers:end -->

---

## See Also

- [Previous: Troubleshooting](/mongodb-cheatsheet/04-production-operations/troubleshooting/)
- [Next: Capacity Planning](/mongodb-cheatsheet/04-production-operations/capacity-planning/)
- [MongoDB Handbook Index](/mongodb-cheatsheet/)
- [Top 150 Interview Questions](/mongodb-cheatsheet/06-interview-guide/top-150-interview-questions/)
