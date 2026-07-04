---
title: "MongoDB vs Cassandra"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "Document database vs wide-column write scale — architect comparison."
tags: ["mongodb-cheatsheet", "mongodb-handbook", "mongodb", "interview"]
categories: ["MongoDB Handbook"]
shortTitle: "vs Cassandra"
module: 5
moduleTitle: "Comparisons"
sectionRef: "5.2"
weight: 502
interviewHandbook: true
---

## Quick Revision

- **Cassandra** — write-optimized wide-column, tunable consistency, masterless ring.
- **MongoDB** — rich document queries, secondary indexes, flexible aggregation.
- Cassandra wins extreme write scale; MongoDB wins query flexibility.

## Design Tradeoffs

| Dimension | MongoDB | Cassandra |
| :--- | :--- | :--- |
| Data model | BSON documents | Wide-column rows |
| Query | Rich ad-hoc queries + indexes | Query must match partition key |
| Consistency | RC/WC per operation | Tunable per read/write |
| Ops | Replica sets + sharding | Gossip, no single master |

## When to Choose MongoDB

- Evolving schema, varied queries, aggregation analytics on documents.

## When to Choose Cassandra

- Time-series at massive write scale, geographic multi-DC with AP tolerance.

## Architect Notes

Do not use Cassandra as a "faster MongoDB" — the query model is fundamentally different.

<!-- interview-answers:start -->

# Interview Answers (Top 150)

## When does Cassandra beat MongoDB for time-series ingestion at billion-events scale?

### Short Answer
The practical MongoDB answer is framing tradeoffs around access patterns, consistency model, and operational maturity rather than feature checklists for: When does Cassandra beat MongoDB for time-series ingestion at billion-events scale.

### Detailed Explanation
MongoDB usually wins on document agility and developer velocity, while alternatives can win on strict relational joins or ultra-specialized write paths for: When does Cassandra beat MongoDB for time-series ingestion at billion-events scale.

### Internal Working
The technical core is locality versus join rigor, partition behavior under skew, and failover semantics under load for: When does Cassandra beat MongoDB for time-series ingestion at billion-events scale.

### Production Notes
You justify it by aligning schema, index, and topology to the access pattern by benchmarking steady-state and failure-state behavior, then documenting ADR assumptions for: When does Cassandra beat MongoDB for time-series ingestion at billion-events scale.

### Common Mistakes
Teams often underestimate dual-write reconciliation cost and overestimate cross-platform operability in: When does Cassandra beat MongoDB for time-series ingestion at billion-events scale.

### Follow-up Questions
What non-functional requirement is decisive for: When does Cassandra beat MongoDB for time-series ingestion at billion-events scale if throughput numbers are similar?

---
<!-- interview-answers:end -->

---

## See Also

- [Previous: Mongodb Vs Postgresql](/mongodb-cheatsheet/05-comparisons/mongodb-vs-postgresql/)
- [Next: Mongodb Vs Couchbase](/mongodb-cheatsheet/05-comparisons/mongodb-vs-couchbase/)
- [MongoDB Handbook Index](/mongodb-cheatsheet/)
- [Top 150 Interview Questions](/mongodb-cheatsheet/06-interview-guide/top-150-interview-questions/)
