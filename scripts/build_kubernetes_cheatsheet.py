"""Build Kubernetes Handbook workload/Docker pages from data/kubernetes_handbook_modules.yaml."""
from __future__ import annotations

import textwrap
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
CONTENT = ROOT / "content" / "kubernetes-handbook"
DATE = "2026-06-30T10:00:00+00:00"
SECTION = "kubernetes-handbook"
CATEGORY = "Kubernetes Handbook"


def cmd(
    name: str,
    purpose: str,
    syntax: str,
    example: str,
    output: str,
    mistakes: list[str],
) -> str:
    bullets = "\n".join(f"- {m}" for m in mistakes)
    return (
        f"### {name}\n\n"
        f"**Purpose:** {purpose}\n\n"
        f"**Syntax:**\n"
        f"```bash\n{syntax.strip()}\n```\n\n"
        f"**Example:**\n"
        f"```bash\n{example.strip()}\n```\n\n"
        f"**Output:**\n"
        f"```\n{output.strip()}\n```\n\n"
        f"**Common mistakes:**\n{bullets}"
    )


def yaml_block(name: str, purpose: str, syntax: str, example: str, mistakes: list[str]) -> str:
    bullets = "\n".join(f"- {m}" for m in mistakes)
    syntax = syntax.replace("\\n", "\n")
    example = example.replace("\\n", "\n")
    return (
        f"### {name}\n\n"
        f"**Purpose:** {purpose}\n\n"
        f"**Syntax:**\n"
        f"```yaml\n{syntax.strip()}\n```\n\n"
        f"**Example:**\n"
        f"```yaml\n{example.strip()}\n```\n\n"
        f"**Common mistakes:**\n{bullets}"
    )


TOPIC_META: dict[str, tuple[str, str, str]] = {
    "kubernetes-architecture": (
        "Kubernetes Architecture",
        "Architecture",
        "Control plane, worker nodes, etcd, and component responsibilities.",
    ),
    "pods": ("Pods", "Pods", "Smallest deployable unit — containers, init containers, and pod lifecycle."),
    "replicasets": ("ReplicaSets", "ReplicaSets", "Replica count enforcement and pod template matching."),
    "deployments": ("Deployments", "Deployments", "Declarative rollouts, scaling, and rollback for stateless apps."),
    "statefulsets": ("StatefulSets", "StatefulSets", "Stable identity, ordered rollout, and persistent storage for stateful apps."),
    "daemonsets": ("DaemonSets", "DaemonSets", "Run one pod per node — agents, log collectors, CNI plugins."),
    "jobs": ("Jobs", "Jobs", "Run-to-completion workloads with parallelism and backoff."),
    "cronjobs": ("CronJobs", "CronJobs", "Scheduled Jobs with cron syntax and concurrency policies."),
    "services": ("Services", "Services", "ClusterIP, NodePort, LoadBalancer, and stable pod endpoints."),
    "ingress": ("Ingress", "Ingress", "HTTP/S routing, TLS, and ingress controller annotations."),
    "network-policies": ("Network Policies", "Network Policies", "Pod-level firewall rules for ingress and egress traffic."),
    "configmaps": ("ConfigMaps", "ConfigMaps", "Non-sensitive configuration as env vars or mounted files."),
    "secrets": ("Secrets", "Secrets", "Sensitive data — encoding, mounting, and production secret management."),
    "persistent-volumes": ("Persistent Volumes", "Persistent Volumes", "PV, PVC, binding, access modes, and reclaim policies."),
    "storage-classes": ("Storage Classes", "Storage Classes", "Dynamic provisioning, provisioners, and volume parameters."),
    "namespaces": ("Namespaces", "Namespaces", "Logical isolation, quotas, and multi-tenant boundaries."),
    "labels-and-selectors": ("Labels & Selectors", "Labels & Selectors", "Key-value metadata for grouping, selection, and service routing."),
    "affinity-and-anti-affinity": (
        "Affinity & Anti-Affinity",
        "Affinity",
        "Pod placement rules — node affinity, pod affinity, and topology spread.",
    ),
    "taints-and-tolerations": (
        "Taints & Tolerations",
        "Taints",
        "Repel pods from nodes unless they tolerate specific taints.",
    ),
    "resource-limits": ("Resource Limits", "Resource Limits", "CPU/memory requests and limits, QoS classes, and LimitRange."),
    "hpa": ("HPA", "HPA", "Horizontal Pod Autoscaler — CPU, memory, and custom metrics scaling."),
    "rolling-updates": ("Rolling Updates", "Rolling Updates", "maxSurge, maxUnavailable, and deployment strategy."),
    "probes": ("Probes", "Probes", "Liveness, readiness, and startup probes — HTTP, TCP, exec."),
    "rbac": ("RBAC", "RBAC", "Roles, ClusterRoles, bindings, and least-privilege access."),
    "helm-basics": ("Helm Basics", "Helm", "Charts, releases, values, and upgrade/rollback workflow."),
    "common-kubectl-commands": (
        "Common kubectl Commands",
        "kubectl",
        "Everyday kubectl for apply, get, logs, exec, port-forward, and debug.",
    ),
    "troubleshooting": ("Troubleshooting", "Troubleshooting", "CrashLoopBackOff, ImagePullBackOff, pending pods, and events."),
    "production-best-practices": (
        "Production Best Practices",
        "Production",
        "Security, reliability, observability, and cluster hygiene checklist.",
    ),
    "docker-architecture": ("Docker Architecture", "Docker Arch", "Client, daemon, containerd, runc, and image registry flow."),
    "dockerfile": ("Dockerfile", "Dockerfile", "FROM, COPY, RUN, CMD, ENTRYPOINT, and layer caching."),
    "image-layers": ("Image Layers", "Layers", "Union filesystem, layer caching, and image inspection."),
    "docker-volumes": ("Docker Volumes", "Volumes", "Named volumes, bind mounts, and tmpfs for persistence."),
    "docker-networks": ("Docker Networks", "Networks", "Bridge, host, overlay, and container DNS."),
    "multi-stage-builds": ("Multi-stage Builds", "Multi-stage", "Separate build and runtime stages for smaller images."),
    "docker-compose": ("Docker Compose", "Compose", "Multi-container local stacks — services, networks, volumes."),
    "docker-commands": ("Docker Commands", "Docker CLI", "Essential docker CLI for images, containers, and registry."),
    "container-lifecycle": ("Container Lifecycle", "Lifecycle", "Create, start, stop, pause, restart, and remove."),
    "docker-best-practices": ("Docker Best Practices", "Docker Prod", "Non-root users, slim bases, .dockerignore, and scanning."),
}


PAGE_BODIES: dict[str, str] = {}


def _register_bodies() -> None:
  global PAGE_BODIES
  PAGE_BODIES = {
    "kubernetes-architecture": _body_kubernetes_architecture(),
    "pods": _body_pods(),
    "replicasets": _body_replicasets(),
    "deployments": _body_deployments(),
    "statefulsets": _body_statefulsets(),
    "daemonsets": _body_daemonsets(),
    "jobs": _body_jobs(),
    "cronjobs": _body_cronjobs(),
    "services": _body_services(),
    "ingress": _body_ingress(),
    "network-policies": _body_network_policies(),
    "configmaps": _body_configmaps(),
    "secrets": _body_secrets(),
    "persistent-volumes": _body_persistent_volumes(),
    "storage-classes": _body_storage_classes(),
    "namespaces": _body_namespaces(),
    "labels-and-selectors": _body_labels_and_selectors(),
    "affinity-and-anti-affinity": _body_affinity(),
    "taints-and-tolerations": _body_taints(),
    "resource-limits": _body_resource_limits(),
    "hpa": _body_hpa(),
    "rolling-updates": _body_rolling_updates(),
    "probes": _body_probes(),
    "rbac": _body_rbac(),
    "helm-basics": _body_helm(),
    "common-kubectl-commands": _body_common_kubectl(),
    "troubleshooting": _body_troubleshooting(),
    "production-best-practices": _body_production(),
    "docker-architecture": _body_docker_architecture(),
    "dockerfile": _body_dockerfile(),
    "image-layers": _body_image_layers(),
    "docker-volumes": _body_docker_volumes(),
    "docker-networks": _body_docker_networks(),
    "multi-stage-builds": _body_multi_stage(),
    "docker-compose": _body_docker_compose(),
    "docker-commands": _body_docker_commands(),
    "container-lifecycle": _body_container_lifecycle(),
    "docker-best-practices": _body_docker_best_practices(),
  }


