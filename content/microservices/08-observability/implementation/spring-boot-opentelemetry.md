---
title: "Spring Boot OpenTelemetry Implementation"
date: 2026-07-17T10:00:00+00:00
draft: false
description: "Instrument a Spring Boot service with portable OpenTelemetry traces, metrics, propagation, and structured log correlation."
tags: ["microservices", "opentelemetry", "spring-boot", "java"]
categories: ["Microservices Architecture Playbook"]
shortTitle: "Spring Boot OpenTelemetry"
module: 8
moduleTitle: "Observability"
sectionRef: "8.26"
weight: 826
playbookVersion: 3
---

## 1. Scope and Version Note

This vendor-neutral guide instruments an order service across REST, an HTTP payment client, Kafka, and PostgreSQL. It implements the architecture in [OpenTelemetry Architecture](/microservices/08-observability/opentelemetry-architecture/) without making telemetry delivery a request-path dependency.

> Configuration names were checked against OpenTelemetry Java agent and OTLP SDK documentation available on 2026-07-17. Agent 2.x and the Spring Boot starter can have different defaults from older releases. Pin and test the Java agent, Spring Boot, Micrometer, and instrumentation versions together.

## 2. Choose an Approach

| Approach | Choose when | Trade-off |
| :--- | :--- | :--- |
| Java agent | Fast, broad framework coverage | Agent compatibility and less explicit code control |
| Spring Boot starter/supported SDK integration | Spring-managed configuration is required | Version alignment and narrower automatic coverage |
| Manual SDK | Custom lifecycle or unsupported runtime | More code, testing, and upgrade ownership |
| Micrometer plus OTLP/Prometheus | Existing Spring metrics are authoritative | Metric semantics must be reconciled |
| Vendor agent | Proprietary depth is worth coupling | Portability and feature parity are not guaranteed |

Start with the Java agent for representative services, then add only domain spans and metrics that automatic instrumentation cannot infer.

## 3. Agent Configuration

{{< code-tabs default="pseudo" pseudo="Shell" >}}
{{< code-tab lang="pseudo" >}}
```bash
export JAVA_TOOL_OPTIONS="-javaagent:/opt/otel/opentelemetry-javaagent.jar"
export OTEL_SERVICE_NAME="order-service"
export OTEL_EXPORTER_OTLP_ENDPOINT="http://otel-collector.observability:4317"
export OTEL_EXPORTER_OTLP_PROTOCOL="grpc"
export OTEL_RESOURCE_ATTRIBUTES="deployment.environment.name=production,service.version=1.4.2,cloud.region=region-a"
export OTEL_PROPAGATORS="tracecontext,baggage"
export OTEL_TRACES_SAMPLER="parentbased_traceidratio"
export OTEL_TRACES_SAMPLER_ARG="0.10"
java -jar app.jar
```
{{< /code-tab >}}
{{< /code-tabs >}}

Use TLS and workload identity outside a trusted local network. Keep exporter headers in a secret reference, never source control. A 10% ratio is illustrative; choose sampling from traffic, failure rarity, tail-sampling design, and cost.

## 4. Manual Domain Span

{{< code-tabs default="java" java="Java" >}}
{{< code-tab lang="java" >}}
```java
private final Tracer tracer = GlobalOpenTelemetry.getTracer("order-domain");

public ValidationResult validate(Order order) {
    Span span = tracer.spanBuilder("order.validate")
        .setAttribute("order.channel", order.channel()) // bounded enum
        .startSpan();
    try (Scope ignored = span.makeCurrent()) {
        ValidationResult result = validator.validate(order);
        span.setAttribute("order.validation.outcome", result.outcome());
        return result;
    } catch (RuntimeException ex) {
        span.recordException(ex);
        span.setStatus(StatusCode.ERROR);
        throw ex;
    } finally {
        span.end();
    }
}
```
{{< /code-tab >}}
{{< /code-tabs >}}

Do not recreate agent-generated server, HTTP client, Kafka, or JDBC spans. Domain names such as `order.validate`, `payment.authorize`, and `inventory.reserve` should represent business boundaries, with bounded outcomes rather than order or user IDs.

## 5. Metrics and Log Correlation

Use counters for `orders.created`, `payment.authorization` outcomes, and retries; histograms for queue wait and dependency duration. Keep dimensions bounded to outcome, channel, dependency, and error class. Do not use request, order, session, or raw tenant identifiers.

Example structured event after the logging framework injects current trace context:

{{< code-tabs default="pseudo" pseudo="JSON" >}}
{{< code-tab lang="pseudo" >}}
```json
{"level":"ERROR","service":"order-service","service_version":"1.4.2","trace_id":"4f...","span_id":"9a...","event":"payment_authorization_failed","error_type":"GatewayTimeout"}
```
{{< /code-tab >}}
{{< /code-tabs >}}

Confirm the chosen logging instrumentation actually populates trace/span fields; MDC key names vary by agent and logging integration.

## 6. Validation

1. Send one successful and one failed request and confirm server spans reach the Collector.
2. Verify HTTP client spans are children of the request and identify the payment dependency.
3. Verify Kafka producer context is extracted by the consumer without unsafe baggage.
4. Confirm JDBC spans use normalized operations and do not expose bind values.
5. Compare counters and histograms with known test traffic.
6. Pivot from a trace to the correlated structured log.
7. Inspect exported attributes for secrets, PII, raw URLs, and cardinality risks.

## 7. Production Hardening

Use batch export, bounded queues, strict timeouts, parent-based or Collector tail sampling, pinned agent compatibility tests, and measured CPU/memory overhead. Decide startup behavior when the agent is invalid and export behavior when the Collector is unavailable. Business requests must continue; drops and queue pressure must be observable. Roll out by version and retain an agent-disable switch.

