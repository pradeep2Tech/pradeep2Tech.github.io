---
title: "Services"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "ClusterIP, NodePort, LoadBalancer, and stable pod endpoints."
tags: ["kubernetes-handbook", "kubernetes", "docker", "cheatsheet", "handbook"]
categories: ["Kubernetes Handbook"]
shortTitle: "Services"
module: 3
moduleTitle: "Networking & Exposure"
sectionRef: "3.1"
cheatSheet: true
aliases: ["/kubernetes-cheatsheet/services/"]
---

## Executive Summary

**Service** provides a stable virtual IP and DNS name routing to pods matching `selector`. Types: **ClusterIP** (default), **NodePort**, **LoadBalancer**, **ExternalName**.

---

## Commands

### kubectl expose deployment

**Purpose:** Create a Service targeting deployment pods.

**Syntax:**
```bash
kubectl expose deployment NAME --port=P --target-port=TP -n NS
```

**Example:**
```bash
kubectl expose deployment myapp --port=80 --target-port=8080 -n myapp
```

**Output:**
```
service/myapp exposed
```

**Common mistakes:**
- Port ≠ targetPort — common misconfiguration for apps listening on 8080
- Selector auto-matches deployment labels — custom labels need YAML

### kubectl get svc

**Purpose:** List Services with CLUSTER-IP and ports.

**Syntax:**
```bash
kubectl get svc -n NAMESPACE
```

**Example:**
```bash
kubectl get svc -n myapp
```

**Output:**
```
NAME    TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)\nmyapp   ClusterIP   10.96.120.45   <none>        80/TCP
```

**Common mistakes:**
- CLUSTER-IP none means headless — returns pod A records
- EXTERNAL-IP pending on cloud LB — check cloud controller logs

### kubectl port-forward svc

**Purpose:** Forward local port to Service for local testing.

**Syntax:**
```bash
kubectl port-forward svc/NAME LOCAL:REMOTE -n NS
```

**Example:**
```bash
kubectl port-forward svc/myapp 8080:80 -n myapp
```

**Output:**
```
Forwarding from 127.0.0.1:8080 -> 80
```

**Common mistakes:**
- Binds localhost only by default — `0.0.0.0` needs `--address`
- Dies when terminal closes — not for production traffic

### kubectl get endpoints / endpointslice

**Purpose:** Verify backend pods behind a Service.

**Syntax:**
```bash
kubectl get endpoints NAME -n NS
```

**Example:**
```bash
kubectl get endpoints myapp -n myapp
```

**Output:**
```
NAME    ENDPOINTS                          AGE\nmyapp   10.244.1.5:8080,10.244.2.3:8080   1d
```

**Common mistakes:**
- Empty ENDPOINTS means selector mismatch or no ready pods
- Prefer EndpointSlice on modern clusters — same diagnostic value

---

## Related Topics

- [Ingress](/kubernetes-handbook/ingress/) · [Network Policies](/kubernetes-handbook/network-policies/) · [Labels & Selectors](/kubernetes-handbook/labels-and-selectors/)
