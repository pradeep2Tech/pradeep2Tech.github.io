---
title: "Pods"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Smallest deployable unit — containers, init containers, and pod lifecycle."
tags: ["kubernetes-handbook", "kubernetes", "docker", "cheatsheet", "handbook"]
categories: ["Kubernetes Handbook"]
shortTitle: "Pods"
module: 2
moduleTitle: "Architecture & Workloads"
sectionRef: "2.2"
cheatSheet: true
aliases: ["/kubernetes-cheatsheet/pods/"]
---

## Executive Summary

A **Pod** wraps one or more containers sharing network namespace, IPC, and volumes. Kubernetes schedules and health-checks pods; controllers (Deployment, StatefulSet) own pod templates.

---

## Commands

### kubectl get pods

**Purpose:** List pods in a namespace with readiness and restart count.

**Syntax:**
```bash
kubectl get pods [-n NAMESPACE] [-o wide]
```

**Example:**
```bash
kubectl get pods -n myapp -o wide
```

**Output:**
```
NAME           READY   STATUS    RESTARTS   AGE   IP           NODE\napi-7f8b9c-xyz  1/1     Running   0          10m   10.244.1.5   node-2
```

**Common mistakes:**
- Omitting `-n` shows only `default` namespace pods
- `0/1 Ready` means readiness probe failing — not necessarily crashed

### kubectl describe pod

**Purpose:** Show events, conditions, container states, and probe failures.

**Syntax:**
```bash
kubectl describe pod POD_NAME -n NAMESPACE
```

**Example:**
```bash
kubectl describe pod api-7f8b9c-xyz -n myapp
```

**Output:**
```
Events:\n  Normal  Scheduled  ...\n  Warning Failed     ...
```

**Common mistakes:**
- Events scroll off quickly — combine with `kubectl get events`
- Last State from previous container helps debug CrashLoopBackOff

### kubectl logs

**Purpose:** Stream stdout/stderr from a container.

**Syntax:**
```bash
kubectl logs POD [-c CONTAINER] [-f] [--tail=N] -n NS
```

**Example:**
```bash
kubectl logs -f api-7f8b9c-xyz -n myapp --tail=100
```

**Output:**
```
2026-06-30T10:00:01 INFO  Started application...
```

**Common mistakes:**
- Multi-container pods require `-c` to pick the right container
- `--previous` needed to see logs from crashed container

### kubectl run (debug pod)

**Purpose:** Spin up a temporary pod for curl/dns/network debugging.

**Syntax:**
```bash
kubectl run NAME --rm -it --image=IMAGE -- COMMAND
```

**Example:**
```bash
kubectl run curl --rm -it --image=curlimages/curl -n myapp -- curl -s http://myapp-svc
```

**Output:**
```
HTTP/1.1 200 OK
```

**Common mistakes:**
- Forgotten `--rm` leaves debug pods behind
- Image must exist in cluster or be pullable — set pull policy if needed

---

## YAML Snippet

### Pod manifest

**Purpose:** Define a single pod (prefer Deployment for production).

**Syntax:**
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: api
  labels:
    app: api
spec:
  containers:
    - name: api
      image: myapp:1.0.0
      ports:
        - containerPort: 8080
```

**Example:**
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: debug
  namespace: myapp
spec:
  restartPolicy: Never
  containers:
    - name: curl
      image: curlimages/curl:8.5.0
      command: ["sleep", "3600"]
```

**Common mistakes:**
- Bare pods are not self-healing — use a controller
- Set `restartPolicy` explicitly for Jobs vs long-running workloads

---

## Related Topics

- [Deployments](/kubernetes-handbook/deployments/) · [Probes](/kubernetes-handbook/probes/) · [Resource Limits](/kubernetes-handbook/resource-limits/)