def _body_kubernetes_architecture() -> str:
    return f"""## Executive Summary

**Kubernetes** separates a **control plane** (API server, scheduler, controller manager, etcd) from **worker nodes** (kubelet, kube-proxy, container runtime). All cluster state flows through the API server.

---

## Core Concepts

```mermaid
flowchart TB
  subgraph cp ["Control plane"]
    api["API Server"]
    sched["Scheduler"]
    cm["Controller Manager"]
    etcd[("etcd")]
  end
  subgraph node ["Worker node"]
    kubelet["kubelet"]
    proxy["kube-proxy"]
    crt["container runtime"]
    pod["Pod"]
  end
  api --> sched
  api --> cm
  api --> etcd
  kubelet --> api
  kubelet --> crt
  crt --> pod
  proxy --> pod
```

| Component | Role |
| :--- | :--- |
| **API Server** | Front door — validates and persists all objects |
| **etcd** | Consistent key-value store for cluster state |
| **Scheduler** | Assigns unscheduled pods to nodes |
| **Controller Manager** | Reconciliation loops (Deployment, ReplicaSet, etc.) |
| **kubelet** | Registers node, runs pods, reports status |
| **kube-proxy** | Service load balancing via iptables/IPVS |

---

## Commands

{cmd("kubectl cluster-info", "Display control plane and CoreDNS endpoints.", "kubectl cluster-info", "kubectl cluster-info", "Kubernetes control plane is running at https://10.0.0.1:6443\\nCoreDNS is running at https://10.0.0.1:6443/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy", ["Assumes kubeconfig points to the right cluster — verify context first", "Fails if API server is unreachable or RBAC denies access"])}

{cmd("kubectl get componentstatuses / get --raw", "Check health of control plane components (deprecated in newer clusters; use /readyz).", "kubectl get --raw='/readyz?verbose'", "kubectl get --raw='/readyz?verbose'", "readyz check passed", ["`componentstatuses` removed in Kubernetes 1.22+ — use `/livez` and `/readyz` instead", "Verbose output is long — pipe to grep for failing checks"])}

{cmd("kubectl get nodes -o wide", "List worker nodes with roles, versions, and internal IPs.", "kubectl get nodes [-o wide|yaml]", "kubectl get nodes -o wide", "NAME     STATUS   ROLES           AGE   VERSION   INTERNAL-IP\\nnode-1   Ready    control-plane   30d   v1.29.0   10.0.0.2", ["`NotReady` often means kubelet or CNI issue — check `kubectl describe node`", "Control-plane nodes may be tainted — workloads won't schedule there by default"])}

{cmd("kubectl api-resources", "Discover available API groups, resources, and short names.", "kubectl api-resources [--namespaced=true|false]", "kubectl api-resources | grep deploy", "deployments    apps/v1    true    Deployment", ["Output is huge — filter with grep", "CRDs appear after operator install — resource may be missing on fresh clusters"])}

---

## Related Topics

- [Pods](/kubernetes-handbook/pods/) — smallest deployable unit
- [Namespaces](/kubernetes-handbook/namespaces/) — logical isolation
- [RBAC](/kubernetes-handbook/rbac/) — API access control
- [Kubernetes Cheatsheet Index](/kubernetes-handbook/)"""


def _body_pods() -> str:
    return f"""## Executive Summary

A **Pod** wraps one or more containers sharing network namespace, IPC, and volumes. Kubernetes schedules and health-checks pods; controllers (Deployment, StatefulSet) own pod templates.

---

## Commands

{cmd("kubectl get pods", "List pods in a namespace with readiness and restart count.", "kubectl get pods [-n NAMESPACE] [-o wide]", "kubectl get pods -n myapp -o wide", "NAME           READY   STATUS    RESTARTS   AGE   IP           NODE\\napi-7f8b9c-xyz  1/1     Running   0          10m   10.244.1.5   node-2", ["Omitting `-n` shows only `default` namespace pods", "`0/1 Ready` means readiness probe failing — not necessarily crashed"])}

{cmd("kubectl describe pod", "Show events, conditions, container states, and probe failures.", "kubectl describe pod POD_NAME -n NAMESPACE", "kubectl describe pod api-7f8b9c-xyz -n myapp", "Events:\\n  Normal  Scheduled  ...\\n  Warning Failed     ...", ["Events scroll off quickly — combine with `kubectl get events`", "Last State from previous container helps debug CrashLoopBackOff"])}

{cmd("kubectl logs", "Stream stdout/stderr from a container.", "kubectl logs POD [-c CONTAINER] [-f] [--tail=N] -n NS", "kubectl logs -f api-7f8b9c-xyz -n myapp --tail=100", "2026-06-30T10:00:01 INFO  Started application...", ["Multi-container pods require `-c` to pick the right container", "`--previous` needed to see logs from crashed container"])}

{cmd("kubectl run (debug pod)", "Spin up a temporary pod for curl/dns/network debugging.", "kubectl run NAME --rm -it --image=IMAGE -- COMMAND", "kubectl run curl --rm -it --image=curlimages/curl -n myapp -- curl -s http://myapp-svc", "HTTP/1.1 200 OK", ["Forgotten `--rm` leaves debug pods behind", "Image must exist in cluster or be pullable — set pull policy if needed"])}

---

## YAML Snippet

{yaml_block("Pod manifest", "Define a single pod (prefer Deployment for production).", "apiVersion: v1\\nkind: Pod\\nmetadata:\\n  name: api\\n  labels:\\n    app: api\\nspec:\\n  containers:\\n    - name: api\\n      image: myapp:1.0.0\\n      ports:\\n        - containerPort: 8080", "apiVersion: v1\\nkind: Pod\\nmetadata:\\n  name: debug\\n  namespace: myapp\\nspec:\\n  restartPolicy: Never\\n  containers:\\n    - name: curl\\n      image: curlimages/curl:8.5.0\\n      command: [\"sleep\", \"3600\"]", ["Bare pods are not self-healing — use a controller", "Set `restartPolicy` explicitly for Jobs vs long-running workloads"])}

---

## Related Topics

- [Deployments](/kubernetes-handbook/deployments/) · [Probes](/kubernetes-handbook/probes/) · [Resource Limits](/kubernetes-handbook/resource-limits/)"""


def _body_replicasets() -> str:
    return f"""## Executive Summary

**ReplicaSet** maintains a stable set of pod replicas matching a label selector. Deployments manage ReplicaSets — you rarely create ReplicaSets directly.

---

## Commands

{cmd("kubectl get rs", "List ReplicaSets and desired/current/ready replica counts.", "kubectl get rs -n NAMESPACE", "kubectl get rs -n myapp", "NAME             DESIRED   CURRENT   READY   AGE\\nmyapp-6d4f8b9c7d   3         3         3       2d", ["Old ReplicaSets with DESIRED=0 are normal after rolling update", "READY < DESIRED indicates failing readiness probes"])}

{cmd("kubectl describe rs", "Inspect selector, pod template, and events for a ReplicaSet.", "kubectl describe rs RS_NAME -n NAMESPACE", "kubectl describe rs myapp-6d4f8b9c7d -n myapp", "Replicas: 3 current / 3 desired\\nPods Status: 3 Running / 0 Waiting / 0 Succeeded / 0 Failed", ["ReplicaSet name hash changes on pod template change", "Events may reference Deployment as owner — follow ownerReferences"])}

{cmd("kubectl scale (via deployment)", "Change replica count — Deployment updates underlying ReplicaSet.", "kubectl scale deployment NAME --replicas=N -n NS", "kubectl scale deployment myapp --replicas=5 -n myapp", "deployment.apps/myapp scaled", ["Scaling ReplicaSet directly is overwritten by Deployment controller", "HPA may scale back if CPU/memory targets differ"])}

---

## Related Topics

- [Deployments](/kubernetes-handbook/deployments/) · [Labels & Selectors](/kubernetes-handbook/labels-and-selectors/)"""


def _body_deployments() -> str:
    return f"""## Executive Summary

**Deployment** declares desired state for stateless apps: replica count, pod template, and rolling update strategy. It owns ReplicaSets and supports rollback.

---

## Commands

{cmd("kubectl apply -f deployment.yaml", "Create or update a Deployment declaratively.", "kubectl apply -f FILE [-n NAMESPACE]", "kubectl apply -f deployment.yaml -n myapp", "deployment.apps/myapp configured", ["`kubectl apply` merges — accidental field removal may not delete nested keys", "Use `--server-side` for large objects or field manager conflicts"])}

{cmd("kubectl rollout status", "Wait until rollout completes successfully.", "kubectl rollout status deployment/NAME -n NS", "kubectl rollout status deployment/myapp -n myapp", "deployment \"myapp\" successfully rolled out", ["Hangs if new pods never become Ready — check probes and image", "CI pipelines should set a timeout"])}

{cmd("kubectl rollout history", "List revision history for rollback.", "kubectl rollout history deployment/NAME -n NS [--revision=N]", "kubectl rollout history deployment/myapp -n myapp", "REVISION  CHANGE-CAUSE\\n1         <none>\\n2         kubectl set image ...", ["Without `--record` or change-cause annotation, history is sparse", "`--revision` shows manifest diff for that revision"])}

{cmd("kubectl rollout undo", "Rollback to previous or specific revision.", "kubectl rollout undo deployment/NAME [--to-revision=N] -n NS", "kubectl rollout undo deployment/myapp -n myapp", "deployment.apps/myapp rolled back", ["Undo only changes pod template — not Service or Ingress", "Test rollback in staging — image tags may have been garbage-collected"])}

{cmd("kubectl set image", "Trigger rolling update by changing container image.", "kubectl set image deployment/NAME CONTAINER=IMAGE -n NS", "kubectl set image deployment/myapp api=myapp:2.0.0 -n myapp", "deployment.apps/myapp image updated", ["Wrong container name silently fails or updates wrong container", "Always pin image digest or semver tag in production"])}

---

## Related Topics

- [Rolling Updates](/kubernetes-handbook/rolling-updates/) · [HPA](/kubernetes-handbook/hpa/) · [Probes](/kubernetes-handbook/probes/)"""


