---
title: "Redis vs Kafka"
date: 2026-07-03T13:00:00+00:00
draft: false
description: "Tradeoffs between Redis Streams and Kafka for eventing and stream-processing workloads."
tags: ["redis-cheatsheet", "redis-handbook", "redis", "interview"]
categories: ["Redis Handbook"]
shortTitle: "vs Kafka"
module: 7
moduleTitle: "Comparisons"
sectionRef: "7.2"
weight: 702
ShowToc: true
---

## Quick Revision

- Redis Streams is strong for lightweight stream processing and short retention.
- Kafka is built for durable, high-retention event logs and replay.
- Select by durability, retention, ecosystem, and scale requirements.

## Design Tradeoffs

| Dimension | Redis Streams | Kafka |
| :--- | :--- | :--- |
| Retention model | In-memory/limited persistence | Durable segmented log |
| Consumer model | Consumer groups, simpler ops | Partitioned replay-centric model |
| Operational overhead | Lower initial overhead | Higher platform complexity |

## Architect Notes

Do not position Redis Streams as a direct Kafka replacement for long-term event sourcing.

## When are Redis Streams architecturally appropriate versus an external log like Kafka?

### Short Answer
For this question, the architecturally correct Redis answer is comparing Redis to alternatives on data model, durability, ops model, and failure semantics — not feature checklists for: When are Redis Streams architecturally appropriate versus an external log like Kafka.

### Detailed Explanation
Redis offers rich structures and optional persistence; Memcached is simpler cache; Kafka/RabbitMQ excel at durable messaging scale for: When are Redis Streams architecturally appropriate versus an external log like Kafka.

### Internal Working
Using Redis as a message bus works for moderate throughput with Streams; very large retention or routing complexity may favor dedicated brokers for: When are Redis Streams architecturally appropriate versus an external log like Kafka.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology by documenting ADR assumptions and exit strategy if load doubles for: When are Redis Streams architecturally appropriate versus an external log like Kafka.

### Common Mistakes
Resume-driven Redis adoption without ops maturity for Sentinel/Cluster causes painful incidents for: When are Redis Streams architecturally appropriate versus an external log like Kafka.

### Follow-up Questions
What requirement in: When are Redis Streams architecturally appropriate versus an external log like Kafka is decisive if throughput numbers are similar across options?

---
## When do Streams with many consumer groups create memory pressure versus Kafka retention?

### Short Answer
The production-grade Redis answer is comparing Redis to alternatives on data model, durability, ops model, and failure semantics — not feature checklists for: When do Streams with many consumer groups create memory pressure versus Kafka retention.

### Detailed Explanation
Redis offers rich structures and optional persistence; Memcached is simpler cache; Kafka/RabbitMQ excel at durable messaging scale for: When do Streams with many consumer groups create memory pressure versus Kafka retention.

### Internal Working
Using Redis as a message bus works for moderate throughput with Streams; very large retention or routing complexity may favor dedicated brokers for: When do Streams with many consumer groups create memory pressure versus Kafka retention.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by documenting ADR assumptions and exit strategy if load doubles for: When do Streams with many consumer groups create memory pressure versus Kafka retention.

### Common Mistakes
Resume-driven Redis adoption without ops maturity for Sentinel/Cluster causes painful incidents for: When do Streams with many consumer groups create memory pressure versus Kafka retention.

### Follow-up Questions
What requirement in: When do Streams with many consumer groups create memory pressure versus Kafka retention is decisive if throughput numbers are similar across options?

---
<!-- interview-answers:end -->

---

## When are Redis Streams architecturally appropriate versus an external log like Kafka?

### Short Answer
For this question, the architecturally correct Redis answer is comparing Redis to alternatives on data model, durability, ops model, and failure semantics — not feature checklists for: When are Redis Streams architecturally appropriate versus an external log like Kafka.

### Detailed Explanation
Redis offers rich structures and optional persistence; Memcached is simpler cache; Kafka/RabbitMQ excel at durable messaging scale for: When are Redis Streams architecturally appropriate versus an external log like Kafka.

### Internal Working
Using Redis as a message bus works for moderate throughput with Streams; very large retention or routing complexity may favor dedicated brokers for: When are Redis Streams architecturally appropriate versus an external log like Kafka.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology by documenting ADR assumptions and exit strategy if load doubles for: When are Redis Streams architecturally appropriate versus an external log like Kafka.

### Common Mistakes
Resume-driven Redis adoption without ops maturity for Sentinel/Cluster causes painful incidents for: When are Redis Streams architecturally appropriate versus an external log like Kafka.

### Follow-up Questions
What requirement in: When are Redis Streams architecturally appropriate versus an external log like Kafka is decisive if throughput numbers are similar across options?

---
## When do Streams with many consumer groups create memory pressure versus Kafka retention?

### Short Answer
The production-grade Redis answer is comparing Redis to alternatives on data model, durability, ops model, and failure semantics — not feature checklists for: When do Streams with many consumer groups create memory pressure versus Kafka retention.

### Detailed Explanation
Redis offers rich structures and optional persistence; Memcached is simpler cache; Kafka/RabbitMQ excel at durable messaging scale for: When do Streams with many consumer groups create memory pressure versus Kafka retention.

### Internal Working
Using Redis as a message bus works for moderate throughput with Streams; very large retention or routing complexity may favor dedicated brokers for: When do Streams with many consumer groups create memory pressure versus Kafka retention.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by documenting ADR assumptions and exit strategy if load doubles for: When do Streams with many consumer groups create memory pressure versus Kafka retention.

