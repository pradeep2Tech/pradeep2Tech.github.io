---
title: "Messaging Reference"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Kafka and RabbitMQ listener/producer snippets."
tags: ["spring-boot", "spring", "cheatsheet", "handbook"]
categories: ["Spring Boot Cheat Sheet"]
shortTitle: "Messaging"
module: 8
moduleTitle: "Distributed"
sectionRef: "8.2"
ShowToc: true
cheatSheet: true
---

## At a Glance

- Kafka: `spring-kafka` + `@KafkaListener`.
- RabbitMQ: `spring-amqp` + `@RabbitListener`.
- Idempotent consumers + dead-letter for failures.

---

## Reference Tables

| Broker | Send | Receive |
| :--- | :--- | :--- |
| Kafka | `KafkaTemplate.send` | `@KafkaListener` |
| RabbitMQ | `RabbitTemplate` | `@RabbitListener` |

| Setting | Why |
| :--- | :--- |
| `enable.auto.commit=false` | Manual ack after processing |
| consumer group | Horizontal scale |

---

## Snippets

```java
@KafkaListener(topics = "orders", groupId = "billing")
public void onOrder(OrderEvent event) { ... }
```

---

## Internals & Gotchas

- Broker internals → [Kafka Handbook](/kafka-handbook/).
- This page is Spring integration only.

---

## Production Notes

- Serialize with schema registry or versioned JSON.
- Outbox for reliable publish with DB.

---

## Interview Probes


{< interview-answer >}
**Q:** @KafkaListener concurrency?

**A:** Container concurrency threads per topic partition cap.
{< /interview-answer >}

---

## See Also

- [Previous: Spring Cloud](/spring-boot/spring-cloud-ref/)
- [Next: Interview](/spring-boot/spring-boot-interview-ref/)
- [Spring Boot Cheat Sheet Index](/spring-boot/)
- [Java Engineering](/java-engineering/)
- [Microservices Playbook](/microservices/)