def _body_statefulsets() -> str:
    return f"""## Executive Summary

**StatefulSet** gives pods stable network identity (`pod-0`, `pod-1`), ordered rollout/scale, and per-pod PersistentVolumeClaims via `volumeClaimTemplates`.

---

## Commands

{cmd("kubectl get statefulset", "List StatefulSets and ready replicas.", "kubectl get sts [-n NAMESPACE]", "kubectl get sts -n data", "NAME   READY   AGE\\npg     3/3     7d", ["Abbreviation `sts` is common", "READY stuck below desired — check PVC binding and pod events"])}

{cmd("kubectl scale statefulset", "Scale replicas — pods created/deleted in ordinal order.", "kubectl scale sts NAME --replicas=N -n NS", "kubectl scale sts pg --replicas=3 -n data", "statefulset.apps/pg scaled", ["Scaling down deletes highest ordinal first — data loss risk without backups", "Scale-up is serial by default — can be slow for large counts"])}

{cmd("kubectl delete pod (force reschedule)", "Delete a StatefulSet pod — controller recreates with same identity.", "kubectl delete pod POD_NAME -n NS", "kubectl delete pod pg-1 -n data", "pod \"pg-1\" deleted", ["Do not delete PVCs unless you intend to wipe data", "Pod name is predictable — use for debugging specific shard"])}

---

## Related Topics

- [Persistent Volumes](/kubernetes-handbook/persistent-volumes/) · [Services](/kubernetes-handbook/services/) (headless)"""


def _body_daemonsets() -> str:
    return f"""## Executive Summary

**DaemonSet** ensures one pod copy runs on every (or selected) node — typical for node agents, log shippers, and CNI plugins.

---

## Commands

{cmd("kubectl get daemonset", "Show desired, current, ready, and available pod counts per DaemonSet.", "kubectl get ds [-n NAMESPACE]", "kubectl get ds -n kube-system", "NAME         DESIRED   CURRENT   READY   UP-TO-DATE   AVAILABLE\\nfluent-bit   5         5         5       5            5", ["DESIRED equals eligible node count — taints reduce eligible nodes", "Not Ready on upgraded nodes often means rolling update in progress"])}

{cmd("kubectl rollout status daemonset", "Wait for DaemonSet rollout to complete on all nodes.", "kubectl rollout status ds/NAME -n NS", "kubectl rollout status ds/fluent-bit -n logging", "daemon set \"fluent-bit\" successfully rolled out", ["Node cordon/drain reduces AVAILABLE temporarily", "MaxUnavailable in updateStrategy affects rollout speed"])}

---

## Related Topics

- [Taints & Tolerations](/kubernetes-handbook/taints-and-tolerations/) · [Node affinity](/kubernetes-handbook/affinity-and-anti-affinity/)"""


def _body_jobs() -> str:
    return f"""## Executive Summary

**Job** runs one or more pods until a fixed number complete successfully. Supports parallelism, completions, backoff, and TTL after finish.

---

## Commands

{cmd("kubectl create job", "Create a Job from an image or manifest.", "kubectl create job NAME --image=IMAGE [-n NS]", "kubectl create job migrate --image=myapp:migrator -n myapp", "job.batch/migrate created", ["Imperative jobs lack resource limits — prefer YAML in production", "Image command must exit 0 for success"])}

{cmd("kubectl get jobs", "List Jobs with completion and duration.", "kubectl get jobs -n NAMESPACE", "kubectl get jobs -n myapp", "NAME      COMPLETIONS   DURATION   AGE\\nmigrate   1/1           45s        2m", ["COMPLETIONS 0/1 with failures — check `kubectl logs job/NAME`", "Suspended jobs show no active pods"])}

{cmd("kubectl logs job/NAME", "Fetch logs from pods owned by a Job.", "kubectl logs job/JOB_NAME -n NS", "kubectl logs job/migrate -n myapp", "Migration completed successfully", ["Parallel jobs need `-l job-name=NAME` or pick pod by label", "Use `--previous` if container restarted within backoff"])}

---

## Related Topics

- [CronJobs](/kubernetes-handbook/cronjobs/) · [Pods](/kubernetes-handbook/pods/)"""


def _body_cronjobs() -> str:
    return f"""## Executive Summary

**CronJob** creates Jobs on a cron schedule. Control concurrency (`Allow`, `Forbid`, `Replace`) and history limits for completed/failed jobs.

---

## Commands

{cmd("kubectl create cronjob", "Schedule a recurring Job from an image.", "kubectl create cronjob NAME --image=IMAGE --schedule='CRON' -n NS", "kubectl create cronjob backup --image=backup:1.0 --schedule='0 2 * * *' -n ops", "cronjob.batch/backup created", ["Cron uses controller timezone (usually UTC) — document timezone", "Standard cron has 5 fields; some docs show 6-field seconds variant"])}

{cmd("kubectl get cronjobs", "List schedules, last schedule time, and active jobs.", "kubectl get cronjobs -n NAMESPACE", "kubectl get cronjobs -n ops", "NAME     SCHEDULE    SUSPEND   ACTIVE   LAST SCHEDULE   AGE\\nbackup   0 2 * * *   False     0        8h              30d", ["SUSPEND True means schedule paused — easy to forget after debug", "ACTIVE > 1 may indicate Forbid policy not set and overlap"])}

{cmd("kubectl delete jobs by label", "Clean up finished Job pods created by CronJob.", "kubectl delete jobs -l cronjob-name=NAME -n NS", "kubectl delete jobs -l cronjob-name=backup -n ops", "job.batch \"backup-29223480\" deleted", ["Deleting CronJob does not delete active Jobs unless cascade set", "Set `successfulJobsHistoryLimit` to auto-prune"])}

---

## Related Topics

- [Jobs](/kubernetes-handbook/jobs/) · [Production Best Practices](/kubernetes-handbook/production-best-practices/)"""


def _body_services() -> str:
    return f"""## Executive Summary

**Service** provides a stable virtual IP and DNS name routing to pods matching `selector`. Types: **ClusterIP** (default), **NodePort**, **LoadBalancer**, **ExternalName**.

---

## Commands

{cmd("kubectl expose deployment", "Create a Service targeting deployment pods.", "kubectl expose deployment NAME --port=P --target-port=TP -n NS", "kubectl expose deployment myapp --port=80 --target-port=8080 -n myapp", "service/myapp exposed", ["Port ≠ targetPort — common misconfiguration for apps listening on 8080", "Selector auto-matches deployment labels — custom labels need YAML"])}

{cmd("kubectl get svc", "List Services with CLUSTER-IP and ports.", "kubectl get svc -n NAMESPACE", "kubectl get svc -n myapp", "NAME    TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)\\nmyapp   ClusterIP   10.96.120.45   <none>        80/TCP", ["CLUSTER-IP none means headless — returns pod A records", "EXTERNAL-IP pending on cloud LB — check cloud controller logs"])}

{cmd("kubectl port-forward svc", "Forward local port to Service for local testing.", "kubectl port-forward svc/NAME LOCAL:REMOTE -n NS", "kubectl port-forward svc/myapp 8080:80 -n myapp", "Forwarding from 127.0.0.1:8080 -> 80", ["Binds localhost only by default — `0.0.0.0` needs `--address`", "Dies when terminal closes — not for production traffic"])}

{cmd("kubectl get endpoints / endpointslice", "Verify backend pods behind a Service.", "kubectl get endpoints NAME -n NS", "kubectl get endpoints myapp -n myapp", "NAME    ENDPOINTS                          AGE\\nmyapp   10.244.1.5:8080,10.244.2.3:8080   1d", ["Empty ENDPOINTS means selector mismatch or no ready pods", "Prefer EndpointSlice on modern clusters — same diagnostic value"])}

---

## Related Topics

- [Ingress](/kubernetes-handbook/ingress/) · [Network Policies](/kubernetes-handbook/network-policies/) · [Labels & Selectors](/kubernetes-handbook/labels-and-selectors/)"""


def _body_ingress() -> str:
    return f"""## Executive Summary

**Ingress** exposes HTTP/S routes to Services. Requires an **ingress controller** (nginx, traefik, AWS ALB, etc.). Handles host/path routing, TLS, and annotations.

---

## Commands

{cmd("kubectl get ingress", "List Ingress resources with hosts and address.", "kubectl get ingress -n NAMESPACE", "kubectl get ingress -n myapp", "NAME    CLASS   HOSTS             ADDRESS       PORTS\\nmyapp   nginx   api.example.com   10.0.0.50     80, 443", ["ADDRESS empty until controller provisions LB or NodePort", "Wrong ingressClassName means controller ignores the Ingress"])}

{cmd("kubectl describe ingress", "Show rules, backends, TLS secrets, and events.", "kubectl describe ingress NAME -n NS", "kubectl describe ingress myapp -n myapp", "Rules:\\n  Host: api.example.com\\n    Path: / -> myapp:80", ["Backend service port must match Service port number", "TLS secret must exist in same namespace"])}

{cmd("curl via /etc/hosts", "Test routing before DNS cutover.", "curl -H 'Host: HOST' http://INGRESS_IP/PATH", "curl -H 'Host: api.example.com' http://10.0.0.50/health", '{"status":"UP"}', ["Forgotten Host header hits default backend", "HTTPS needs `-k` with self-signed or proper SNI"])}

---

## Related Topics

- [Services](/kubernetes-handbook/services/) · [TLS Secrets](/kubernetes-handbook/secrets/) · [Kubernetes Handbook — NGINX Ingress](/kubernetes-handbook/nginx-ingress/)"""


