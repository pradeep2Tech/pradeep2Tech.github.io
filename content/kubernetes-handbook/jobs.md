---
title: "Jobs"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Run-to-completion workloads with parallelism and backoff."
tags: ["kubernetes-handbook", "kubernetes", "docker", "cheatsheet", "handbook"]
categories: ["Kubernetes Handbook"]
shortTitle: "Jobs"
module: 1
moduleTitle: "Architecture & Workloads"
sectionRef: "1.7"
ShowToc: true
cheatSheet: true
aliases: ["/kubernetes-cheatsheet/jobs/"]
---

## Executive Summary

**Job** runs one or more pods until a fixed number complete successfully. Supports parallelism, completions, backoff, and TTL after finish.

---

## Commands

### kubectl create job

**Purpose:** Create a Job from an image or manifest.

**Syntax:**
```bash
kubectl create job NAME --image=IMAGE [-n NS]
```

**Example:**
```bash
kubectl create job migrate --image=myapp:migrator -n myapp
```

**Output:**
```
job.batch/migrate created
```

**Common mistakes:**
- Imperative jobs lack resource limits — prefer YAML in production
- Image command must exit 0 for success

### kubectl get jobs

**Purpose:** List Jobs with completion and duration.

**Syntax:**
```bash
kubectl get jobs -n NAMESPACE
```

**Example:**
```bash
kubectl get jobs -n myapp
```

**Output:**
```
NAME      COMPLETIONS   DURATION   AGE\nmigrate   1/1           45s        2m
```

**Common mistakes:**
- COMPLETIONS 0/1 with failures — check `kubectl logs job/NAME`
- Suspended jobs show no active pods

### kubectl logs job/NAME

**Purpose:** Fetch logs from pods owned by a Job.

**Syntax:**
```bash
kubectl logs job/JOB_NAME -n NS
```

**Example:**
```bash
kubectl logs job/migrate -n myapp
```

**Output:**
```
Migration completed successfully
```

**Common mistakes:**
- Parallel jobs need `-l job-name=NAME` or pick pod by label
- Use `--previous` if container restarted within backoff

---

## Related Topics

- [CronJobs](/kubernetes-handbook/cronjobs/) · [Pods](/kubernetes-handbook/pods/)
