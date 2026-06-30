---
title: "Ingress"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "HTTP/S routing, TLS, and ingress controller annotations."
tags: ["kubernetes-cheatsheet", "kubernetes", "docker", "cheatsheet", "handbook"]
categories: ["Kubernetes Cheatsheet"]
shortTitle: "Ingress"
module: 2
moduleTitle: "Networking & Exposure"
sectionRef: "2.2"
ShowToc: true
---

## Executive Summary

**Ingress** exposes HTTP/S routes to Services. Requires an **ingress controller** (nginx, traefik, AWS ALB, etc.). Handles host/path routing, TLS, and annotations.

---

## Commands

### kubectl get ingress

**Purpose:** List Ingress resources with hosts and address.

**Syntax:**
```bash
kubectl get ingress -n NAMESPACE
```

**Example:**
```bash
kubectl get ingress -n myapp
```

**Output:**
```
NAME    CLASS   HOSTS             ADDRESS       PORTS\nmyapp   nginx   api.example.com   10.0.0.50     80, 443
```

**Common mistakes:**
- ADDRESS empty until controller provisions LB or NodePort
- Wrong ingressClassName means controller ignores the Ingress

### kubectl describe ingress

**Purpose:** Show rules, backends, TLS secrets, and events.

**Syntax:**
```bash
kubectl describe ingress NAME -n NS
```

**Example:**
```bash
kubectl describe ingress myapp -n myapp
```

**Output:**
```
Rules:\n  Host: api.example.com\n    Path: / -> myapp:80
```

**Common mistakes:**
- Backend service port must match Service port number
- TLS secret must exist in same namespace

### curl via /etc/hosts

**Purpose:** Test routing before DNS cutover.

**Syntax:**
```bash
curl -H 'Host: HOST' http://INGRESS_IP/PATH
```

**Example:**
```bash
curl -H 'Host: api.example.com' http://10.0.0.50/health
```

**Output:**
```
{"status":"UP"}
```

**Common mistakes:**
- Forgotten Host header hits default backend
- HTTPS needs `-k` with self-signed or proper SNI

---

## Related Topics

- [Services](/kubernetes-cheatsheet/services/) · [TLS Secrets](/kubernetes-cheatsheet/secrets/) · [Kubernetes Handbook — NGINX Ingress](/kubernetes-handbook/nginx-ingress/)