def _body_network_policies() -> str:
    return f"""## Executive Summary

**NetworkPolicy** filters pod ingress/egress by namespace, pod labels, IP blocks, and ports. Requires a CNI that enforces policies (Calico, Cilium, etc.).

---

## Commands

{cmd("kubectl get networkpolicies", "List policies and which pods they may affect.", "kubectl get networkpolicies -n NAMESPACE", "kubectl get netpol -n myapp", "NAME           POD-SELECTOR   AGE\\napi-allow-db   app=api        5d", ["No policies often means allow-all — verify CNI default", "Policy only selects pods listed in `podSelector` — empty selects all in namespace"])}

{cmd("kubectl describe networkpolicy", "Inspect ingress/egress rules and peers.", "kubectl describe netpol NAME -n NS", "kubectl describe netpol api-allow-db -n myapp", "Policy Types: Ingress\\nAllowed Ingress: ...", ["Egress denied by default only if policy types include Egress", "Cross-namespace rules need namespaceSelector labels"])}

{cmd("kubectl run netshoot (debug)", "Test connectivity from a pod with shell and network tools.", "kubectl run netshoot --rm -it --image=nicolaka/netshoot -- bash", "kubectl run netshoot --rm -it --image=nicolaka/netshoot -n myapp -- curl -v telnet://db:5432", "Connected to db.myapp.svc.cluster.local", ["Debug pod must match policy labels to simulate real workload", "DNS egress may need explicit allow rule"])}

---

## Related Topics

- [Services](/kubernetes-handbook/services/) · [Namespaces](/kubernetes-handbook/namespaces/)"""


def _body_configmaps() -> str:
    return f"""## Executive Summary

**ConfigMap** stores non-sensitive config as key-value pairs or file snippets. Inject via env vars, envFrom, or volume mounts.

---

## Commands

{cmd("kubectl create configmap", "Create from literals or files.", "kubectl create configmap NAME --from-literal=k=v [--from-file=path] -n NS", "kubectl create configmap myapp-config --from-literal=LOG_LEVEL=info -n myapp", "configmap/myapp-config created", ["`--from-env-file` expects KEY=VALUE lines", "Large ConfigMaps hit 1Mi etcd object limit — split or use volumes"])}

{cmd("kubectl get configmap -o yaml", "Export ConfigMap for review or GitOps.", "kubectl get configmap NAME -o yaml -n NS", "kubectl get configmap myapp-config -o yaml -n myapp", "apiVersion: v1\\nkind: ConfigMap\\ndata:\\n  LOG_LEVEL: info", ["Editing live ConfigMap does not restart pods using envFrom — remount or rollout", "Binary data belongs in Secrets or external store"])}

{cmd("kubectl rollout restart", "Restart pods to pick up mounted ConfigMap changes.", "kubectl rollout restart deployment/NAME -n NS", "kubectl rollout restart deployment/myapp -n myapp", "deployment.apps/myapp restarted", ["Env var injection is immutable at pod start — restart required", "SubPath volume mounts do not auto-update — avoid subPath for hot reload"])}

---

## Related Topics

- [Secrets](/kubernetes-handbook/secrets/) · [Deployments](/kubernetes-handbook/deployments/)"""


def _body_secrets() -> str:
    return f"""## Executive Summary

**Secret** stores sensitive bytes (base64 in etcd). Types: **Opaque**, **kubernetes.io/tls**, **dockerconfigjson**. Prefer external secret operators in production.

---

## Commands

{cmd("kubectl create secret generic", "Create Opaque secret from literals or files.", "kubectl create secret generic NAME --from-literal=k=v -n NS", "kubectl create secret generic db-creds --from-literal=password='s3cret' -n myapp", "secret/db-creds created", ["Literal passwords appear in shell history — use `--from-env-file` or stdin", "Base64 is encoding not encryption — restrict RBAC"])}

{cmd("kubectl get secret", "List secrets (values hidden by default).", "kubectl get secrets -n NAMESPACE", "kubectl get secrets -n myapp", "NAME       TYPE     DATA   AGE\\ndb-creds   Opaque   1      1h", ["`kubectl get secret -o yaml` exposes decoded data — never paste in tickets", "Service account tokens auto-created as secrets in older clusters"])}

{cmd("kubectl create secret docker-registry", "Pull private images via imagePullSecrets.", "kubectl create secret docker-registry NAME --docker-server=REG --docker-username=U --docker-password=P -n NS", "kubectl create secret docker-registry regcred --docker-server=registry.example.com --docker-username=ci --docker-password=token -n myapp", "secret/regcred created", ["Must reference secret in pod spec `imagePullSecrets`", "Expired registry tokens cause ImagePullBackOff"])}

---

## Related Topics

- [ConfigMaps](/kubernetes-handbook/configmaps/) · [RBAC](/kubernetes-handbook/rbac/) · [Production Best Practices](/kubernetes-handbook/production-best-practices/)"""


def _body_persistent_volumes() -> str:
    return f"""## Executive Summary

**PersistentVolume (PV)** is cluster storage. **PersistentVolumeClaim (PVC)** requests capacity and access mode. Binding is one-to-one for static PVs; StorageClass enables dynamic provisioning.

---

## Commands

{cmd("kubectl get pv,pvc", "List volumes and claims with status and capacity.", "kubectl get pv,pvc [-n NAMESPACE]", "kubectl get pvc -n myapp", "NAME        STATUS   VOLUME     CAPACITY   ACCESS MODES\\ndata-pvc    Bound    pv-abc     10Gi       RWO", ["Pending PVC — no matching PV or StorageClass provisioner failed", "Released PV needs reclaim policy handled before reuse"])}

{cmd("kubectl describe pvc", "See events for provisioning failures and selected StorageClass.", "kubectl describe pvc NAME -n NS", "kubectl describe pvc data-pvc -n myapp", "Events: Provisioning succeeded...", ["Wrong access mode (RWO vs RWM) blocks binding", "Zone mismatch in multi-AZ clusters — check topology"])}

{cmd("kubectl delete pvc", "Release claim — PV behavior depends on reclaim policy.", "kubectl delete pvc NAME -n NS", "kubectl delete pvc data-pvc -n myapp", "persistentvolumeclaim \"data-pvc\" deleted", ["Retain policy leaves PV in Released — manual cleanup needed", "Deleting PVC wipes data on Delete reclaim policy"])}

---

## Related Topics

- [Storage Classes](/kubernetes-handbook/storage-classes/) · [StatefulSets](/kubernetes-handbook/statefulsets/)"""


def _body_storage_classes() -> str:
    return f"""## Executive Summary

**StorageClass** defines provisioner, parameters, reclaim policy, and volume binding mode (`Immediate` vs `WaitForFirstConsumer`).

---

## Commands

{cmd("kubectl get storageclass", "List available classes and default annotation.", "kubectl get sc", "kubectl get sc", "NAME                 PROVISIONER             RECLAIMPOLICY\\nstandard (default)   kubernetes.io/gce-pd   Delete", ["No default SC causes PVC to stay Pending without explicit className", "Cloud provisioner name differs per platform"])}

{cmd("kubectl describe storageclass", "Inspect provisioner parameters and binding mode.", "kubectl describe sc NAME", "kubectl describe sc fast-ssd", "Parameters: type=pd-ssd\\nVolumeBindingMode: WaitForFirstConsumer", ["WaitForFirstConsumer delays binding until pod scheduled — normal", "Wrong parameter keys silently fail on some provisioners"])}

---

## Related Topics

- [Persistent Volumes](/kubernetes-handbook/persistent-volumes/) · [Affinity](/kubernetes-handbook/affinity-and-anti-affinity/) (zones)"""


def _body_namespaces() -> str:
    return f"""## Executive Summary

**Namespace** scopes names for objects and pairs with RBAC, quotas, and network policies for multi-tenant isolation.

---

## Commands

{cmd("kubectl create namespace", "Create a new namespace.", "kubectl create namespace NAME", "kubectl create namespace myapp", "namespace/myapp created", ["Namespace names cannot be changed — plan env prefix (`myapp-prod`)", "Deleting namespace deletes all objects inside — irreversible"])}

{cmd("kubectl config set-context --namespace", "Set default namespace for current context.", "kubectl config set-context --current --namespace=NS", "kubectl config set-context --current --namespace=myapp", "Context \"prod\" modified.", ["Easy to forget and run commands in wrong namespace", "CI should pass `-n` explicitly instead of relying on context"])}

{cmd("kubectl get all -n", "List common namespaced resources in one namespace.", "kubectl get all -n NAMESPACE", "kubectl get all -n myapp", "pod/... service/... deployment/...", ["`kubectl get all` omits Ingress, PVC, HPA — not literally everything", "Cluster-scoped resources (PV, SC) not shown"])}

{cmd("kubectl get resourcequota", "Check namespace quota usage.", "kubectl get resourcequota -n NS", "kubectl get resourcequota -n myapp", "NAME    AGE   REQUESTS.CPU   LIMITS.MEMORY\\nquota   30d   2/4            8Gi/16Gi", ["Quota enforced at admission — pods rejected without clear pod events sometimes", "LimitRange defaults apply per-container"])}

---

## Related Topics

- [RBAC](/kubernetes-handbook/rbac/) · [Resource Limits](/kubernetes-handbook/resource-limits/)"""


