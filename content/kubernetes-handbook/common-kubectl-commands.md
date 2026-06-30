---
title: "Common kubectl Commands"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Everyday kubectl for apply, get, logs, exec, port-forward, and debug."
tags: ["kubernetes-handbook", "kubernetes", "docker", "cheatsheet", "handbook"]
categories: ["Kubernetes Handbook"]
shortTitle: "kubectl"
module: 5
moduleTitle: "Operations & Security"
sectionRef: "5.5"
ShowToc: true
cheatSheet: true
aliases: ["/kubernetes-cheatsheet/common-kubectl-commands/"]
---

## Executive Summary

Day-to-day **kubectl** for apply, diff, watch, contexts, and output formatting. Prefer declarative manifests over imperative creates in production.

---

## Commands

### kubectl apply -f

**Purpose:** Declarative create/update from file or directory.

**Syntax:**
```bash
kubectl apply -f PATH [-n NS]
```

**Example:**
```bash
kubectl apply -f k8s/ -n myapp
```

**Output:**
```
deployment.apps/myapp configured\nservice/myapp unchanged
```

**Common mistakes:**
- Recursive `-f k8s/` applies all yaml — order does not matter
- Use `kubectl diff -f` before apply in production

### kubectl get -w

**Purpose:** Watch resource changes in real time.

**Syntax:**
```bash
kubectl get RESOURCE -w -n NS
```

**Example:**
```bash
kubectl get pods -w -n myapp
```

**Output:**
```
NAME    READY   STATUS\napi-0   1/1     Running\napi-1   0/1     ContainerCreating
```

**Common mistakes:**
- Watch streams until interrupted — use timeout in scripts
- High churn namespaces produce noisy output

### kubectl config use-context

**Purpose:** Switch kubeconfig cluster/user/namespace context.

**Syntax:**
```bash
kubectl config use-context CONTEXT
```

**Example:**
```bash
kubectl config use-context prod-eks
```

**Output:**
```
Switched to context "prod-eks".
```

**Common mistakes:**
- Easy to apply to prod while thinking staging — prompt context in PS1
- Multiple kubeconfig files merge — know precedence rules

### kubectl explain

**Purpose:** OpenAPI docs for resource fields in terminal.

**Syntax:**
```bash
kubectl explain RESOURCE.FIELD
```

**Example:**
```bash
kubectl explain deployment.spec.strategy
```

**Output:**
```
KIND: Deployment\nFIELD: strategy ...
```

**Common mistakes:**
- Requires cluster connectivity for live schema
- Offline use `kubectl explain --api-version=apps/v1 deployment`

### kubectl get events

**Purpose:** Sort cluster events for debugging recent failures.

**Syntax:**
```bash
kubectl get events -n NS --sort-by='.lastTimestamp'
```

**Example:**
```bash
kubectl get events -n myapp --sort-by='.lastTimestamp'
```

**Output:**
```
LAST SEEN   TYPE     REASON    OBJECT        MESSAGE
```

**Common mistakes:**
- Events expire after ~1h — use cluster logging for history
- Normal events filtered out — grep Warning

---

## Related Topics

- [Troubleshooting](/kubernetes-handbook/troubleshooting/) · [Kubernetes Architecture](/kubernetes-handbook/kubernetes-architecture/)
