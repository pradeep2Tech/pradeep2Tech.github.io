---
title: "SLO Alert Examples"
date: 2026-07-17T10:00:00+00:00
draft: false
description: "Implement request, latency, freshness, and business SLIs with error-budget burn alerts and actionable annotations."
tags: ["microservices", "slo", "prometheus", "alerting"]
categories: ["Microservices Architecture Playbook"]
shortTitle: "SLO Alert Examples"
module: 8
moduleTitle: "Observability"
sectionRef: "8.31"
weight: 831
playbookVersion: 3
---

## 1. Select the SLI

| SLI | Good event or interval |
| :--- | :--- |
| Request availability | Valid request has an acceptable outcome |
| Request latency | Valid request succeeds below its threshold |
| Time-based availability | Service meets the condition during a time interval |
| Queue freshness | Work completes before maximum age |
| Business outcome | Eligible checkout/payment/fulfillment reaches the defined outcome |

Define exclusions before implementation. Invalid client requests, health checks, synthetic traffic, and load shedding may have different treatment, but exclusions must not hide customer harm.

## 2. Core Calculations

```text
Availability SLI = good requests / valid requests
Latency SLI      = successful requests below threshold / valid requests
Error budget     = 1 - SLO target
Burn rate        = observed bad-event ratio / allowed bad-event ratio
```

For a 99.9% target, the allowed bad ratio is 0.001. A burn rate of 10 consumes budget ten times faster than the steady rate allowed by the objective.

## 3. Illustrative Prometheus Alert

> Metric and recorded-rule names are illustrative. Validate semantics, labels, traffic behavior, and Prometheus rule syntax against the deployed versions.

{{< code-tabs default="pseudo" pseudo="Prometheus Rules" >}}
{{< code-tab lang="pseudo" >}}
```yaml
groups:
  - name: checkout-slo-v1
    rules:
      - alert: CheckoutAvailabilityFastBurn
        expr: |
          service:http_error_ratio:rate5m{service="checkout"} > (14 * 0.001)
          and
          service:http_error_ratio:rate1h{service="checkout"} > (14 * 0.001)
        for: 2m
        labels:
          severity: page
          owner: checkout-platform
          slo: checkout-availability
        annotations:
          summary: "Checkout availability is consuming error budget rapidly"
          dashboard: "https://observability.example.invalid/d/checkout"
          runbook: "https://runbooks.example.invalid/checkout-availability"
          current_burn: "{{ $value }}"
          recent_deployment: "check deployment annotations"

      - alert: CheckoutAvailabilitySlowBurn
        expr: |
          service:http_error_ratio:rate30m{service="checkout"} > (3 * 0.001)
          and
          service:http_error_ratio:rate6h{service="checkout"} > (3 * 0.001)
        for: 15m
        labels:
          severity: warning
          owner: checkout-platform
          slo: checkout-availability
```
{{< /code-tab >}}
{{< /code-tabs >}}

The windows and multipliers are examples, not universal defaults. Tune them for the SLO window, traffic, response time, ingestion delay, severity, and operating model. Low-volume services may require longer windows, event-based evaluation, or synthetic evidence.

## 4. Actionable Annotations

Include affected service and journey, SLO and target, current burn, estimated exhaustion where reliable, dashboard, runbook, owner, region/version scope, and recent deployment. Do not put secrets or unique customer identifiers into labels or annotations.

## 5. Validation

Backtest against historical incidents and known healthy periods. Inject controlled failures for error rate, latency, queue age, and business outcomes. Verify alert timing, grouping, routing, deduplication, recovery, no-data behavior, and whether the responder can validate and mitigate from linked evidence. Review objectives and alert parameters after material traffic or architecture changes.

For the governing concepts, see [Alerting, SLOs, and Error Budgets](/microservices/08-observability/alerting-slos-and-error-budgets/).
