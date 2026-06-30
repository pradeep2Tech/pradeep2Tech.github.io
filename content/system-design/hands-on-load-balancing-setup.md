---
title: "Hands-On Load Balancer Provisioning"
date: 2026-06-28T10:36:00+00:00
draft: false
description: "Operational ingress debugging — misconfigured health probes, asymmetric routing under NAT, and TLS cert rotation blackouts."
tags: ["system-fundamentals", "load-balancing", "hands-on"]
categories: ["System Fundamentals"]
shortTitle: "Hands-On Load Balancer Provisioning"
module: 1
moduleTitle: "Boundary Ingress Routing & Proxy Mechanics"
sectionRef: "1.4"
---

### Practical Infrastructure Provisioning
To establish horizontal scaling across a cloud compute fleet, backend instances must be cloned from a common baseline state and placed behind a high-availability ingress proxy layer.

#### 1. Compute Instance Replication (The Gold Image Template)
* Instead of deploying and manual-scripting individual server dependencies, capture an exact, point-in-time snapshot clone of an active, production-ready compute host.
* Provision twin target droplets (`Instance 1` and `Instance 2`) using this base image template.
* Pin all newly provisioned computing resources to the identical cloud availability zone and datacenter regional routing boundary (e.g., `San Francisco - Datacenter 3`). Mixing regions prevents the load balancer from cleanly mapping internal private network targets.

#### 2. Local Port Isolation & Runtime Execution
Launch the instance terminal console for each node and configure the local operating system firewall (Uncomplicated Firewall) to allow inbound application proxy traffic:

```bash
sudo ufw allow 3000/tcp
sudo ufw enable
sudo ufw status
```

Start the application process bound to the private interface on port `3000` on both instances. Verify local reachability before registering backends with the load balancer:

```bash
curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:3000/health
# Expected: 200
```

#### 3. Backend Pool Registration
Register each instance's **private** IP address (not the public floating IP) as a backend target on the load balancer. Cloud providers route health probes and forwarded client traffic over the internal VPC fabric; binding backends to public IPs introduces NAT hairpin failures and asymmetric return paths.

```text
[ Internet Clients ]
        │
        ▼
┌───────────────────┐
│  Load Balancer    │  ◄── Public VIP (443/80)
│  (L4 or L7)       │
└─────────┬─────────┘
          │ Private VPC
    ┌─────┴─────┐
    ▼           ▼
┌─────────┐ ┌─────────┐
│ Inst 1  │ │ Inst 2  │  ◄── 10.0.1.11:3000 / 10.0.1.12:3000
└─────────┘ └─────────┘
```

Configure the backend pool with:
* **Protocol / Port:** `HTTP` on `3000` (or `TCP` for pure L4 passthrough)
* **Health check path:** `/health` returning `200 OK`
* **Health check interval:** 10s with 3 consecutive failures before drain
* **Connection draining:** 30s grace period during rolling deploys

---

### Critical Failure Modes & Operational Vulnerabilities

#### 1. Misconfigured Health Probes
The most common production outage after provisioning a new backend pool is a health probe that does not match what the application actually serves.
* **Wrong Port or Path:** A probe targeting `/` when the app only exposes `/health` marks every backend unhealthy within seconds, removing all targets from rotation and returning `503 Service Unavailable` to clients.
* **Host Header Mismatch:** L7 probes that send `Host: localhost` while the application enforces virtual-host routing (`Host: api.example.com`) fail silently — the probe receives `404` even though the service is running.
* *Mitigation:* Mirror the exact probe URL, port, and `Host` header the load balancer will use in production. Validate with `curl -H "Host: api.example.com" http://10.0.1.11:3000/health` from a bastion inside the VPC before enabling the pool.

#### 2. Asymmetric Routing under NAT
When backends are registered with public IPs or span subnets without proper return-path routing, reply packets may leave via a different interface than the one that received the forwarded request.
* **The Failure Mode:** The load balancer forwards a SYN to `Instance 1` via its private IP, but the instance replies via its default gateway on a public route. The load balancer never sees the response and marks the backend down.
* *Mitigation:* Always register private VPC addresses. Disable source-NAT on the load balancer for backend traffic, and ensure security groups allow inbound from the LB subnet *and* outbound return traffic on ephemeral ports.

#### 3. TLS Certificate Rotation Blackouts
Terminating TLS at the load balancer simplifies backend management, but certificate expiry or botched rotation takes down the entire ingress edge simultaneously.
* **The Failure Mode:** A renewed certificate is uploaded to one load balancer node in an active-active pair but not the standby. During failover or rolling LB maintenance, clients hit the node with the expired cert and receive TLS handshake failures.
* *Mitigation:* Automate cert renewal (e.g., ACME / Let's Encrypt with managed LB integration). Run pre-expiry alerts at 30/14/7 days. After rotation, verify the full chain with `openssl s_client -connect api.example.com:443 -servername api.example.com` from an external vantage point before closing the change ticket.

---

### Post-Provision Verification Checklist

| Check | Command / Action | Expected |
| :--- | :--- | :--- |
| Backend local health | `curl http://127.0.0.1:3000/health` on each instance | `200` |
| LB → backend reachability | `curl http://10.0.1.11:3000/health` from LB subnet | `200` |
| End-to-end via VIP | `curl https://api.example.com/health` | `200` |
| Drain behavior | Stop app on `Instance 1`, wait 3 probe cycles | Traffic shifts to `Instance 2` only |
| Sticky session (if enabled) | Repeat requests, inspect `Set-Cookie` / source IP hash | Same backend across session |

---