def _body_labels_and_selectors() -> str:
    return f"""## Executive Summary

**Labels** are arbitrary key/value metadata on objects. **Selectors** filter resources — equality (`app=api`) or set-based (`env in (prod,staging)`).

---

## Commands

{cmd("kubectl get pods -l", "Filter pods by label selector.", "kubectl get pods -l KEY=VALUE [-n NS]", "kubectl get pods -l app=api,tier=frontend -n myapp", "NAME           READY   STATUS\\napi-7f8b9c-xyz  1/1     Running", ["Comma is AND — use `-l 'env in (prod)'` for OR/set syntax", "Typos in labels return empty list — verify with `--show-labels`"])}

{cmd("kubectl label", "Add or update labels on resources.", "kubectl label RESOURCE NAME KEY=VALUE [--overwrite] -n NS", "kubectl label pod api-7f8b9c-xyz version=2.0.0 -n myapp", "pod/api-7f8b9c-xyz labeled", ["Changing labels breaks Service/Deployment selectors if inconsistent", "Immutable label keys on some controllers — check webhook errors"])}

{cmd("kubectl get pods --show-labels", "Display all labels for troubleshooting selector mismatches.", "kubectl get pods --show-labels -n NS", "kubectl get pods --show-labels -n myapp", "NAME    ...   LABELS\\napi-...       app=api,tier=frontend", ["Label values appear in metrics cardinality — avoid high-cardinality values", "Recommended labels: app.kubernetes.io/name, instance, version"])}

---

## Related Topics

- [Services](/kubernetes-handbook/services/) · [Deployments](/kubernetes-handbook/deployments/)"""


def _body_affinity() -> str:
    return f"""## Executive Summary

**Affinity** attracts pods to nodes or other pods; **anti-affinity** spreads replicas across hosts/zones. **topologySpreadConstraints** distribute pods evenly.

---

## Commands

{cmd("kubectl get pods -o wide (spread check)", "Verify pods distributed across nodes after anti-affinity rules.", "kubectl get pods -o wide -l app=NAME -n NS", "kubectl get pods -o wide -l app=api -n myapp", "NAME    NODE\\napi-0   node-1\\napi-1   node-2\\napi-2   node-3", ["All pods on one node — required anti-affinity missing or soft preference ignored", "Insufficient nodes makes hard anti-affinity leave pods Pending"])}

{cmd("kubectl describe pod (scheduling)", "See events when affinity/anti-affinity blocks scheduling.", "kubectl describe pod PENDING_POD -n NS", "kubectl describe pod api-xyz -n myapp", "0/5 nodes available: 3 node(s) didn't match pod anti-affinity rules", ["Soft affinity (`preferredDuringScheduling`) never blocks — check if you needed hard", "Topology key must exist on nodes (`topology.kubernetes.io/zone`)"])}

---

## YAML Snippet

{yaml_block("podAntiAffinity", "Spread replicas across hosts.", "podAntiAffinity:\\n  requiredDuringSchedulingIgnoredDuringExecution:\\n    - labelSelector:\\n        matchLabels:\\n          app: api\\n      topologyKey: kubernetes.io/hostname", "podAntiAffinity:\\n  preferredDuringSchedulingIgnoredDuringExecution:\\n    - weight: 100\\n      podAffinityTerm:\\n        labelSelector:\\n          matchLabels:\\n            app: api\\n        topologyKey: topology.kubernetes.io/zone", ["`IgnoredDuringExecution` means rules not re-evaluated after schedule", "Mixing required rules too aggressively causes capacity fragmentation"])}

---

## Related Topics

- [Taints & Tolerations](/kubernetes-handbook/taints-and-tolerations/) · [DaemonSets](/kubernetes-handbook/daemonsets/)"""


def _body_taints() -> str:
    return f"""## Executive Summary

**Taints** repel pods from nodes unless pods have matching **tolerations**. Used for dedicated nodes, GPU pools, and control-plane isolation.

---

## Commands

{cmd("kubectl taint nodes", "Add or remove taints on a node.", "kubectl taint nodes NODE KEY=VALUE:Effect", "kubectl taint nodes node-2 dedicated=gpu:NoSchedule", "node/node-2 tainted", ["Effect NoExecute evicts existing pods without toleration", "Removing taint requires `-` suffix: `dedicated=gpu:NoSchedule-`"])}

{cmd("kubectl describe node", "View taints and allocated resources on a node.", "kubectl describe node NODE", "kubectl describe node node-2", "Taints: dedicated=gpu:NoSchedule", ["Cordon (`SchedulingDisabled`) is not a taint — different mechanism", "NotReady nodes retain taints — drain before maintenance"])}

{cmd("kubectl drain", "Evict pods and mark node unschedulable for maintenance.", "kubectl drain NODE --ignore-daemonsets --delete-emptydir-data", "kubectl drain node-2 --ignore-daemonsets --delete-emptydir-data", "node/node-2 cordoned\\n... evicted", ["Without `--ignore-daemonsets` drain hangs on DaemonSet pods", "Pods with local storage need `--delete-emptydir-data` or manual handling"])}

---

## Related Topics

- [Affinity](/kubernetes-handbook/affinity-and-anti-affinity/) · [Production Best Practices](/kubernetes-handbook/production-best-practices/)"""


def _body_resource_limits() -> str:
    return f"""## Executive Summary

**requests** reserve schedulable capacity; **limits** cap usage. QoS classes: **Guaranteed**, **Burstable**, **BestEffort**. Set JVM/Go runtime flags to respect container limits.

---

## Commands

{cmd("kubectl top pods", "Show live CPU/memory usage (requires metrics-server).", "kubectl top pods -n NAMESPACE", "kubectl top pods -n myapp", "NAME    CPU(cores)   MEMORY(bytes)\\napi-0   120m         512Mi", ["Metrics absent if metrics-server not installed", "Usage near limit triggers CPU throttle or OOMKill"])}

{cmd("kubectl describe pod (QoS)", "Inspect QoS class and resource fields.", "kubectl describe pod NAME -n NS", "kubectl describe pod api-0 -n myapp", "QoS Class: Burstable\\nLimits: cpu 500m, memory 512Mi", ["Limits without requests get request=limit for CPU/memory", "BestEffort pods evicted first under node pressure"])}

{cmd("kubectl get limitrange", "View default/min/max container resources per namespace.", "kubectl get limitrange -n NS", "kubectl get limitrange -n myapp", "NAME    CREATED AT\\nlimits  2026-01-01", ["Pods without resources inherit LimitRange defaults at admission", "ResourceQuota caps namespace totals — different from LimitRange"])}

---

## Related Topics

- [HPA](/kubernetes-handbook/hpa/) · [Production Best Practices](/kubernetes-handbook/production-best-practices/)"""


def _body_hpa() -> str:
    return f"""## Executive Summary

**HorizontalPodAutoscaler** scales Deployment/StatefulSet replicas based on metrics (CPU, memory, custom, external). Requires metrics-server or custom metrics adapter.

---

## Commands

{cmd("kubectl autoscale", "Create HPA for a deployment quickly.", "kubectl autoscale deployment NAME --min=N --max=M --cpu-percent=P -n NS", "kubectl autoscale deployment myapp --min=2 --max=10 --cpu-percent=70 -n myapp", "horizontalpodautoscaler.autoscaling/myapp autoscaled", ["v2 HPA prefers YAML for memory/custom metrics", "Target % is of requests — missing requests makes HPA ineffective"])}

{cmd("kubectl get hpa", "Watch current/desired replicas and metric targets.", "kubectl get hpa -n NAMESPACE", "kubectl get hpa -n myapp", "NAME    REFERENCE          TARGETS   MINPODS   MAXPODS   REPLICAS\\nmyapp   Deployment/myapp   45%/70%   2         10        4", ["`<unknown>/70%` means metrics not available", "Rapid flapping — tune behavior stabilization windows in YAML"])}

{cmd("kubectl describe hpa", "Debug scaling events and metric resolution failures.", "kubectl describe hpa NAME -n NS", "kubectl describe hpa myapp -n myapp", "Conditions: AbleToScale True ...", ["Custom metrics need prometheus-adapter or equivalent", "Scale-down delay defaults may feel slow during traffic drops"])}

---

## Related Topics

- [Resource Limits](/kubernetes-handbook/resource-limits/) · [Deployments](/kubernetes-handbook/deployments/)"""


def _body_rolling_updates() -> str:
    return f"""## Executive Summary

Deployment **strategy** controls rollout: `RollingUpdate` with `maxSurge` and `maxUnavailable`, or `Recreate` for single-replica stateful behavior.

---

## Commands

{cmd("kubectl set image (trigger rollout)", "Change image to start a rolling update.", "kubectl set image deployment/NAME CONTAINER=IMAGE -n NS", "kubectl set image deployment/myapp api=myapp:2.1.0 -n myapp", "deployment.apps/myapp image updated", ["maxUnavailable 0 with maxSurge 1 is safest but slower", "Readiness probe must pass before old pods terminate"])}

{cmd("kubectl rollout pause / resume", "Pause rollout to batch changes or verify canary.", "kubectl rollout pause deployment/NAME -n NS", "kubectl rollout pause deployment/myapp -n myapp", "deployment.apps/myapp paused", ["Forgotten pause leaves rollout stuck — document runbooks", "Resume continues from current revision"])}

{cmd("kubectl rollout status", "Block until rollout completes or fails.", "kubectl rollout status deployment/NAME -n NS --timeout=5m", "kubectl rollout status deployment/myapp -n myapp --timeout=5m", "Waiting for deployment \"myapp\" rollout to finish: 2 of 3 updated replicas are available...", ["Timeout in CI should fail pipeline", "Progress deadline exceeded — check `kubectl describe deploy`"])}

---

## Related Topics

- [Deployments](/kubernetes-handbook/deployments/) · [Probes](/kubernetes-handbook/probes/)"""


