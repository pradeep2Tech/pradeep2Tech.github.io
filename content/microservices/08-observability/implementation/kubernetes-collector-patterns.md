---
title: "Kubernetes OpenTelemetry Collector Patterns"
date: 2026-07-17T10:00:00+00:00
draft: false
description: "Deploy node agents and regional Collector gateways with bounded backpressure, enrichment, sampling, isolation, and failure tests."
tags: ["microservices", "opentelemetry", "kubernetes", "collector"]
categories: ["Microservices Architecture Playbook"]
shortTitle: "Kubernetes Collector Patterns"
module: 8
moduleTitle: "Observability"
sectionRef: "8.28"
weight: 828
playbookVersion: 3
---

## 1. Deployment Models

| Pattern | Use for | Main risk |
| :--- | :--- | :--- |
| DaemonSet agent | Host/kubelet metrics, file logs, node enrichment, local OTLP | Per-node resource use and privileged access |
| Gateway Deployment | Policy, credentials, routing, tail sampling, tenancy, egress | Central saturation and affinity requirements |
| Hybrid | Local collection plus regional policy and export | Two capacity and failure domains |
| Sidecar | Strict workload isolation or legacy local-only integration | Pod multiplication and lifecycle overhead |

Sidecars are exceptions, not the default.

```text
Applications -> Node-local Collector -> Regional Gateway Collectors -> Backends
```

## 2. Representative Collector Configuration

> This example targets the OpenTelemetry Collector Kubernetes/contrib component set documented on 2026-07-17. Component stability and configuration change by release; validate against the exact pinned distribution with its `validate` command before rollout.

{{< code-tabs default="pseudo" pseudo="YAML" >}}
{{< code-tab lang="pseudo" >}}
```yaml
receivers:
  otlp:
    protocols:
      grpc:
        endpoint: 0.0.0.0:4317
      http:
        endpoint: 0.0.0.0:4318

processors:
  memory_limiter:
    check_interval: 1s
    limit_percentage: 75
    spike_limit_percentage: 15
  k8sattributes:
    auth_type: serviceAccount
    passthrough: false
  resource:
    attributes:
      - key: deployment.environment.name
        value: production
        action: upsert
  tail_sampling:
    decision_wait: 10s
    num_traces: 50000
    policies:
      - name: errors
        type: status_code
        status_code: {status_codes: [ERROR]}
      - name: baseline
        type: probabilistic
        probabilistic: {sampling_percentage: 10}
  batch: {}

exporters:
  otlp/backend:
    endpoint: telemetry-backend.observability:4317
    tls: {insecure: false}
    sending_queue:
      enabled: true
      queue_size: 5000
    retry_on_failure:
      enabled: true
      max_elapsed_time: 300s

service:
  telemetry:
    metrics:
      level: normal
  pipelines:
    traces:
      receivers: [otlp]
      processors: [memory_limiter, k8sattributes, resource, tail_sampling, batch]
      exporters: [otlp/backend]
```
{{< /code-tab >}}
{{< /code-tabs >}}

Run tail sampling only at a tier that receives every span for a trace and provides stable trace-to-gateway routing. Put the memory limiter early and batch late. Queue sizing must follow memory, event size, outage tolerance, and loss policy—not copied defaults.

## 3. Kubernetes Resources

Provide measured requests/limits, PodDisruptionBudget, topology spread or anti-affinity, horizontal scaling for gateways, stable Services, default-deny NetworkPolicy with explicit flows, workload identity/service accounts, reviewed configuration delivery, and secret references. Keep configuration versioned and progressively roll it out. DaemonSets require node selectors/tolerations that match intended coverage.

Gateway scaling signals should include CPU, memory, receive rate, refusal/drop rate, queue use, export latency, and load-balancing skew. Scaling cannot recover traces already split incorrectly for tail sampling.

## 4. Failure Handling and Tests

| Test | Expected behavior |
| :--- | :--- |
| Backend unavailable | Bounded retry/queue, visible pressure, business traffic unaffected |
| Collector terminated | Redundant route or short controlled loss; restart does not surge uncontrollably |
| Queue full | Explicit drop/refusal metrics and owner alert |
| Invalid credentials | Fast detection, no infinite retry hiding configuration error |
| Network partition | Bounded buffering and regional isolation |
| Traffic spike | Load shedding protects memory and critical signals |
| Malformed telemetry | Rejection is attributable without pipeline crash |
| Cardinality attack | Limits and filtering contain backend impact |

Also rehearse configuration rollback and regional backend failover. Monitor Collector internal telemetry from an independent path where practical.

