---
title: "Messaging & Events"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Spring Events, Kafka, RabbitMQ, retry, DLQ, idempotency — integration patterns."
tags: ["spring-boot", "spring", "handbook", "interview"]
categories: ["Spring Boot Handbook"]
shortTitle: "Messaging"
module: 7
moduleTitle: "Messaging & Events"
sectionRef: "7.1"
interviewHandbook: true
aliases:
  - events-ref
  - messaging-ref
---

## Spring Application Events vs message broker?

**Difficulty:** Medium  
**Expected Answer Time:** 1 min

### Short Answer

In-process `ApplicationEventPublisher` is synchronous by default within same JVM. Broker (Kafka/RabbitMQ) is cross-service, durable, at-least-once.

### Detailed Explanation

`@EventListener` runs in publisher thread unless `@Async`. `@TransactionalEventListener(AFTER_COMMIT)` ensures handlers see committed data. Domain events stay in-process; integration events go to broker.

### Internal Working

Events published via `ApplicationEventMulticaster`.

### Production Notes

For reliable cross-service publish with DB write, use transactional outbox — see [Microservices Playbook](/microservices/).

### Common Mistakes

Treating in-process events as delivery guarantee across pods.

### Follow-up Questions

- Outbox pattern?
- Event sourcing vs events?

---
## Kafka vs RabbitMQ in Spring Boot?

**Difficulty:** Medium  
**Expected Answer Time:** 1 min

### Short Answer

Kafka: log, partitioned, replay, high throughput — `spring-kafka`, `@KafkaListener`. RabbitMQ: queue routing, flexible exchanges — `spring-amqp`, `@RabbitListener`.

### Detailed Explanation

Kafka consumer groups scale with partitions. Rabbit competing consumers on queue. Spring abstracts template/listener containers; ack mode manual for at-least-once.

### Internal Working

`ConcurrentKafkaListenerContainerFactory` sets concurrency ≤ partitions.

### Production Notes

Idempotent consumers with business key dedup. DLQ for poison messages. Schema registry for evolution.

### Common Mistakes

Auto-commit before processing completes. No retry backoff — hammering downstream.

### Follow-up Questions

- Exactly-once semantics?
- When Kafka vs Rabbit?

---
## Retry patterns and DLQ?

**Difficulty:** Medium  
**Expected Answer Time:** 1 min

### Short Answer

Spring Retry / `@Retryable` for transient failures; after max attempts route to DLQ topic/queue for manual inspection.

### Detailed Explanation

Kafka: `SeekToCurrentErrorHandler` + `DeadLetterPublishingRecoverer`. Rabbit: `RepublishMessageRecoverer`. Exponential backoff with jitter. Distinguish retryable vs non-retryable exceptions.

### Internal Working

Listener container ack after successful processing when manual ack enabled.

### Production Notes

Monitor DLQ depth alert. Include original headers + failure reason in DLQ message.

### Common Mistakes

Infinite retry on bad payload. DLQ without replay tooling.

### Follow-up Questions

- Idempotency key storage?
- Saga vs retry?

---

## See Also

- [Previous: Cache & Perf](/spring-boot/caching-performance/)
- [Next: Observability](/spring-boot/observability/)
- [Cache & Perf](/spring-boot/caching-performance/)
- [100+ Interview Questions](/spring-boot/interview-questions/)
- [Spring Boot Handbook Index](/spring-boot/)
- [Java Engineering](/java-engineering/)
- [Microservices Playbook](/microservices/) — Saga, Outbox, CQRS, API Gateway
- [Kafka Handbook](/kafka-handbook/)
- [Security Architecture](/security-architecture/)
