---
title: "Interview Revision Path"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "30–60 minute Kafka interview cram — highest-yield topics and question banks."
tags: ["kafka-handbook", "kafka", "messaging", "streaming", "interview", "learning-path"]
categories: ["Kafka Handbook"]
shortTitle: "Interview Revision"
module: 5
moduleTitle: "Learning Paths"
sectionRef: "5.4"
weight: 504
ShowToc: true
interviewHandbook: true
---

# Interview Revision Path

**Audience:** Anyone with an interview in 30–60 minutes.  
**Outcome:** Refresh mental model, top failure modes, and where to find full answers.

## 30-Minute Sprint

| Minutes | Topic | Page |
| :---: | :--- | :--- |
| 5 | Log vs queue | [Queue vs Stream](/kafka-handbook/01-fundamentals/queue-vs-stream/) |
| 10 | Core vocabulary | [Kafka Core](/kafka-handbook/02-kafka/kafka-core/) — Quick Revision section |
| 10 | ISR + acks | [Kafka Internals](/kafka-handbook/02-kafka/kafka-internals/) |
| 5 | Semantics | [Delivery Semantics](/kafka-handbook/02-kafka/kafka-delivery-semantics/) |

## 60-Minute Add-On

| Minutes | Topic | Page |
| :---: | :--- | :--- |
| 15 | Consumer groups + rebalance | [Consumer Groups](/kafka-handbook/02-kafka/kafka-consumer-groups/) |
| 10 | Lag + DLT | [Troubleshooting](/kafka-handbook/02-kafka/kafka-troubleshooting/) |
| 5 | One comparison | [Kafka vs RabbitMQ](/kafka-handbook/03-broker-comparisons/kafka-vs-rabbitmq/) |

## Question Banks (No Answers)

Pick one list matching your role:

- [Top 150](/kafka-handbook/04-interview-guide/top-150-interview-questions/) — full bank with Deep Dive links
- [Architect](/kafka-handbook/04-interview-guide/architect-questions/)
- [Troubleshooting](/kafka-handbook/04-interview-guide/troubleshooting-questions/)
- [Performance](/kafka-handbook/04-interview-guide/performance-questions/)

## Whiteboard Drill

Draw: `Producer → Leader → ISR → Consumer fetch → offset commit`  
Say aloud: delivery guarantee + idempotency + DLQ for every reliability question.

## See Also

- [Senior Engineer Path](/kafka-handbook/05-learning-paths/kafka-senior-engineer-path/) — deeper study order
