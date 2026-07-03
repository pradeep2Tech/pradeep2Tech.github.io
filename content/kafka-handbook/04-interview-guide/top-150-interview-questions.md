---
title: "Top 150 Kafka Interview Questions"
date: 2026-07-03T10:00:00+00:00
draft: false
description: "150 production-oriented Kafka interview questions mapped to handbook topics."
tags: ["kafka-handbook", "kafka", "messaging", "streaming", "interview"]
categories: ["Kafka Handbook"]
shortTitle: "Top 150"
module: 4
moduleTitle: "Interview Guide"
sectionRef: "4.1"
weight: 401
ShowToc: true
interviewHandbook: true
---

Curated questions for **6+ year** engineers, senior engineers, tech leads, and architects. **Questions only** — each **Deep Dive** links to the architect cheatsheet page (revision bullets, tables, diagrams).

| # | Question | Difficulty | Level | Topic | Deep Dive |
|---|----------|------------|--------|-------|------------------|
| 1 | Why does Kafka model messaging as a distributed commit log instead of a traditional point-to-point queue? | Medium | Senior Engineer | Fundamentals | [Messaging Models](/kafka-handbook/01-fundamentals/messaging-models/) |
| 2 | How does append-only log storage enable independent replay by multiple consumer groups on the same topic? | Medium | Senior Engineer | Internals | [Kafka Internals](/kafka-handbook/02-kafka/kafka-internals//) |
| 3 | What delivery semantics does at-least-once processing imply for consumer application design? | Medium | Senior Engineer | Reliability | [Kafka Delivery Semantics](/kafka-handbook/02-kafka/kafka-delivery-semantics//) |
| 4 | Why are idempotent consumers mandatory when brokers guarantee at-least-once delivery with retries? | Medium | Lead | Reliability | [Kafka Delivery Semantics](/kafka-handbook/02-kafka/kafka-delivery-semantics//) |
| 5 | How do partition keys preserve ordering, and what hot-partition failure mode does poor key choice create? | Hard | Senior Engineer | Performance | [Kafka Performance](/kafka-handbook/02-kafka/kafka-performance//) |
| 6 | Why is global ordering across an entire topic expensive in a distributed log architecture? | Hard | Senior Engineer | Architecture | [Kafka Core](/kafka-handbook/02-kafka/kafka-core//) |
| 7 | When would you isolate real-time and batch consumers using separate consumer groups on the same topic? | Medium | Lead | Architecture | [Kafka Core](/kafka-handbook/02-kafka/kafka-core//) |
| 8 | How would you design a dead-letter topic and replay runbook for poison messages that block partition progress? | Hard | Lead | Troubleshooting | [Kafka Troubleshooting](/kafka-handbook/02-kafka/kafka-troubleshooting//) |
| 9 | What is consumer lag, and which operational signals would you monitor before a high-traffic campaign? | Medium | Lead | Observability | [Kafka Operations](/kafka-handbook/02-kafka/kafka-operations//) |
| 10 | How do you size topic partition count for peak throughput versus maximum consumer parallelism? | Hard | Senior Engineer | Performance | [Kafka Performance](/kafka-handbook/02-kafka/kafka-performance//) |
| 11 | Why does the handbook recommend sizing partitions for peak traffic rather than average load? | Medium | Senior Engineer | Performance | [Kafka Performance](/kafka-handbook/02-kafka/kafka-performance//) |
| 12 | How does schema drift break downstream deserializers, and what governance would you enforce with a schema registry? | Medium | Lead | Reliability | [Kafka Schema Registry](/kafka-handbook/02-kafka/kafka-schema-registry//) |
| 13 | How do you propagate distributed trace context through Kafka message headers without breaking consumers? | Medium | Lead | Observability | [Kafka Operations](/kafka-handbook/02-kafka/kafka-operations//) |
| 14 | What team capabilities must exist before choosing self-hosted Kafka over a managed cloud queue? | Medium | Senior Engineer | Security | [Kafka Security](/kafka-handbook/02-kafka/kafka-security//) |
| 15 | When does synchronous cross-service consistency make Kafka a poor primary integration choice without sagas? | Medium | Senior Engineer | Design Tradeoffs | [Kafka Core](/kafka-handbook/02-kafka/kafka-core//) |
| 16 | How does temporal decoupling in event-driven architectures complicate end-to-end debugging compared to sync RPC? | Medium | Senior Engineer | Troubleshooting | [Kafka Troubleshooting](/kafka-handbook/02-kafka/kafka-troubleshooting//) |
| 17 | What business keys would you use to make consumer processing idempotent in an order-processing domain? | Medium | Senior Engineer | Reliability | [Kafka Delivery Semantics](/kafka-handbook/02-kafka/kafka-delivery-semantics//) |
| 18 | How would you auto-scale consumers in response to sustained consumer lag during traffic spikes? | Hard | Senior Engineer | Performance | [Kafka Performance](/kafka-handbook/02-kafka/kafka-performance//) |
| 19 | When is a managed cloud queue preferable to self-hosted Kafka despite reduced operational control? | Medium | Architect | Design Tradeoffs | [Kafka Core](/kafka-handbook/02-kafka/kafka-core//) |
| 20 | How does Kafka buffer producer bursts without dropping users when downstream processing is slower? | Medium | Senior Engineer | Performance | [Kafka Performance](/kafka-handbook/02-kafka/kafka-performance//) |
| 21 | What ordering guarantees can you realistically promise to product teams when partition count exceeds one? | Hard | Architect | Architecture | [Kafka Core](/kafka-handbook/02-kafka/kafka-core//) |
| 22 | How would you troubleshoot a single partition falling behind while others remain healthy? | Hard | Lead | Troubleshooting | [Kafka Troubleshooting](/kafka-handbook/02-kafka/kafka-troubleshooting//) |
| 23 | What failure modes appear during broker patching when partition leadership moves across the cluster? | Hard | Lead | Troubleshooting | [Kafka Troubleshooting](/kafka-handbook/02-kafka/kafka-troubleshooting//) |
| 24 | How do you decide between log/stream platforms and classic queue brokers for a new microservice integration? | Medium | Senior Engineer | Design Tradeoffs | [Broker Selection Guide](/kafka-handbook/03-broker-comparisons//) |
| 25 | What ADR criteria from the handbook would you use to justify Kafka as the enterprise event backbone? | Medium | Senior Engineer | Architecture | [Broker Selection Guide](/kafka-handbook/03-broker-comparisons//) |
| 26 | How do throughput, ordering, and operational trade-offs differ across brokers listed in the messaging module? | Hard | Architect | Architecture | [Broker Selection Guide](/kafka-handbook/03-broker-comparisons//) |
| 27 | When would you pick Kafka over RabbitMQ for high-volume event fan-out with replay requirements? | Medium | Architect | Design Tradeoffs | [Kafka Vs Rabbitmq](/kafka-handbook/03-broker-comparisons/kafka-vs-rabbitmq//) |
| 28 | When would RabbitMQ be the better fit for task queues with complex routing and per-message acknowledgement? | Medium | Architect | Design Tradeoffs | [Kafka Vs Rabbitmq](/kafka-handbook/03-broker-comparisons/kafka-vs-rabbitmq//) |
| 29 | How does AMQP exchange-and-queue routing differ from Kafka topic-and-partition consumption mentally? | Medium | Senior Engineer | Fundamentals | [Kafka Vs Rabbitmq](/kafka-handbook/03-broker-comparisons/kafka-vs-rabbitmq//) |
| 30 | Why is RabbitMQ a poor long-retention system of record for analytics compared to a durable log? | Medium | Lead | Architecture | [Kafka Vs Rabbitmq](/kafka-handbook/03-broker-comparisons/kafka-vs-rabbitmq//) |
| 31 | How would you implement payment retry with TTL queues and dead-letter routing in RabbitMQ versus Kafka? | Hard | Lead | Architecture | [Kafka Vs Rabbitmq](/kafka-handbook/03-broker-comparisons/kafka-vs-rabbitmq//) |
| 32 | What hybrid architecture uses Kafka for event streaming and RabbitMQ for task distribution in the same platform? | Hard | Senior Engineer | Architecture | [Kafka Vs Rabbitmq](/kafka-handbook/03-broker-comparisons/kafka-vs-rabbitmq//) |
| 33 | When is Redpanda a credible alternative to self-hosted Apache Kafka for an event platform? | Medium | Architect | Design Tradeoffs | [Kafka Vs Redpanda](/kafka-handbook/03-broker-comparisons/kafka-vs-redpanda//) |
| 34 | What operational simplification does removing ZooKeeper provide in a Kafka-compatible deployment? | Medium | Lead | Operations | [Kafka Vs Redpanda](/kafka-handbook/03-broker-comparisons/kafka-vs-redpanda//) |
| 35 | What compatibility risks remain when migrating clients from Apache Kafka to Redpanda in production? | Hard | Lead | Troubleshooting | [Kafka Vs Redpanda](/kafka-handbook/03-broker-comparisons/kafka-vs-redpanda//) |
| 36 | When would Apache Pulsar's unified queue-and-log model beat Kafka for multi-tenant streaming? | Hard | Architect | Design Tradeoffs | [Kafka Vs Pulsar](/kafka-handbook/03-broker-comparisons/kafka-vs-pulsar//) |
| 37 | How does built-in geo-replication in Pulsar influence multi-datacenter architecture decisions versus MirrorMaker? | Hard | Architect | Architecture | [Kafka Multi Region](/kafka-handbook/02-kafka/kafka-multi-region//) |
| 38 | What tenancy isolation requirements would push you toward Pulsar over a single shared Kafka cluster? | Hard | Architect | Security | [Kafka Vs Pulsar](/kafka-handbook/03-broker-comparisons/kafka-vs-pulsar//) |
| 39 | When is Amazon SQS the right choice over Kafka for decoupling without broker operations? | Medium | Lead | Design Tradeoffs | [Cloud Messaging Services](/kafka-handbook/03-broker-comparisons/cloud-messaging-services//) |
| 40 | What replay and fan-out limitations does SQS impose compared to a retained commit log? | Medium | Senior Engineer | Architecture | [Cloud Messaging Services](/kafka-handbook/03-broker-comparisons/cloud-messaging-services//) |
| 41 | How would you design SNS fan-out to multiple SQS queues versus a single Kafka topic with consumer groups? | Hard | Senior Engineer | Architecture | [Cloud Messaging Services](/kafka-handbook/03-broker-comparisons/cloud-messaging-services//) |
| 42 | When does Google Pub/Sub's cloud-native pub/sub model replace self-hosted Kafka in GCP architectures? | Medium | Architect | Design Tradeoffs | [Cloud Messaging Services](/kafka-handbook/03-broker-comparisons/cloud-messaging-services//) |
| 43 | How do Azure Service Bus sessions and dead-lettering compare to Kafka partition ordering and DLT patterns? | Hard | Lead | Security | [Cloud Messaging Services](/kafka-handbook/03-broker-comparisons/cloud-messaging-services//) |
| 44 | When would NATS be preferred over Kafka for low-latency messaging at the edge of a system? | Medium | Lead | Design Tradeoffs | [Kafka Vs Nats](/kafka-handbook/03-broker-comparisons/kafka-vs-nats//) |
| 45 | What legacy enterprise integration scenarios still favor ActiveMQ or IBM MQ over Kafka? | Medium | Architect | Design Tradeoffs | [Cloud Messaging Services](/kafka-handbook/03-broker-comparisons/cloud-messaging-services//) |
| 46 | How do JMS semantics in ActiveMQ differ from Kafka consumer offset management in practice? | Hard | Senior Engineer | Internals | [Cloud Messaging Services](/kafka-handbook/03-broker-comparisons/cloud-messaging-services//) |
| 47 | What operational burden does IBM MQ HA clustering add compared to Kafka broker replication? | Hard | Lead | Operations | [Cloud Messaging Services](/kafka-handbook/03-broker-comparisons/cloud-messaging-services//) |
| 48 | How would you map the handbook's log versus queue versus cloud pub/sub taxonomy to a retail order platform? | Hard | Senior Engineer | Architecture | [Cloud Messaging Services](/kafka-handbook/03-broker-comparisons/cloud-messaging-services//) |
| 49 | What happens to message ordering when you increase partition count on an existing high-traffic topic? | Hard | Senior Engineer | Performance | [Kafka Performance](/kafka-handbook/02-kafka/kafka-performance//) |
| 50 | How do consumer groups divide partition ownership, and what triggers a rebalance storm? | Hard | Senior Engineer | Internals | [Kafka Consumer Groups](/kafka-handbook/02-kafka/kafka-consumer-groups//) |
| 51 | What strategies minimize duplicate processing during consumer group rebalancing? | Hard | Lead | Reliability | [Kafka Consumer Groups](/kafka-handbook/02-kafka/kafka-consumer-groups//) |
| 52 | How does cooperative sticky rebalancing differ from eager rebalancing in production consumer upgrades? | Hard | Senior Engineer | Troubleshooting | [Kafka Consumer Groups](/kafka-handbook/02-kafka/kafka-consumer-groups//) |
| 53 | When should consumers commit offsets synchronously versus asynchronously, and what data loss risk changes? | Hard | Lead | Reliability | [Kafka Internals](/kafka-handbook/02-kafka/kafka-internals//) |
| 54 | How would you reset offsets safely to replay a topic after a downstream bug without corrupting idempotent state? | Hard | Lead | Troubleshooting | [Kafka Troubleshooting](/kafka-handbook/02-kafka/kafka-troubleshooting//) |
| 55 | What is the tradeoff between `acks=1` and `acks=all` for write durability under broker failure? | Hard | Architect | Reliability | [Kafka Internals](/kafka-handbook/02-kafka/kafka-internals//) |
| 56 | How does replication factor interact with rack awareness and cross-AZ fault tolerance? | Hard | Architect | Reliability | [Kafka Internals](/kafka-handbook/02-kafka/kafka-internals//) |
| 57 | What is the In-Sync Replica set, and how does ISR shrinkage affect durability guarantees? | Hard | Architect | Internals | [Kafka Internals](/kafka-handbook/02-kafka/kafka-internals//) |
| 58 | What happens during an unclean leader election, and when would you allow it in production? | Hard | Architect | Troubleshooting | [Kafka Internals](/kafka-handbook/02-kafka/kafka-internals//) |
| 59 | How do min.insync.replicas and producer acks combine to prevent silent data loss? | Hard | Lead | Reliability | [Kafka Internals](/kafka-handbook/02-kafka/kafka-internals//) |
| 60 | How would you troubleshoot under-replicated partitions after a broker network partition? | Hard | Lead | Troubleshooting | [Kafka Internals](/kafka-handbook/02-kafka/kafka-internals//) |
| 61 | What symptoms indicate broker disk saturation, and how do log segments contribute? | Hard | Lead | Performance | [Kafka Internals](/kafka-handbook/02-kafka/kafka-internals//) |
| 62 | How does segment rolling affect retention enforcement and disk I/O patterns? | Medium | Senior Engineer | Performance | [Kafka Performance](/kafka-handbook/02-kafka/kafka-performance//) |
| 63 | When would you choose log compaction over time-based retention for a topic? | Hard | Architect | Architecture | [Kafka Internals](/kafka-handbook/02-kafka/kafka-internals//) |
| 64 | What tombstone records and compaction lag issues break compacted topic consumers? | Hard | Lead | Troubleshooting | [Kafka Troubleshooting](/kafka-handbook/02-kafka/kafka-troubleshooting//) |
| 65 | How do idempotent producers prevent duplicate writes without full transactional semantics? | Hard | Senior Engineer | Reliability | [Kafka Delivery Semantics](/kafka-handbook/02-kafka/kafka-delivery-semantics//) |
| 66 | When are Kafka transactions required versus idempotent producers plus idempotent consumers? | Hard | Architect | Reliability | [Kafka Delivery Semantics](/kafka-handbook/02-kafka/kafka-delivery-semantics//) |
| 67 | How does exactly-once stream processing differ from end-to-end exactly-once across Kafka and a database? | Hard | Senior Engineer | Architecture | [Kafka Delivery Semantics](/kafka-handbook/02-kafka/kafka-delivery-semantics//) |
| 68 | What is the read-process-write pattern risk when consuming and producing within the same transaction? | Hard | Lead | Reliability | [Kafka Internals](/kafka-handbook/02-kafka/kafka-internals//) |
| 69 | How would you tune producer batch size and linger.ms for throughput without breaching latency SLOs? | Hard | Lead | Performance | [Kafka Performance](/kafka-handbook/02-kafka/kafka-performance//) |
| 70 | What compression codec tradeoffs apply at high throughput — lz4, snappy, zstd, gzip? | Medium | Senior Engineer | Performance | [Kafka Performance](/kafka-handbook/02-kafka/kafka-performance//) |
| 71 | How does fetch.min.bytes and max.wait.ms on consumers affect end-to-end latency? | Medium | Senior Engineer | Performance | [Kafka Performance](/kafka-handbook/02-kafka/kafka-performance//) |
| 72 | What JVM and OS tuning would you apply on Kafka brokers serving millions of messages per day? | Hard | Architect | Performance | [Kafka Performance](/kafka-handbook/02-kafka/kafka-performance//) |
| 73 | How do page cache and sequential disk writes explain Kafka's throughput on spinning disks versus NVMe? | Hard | Architect | Internals | [Kafka Internals](/kafka-handbook/02-kafka/kafka-internals//) |
| 74 | What network and disk capacity math would you use for 30-day retention with replication factor three? | Hard | Senior Engineer | Performance | [Kafka Performance](/kafka-handbook/02-kafka/kafka-performance//) |
| 75 | How do you plan broker count and partition leadership distribution to avoid hotspot brokers? | Hard | Senior Engineer | Performance | [Kafka Performance](/kafka-handbook/02-kafka/kafka-performance//) |
| 76 | When does adding consumers stop reducing lag because partition count is the bottleneck? | Medium | Lead | Performance | [Kafka Performance](/kafka-handbook/02-kafka/kafka-performance//) |
| 77 | What is the upper bound on useful partition count for a topic, and what metadata overhead grows? | Hard | Senior Engineer | Performance | [Kafka Performance](/kafka-handbook/02-kafka/kafka-performance//) |
| 78 | How would you design Kafka for multi-region active-active deployment with conflict resolution? | Hard | Architect | Architecture | [Kafka Multi Region](/kafka-handbook/02-kafka/kafka-multi-region//) |
| 79 | What role does MirrorMaker 2 play in disaster recovery versus real-time dual writes? | Hard | Architect | Architecture | [Kafka Multi Region](/kafka-handbook/02-kafka/kafka-multi-region//) |
| 80 | How do cloud-managed Kafka offerings (MSK, Confluent Cloud, Event Hubs) change operational ownership? | Medium | Senior Engineer | Security | [Kafka Operations](/kafka-handbook/02-kafka/kafka-operations//) |
| 81 | What Kubernetes operator patterns apply to running Kafka on Kubernetes at production scale? | Hard | Architect | Reliability | [Kafka Operations](/kafka-handbook/02-kafka/kafka-operations//) |
| 82 | How do persistent volumes and pod disruption budgets affect Kafka broker upgrade safety on K8s? | Hard | Lead | Security | [Kafka Operations](/kafka-handbook/02-kafka/kafka-operations//) |
| 83 | What metrics beyond consumer lag define Kafka cluster health in production? | Medium | Lead | Observability | [Kafka Operations](/kafka-handbook/02-kafka/kafka-operations//) |
| 84 | How would you alert on ISR shrink, offline partitions, and request handler idle ratio? | Hard | Lead | Observability | [Kafka Operations](/kafka-handbook/02-kafka/kafka-operations//) |
| 85 | What dashboards and SLOs would you define for p99 produce and fetch latency? | Medium | Lead | Observability | [Kafka Operations](/kafka-handbook/02-kafka/kafka-operations//) |
| 86 | How do you run a controlled failure drill on a Kafka cluster without customer impact? | Hard | Architect | Troubleshooting | [Kafka Troubleshooting](/kafka-handbook/02-kafka/kafka-troubleshooting//) |
| 87 | What is your incident runbook when all consumers in a critical group stop committing offsets? | Hard | Lead | Troubleshooting | [Kafka Troubleshooting](/kafka-handbook/02-kafka/kafka-troubleshooting//) |
| 88 | How would you diagnose metadata request storms after a large-scale topic creation event? | Hard | Lead | Troubleshooting | [Kafka Troubleshooting](/kafka-handbook/02-kafka/kafka-troubleshooting//) |
| 89 | What causes rebalance loops when session.timeout.ms and max.poll.interval.ms are misconfigured? | Hard | Senior Engineer | Troubleshooting | [Kafka Consumer Groups](/kafka-handbook/02-kafka/kafka-consumer-groups//) |
| 90 | How do you troubleshoot a producer receiving NOT_LEADER_FOR_PARTITION errors during cluster maintenance? | Medium | Senior Engineer | Troubleshooting | [Kafka Troubleshooting](/kafka-handbook/02-kafka/kafka-troubleshooting//) |
| 91 | What steps isolate whether lag is producer-side, broker-side, or consumer-side? | Hard | Lead | Troubleshooting | [Kafka Troubleshooting](/kafka-handbook/02-kafka/kafka-troubleshooting//) |
| 92 | How would you handle a topic accidentally created with replication factor one in production? | Hard | Lead | Troubleshooting | [Kafka Troubleshooting](/kafka-handbook/02-kafka/kafka-troubleshooting//) |
| 93 | What upgrade strategy minimizes risk when moving from ZooKeeper to KRaft mode? | Hard | Architect | Troubleshooting | [Kafka Operations](/kafka-handbook/02-kafka/kafka-operations//) |
| 94 | How do rolling broker restarts interact with controller failover and partition availability? | Hard | Architect | Troubleshooting | [Kafka Troubleshooting](/kafka-handbook/02-kafka/kafka-troubleshooting//) |
| 95 | What backward-compatibility checks run before a major Kafka broker version jump? | Medium | Lead | Troubleshooting | [Kafka Troubleshooting](/kafka-handbook/02-kafka/kafka-troubleshooting//) |
| 96 | How does Schema Registry enforce compatibility modes (BACKWARD, FORWARD, FULL) during deployments? | Hard | Lead | Reliability | [Kafka Schema Registry](/kafka-handbook/02-kafka/kafka-schema-registry//) |
| 97 | When would Avro, Protobuf, or JSON Schema be the wrong choice for high-evolution event contracts? | Medium | Architect | Design Tradeoffs | [Kafka Schema Registry](/kafka-handbook/02-kafka/kafka-schema-registry//) |
| 98 | How do Kafka Connect offset topics and connector failures affect CDC pipeline continuity? | Hard | Lead | Troubleshooting | [Kafka Connect](/kafka-handbook/02-kafka/kafka-connect//) |
| 99 | What delivery guarantees does Kafka Connect provide for database source connectors? | Medium | Senior Engineer | Reliability | [Kafka Connect](/kafka-handbook/02-kafka/kafka-connect//) |
| 100 | How do Kafka Streams state stores recover after application redeploy or rebalance? | Hard | Lead | Troubleshooting | [Kafka Streams](/kafka-handbook/02-kafka/kafka-streams//) |
| 101 | When is Kafka Streams preferable to an external stream processor for aggregations? | Medium | Architect | Design Tradeoffs | [Kafka Streams](/kafka-handbook/02-kafka/kafka-streams//) |
| 102 | How would you secure Kafka with mutual TLS between clients and brokers? | Hard | Lead | Security | [Kafka Security](/kafka-handbook/02-kafka/kafka-security//) |
| 103 | What SASL mechanisms are appropriate for multi-tenant clusters, and what are their tradeoffs? | Hard | Architect | Security | [Kafka Security](/kafka-handbook/02-kafka/kafka-security//) |
| 104 | How do ACLs on topics, groups, and cluster operations enforce least privilege? | Medium | Lead | Security | [Kafka Security](/kafka-handbook/02-kafka/kafka-security//) |
| 105 | What risks does plaintext listener exposure create inside a Kubernetes cluster? | Medium | Senior Engineer | Security | [Kafka Security](/kafka-handbook/02-kafka/kafka-security//) |
| 106 | How would you rotate broker certificates without dropping in-flight client connections? | Hard | Lead | Security | [Kafka Security](/kafka-handbook/02-kafka/kafka-security//) |
| 107 | What audit logging would you enable for compliance on a regulated event platform? | Medium | Architect | Security | [Kafka Security](/kafka-handbook/02-kafka/kafka-security//) |
| 108 | How do you prevent unauthorized consumers from reading sensitive PII topics? | Hard | Architect | Security | [Kafka Security](/kafka-handbook/02-kafka/kafka-security//) |
| 109 | What network segmentation model isolates Kafka brokers from application tiers? | Medium | Architect | Security | [Kafka Security](/kafka-handbook/02-kafka/kafka-security//) |
| 110 | How does encryption at rest interact with broker performance and key management? | Hard | Lead | Security | [Kafka Security](/kafka-handbook/02-kafka/kafka-security//) |
| 111 | When would you encrypt payloads at the application layer in addition to wire encryption? | Medium | Architect | Security | [Kafka Security](/kafka-handbook/02-kafka/kafka-security//) |
| 112 | How do you evaluate whether Event Hubs Kafka protocol compatibility meets your ordering needs? | Medium | Architect | Design Tradeoffs | [Kafka Core](/kafka-handbook/02-kafka/kafka-core//) |
| 113 | What contract-test strategy catches schema drift before production consumer deploys? | Medium | Lead | Reliability | [Kafka Schema Registry](/kafka-handbook/02-kafka/kafka-schema-registry//) |
| 114 | How does the transactional outbox pattern pair with Kafka to avoid dual-write inconsistencies? | Hard | Architect | Architecture | [Kafka Delivery Semantics](/kafka-handbook/02-kafka/kafka-delivery-semantics//) |
| 115 | When is CDC preferable to application-published domain events for Kafka ingestion? | Hard | Architect | Architecture | [Kafka Connect](/kafka-handbook/02-kafka/kafka-connect//) |
| 116 | How would you design event versioning so multiple consumer versions coexist during rollout? | Hard | Architect | Architecture | [Kafka Core](/kafka-handbook/02-kafka/kafka-core//) |
| 117 | What saga orchestration patterns map cleanly to Kafka topics versus choreographed events? | Hard | Architect | Architecture | [Kafka Core](/kafka-handbook/02-kafka/kafka-core//) |
| 118 | How do you enforce ordering per customer entity across multiple event types? | Hard | Lead | Architecture | [Kafka Core](/kafka-handbook/02-kafka/kafka-core//) |
| 119 | What anti-patterns appear when microservices share one consumer group across different services? | Medium | Senior Engineer | Architecture | [Kafka Core](/kafka-handbook/02-kafka/kafka-core//) |
| 120 | How would you blueprint an event-driven architecture ADR using the handbook's selection criteria? | Medium | Architect | Architecture | [Broker Selection Guide](/kafka-handbook/03-broker-comparisons//) |
| 121 | What load-test scenarios validate partition and consumer sizing before Black Friday traffic? | Hard | Lead | Performance | [Kafka Performance](/kafka-handbook/02-kafka/kafka-performance//) |
| 122 | How do you benchmark producer throughput separately from consumer processing capacity? | Medium | Senior Engineer | Performance | [Kafka Performance](/kafka-handbook/02-kafka/kafka-performance//) |
| 123 | What GC pauses on brokers correlate with request timeout spikes on producers? | Hard | Lead | Performance | [Kafka Performance](/kafka-handbook/02-kafka/kafka-performance//) |
| 124 | How does increasing retention without storage planning cause emergency disk expansion? | Medium | Lead | Troubleshooting | [Kafka Troubleshooting](/kafka-handbook/02-kafka/kafka-troubleshooting//) |
| 125 | What happens when a compacted topic's disk usage grows because compaction cannot keep pace? | Hard | Lead | Troubleshooting | [Kafka Troubleshooting](/kafka-handbook/02-kafka/kafka-troubleshooting//) |
| 126 | How would you recover from accidental topic deletion in a production cluster? | Hard | Architect | Troubleshooting | [Kafka Troubleshooting](/kafka-handbook/02-kafka/kafka-troubleshooting//) |
| 127 | What backup strategy covers Kafka metadata and topic data for disaster recovery? | Hard | Architect | Troubleshooting | [Kafka Troubleshooting](/kafka-handbook/02-kafka/kafka-troubleshooting//) |
| 128 | How do you validate failover RTO and RPO for a multi-broker Kafka deployment? | Hard | Architect | Reliability | [Kafka Internals](/kafka-handbook/02-kafka/kafka-internals//) |
| 129 | What quorum loss symptoms appear in KRaft or ZooKeeper during a zone outage? | Hard | Architect | Troubleshooting | [Kafka Operations](/kafka-handbook/02-kafka/kafka-operations//) |
| 130 | How would you throttle misbehaving clients flooding a shared cluster? | Hard | Lead | Performance | [Kafka Performance](/kafka-handbook/02-kafka/kafka-performance//) |
| 131 | What quotas and ACL policies protect multi-team clusters from noisy neighbors? | Medium | Lead | Performance | [Kafka Performance](/kafka-handbook/02-kafka/kafka-performance//) |
| 132 | How do you right-size `num.network.threads` and `num.io.threads` under heavy fetch load? | Hard | Senior Engineer | Performance | [Kafka Performance](/kafka-handbook/02-kafka/kafka-performance//) |
| 133 | When does cross-datacenter replication latency dominate end-to-end event freshness SLOs? | Hard | Architect | Performance | [Kafka Multi Region](/kafka-handbook/02-kafka/kafka-multi-region//) |
| 134 | How would you compare total cost of ownership for MSK versus self-hosted Kafka at scale? | Hard | Architect | Design Tradeoffs | [Kafka Core](/kafka-handbook/02-kafka/kafka-core//) |
| 135 | What staffing model supports 24/7 Kafka on-call for a business-critical event platform? | Medium | Architect | Reliability | [Kafka Internals](/kafka-handbook/02-kafka/kafka-internals//) |
| 136 | How do you document and test replay procedures before they are needed in an incident? | Medium | Lead | Troubleshooting | [Kafka Troubleshooting](/kafka-handbook/02-kafka/kafka-troubleshooting//) |
| 137 | What developer guardrails prevent publishing events without registered schemas? | Medium | Lead | Reliability | [Kafka Schema Registry](/kafka-handbook/02-kafka/kafka-schema-registry//) |
| 138 | How does choosing random UUID partition keys destroy ordering and create hot spots? | Easy | Developer | Performance | [Kafka Performance](/kafka-handbook/02-kafka/kafka-performance//) |
| 139 | Why is tight latency budget request/response often a signal to avoid Kafka on the critical path? | Easy | Developer | Design Tradeoffs | [Kafka Core](/kafka-handbook/02-kafka/kafka-core//) |
| 140 | What minimal consumer design handles at-least-once delivery without data corruption? | Easy | Developer | Reliability | [Kafka Delivery Semantics](/kafka-handbook/02-kafka/kafka-delivery-semantics//) |
| 141 | How do multiple subscribers on one SNS topic differ from multiple Kafka consumer groups? | Easy | Developer | Fundamentals | [Cloud Messaging Services](/kafka-handbook/03-broker-comparisons/cloud-messaging-services//) |
| 142 | What does back-pressure mean in async messaging, and how does a log absorb bursts? | Easy | Developer | Fundamentals | [Messaging Models](/kafka-handbook/01-fundamentals/messaging-models//) |
| 143 | When would you choose a cloud pub/sub product over operating any broker yourself? | Easy | Developer | Design Tradeoffs | [Cloud Messaging Services](/kafka-handbook/03-broker-comparisons/cloud-messaging-services//) |
| 144 | How does message retention after consumption differ between Kafka and classic queues? | Easy | Developer | Fundamentals | [Kafka Vs Rabbitmq](/kafka-handbook/03-broker-comparisons/kafka-vs-rabbitmq//) |
| 145 | What is the first check when consumer lag alerts fire during normal business hours? | Easy | Developer | Troubleshooting | [Kafka Troubleshooting](/kafka-handbook/02-kafka/kafka-troubleshooting//) |
| 146 | Why should dead-letter handling be designed before production launch, not after an incident? | Easy | Developer | Troubleshooting | [Kafka Troubleshooting](/kafka-handbook/02-kafka/kafka-troubleshooting//) |
| 147 | How does propagating trace IDs in headers help compare async flows to HTTP traces? | Easy | Developer | Observability | [Kafka Operations](/kafka-handbook/02-kafka/kafka-operations//) |
| 148 | What questions would you ask stakeholders before committing to global message ordering? | Easy | Developer | Architecture | [Kafka Core](/kafka-handbook/02-kafka/kafka-core//) |
| 149 | How do integration tests validate idempotent consumer behavior under duplicate delivery? | Medium | Developer | Reliability | [Kafka Delivery Semantics](/kafka-handbook/02-kafka/kafka-delivery-semantics//) |
| 150 | What handbook guidance applies when peak traffic exceeds synchronous processing capacity? | Easy | Developer | Performance | [Kafka Performance](/kafka-handbook/02-kafka/kafka-performance//) |

# Top 25 Frequently Asked Questions

1. Why does Kafka model messaging as a distributed commit log instead of a traditional point-to-point queue?
2. What delivery semantics does at-least-once processing imply for consumer application design?
3. Why are idempotent consumers mandatory when brokers guarantee at-least-once delivery with retries?
4. How do partition keys preserve ordering, and what hot-partition failure mode does poor key choice create?
5. What is consumer lag, and which operational signals would you monitor before a high-traffic campaign?
6. How do you size topic partition count for peak throughput versus maximum consumer parallelism?
7. How does schema drift break downstream deserializers, and what governance would you enforce with a schema registry?
8. When would you pick Kafka over RabbitMQ for high-volume event fan-out with replay requirements?
9. When is Redpanda a credible alternative to self-hosted Apache Kafka for an event platform?
10. How do consumer groups divide partition ownership, and what triggers a rebalance storm?
11. What is the tradeoff between `acks=1` and `acks=all` for write durability under broker failure?
12. What is the In-Sync Replica set, and how does ISR shrinkage affect durability guarantees?
13. When would you choose log compaction over time-based retention for a topic?
14. How would you tune producer batch size and linger.ms for throughput without breaching latency SLOs?
15. When does adding consumers stop reducing lag because partition count is the bottleneck?
16. What metrics beyond consumer lag define Kafka cluster health in production?
17. What is your incident runbook when all consumers in a critical group stop committing offsets?
18. How would you secure Kafka with mutual TLS between clients and brokers?
19. How does the transactional outbox pattern pair with Kafka to avoid dual-write inconsistencies?
20. How do you decide between log/stream platforms and classic queue brokers for a new microservice integration?
21. What happens during an unclean leader election, and when would you allow it in production?
22. How do idempotent producers prevent duplicate writes without full transactional semantics?
23. What failure modes appear during broker patching when partition leadership moves across the cluster?
24. How would you design a dead-letter topic and replay runbook for poison messages that block partition progress?
25. What team capabilities must exist before choosing self-hosted Kafka over a managed cloud queue?

# Top 25 Architect-Level Questions

1. Why is global ordering across an entire topic expensive in a distributed log architecture?
2. What ordering guarantees can you realistically promise to product teams when partition count exceeds one?
3. When is a managed cloud queue preferable to self-hosted Kafka despite reduced operational control?
4. What ADR criteria from the handbook would you use to justify Kafka as the enterprise event backbone?
5. How do throughput, ordering, and operational trade-offs differ across brokers listed in the messaging module?
6. What hybrid architecture uses Kafka for event streaming and RabbitMQ for task distribution in the same platform?
7. When would Apache Pulsar's unified queue-and-log model beat Kafka for multi-tenant streaming?
8. How does built-in geo-replication in Pulsar influence multi-datacenter architecture decisions versus MirrorMaker?
9. What tenancy isolation requirements would push you toward Pulsar over a single shared Kafka cluster?
10. How would you design SNS fan-out to multiple SQS queues versus a single Kafka topic with consumer groups?
11. How would you map the handbook's log versus queue versus cloud pub/sub taxonomy to a retail order platform?
12. How do consumer groups divide partition ownership, and what triggers a rebalance storm?
13. How does replication factor interact with rack awareness and cross-AZ fault tolerance?
14. When are Kafka transactions required versus idempotent producers plus idempotent consumers?
15. How does exactly-once stream processing differ from end-to-end exactly-once across Kafka and a database?
16. How would you design Kafka for multi-region active-active deployment with conflict resolution?
17. What role does MirrorMaker 2 play in disaster recovery versus real-time dual writes?
18. What Kubernetes operator patterns apply to running Kafka on Kubernetes at production scale?
19. How do you run a controlled failure drill on a Kafka cluster without customer impact?
20. What SASL mechanisms are appropriate for multi-tenant clusters, and what are their tradeoffs?
21. How do you prevent unauthorized consumers from reading sensitive PII topics?
22. How does the transactional outbox pattern pair with Kafka to avoid dual-write inconsistencies?
23. When is CDC preferable to application-published domain events for Kafka ingestion?
24. What saga orchestration patterns map cleanly to Kafka topics versus choreographed events?
25. How would you blueprint an event-driven architecture ADR using the handbook's selection criteria?

# Top 25 Production Troubleshooting Questions

1. How would you design a dead-letter topic and replay runbook for poison messages that block partition progress?
2. How does temporal decoupling in event-driven architectures complicate end-to-end debugging compared to sync RPC?
3. How would you troubleshoot a single partition falling behind while others remain healthy?
4. What failure modes appear during broker patching when partition leadership moves across the cluster?
5. What compatibility risks remain when migrating clients from Apache Kafka to Redpanda in production?
6. What happens during an unclean leader election, and when would you allow it in production?
7. How would you troubleshoot under-replicated partitions after a broker network partition?
8. What tombstone records and compaction lag issues break compacted topic consumers?
9. What causes rebalance loops when session.timeout.ms and max.poll.interval.ms are misconfigured?
10. How do you troubleshoot a producer receiving NOT_LEADER_FOR_PARTITION errors during cluster maintenance?
11. What steps isolate whether lag is producer-side, broker-side, or consumer-side?
12. How would you handle a topic accidentally created with replication factor one in production?
13. What is your incident runbook when all consumers in a critical group stop committing offsets?
14. How would you diagnose metadata request storms after a large-scale topic creation event?
15. How do Kafka Connect offset topics and connector failures affect CDC pipeline continuity?
16. How do Kafka Streams state stores recover after application redeploy or rebalance?
17. How does increasing retention without storage planning cause emergency disk expansion?
18. What happens when a compacted topic's disk usage grows because compaction cannot keep pace?
19. How would you recover from accidental topic deletion in a production cluster?
20. What quorum loss symptoms appear in KRaft or ZooKeeper during a zone outage?
21. How would you reset offsets safely to replay a topic after a downstream bug without corrupting idempotent state?
22. What symptoms indicate broker disk saturation, and how do log segments contribute?
23. What GC pauses on brokers correlate with request timeout spikes on producers?
24. What is the first check when consumer lag alerts fire during normal business hours?
25. How would you throttle misbehaving clients flooding a shared cluster?

# Top 25 Performance & Scalability Questions

1. Why does the handbook recommend sizing partitions for peak traffic rather than average load?
2. How does Kafka buffer producer bursts without dropping users when downstream processing is slower?
3. How would you auto-scale consumers in response to sustained consumer lag during traffic spikes?
4. How do you size topic partition count for peak throughput versus maximum consumer parallelism?
5. What happens to message ordering when you increase partition count on an existing high-traffic topic?
6. What symptoms indicate broker disk saturation, and how do log segments contribute?
7. How would you tune producer batch size and linger.ms for throughput without breaching latency SLOs?
8. What compression codec tradeoffs apply at high throughput — lz4, snappy, zstd, gzip?
9. How does fetch.min.bytes and max.wait.ms on consumers affect end-to-end latency?
10. What JVM and OS tuning would you apply on Kafka brokers serving millions of messages per day?
11. How do page cache and sequential disk writes explain Kafka's throughput on spinning disks versus NVMe?
12. What network and disk capacity math would you use for 30-day retention with replication factor three?
13. How do you plan broker count and partition leadership distribution to avoid hotspot brokers?
14. When does adding consumers stop reducing lag because partition count is the bottleneck?
15. What is the upper bound on useful partition count for a topic, and what metadata overhead grows?
16. What load-test scenarios validate partition and consumer sizing before Black Friday traffic?
17. How do you benchmark producer throughput separately from consumer processing capacity?
18. What GC pauses on brokers correlate with request timeout spikes on producers?
19. How would you throttle misbehaving clients flooding a shared cluster?
20. What quotas and ACL policies protect multi-team clusters from noisy neighbors?
21. How do you right-size `num.network.threads` and `num.io.threads` under heavy fetch load?
22. When does cross-datacenter replication latency dominate end-to-end event freshness SLOs?
23. How does choosing random UUID partition keys destroy ordering and create hot spots?
24. How do partition keys preserve ordering, and what hot-partition failure mode does poor key choice create?
25. What handbook guidance applies when peak traffic exceeds synchronous processing capacity?

# Top 25 Design & Architecture Questions

1. Why is global ordering across an entire topic expensive in a distributed log architecture?
2. When would you isolate real-time and batch consumers using separate consumer groups on the same topic?
3. What ordering guarantees can you realistically promise to product teams when partition count exceeds one?
4. When does synchronous cross-service consistency make Kafka a poor primary integration choice without sagas?
5. How do you decide between log/stream platforms and classic queue brokers for a new microservice integration?
6. What ADR criteria from the handbook would you use to justify Kafka as the enterprise event backbone?
7. When would you pick Kafka over RabbitMQ for high-volume event fan-out with replay requirements?
8. What hybrid architecture uses Kafka for event streaming and RabbitMQ for task distribution in the same platform?
9. When would Apache Pulsar's unified queue-and-log model beat Kafka for multi-tenant streaming?
10. How does built-in geo-replication in Pulsar influence multi-datacenter architecture decisions versus MirrorMaker?
11. How would you design SNS fan-out to multiple SQS queues versus a single Kafka topic with consumer groups?
12. How would you map the handbook's log versus queue versus cloud pub/sub taxonomy to a retail order platform?
13. When would you choose log compaction over time-based retention for a topic?
14. How does exactly-once stream processing differ from end-to-end exactly-once across Kafka and a database?
15. How would you design Kafka for multi-region active-active deployment with conflict resolution?
16. What role does MirrorMaker 2 play in disaster recovery versus real-time dual writes?
17. How does the transactional outbox pattern pair with Kafka to avoid dual-write inconsistencies?
18. When is CDC preferable to application-published domain events for Kafka ingestion?
19. How would you design event versioning so multiple consumer versions coexist during rollout?
20. What saga orchestration patterns map cleanly to Kafka topics versus choreographed events?
21. How do you enforce ordering per customer entity across multiple event types?
22. What anti-patterns appear when microservices share one consumer group across different services?
23. How would you blueprint an event-driven architecture ADR using the handbook's selection criteria?
24. How does replication factor interact with rack awareness and cross-AZ fault tolerance?
25. When is Kafka Streams preferable to an external stream processor for aggregations?
