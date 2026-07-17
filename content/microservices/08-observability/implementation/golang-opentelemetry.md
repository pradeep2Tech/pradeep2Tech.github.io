---
title: "Go OpenTelemetry Implementation"
date: 2026-07-17T10:00:00+00:00
draft: false
description: "Configure Go OpenTelemetry providers, OTLP export, propagation, HTTP instrumentation, domain spans, metrics, and shutdown."
tags: ["microservices", "opentelemetry", "golang", "implementation"]
categories: ["Microservices Architecture Playbook"]
shortTitle: "Go OpenTelemetry"
module: 8
moduleTitle: "Observability"
sectionRef: "8.27"
weight: 827
playbookVersion: 3
---

## 1. Scope and Version Note

The example covers an inventory service receiving HTTP or gRPC work, consuming Kafka/NATS messages, and calling PostgreSQL. It assumes current stable OpenTelemetry Go API/SDK and OTLP modules; module paths and instrumentation packages evolve independently.

> Pin exact module versions in `go.mod`, review each instrumentation library's compatibility, and validate against the official OpenTelemetry Go documentation before production adoption.

## 2. Provider Lifecycle

{{< code-tabs default="golang" golang="Go" >}}
{{< code-tab lang="golang" >}}
```go
func newTracerProvider(ctx context.Context, endpoint string) (*sdktrace.TracerProvider, error) {
    exporter, err := otlptracegrpc.New(ctx,
        otlptracegrpc.WithEndpoint(endpoint),
        otlptracegrpc.WithInsecure(), // local cluster example; use TLS in production
    )
    if err != nil {
        return nil, fmt.Errorf("create OTLP trace exporter: %w", err)
    }

    res, err := resource.Merge(resource.Default(), resource.NewWithAttributes(
        semconv.SchemaURL,
        semconv.ServiceName("inventory-service"),
        semconv.ServiceVersion("1.4.2"),
        attribute.String("deployment.environment.name", "production"),
    ))
    if err != nil {
        return nil, fmt.Errorf("create resource: %w", err)
    }

    return sdktrace.NewTracerProvider(
        sdktrace.WithResource(res),
        sdktrace.WithSampler(sdktrace.ParentBased(sdktrace.TraceIDRatioBased(0.10))),
        sdktrace.WithBatcher(exporter),
    ), nil
}

func run(ctx context.Context) error {
    tp, err := newTracerProvider(ctx, "otel-collector.observability:4317")
    if err != nil {
        return err
    }
    otel.SetTracerProvider(tp)
    otel.SetTextMapPropagator(propagation.NewCompositeTextMapPropagator(
        propagation.TraceContext{}, propagation.Baggage{},
    ))
    defer func() {
        shutdownCtx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
        defer cancel()
        _ = tp.Shutdown(shutdownCtx)
    }()

    handler := otelhttp.NewHandler(http.HandlerFunc(reserveInventory), "inventory.reserve.http")
    return serveUntilCancelled(ctx, handler)
}
```
{{< /code-tab >}}
{{< /code-tabs >}}

`WithInsecure` is suitable only for a trusted local example. Use authenticated TLS and workload identity in production. A production bootstrap should initialize meter providers similarly, use periodic metric export, and surface initialization/shutdown errors without making exporter loss terminate the business service.

## 3. Context and Domain Spans

{{< code-tabs default="golang" golang="Go" >}}
{{< code-tab lang="golang" >}}
```go
func reserve(ctx context.Context, skuClass string) error {
    ctx, span := otel.Tracer("inventory-domain").Start(ctx, "inventory.reserve",
        trace.WithAttributes(attribute.String("inventory.sku_class", skuClass)),
    )
    defer span.End()

    if err := repository.Reserve(ctx); err != nil {
        span.RecordError(err)
        span.SetStatus(codes.Error, "reservation failed")
        return err
    }
    span.SetAttributes(attribute.String("inventory.outcome", "reserved"))
    return nil
}
```
{{< /code-tab >}}
{{< /code-tabs >}}

Pass `ctx` into HTTP clients, database calls, and goroutines. For detached work, deliberately define whether to preserve the parent, create a link, or start a new trace. Kafka/NATS producers inject into message headers; consumers extract before starting their processing span. Never place secrets or high-cardinality business identifiers in baggage.

## 4. Instrumentation Boundaries

- Wrap HTTP servers and transports with supported instrumentation.
- Use maintained database instrumentation or create spans around repository boundaries without recording bind values.
- Instrument Kafka/NATS publish, broker wait where available, consume, retry, and dead-letter transitions.
- Create counters for outcomes/retries and histograms for queue wait/dependency duration with bounded dimensions.
- Add current trace/span IDs to structured logs through an explicit logging adapter.

Avoid instrumenting high-frequency internal functions or duplicating spans emitted by libraries.

## 5. Validation and Hardening

Verify parent-child relationships, message-header propagation, database spans, metric aggregation, log correlation, graceful flush, and absence of sensitive attributes. Test Collector loss and confirm batch queues remain bounded and requests continue.

Go-specific failure modes include losing context across goroutines, forgetting `span.End`, skipping shutdown flush, adding unbounded attributes, blocking on synchronous export, and incompatible instrumentation modules. Pin dependencies, run `go test`, `go vet`, and `gofmt` in the actual application module, benchmark overhead, and use an operational kill switch.

