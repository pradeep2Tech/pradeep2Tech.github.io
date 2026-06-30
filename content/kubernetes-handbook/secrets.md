---
title: "Secrets"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Sensitive data — encoding, mounting, and production secret management."
tags: ["kubernetes-handbook", "kubernetes", "docker", "cheatsheet", "handbook"]
categories: ["Kubernetes Handbook"]
shortTitle: "Secrets"
module: 3
moduleTitle: "Configuration & Storage"
sectionRef: "3.2"
ShowToc: true
cheatSheet: true
aliases: ["/kubernetes-cheatsheet/secrets/"]
---

## Executive Summary

**Secret** stores sensitive bytes (base64 in etcd). Types: **Opaque**, **kubernetes.io/tls**, **dockerconfigjson**. Prefer external secret operators in production.

---

## Commands

### kubectl create secret generic

**Purpose:** Create Opaque secret from literals or files.

**Syntax:**
```bash
kubectl create secret generic NAME --from-literal=k=v -n NS
```

**Example:**
```bash
kubectl create secret generic db-creds --from-literal=password='s3cret' -n myapp
```

**Output:**
```
secret/db-creds created
```

**Common mistakes:**
- Literal passwords appear in shell history — use `--from-env-file` or stdin
- Base64 is encoding not encryption — restrict RBAC

### kubectl get secret

**Purpose:** List secrets (values hidden by default).

**Syntax:**
```bash
kubectl get secrets -n NAMESPACE
```

**Example:**
```bash
kubectl get secrets -n myapp
```

**Output:**
```
NAME       TYPE     DATA   AGE\ndb-creds   Opaque   1      1h
```

**Common mistakes:**
- `kubectl get secret -o yaml` exposes decoded data — never paste in tickets
- Service account tokens auto-created as secrets in older clusters

### kubectl create secret docker-registry

**Purpose:** Pull private images via imagePullSecrets.

**Syntax:**
```bash
kubectl create secret docker-registry NAME --docker-server=REG --docker-username=U --docker-password=P -n NS
```

**Example:**
```bash
kubectl create secret docker-registry regcred --docker-server=registry.example.com --docker-username=ci --docker-password=token -n myapp
```

**Output:**
```
secret/regcred created
```

**Common mistakes:**
- Must reference secret in pod spec `imagePullSecrets`
- Expired registry tokens cause ImagePullBackOff

---

## Related Topics

- [ConfigMaps](/kubernetes-handbook/configmaps/) · [RBAC](/kubernetes-handbook/rbac/) · [Production Best Practices](/kubernetes-handbook/production-best-practices/)
