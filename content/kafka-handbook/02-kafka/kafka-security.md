---
title: "Kafka Security"
date: 2026-07-03T10:00:00+00:00
draft: false
description: "TLS, SASL, ACLs, encryption, and multi-tenant isolation."
tags: ["kafka-handbook", "kafka", "messaging", "streaming", "interview"]
categories: ["Kafka Handbook"]
shortTitle: "Security"
module: 2
moduleTitle: "Apache Kafka"
sectionRef: "2.6"
weight: 206
interviewHandbook: true
---

## Quick Revision

- **mTLS** for client↔broker and broker↔broker.
- **SASL** (SCRAM, OAuth/OIDC) for authentication.
- **ACLs** for least-privilege topic/group/cluster ops.
- **Encryption at rest** via disk/KMS; app-layer for PII payloads.

## Core Concepts

| Layer | Mechanism |
| :--- | :--- |
| Transport | SSL/TLS listeners |
| Auth | SASL mechanisms |
| AuthZ | Kafka ACLs / RBAC (managed) |
| Audit | Authorizer logs, cloud audit trails |

## Internal Working

Clients bootstrap metadata over TLS; ACL authorizer checks principal on each API.

## Architecture

Segment networks: brokers in private subnets; no plaintext listeners in K8s production.

## Design Tradeoffs

| Approach | Notes |
| :--- | :--- |
| SCRAM | Simple; credential rotation discipline |
| mTLS | Strong; cert lifecycle ops |
| OAuth | Enterprise SSO; broker plugin support |

## Production Patterns

- Rotate broker certs with rolling restarts.
- Separate principals per service; deny `*` consume on PII topics.

## Scalability

ACL cache and authorizer latency — keep ACL sets maintainable.

## Reliability

Security misconfig shows as `TOPIC_AUTHORIZATION_FAILED` in clients.

## Security

{{% warning %}}
Plaintext listeners inside a cluster still expose traffic to anyone with pod network access.
{{% /warning %}}

## Observability

Alert on authorization failure spikes; audit admin operations.

## Troubleshooting

Client works in dev (PLAINTEXT) fails in prod (SSL) — check `security.protocol` and truststore.

## Common Mistakes

- Shared service account for all producers.
- Storing secrets in consumer properties in git.

## Interview Questions

- How would you rotate broker certificates without dropping clients?
- When is application-layer encryption needed beyond TLS?
- How do ACLs enforce least privilege on shared clusters?

## Architect Notes

Managed offerings (MSK, Confluent Cloud) shift authZ to IAM/RBAC — understand shared responsibility.