def _body_probes() -> str:
    return f"""## Executive Summary

**livenessProbe** restarts unhealthy containers. **readinessProbe** removes pod from Service endpoints. **startupProbe** protects slow-starting apps from premature liveness kills.

| Probe | Kubelet action on failure | Use when |
| :--- | :--- | :--- |
| **Startup** | Blocks other probes until success | JVM/Spring slow boot (>30s) |
| **Liveness** | Restart container | Deadlock, unrecoverable hang |
| **Readiness** | Remove from Service endpoints | Temporarily cannot serve traffic |

**Rule:** Liveness = "should restart?" Readiness = "should receive traffic?" Never point both at the same shallow `/health` if it does not distinguish the two.

---

## Core Concepts

```mermaid
flowchart LR
    subgraph probes [Probe lifecycle]
        S[startupProbe] -->|pass| R[readinessProbe]
        R -->|pass| T[Receives traffic]
        L[livenessProbe] -->|fail| X[Container restart]
        R -->|fail| N[Removed from endpoints]
    end
```

| Setting | Typical value | Notes |
| :--- | :--- | :--- |
| `periodSeconds` | 5–10 | How often to probe |
| `timeoutSeconds` | 1–3 | Must be < app SLA |
| `failureThreshold` | 3 | Failures before action |
| `startupProbe.failureThreshold` | 30+ | Allows 5 min boot at period=10 |

---

## Commands

{cmd("kubectl describe pod (probe failures)", "See probe failure messages and restart counts.", "kubectl describe pod NAME -n NS", "kubectl describe pod api-0 -n myapp", "Warning  Unhealthy  Liveness probe failed: HTTP probe failed with statuscode: 503", ["Liveness too aggressive kills app during GC spikes", "Readiness failure during rollout removes capacity — expected briefly"])}

{cmd("kubectl logs (after restart)", "Correlate probe kills with application errors.", "kubectl logs POD -n NS --previous", "kubectl logs api-0 -n myapp --previous", "OOMKilled or stack trace...", ["`--previous` empty if pod never started successfully", "Exec probe shell must exist in image — alpine lacks bash"])}

---

## YAML Snippet

{yaml_block("HTTP readiness + liveness", "Standard Spring Boot / HTTP service probes.", """readinessProbe:
  httpGet:
    path: /actuator/health/readiness
    port: 8080
  initialDelaySeconds: 10
  periodSeconds: 5
livenessProbe:
  httpGet:
    path: /actuator/health/liveness
    port: 8080
  initialDelaySeconds: 30""", """startupProbe:
  httpGet:
    path: /actuator/health
    port: 8080
  failureThreshold: 30
  periodSeconds: 10""", ["Same path for liveness and readiness causes traffic to unhealthy instances", "initialDelaySeconds deprecated pattern — prefer startupProbe"])}

---

## Related Topics

- [Deployments](/kubernetes-handbook/deployments/) · [Troubleshooting](/kubernetes-handbook/troubleshooting/)"""


def _body_rbac() -> str:
    return f"""## Executive Summary

**RBAC** grants permissions via **Role/ClusterRole** + **RoleBinding/ClusterRoleBinding**. Principle of least privilege — separate CI, dev, and admin roles.

---

## Commands

{cmd("kubectl auth can-i", "Check whether current user/service account can perform action.", "kubectl auth can-i VERB RESOURCE [--as=USER] -n NS", "kubectl auth can-i create deployments -n myapp", "yes", ["Use `--as=system:serviceaccount:ns:sa` for SA checks", "Cluster-scoped verbs need omitting `-n` or ClusterRole"])}

{cmd("kubectl create rolebinding", "Bind a Role to user/group/service account.", "kubectl create rolebinding NAME --role=ROLE --user=USER -n NS", "kubectl create rolebinding deployer --role=deployer --user=ci-bot -n myapp", "rolebinding.rbac.authorization.k8s.io/deployer created", ["RoleBinding only grants namespace scope — use ClusterRoleBinding for CRDs cluster-wide", "Default SA in namespace often over-permissioned in dev clusters"])}

{cmd("kubectl get role,rolebinding", "Audit RBAC objects in namespace.", "kubectl get role,rolebinding -n NS", "kubectl get role,rolebinding -n myapp", "NAME        CREATED AT\\ndeployer    2026-01-01", ["Bindings reference role by name — deleting role breaks binding silently", "Use `kubectl who-can` plugins for bulk audits"])}

---

## Related Topics

- [Namespaces](/kubernetes-handbook/namespaces/) · [Production Best Practices](/kubernetes-handbook/production-best-practices/)"""


def _body_helm() -> str:
    return f"""## Executive Summary

**Helm** packages Kubernetes manifests as **charts**. **Releases** are installed chart instances with versioned **values** overrides.

---

## Commands

{cmd("helm install", "Deploy a chart release into a namespace.", "helm install RELEASE CHART [-n NS] [--create-namespace] [-f values.yaml]", "helm install myapp oci://registry.example.com/charts/myapp -n myapp --create-namespace -f prod.yaml", "NAME: myapp\\nSTATUS: deployed\\nREVISION: 1", ["Release name must be unique per namespace", "Wrong values file key silently ignored — validate with `helm template`"])}

{cmd("helm upgrade --install", "Idempotent install or upgrade (CI-friendly).", "helm upgrade --install RELEASE CHART -n NS -f values.yaml", "helm upgrade --install myapp ./chart -n myapp -f prod.yaml", "Release \"myapp\" has been upgraded. Happy Helming!", ["Without `--atomic`, failed upgrade may leave partial resources", "Use `--dry-run` in pipeline before apply"])}

{cmd("helm rollback", "Revert release to previous revision.", "helm rollback RELEASE REVISION -n NS", "helm rollback myapp 3 -n myapp", "Rollback was a success! Happy Helming!", ["Revision 1 may reference deleted chart version — keep chart artifacts", "Rollback does not rollback CRDs always — test CRD upgrades"])}

{cmd("helm list / history", "List releases and revision history.", "helm history RELEASE -n NS", "helm history myapp -n myapp", "REVISION  STATUS      CHART\\n3         deployed    myapp-1.2.0", ["`-a` shows failed/uninstalled releases", "Secrets backend stores release data — protect etcd backups"])}

---

## Related Topics

- [Deployments](/kubernetes-handbook/deployments/) · [Production Best Practices](/kubernetes-handbook/production-best-practices/)"""


def _body_common_kubectl() -> str:
    return f"""## Executive Summary

Day-to-day **kubectl** for apply, diff, watch, contexts, and output formatting. Prefer declarative manifests over imperative creates in production.

---

## Commands

{cmd("kubectl apply -f", "Declarative create/update from file or directory.", "kubectl apply -f PATH [-n NS]", "kubectl apply -f k8s/ -n myapp", "deployment.apps/myapp configured\\nservice/myapp unchanged", ["Recursive `-f k8s/` applies all yaml — order does not matter", "Use `kubectl diff -f` before apply in production"])}

{cmd("kubectl get -w", "Watch resource changes in real time.", "kubectl get RESOURCE -w -n NS", "kubectl get pods -w -n myapp", "NAME    READY   STATUS\\napi-0   1/1     Running\\napi-1   0/1     ContainerCreating", ["Watch streams until interrupted — use timeout in scripts", "High churn namespaces produce noisy output"])}

{cmd("kubectl config use-context", "Switch kubeconfig cluster/user/namespace context.", "kubectl config use-context CONTEXT", "kubectl config use-context prod-eks", "Switched to context \"prod-eks\".", ["Easy to apply to prod while thinking staging — prompt context in PS1", "Multiple kubeconfig files merge — know precedence rules"])}

{cmd("kubectl explain", "OpenAPI docs for resource fields in terminal.", "kubectl explain RESOURCE.FIELD", "kubectl explain deployment.spec.strategy", "KIND: Deployment\\nFIELD: strategy ...", ["Requires cluster connectivity for live schema", "Offline use `kubectl explain --api-version=apps/v1 deployment`"])}

{cmd("kubectl get events", "Sort cluster events for debugging recent failures.", "kubectl get events -n NS --sort-by='.lastTimestamp'", "kubectl get events -n myapp --sort-by='.lastTimestamp'", "LAST SEEN   TYPE     REASON    OBJECT        MESSAGE", ["Events expire after ~1h — use cluster logging for history", "Normal events filtered out — grep Warning"])}

---

## Related Topics

- [Troubleshooting](/kubernetes-handbook/troubleshooting/) · [Kubernetes Architecture](/kubernetes-handbook/kubernetes-architecture/)"""


def _body_troubleshooting() -> str:
    return f"""## Executive Summary

Systematic debug flow: **events → describe → logs → exec → endpoints → network**. Common failure modes: **CrashLoopBackOff**, **ImagePullBackOff**, **Pending**, **OOMKilled**.

---

## Commands

{cmd("Diagnose CrashLoopBackOff", "Get restart reason and previous logs.", "kubectl describe pod POD -n NS && kubectl logs POD -n NS --previous", "kubectl logs api-0 -n myapp --previous", "Error: main class not found / exit code 1", ["Current logs may be empty if container dies instantly", "Check liveness probe killing healthy-but-slow app"])}

{cmd("Diagnose ImagePullBackOff", "Verify image name, tag, pull secrets, and registry auth.", "kubectl describe pod POD -n NS", "kubectl describe pod api-0 -n myapp", "Failed to pull image \"myapp:latest\": not found", ["`:latest` tag not pulled if already cached with old digest", "Private registry needs imagePullSecrets on pod spec"])}

{cmd("Diagnose Pending pod", "Find scheduling failures — resources, affinity, taints, PVC.", "kubectl describe pod POD -n NS", "kubectl describe pod api-0 -n myapp", "0/3 nodes available: insufficient cpu", ["Pending without events — check scheduler logs", "PVC unbound blocks WaitForFirstConsumer pods"])}

{cmd("kubectl debug (ephemeral container)", "Attach debug container to running pod (K8s 1.23+).", "kubectl debug -it POD -n NS --image=busybox --target=CONTAINER", "kubectl debug -it api-0 -n myapp --image=busybox --target=api", "Targeting container \"api\". If you don't see a command prompt, try pressing enter.", ["Ephemeral containers need feature gate/enabled on older distros", "Cannot copy files into main container filesystem easily"])}

---

## Related Topics

- [Probes](/kubernetes-handbook/probes/) · [Resource Limits](/kubernetes-handbook/resource-limits/) · [Events & kubectl](/kubernetes-handbook/common-kubectl-commands/)"""