### Common Mistakes
Resume-driven Redis adoption without ops maturity for Sentinel/Cluster causes painful incidents for: When do Streams with many consumer groups create memory pressure versus Kafka retention.

### Follow-up Questions
What requirement in: When do Streams with many consumer groups create memory pressure versus Kafka retention is decisive if throughput numbers are similar across options?

---
<!-- interview-answers:end -->

---

## When are Redis Streams architecturally appropriate versus an external log like Kafka?

### Short Answer
For this question, the architecturally correct Redis answer is comparing Redis to alternatives on data model, durability, ops model, and failure semantics — not feature checklists for: When are Redis Streams architecturally appropriate versus an external log like Kafka.

### Detailed Explanation
Redis offers rich structures and optional persistence; Memcached is simpler cache; Kafka/RabbitMQ excel at durable messaging scale for: When are Redis Streams architecturally appropriate versus an external log like Kafka.

### Internal Working
Using Redis as a message bus works for moderate throughput with Streams; very large retention or routing complexity may favor dedicated brokers for: When are Redis Streams architecturally appropriate versus an external log like Kafka.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology by documenting ADR assumptions and exit strategy if load doubles for: When are Redis Streams architecturally appropriate versus an external log like Kafka.

### Common Mistakes
Resume-driven Redis adoption without ops maturity for Sentinel/Cluster causes painful incidents for: When are Redis Streams architecturally appropriate versus an external log like Kafka.

### Follow-up Questions
What requirement in: When are Redis Streams architecturally appropriate versus an external log like Kafka is decisive if throughput numbers are similar across options?

---
## When do Streams with many consumer groups create memory pressure versus Kafka retention?

### Short Answer
The production-grade Redis answer is comparing Redis to alternatives on data model, durability, ops model, and failure semantics — not feature checklists for: When do Streams with many consumer groups create memory pressure versus Kafka retention.

### Detailed Explanation
Redis offers rich structures and optional persistence; Memcached is simpler cache; Kafka/RabbitMQ excel at durable messaging scale for: When do Streams with many consumer groups create memory pressure versus Kafka retention.

### Internal Working
Using Redis as a message bus works for moderate throughput with Streams; very large retention or routing complexity may favor dedicated brokers for: When do Streams with many consumer groups create memory pressure versus Kafka retention.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by documenting ADR assumptions and exit strategy if load doubles for: When do Streams with many consumer groups create memory pressure versus Kafka retention.

### Common Mistakes
Resume-driven Redis adoption without ops maturity for Sentinel/Cluster causes painful incidents for: When do Streams with many consumer groups create memory pressure versus Kafka retention.

### Follow-up Questions
What requirement in: When do Streams with many consumer groups create memory pressure versus Kafka retention is decisive if throughput numbers are similar across options?

---
<!-- interview-answers:end -->

---

## When are Redis Streams architecturally appropriate versus an external log like Kafka?

### Short Answer
For this question, the architecturally correct Redis answer is comparing Redis to alternatives on data model, durability, ops model, and failure semantics — not feature checklists for: When are Redis Streams architecturally appropriate versus an external log like Kafka.

### Detailed Explanation
Redis offers rich structures and optional persistence; Memcached is simpler cache; Kafka/RabbitMQ excel at durable messaging scale for: When are Redis Streams architecturally appropriate versus an external log like Kafka.

### Internal Working
Using Redis as a message bus works for moderate throughput with Streams; very large retention or routing complexity may favor dedicated brokers for: When are Redis Streams architecturally appropriate versus an external log like Kafka.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology by documenting ADR assumptions and exit strategy if load doubles for: When are Redis Streams architecturally appropriate versus an external log like Kafka.

### Common Mistakes
Resume-driven Redis adoption without ops maturity for Sentinel/Cluster causes painful incidents for: When are Redis Streams architecturally appropriate versus an external log like Kafka.

### Follow-up Questions
What requirement in: When are Redis Streams architecturally appropriate versus an external log like Kafka is decisive if throughput numbers are similar across options?

---
## When do Streams with many consumer groups create memory pressure versus Kafka retention?

### Short Answer
The production-grade Redis answer is comparing Redis to alternatives on data model, durability, ops model, and failure semantics — not feature checklists for: When do Streams with many consumer groups create memory pressure versus Kafka retention.

### Detailed Explanation
Redis offers rich structures and optional persistence; Memcached is simpler cache; Kafka/RabbitMQ excel at durable messaging scale for: When do Streams with many consumer groups create memory pressure versus Kafka retention.

### Internal Working
Using Redis as a message bus works for moderate throughput with Streams; very large retention or routing complexity may favor dedicated brokers for: When do Streams with many consumer groups create memory pressure versus Kafka retention.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by documenting ADR assumptions and exit strategy if load doubles for: When do Streams with many consumer groups create memory pressure versus Kafka retention.

### Common Mistakes
Resume-driven Redis adoption without ops maturity for Sentinel/Cluster causes painful incidents for: When do Streams with many consumer groups create memory pressure versus Kafka retention.

### Follow-up Questions
What requirement in: When do Streams with many consumer groups create memory pressure versus Kafka retention is decisive if throughput numbers are similar across options?

---
<!-- interview-answers:end -->

---

## See Also

- [Previous: Redis Vs Memcached](/redis-cheatsheet/07-comparisons/redis-vs-memcached/)
- [Next: Redis Vs Rabbitmq](/redis-cheatsheet/07-comparisons/redis-vs-rabbitmq/)
- [Redis Handbook Index](/redis-cheatsheet/)
- [Top 150 Interview Questions](/redis-cheatsheet/08-interview-guide/top-150-interview-questions/)
