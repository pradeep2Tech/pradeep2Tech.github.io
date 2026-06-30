---
title: "Code Tabs Example (Internal Reference)"
date: 2026-06-30T12:00:00+00:00
draft: true
description: "Example of Java / Go / Python / Pseudo horizontal code tabs for microservices playbook posts."
tags: ["microservices", "example"]
categories: ["Distributed Microservices"]
shortTitle: "Code Tabs Example"
module: 2
moduleTitle: "API Boundaries, Discovery & Fault Tolerance"
sectionRef: "2.0"
playbookVersion: 2
---

This page demonstrates the `code-tabs` shortcode. It is `draft: true` and not linked from the curriculum index.

## 11. Implementation

{{< code-tabs default="java" java="Java" golang="Go" python="Python" pseudo="Pseudo" >}}
{{< code-tab lang="java" >}}

```java
@Retry(name = "inventory")
@CircuitBreaker(name = "inventory", fallbackMethod = "reserveFallback")
public boolean reserve(String sku, int qty) {
    return inventoryClient.reserve(sku, qty);
}
```

{{< /code-tab >}}
{{< code-tab lang="golang" >}}

```go
func (c *InventoryClient) Reserve(ctx context.Context, sku string, qty int) error {
    _, err := c.breaker.Execute(func() (interface{}, error) {
        return nil, c.client.Post(ctx, "/reserve", ReserveRequest{SKU: sku, Qty: qty})
    })
    return err
}
```

{{< /code-tab >}}
{{< code-tab lang="python" >}}

```python
@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=0.5))
def reserve(sku: str, qty: int) -> bool:
    response = httpx.post("/reserve", json={"sku": sku, "qty": qty}, timeout=2.0)
    response.raise_for_status()
    return response.json()["reserved"]
```

{{< /code-tab >}}
{{< code-tab lang="pseudo" >}}

```text
ON reserve(sku, qty):
  IF circuit.state == OPEN: RETURN fallback
  TRY remote_call("/reserve")
  ON success: RETURN true
  ON failure: INCREMENT failure_count; MAYBE trip circuit
```

{{< /code-tab >}}
{{< /code-tabs >}}