def _body_production() -> str:
    return f"""## Executive Summary

Production checklist: **RBAC least privilege**, **resource requests/limits**, **PDBs**, **network policies**, **no `:latest`**, **GitOps**, **backup etcd/PV**, **ingress TLS**, **monitoring & alerts**.

---

## Commands

{cmd("kubectl create poddisruptionbudget", "Ensure minimum availability during voluntary disruptions.", "kubectl create poddisruptionbudget NAME --selector=LABEL=VALUE --min-available=N -n NS", "kubectl create pdb api-pdb --selector=app=api --min-available=2 -n myapp", "poddisruptionbudget.policy/api-pdb created", ["maxUnavailable and minAvailable conflict — set only one", "PDB ignored for single-replica deployments — still allows drain issues"])}

{cmd("kubectl cordon / uncordon", "Prevent new schedules without evicting (cordon).", "kubectl cordon NODE && kubectl uncordon NODE", "kubectl cordon node-3", "node/node-3 cordoned", ["Cordon alone does not migrate workloads — pair with drain", "Forgotten cordon reduces cluster capacity silently"])}

{cmd("kubectl get pdb,hpa,netpol", "Audit resilience objects in namespace.", "kubectl get pdb,hpa,networkpolicies -n NS", "kubectl get pdb,hpa,netpol -n myapp", "NAME      MIN AVAILABLE   ALLOWED DISRUPTIONS\\napi-pdb   2               1", ["Missing netpol in multi-tenant cluster is a security gap", "Review Helm values for production overrides in CI"])}

---

## Related Topics

- [RBAC](/kubernetes-handbook/rbac/) · [Network Policies](/kubernetes-handbook/network-policies/) · [HPA](/kubernetes-handbook/hpa/) · [Microservices — Zero-Downtime Deployment](/microservices/zero-downtime-deployment-topologies/)"""


def _body_docker_architecture() -> str:
    return f"""## Executive Summary

**Docker CLI** talks to **dockerd**, which uses **containerd** and **runc** to create OCI containers. Images live in registries; local storage uses layered graph drivers.

---

## Core Concepts

```mermaid
flowchart LR
  cli["docker CLI"] --> daemon["dockerd"]
  daemon --> containerd["containerd"]
  containerd --> runc["runc"]
  runc --> container["Container"]
  daemon --> registry["Registry"]
```

---

## Commands

{cmd("docker version", "Show client and server API versions.", "docker version", "docker version", "Client: Docker Engine 26.1.0\\nServer: Docker Engine 26.1.0", ["Client/server version skew can cause API errors", "Server section missing means daemon not running"])}

{cmd("docker info", "Display storage driver, cgroup, registry mirrors, and limits.", "docker info", "docker info", "Storage Driver: overlay2\\nCgroup Driver: systemd", ["Root dir full causes cryptic pull/build failures", "Check `Insecure Registries` for on-prem registry config"])}

{cmd("docker context ls", "List Docker contexts (local, remote, ECS).", "docker context ls", "docker context ls", "NAME        DESCRIPTION\\ndefault *   Current DOCKER_HOST", ["Wrong context pushes images to unexpected host", "Remote context needs TLS certs configured"])}

---

## Related Topics

- [Docker Commands](/kubernetes-handbook/docker-commands/) · [Container Lifecycle](/kubernetes-handbook/container-lifecycle/) · [Kubernetes Handbook — Docker](/kubernetes-handbook/docker/)"""


def _body_dockerfile() -> str:
    return f"""## Executive Summary

**Dockerfile** instructions build images layer by layer. Order matters for cache: pin bases, copy dependency files before source, combine RUN where sensible.

---

## Commands

{cmd("docker build", "Build image from Dockerfile in context directory.", "docker build -t NAME:TAG [PATH] [-f Dockerfile]", "docker build -t myapp:1.0.0 .", "Successfully tagged myapp:1.0.0", ["Large build context slows build — use `.dockerignore`", "`-f` wrong path builds unexpected recipe"])}

{cmd("docker build --no-cache", "Force full rebuild ignoring layer cache.", "docker build --no-cache -t NAME:TAG .", "docker build --no-cache -t myapp:1.0.0 .", "Successfully tagged myapp:1.0.0", ["Slower but needed when base image security patch must apply", "CI should periodically use no-cache for supply chain hygiene"])}

{cmd("docker history", "Show Dockerfile layer commands and sizes.", "docker history IMAGE", "docker history myapp:1.0.0", "IMAGE       CREATED        SIZE\\n<missing>   2 minutes ago   120MB", ["`<missing>` layers from squashed or pulled images", "Large RUN layers — refactor Dockerfile"])}

---

## Dockerfile Snippet

```dockerfile
FROM eclipse-temurin:21-jre-alpine
RUN addgroup -S app && adduser -S app -G app
WORKDIR /app
COPY target/app.jar app.jar
USER app
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "app.jar"]
```

---

## Related Topics

- [Multi-stage Builds](/kubernetes-handbook/multi-stage-builds/) · [Image Layers](/kubernetes-handbook/image-layers/) · [Docker Best Practices](/kubernetes-handbook/docker-best-practices/)"""


def _body_image_layers() -> str:
    return f"""## Executive Summary

Images are **read-only layers** stacked with copy-on-write. Reuse layers across images to save disk and speed pulls.

---

## Commands

{cmd("docker image inspect", "View layer IDs, env, cmd, and rootfs.", "docker image inspect IMAGE [--format='{{{{json .RootFS.Layers}}}}']", "docker image inspect myapp:1.0.0 --format='{{{{.Size}}}}'", "125829120", ["Format string typos return template errors", "Size is compressed transport size estimate — not exact disk"])}

{cmd("docker system df -v", "Break down image, container, and volume disk usage.", "docker system df -v", "docker system df -v", "Images space usage:\\nREPOSITORY   TAG   SIZE", ["Dangling `<none>` images accumulate from rebuilds", "Prune carefully in shared CI runners"])}

{cmd("docker pull", "Download image layers from registry.", "docker pull REPO:TAG", "docker pull nginx:1.27-alpine", "Status: Downloaded newer image for nginx:1.27-alpine", ["Pulling `latest` is non-reproducible — pin digest in prod", "Auth failure needs `docker login` first"])}

---

## Related Topics

- [Dockerfile](/kubernetes-handbook/dockerfile/) · [Docker Best Practices](/kubernetes-handbook/docker-best-practices/)"""


def _body_docker_volumes() -> str:
    return f"""## Executive Summary

**Volumes** persist data outside container lifecycle. Prefer **named volumes** over anonymous; **bind mounts** for dev hot-reload.

---

## Commands

{cmd("docker volume create", "Create a named volume.", "docker volume create NAME", "docker volume create pgdata", "pgdata", ["Volume names global on host — coordinate in Compose", "Wrong driver for swarm vs local"])}

{cmd("docker run -v", "Mount volume or bind path into container.", "docker run -v VOLUME_OR_PATH:CONTAINER_PATH IMAGE", "docker run -d -v pgdata:/var/lib/postgresql/data postgres:16", "container id...", ["Bind mount `:Z` SELinux label needed on RHEL/Fedora", "Windows path syntax differs for bind mounts"])}

{cmd("docker volume ls / inspect", "List volumes and find mountpoint on host.", "docker volume inspect NAME", "docker volume inspect pgdata", "Mountpoint: /var/lib/docker/volumes/pgdata/_data", ["`docker volume prune` deletes unused — data loss", "Backup requires stopping container or filesystem snapshot"])}

---

## Related Topics

- [Docker Compose](/kubernetes-handbook/docker-compose/) · [Container Lifecycle](/kubernetes-handbook/container-lifecycle/)"""


def _body_docker_networks() -> str:
    return f"""## Executive Summary

Default **bridge** network isolates containers on host. **user-defined bridge** adds DNS by container name. **overlay** for swarm multi-host.

---

## Commands

{cmd("docker network create", "Create custom bridge network.", "docker network create NAME", "docker network create app-net", "app-net", ["Containers on default bridge cannot resolve names", "Subnet overlap breaks compose stacks joining multiple networks"])}

{cmd("docker run --network", "Attach container to network at start.", "docker run --network NETWORK IMAGE", "docker run -d --name api --network app-net myapp:1.0", "container id...", ["Cannot change network of running container without reconnect", "`host` network removes isolation on Linux"])}

{cmd("docker network inspect", "See connected containers and IPAM config.", "docker network inspect NETWORK", "docker network inspect app-net", "Containers: {{ \"api\": {{ ... }} }}", ["Empty Containers means wrong network name", "iptables rules from Docker can conflict with VPN"])}

---

## Related Topics

- [Docker Compose](/kubernetes-handbook/docker-compose/) · [Services in Kubernetes](/kubernetes-handbook/services/)"""


