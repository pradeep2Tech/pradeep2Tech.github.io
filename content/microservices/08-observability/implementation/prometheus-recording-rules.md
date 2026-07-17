---
title: "Prometheus Recording Rules for Service Health"
date: 2026-07-17T10:00:00+00:00
draft: false
description: "Build reusable Prometheus request, error, latency, retry, pool, and lag calculations with controlled dimensions."
tags: ["microservices", "prometheus", "recording-rules", "promql"]
categories: ["Microservices Architecture Playbook"]
shortTitle: "Prometheus Recording Rules"
module: 8
moduleTitle: "Observability"
sectionRef: "8.29"
weight: 829
playbookVersion: 3
---

## 1. Purpose and Version Note

Recording rules precompute expensive queries, standardize health calculations, improve dashboards, create reusable SLI inputs, and isolate consumers from raw metric complexity. They do not repair incorrect instruments or unsafe labels.

> PromQL examples follow Prometheus documentation available on 2026-07-17. Metric names are illustrative unless identified as application contract; adapt them to the exporter and instrumentation version in use.

## 2. Request, Error, and Latency Rules

{{< code-tabs default="pseudo" pseudo="Prometheus Rules" >}}
{{< code-tab lang="pseudo" >}}
```yaml
groups:
  - name: service-health-v1
    interval: 30s
    rules:
      - record: service:http_requests:rate5m
        expr: |
          sum by (service, route) (
            rate(http_server_request_duration_seconds_count[5m])
          )

      - record: service:http_errors:rate5m
        expr: |
          sum by (service, route) (
            rate(http_server_request_duration_seconds_count{http_response_status_code=~"5.."}[5m])
          )

      - record: service:http_error_ratio:rate5m
        expr: |
          service:http_errors:rate5m
          /
          clamp_min(service:http_requests:rate5m, 1e-12)

      - record: service:http_duration_seconds:p95_5m
        expr: |
          histogram_quantile(0.95,
            sum by (le, service, route) (
              rate(http_server_request_duration_seconds_bucket[5m])
            )
          )
```
{{< /code-tab >}}
{{< /code-tabs >}}

Aggregate classic histogram buckets by `le` plus every output dimension. Do not average precomputed percentiles. Decide whether zero traffic should appear as absent, zero, or a separate availability condition; `clamp_min` prevents division by zero but does not define missing-series semantics.

## 3. Retry, Pool, and Queue Patterns

{{< code-tabs default="pseudo" pseudo="PromQL" >}}
{{< code-tab lang="pseudo" >}}
```promql
# Retry amplification: attempts per logical operation
sum by (service, dependency) (rate(dependency_attempts_total[5m]))
/
clamp_min(sum by (service, dependency) (rate(dependency_operations_total[5m])), 1e-12)

# Connection pool utilization
sum by (service, pool) (db_client_connections_usage{state="used"})
/
clamp_min(sum by (service, pool) (db_client_connections_limit), 1)

# Illustrative exporter metrics: verify names and semantics
max by (cluster, consumer_group, topic) (kafka_consumer_group_lag)
max by (cluster, consumer_group, topic) (kafka_consumer_oldest_message_age_seconds)
```
{{< /code-tab >}}
{{< /code-tabs >}}

Lag is workload-specific: absolute lag, lag growth, and oldest-message age answer different questions. Partition aggregation can hide one stuck partition; retaining every partition can be expensive.

## 4. Ownership and Validation

- Retain only dimensions needed for routing or diagnosis; use route templates.
- Apply `rate` before aggregating counters so resets are handled per series.
- Choose evaluation interval relative to scrape interval and alert response needs.
- Version rule groups and define a compatibility period for renamed outputs.
- Assign every recorded series an owner and downstream-consumer inventory.
- Test with `promtool check rules` and `promtool test rules`, including missing data, resets, low traffic, and absent buckets.
- Compare results against raw queries and known request counts before alerts depend on them.

See [Metrics Design](/microservices/08-observability/metrics-design/) for instrument and cardinality semantics.