def _body_multi_stage() -> str:
    return f"""## Executive Summary

**Multi-stage builds** use multiple `FROM` stages — compile in SDK image, copy artifacts into minimal runtime image.

---

## Commands

{cmd("docker build --target", "Build only up to named stage.", "docker build --target STAGE -t TAG .", "docker build --target runtime -t myapp:prod .", "Successfully tagged myapp:prod", ["Wrong target name fails at end of Dockerfile", "Dev stage may lack files copied only in later stage"])}

{cmd("docker build (multi-stage)", "Full multi-stage build producing small runtime image.", "docker build -t NAME:TAG .", "docker build -t myapp:1.0.0 .", "Successfully tagged myapp:1.0.0", ["COPY --from= wrong stage name breaks build", "Build tools in final stage bloat image and attack surface"])}

---

## Dockerfile Snippet

```dockerfile
FROM eclipse-temurin:21-jdk-alpine AS build
WORKDIR /app
COPY . .
RUN ./mvnw -q -DskipTests package

FROM eclipse-temurin:21-jre-alpine AS runtime
COPY --from=build /app/target/*.jar app.jar
ENTRYPOINT ["java", "-jar", "app.jar"]
```

---

## Related Topics

- [Dockerfile](/kubernetes-handbook/dockerfile/) · [Docker Best Practices](/kubernetes-handbook/docker-best-practices/)"""


def _body_docker_compose() -> str:
    return f"""## Executive Summary

**Docker Compose** defines multi-container apps in `compose.yaml` — services, networks, volumes, env, and dependencies.

---

## Commands

{cmd("docker compose up", "Create and start all services.", "docker compose up [-d] [-f FILE]", "docker compose up -d", "Container myapp-api-1  Started", ["Forgot `-d` attaches logs to terminal", "Stale orphans from renamed services — `docker compose down --remove-orphans`"])}

{cmd("docker compose ps", "List compose project containers and ports.", "docker compose ps", "docker compose ps", "NAME          IMAGE        STATUS    PORTS\\nmyapp-api-1   myapp:1.0    running   0.0.0.0:8080->8080/tcp", ["Shows only current project — set `COMPOSE_PROJECT_NAME`", "Healthcheck failing shows unhealthy status"])}

{cmd("docker compose logs", "Tail logs for one or all services.", "docker compose logs [-f] [SERVICE]", "docker compose logs -f api", "api-1  | Started on port 8080", ["`-f` never exits — use in dev only", "Service name is compose key not container name"])}

{cmd("docker compose down", "Stop and remove containers and default network.", "docker compose down [-v]", "docker compose down -v", "Container myapp-api-1  Removed", ["`-v` deletes named volumes — data loss", "Does not remove built images — prune separately"])}

---

## Related Topics

- [Docker Networks](/kubernetes-handbook/docker-networks/) · [Docker Volumes](/kubernetes-handbook/docker-volumes/)"""


def _body_docker_commands() -> str:
    return f"""## Executive Summary

Essential **docker** CLI — images, containers, registry, and cleanup.

---

## Commands

{cmd("docker images", "List local images with tags and sizes.", "docker images [REPO]", "docker images myapp", "REPOSITORY   TAG    IMAGE ID       SIZE\\nmyapp        1.0    abc123def456   220MB", ["Dangling `<none>` tags from rebuild — filter or prune", "IMAGE ID enough for local ops — prefer name:tag in scripts"])}

{cmd("docker ps", "List running containers.", "docker ps [-a] [--filter label=...]", "docker ps -a --filter name=api", "CONTAINER ID   IMAGE     STATUS\\nabc123         myapp:1.0 Exited (1) 2h ago", ["Exited containers still hold writable layer — `docker rm`", "Name filter is substring — can match multiple"])}

{cmd("docker tag / push", "Tag image for registry and upload.", "docker tag SRC:TAG REGISTRY/REPO:TAG && docker push REGISTRY/REPO:TAG", "docker tag myapp:1.0 registry.example.com/myapp:1.0 && docker push registry.example.com/myapp:1.0", "1.0: digest: sha256:... size: ...", ["Push wrong arch image to multi-arch repo breaks pulls", "Must docker login to private registry first"])}

{cmd("docker exec", "Run command in running container.", "docker exec [-it] CONTAINER COMMAND", "docker exec -it api sh", "# shell prompt", ["`-it` needs TTY — fails in some CI environments", "Changes in exec session not in image — rebuild to persist"])}

{cmd("docker system prune", "Remove unused data.", "docker system prune [-a] [-f] [--volumes]", "docker system prune -af", "Total reclaimed space: 2.5GB", ["`-a` removes all unused images — aggressive on dev machine", "`--volumes` deletes unused volumes — irreversible"])}

---

## Related Topics

- [Container Lifecycle](/kubernetes-handbook/container-lifecycle/) · [Docker Best Practices](/kubernetes-handbook/docker-best-practices/)"""


def _body_container_lifecycle() -> str:
    return f"""## Executive Summary

Container states: **created → running → paused/stopped → removed**. Restart policies control daemon restart behavior.

---

## Commands

{cmd("docker run", "Create and start container from image.", "docker run [OPTIONS] IMAGE [COMMAND]", "docker run -d --name api --restart unless-stopped -p 8080:8080 myapp:1.0", "long-container-id", ["Port already allocated error — pick free host port", "`--rm` auto-deletes on stop — good for CI, bad for debug"])}

{cmd("docker stop / start", "Graceful SIGTERM then SIGKILL stop; start existing container.", "docker stop CONTAINER [&& docker start CONTAINER]", "docker stop api && docker start api", "api\\napi", ["Default stop timeout 10s — apps need longer graceful shutdown", "Start fails if name conflict with new container"])}

{cmd("docker restart", "Restart running or stopped container.", "docker restart CONTAINER", "docker restart api", "api", ["Restart does not pull new image — recreate container for upgrades", "Rapid restart loops hide application crash cause — check logs"])}

{cmd("docker rm", "Remove stopped container.", "docker rm [-f] CONTAINER", "docker rm -f api", "api", ["`-f` kills running container — data loss in container layer", "Cannot remove running without `-f`"])}

---

## Related Topics

- [Docker Commands](/kubernetes-handbook/docker-commands/) · [Pods lifecycle](/kubernetes-handbook/pods/)"""


def _body_docker_best_practices() -> str:
    return f"""## Executive Summary

Run as **non-root**, use **minimal base images**, pin **digests**, scan in CI, keep secrets out of layers, and set **healthcheck** / **resource limits** in orchestrators.

---

## Commands

{cmd("docker scout cve / scan (or trivy)", "Scan image for known vulnerabilities.", "docker scout cve IMAGE  # or: trivy image IMAGE", "docker scout cve myapp:1.0", "TARGET myapp:1.0\\n  CRITICAL  0\\n  HIGH      2", ["Base image choice drives CVE count — alpine vs distroless tradeoffs", "Scan in CI gate — not only before prod deploy"])}

{cmd("docker build with USER", "Verify container runs non-root.", "docker run --rm IMAGE id", "docker run --rm myapp:1.0 id", "uid=1000(app) gid=1000(app)", ["Bind ports <1024 need root or CAP_NET_BIND_SERVICE", "Volume mount permissions must match USER"])}

{cmd("docker inspect Health", "Check Dockerfile HEALTHCHECK status.", "docker inspect --format='{{{{.State.Health.Status}}}}' CONTAINER", "docker inspect --format='{{{{.State.Health.Status}}}}' api", "healthy", ["Missing HEALTHCHECK means orchestrator must define probes", "Unhealthy container still running — depends on restart policy"])}

---

## Related Topics

- [Multi-stage Builds](/kubernetes-handbook/multi-stage-builds/) · [Production Best Practices](/kubernetes-handbook/production-best-practices/) · [Microservices — Application Containerization](/microservices/application-containerization-docker/)"""


def front_matter(slug: str, module_id: int, module_title: str, section_ref: str) -> str:
    title, short, desc = TOPIC_META[slug]
    return textwrap.dedent(
        f"""---
title: "{title}"
date: {DATE}
draft: false
description: "{desc}"
tags: ["{SECTION}", "kubernetes", "docker", "cheatsheet", "handbook"]
categories: ["{CATEGORY}"]
shortTitle: "{short}"
module: {module_id}
moduleTitle: "{module_title}"
sectionRef: "{section_ref}"
cheatSheet: true
aliases: ["/kubernetes-cheatsheet/{slug}/"]
---
"""
    )


def build() -> None:
    _register_bodies()
    modules_data = yaml.safe_load((DATA / "kubernetes_handbook_modules.yaml").read_text(encoding="utf-8"))
    CONTENT.mkdir(parents=True, exist_ok=True)

    expected_slugs: set[str] = set()
    for mod in modules_data["modules"]:
        mid = mod["id"]
        mtitle = mod["focus"]
        for slug in mod["topics"]:
            body = PAGE_BODIES.get(slug)
            if not body:
                continue
            expected_slugs.add(slug)
            local_idx = mod["topics"].index(slug) + 1
            ref = f"{mid}.{local_idx}"
            content = front_matter(slug, mid, mtitle, ref) + "\n" + body + "\n"
            out = CONTENT / f"{slug}.md"
            out.write_text(content, encoding="utf-8")
            print(f"Wrote {out.relative_to(ROOT)}")

    for path in CONTENT.glob("*.md"):
        if path.name == "_index.md":
            continue
        if path.stem in PAGE_BODIES and path.stem not in expected_slugs:
            path.unlink()
            print(f"Removed orphan {path.relative_to(ROOT)}")


if __name__ == "__main__":
    build()
