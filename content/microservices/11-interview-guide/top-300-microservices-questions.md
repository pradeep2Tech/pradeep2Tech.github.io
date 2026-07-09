---
title: "Top 300 Questions (Master Index)"
date: 2026-07-03T15:00:00+00:00
draft: false
description: "Master index — 300 production microservices interview questions."
tags: ["microservices", "architecture-playbook", "distributed-systems"]
categories: ["Microservices Architecture Playbook"]
shortTitle: "Top 300"
module: 11
moduleTitle: "Interview Guide"
sectionRef: "11.1"
weight: 1101
playbookVersion: 3
interviewHandbook: true
---

# Top 300 Questions (Master Index)

Master index for **Senior Engineers**, **Staff Engineers**, and **Principal Architects**. **Questions only** — no answers. Category pages ([Architecture](/microservices/11-interview-guide/architect-questions/), [Distributed Systems](/microservices/11-interview-guide/distributed-systems-interviews/), [Scalability](/microservices/11-interview-guide/scalability-questions/), [Reliability](/microservices/11-interview-guide/reliability-questions/), [Observability](/microservices/11-interview-guide/observability-questions/), [Troubleshooting](/microservices/11-interview-guide/troubleshooting-questions/), [Case Studies](/microservices/11-interview-guide/system-design-case-studies/), [Staff/Principal](/microservices/11-interview-guide/staff-principal-scenarios/)) add unique depth without repeating these prompts.

1. When does a modular monolith outperform a microservices fleet for a 12-person product team?
2. How does Conway's Law influence your decomposition boundaries?
3. What signals indicate you are building a distributed monolith?
4. How would you compare SOA ESB-centric integration with modern event-driven microservices in a migration interview?
5. When would you reject a microservices migration proposal from leadership?
6. How do you define service boundaries using bounded contexts?
7. What operational tax does microservices impose vs modular monolith?
8. How do API gateway and BFF responsibilities differ at the edge?
9. When should a BFF aggregate five calls vs delegate to a domain service?
10. How do you prevent the API gateway from becoming a distributed monolith?
11. Design service discovery for multi-cluster Kubernetes without hardcoded IPs.
12. When is client-side discovery preferable to server-side load balancing?
13. How do you choose sync gRPC vs async events for a new integration?
14. How would you enforce database-per-service and eliminate cross-schema JOINs in a decomposing monolith?
15. When is CQRS worth the operational cost over simple CRUD?
16. Orchestration vs choreography saga — decision criteria?
17. Why is dual-write an anti-pattern and what replaces it?
18. How does outbox differ from CDC for event publication?
19. When would you use event sourcing vs event-carried state transfer?
20. How do you model cross-domain reporting without shared operational databases?
21. How do you align team topology with service ownership?
22. When would you choose a strangler fig migration over a full rewrite for a revenue-critical monolith?
23. How do you phase database decomposition without big-bang cutover?
24. What anti-corruption layer responsibilities exist at legacy boundaries?
25. When is a service mesh operational tax not justified?
26. What Kubernetes primitives are mandatory for stateless microservices?
27. How do PodDisruptionBudgets interact with rolling deployments?
28. How would you run an expand-contract schema migration on a table receiving 5K writes/sec?
29. How do you structure ADRs for a contentious broker selection?
30. How would you differentiate monolith, modular monolith, microservices, and SOA for a fintech platform?
31. What bounded context would you extract first from an e-commerce monolith?
32. How do you measure whether decomposition improved deploy frequency?
33. When does shared library coupling negate microservices benefits?
34. How do you govern API versioning across autonomous teams?
35. How would you apply smart endpoints and dumb pipes when every team wants logic in the gateway?
36. How would you decide whether checkout, catalog, and fulfillment belong in one deployable unit or three autonomous services?
37. Walk me through decomposing a 400K-line ERP monolith when finance insists on shared GL reporting.
38. Design a platform team boundary so internal developer tooling does not become a second monolith.
39. How would you choose between REST, gRPC, and async events for a new loyalty-points integration?
40. Why would you standardize on one message broker vs allow team-level selection — and how would you govern it?
41. How would you evolve a synchronous order chain into event-driven fulfillment without a big-bang rewrite?
42. Design service ownership when three teams share writes to the same customer profile aggregate.
43. How would you evaluate building a custom API gateway vs adopting Kong, Envoy, or cloud edge?
44. Walk me through an ADR process when two principal engineers disagree on CQRS for read-heavy catalog.
45. How would you prevent domain logic from leaking into shared infrastructure libraries?
46. Design multi-tenant isolation for a B2B SaaS where some tenants require dedicated databases.
47. How would you architect cross-cutting auth so each service does not reimplement OAuth validation?
48. When would you introduce a workflow engine vs keep saga logic in application code?
49. How would you structure a reference architecture that teams can adopt without copy-paste drift?
50. Design an internal service catalog that stays accurate as teams rename APIs weekly.
51. How would you reason about build-vs-buy for a real-time fraud scoring dependency?
52. Walk me through splitting a payments monolith when PCI scope must shrink per service.
53. How would you handle schema versioning when mobile clients lag server releases by six months?
54. Design governance for breaking API changes across 40 autonomous squads.
55. How would you decide whether search belongs in catalog service, a BFF, or a dedicated search platform?
56. Why would you reject event sourcing for a team that only needs audit trails?
57. How would you model service tiers so tier-3 batch jobs cannot starve tier-1 checkout paths?
58. Design a data mesh vs centralized data lake strategy for product analytics across microservices.
59. How would you align architecture reviews with actual incident history instead of theoretical purity?
60. Walk me through choosing PostgreSQL vs DynamoDB for a high-write session store at Netflix scale.
61. Walk me through CAP during a network partition with a concrete ledger example.
62. What does PACELC add beyond CAP for normal operation?
63. Why is there no production CA system under partition?
64. When would CP be wrong for a social feed?
65. How does consistent hashing minimize data movement on node add?
66. What are virtual nodes and why use them on a hash ring?
67. How would you compare modulo sharding vs consistent hashing for hot keys?
68. What anomalies does READ COMMITTED prevent vs SERIALIZABLE?
69. Optimistic vs pessimistic concurrency — when each in order service?
70. How do distributed deadlocks arise across saga steps?
71. Map CP/AP choices to inventory holds vs recommendation feeds.
72. How does quorum loss manifest in etcd during AZ failure?
73. How would you reason about sloppy quorum, and when would you accept it?
74. How do vector clocks help detect concurrent writes in AP systems?
75. When is last-write-wins dangerous for financial balances?
76. How does PACELC PC/EL apply to MongoDB majority writes?
77. What read-your-writes guarantee can you promise with async replicas?
78. How do phantom reads appear under REPEATABLE READ?
79. Design shard key for multi-tenant SaaS orders table.
80. What happens to CAP choice during cross-region network blip?
81. How would you reason about linearizability vs serializability for a wallet balance read during failover?
82. Walk me through designing a shard rebalancer that avoids thundering herd on moved keys.
83. How would you detect and resolve write skew when two services update related inventory rows concurrently?
84. Design a lease-based leader election that survives clock drift and GC pauses.
85. How would you choose between CRDTs and operational transform for collaborative document editing?
86. What happens if a quorum write succeeds on minority nodes during a network partition?
87. How would you design compare-and-swap retries for optimistic concurrency without livelock?
88. Walk me through fencing tokens in a distributed lock used by a payment capture job.
89. How would you handle a split vote when two regions both believe they are the write leader?
90. Design idempotent sequence generation across three data centers without a single global counter.
91. How would you reason about causal consistency for a social feed vs a ledger posting?
92. What failure modes appear when you rely on wall-clock timestamps for event ordering?
93. How would you design a gossip protocol health check that does not amplify partition rumors?
94. Walk me through repairing inconsistent secondary indexes after a partial write failure.
95. How would you choose between two-phase commit and saga for a travel booking with three providers?
96. Design a conflict-free replicated shopping cart that merges offline and online edits.
97. How would you test split-brain scenarios in staging before they happen in production?
98. What happens if a consumer reads from a replica that has not caught up after a leader election?
99. How would you design a distributed cache invalidation protocol that avoids stale reads?
100. Walk me through handling duplicate delivery when exactly-once semantics are marketed but impossible.
101. How would you size virtual nodes on a consistent hash ring for 200 Redis shards?
102. Design a workflow checkpoint format so workers can resume mid-saga after a pod eviction.
103. How would you reason about PACELC when latency spikes but no partition has occurred?
104. What tradeoffs do you accept when choosing AP for a notification preference store?
105. How would you design a global secondary index that stays eventually consistent with the primary?
106. Walk me through detecting and quarantining Byzantine behavior in a peer-to-peer sync mesh.
107. How would you handle a hot key that exceeds single-node memory on a DynamoDB partition?
108. Design a read repair strategy for an AP key-value store serving product availability.
109. How would you propagate partial failure information through a synchronous microservice graph?
110. Walk me through choosing isolation levels when money movement spans two PostgreSQL instances.
111. How do you scale a stateless order API vs its database tier?
112. How would you diagnose scatter-gather penalty when a sharded SQL query fans out to every shard?
113. How do you detect and fix hot shard skew?
114. When do read replicas help vs break read-your-writes UX?
115. Design tiered rate limiting: CDN edge, API gateway, service.
116. Fail-open vs fail-closed when Redis rate limiter is unavailable?
117. Cache-aside vs write-through for product catalog reads?
118. How do you prevent cache stampede on viral product keys?
119. CDC-driven cache invalidation vs TTL-only staleness windows?
120. HPA on CPU vs custom metrics for Kafka consumer lag?
121. When autoscale stateless pods but DB is saturated?
122. How size connection pools per instance at 10× traffic?
123. How would you size a bulkhead pool for a payment dependency that stalls the rest of checkout?
124. Horizontal pod autoscaler vs cluster autoscaler interaction?
125. When shard vs vertical scale for PostgreSQL order DB?
126. Black Friday traffic is 15× baseline — how would you scale checkout before the database becomes the bottleneck?
127. Walk me through autoscaling Kafka consumers when lag spikes but broker CPU is flat.
128. How would you fix a Redis hot key on a celebrity product page without rewriting the catalog schema?
129. Design CDN cache rules for a flash sale where inventory changes every few seconds.
130. How would you partition an orders topic when order_id hashing creates one overloaded partition?
131. What happens if HPA scales pods 10× but connection pools exhaust the database max_connections?
132. How would you scale read replicas when replication lag breaks post-checkout order status pages?
133. Walk me through tiered caching when L1 in-process, L2 Redis, and L3 CDN all miss simultaneously.
134. How would you rate-limit abusive API partners without throttling legitimate bulk importers?
135. Design autoscaling for a bursty webhook ingestion service with unpredictable partner traffic.
136. How would you scale Elasticsearch indexing when catalog updates spike during a product launch?
137. What would you do when vertical scaling hits instance limits but sharding is six months away?
138. How would you load-balance gRPC streams when connection affinity hides uneven pod CPU?
139. Walk me through scaling a GraphQL BFF that fans out to twelve downstream services per request.
140. How would you prevent autoscaling oscillation when CPU spikes during GC but RPS is stable?
141. Design a sharding strategy for multi-tenant SaaS where one tenant generates 40% of writes.
142. How would you scale outbound HTTP connection pools when egress NAT ports become the limit?
143. What happens if you scale stateless APIs but the shared Redis cluster hits single-master throughput?
144. How would you use request coalescing to protect a database during a cache stampede?
145. Walk me through scaling a batch reconciliation job that must finish before market open.
146. How would you size Kafka partitions for a topic that must preserve per-user ordering?
147. Design edge rate limiting when CloudFront and API gateway limits disagree on client identity.
148. How would you scale a websocket fan-out layer for live auction bidding?
149. What tradeoffs do you accept when over-provisioning for peak vs paying for idle capacity year-round?
150. How would you diagnose and fix scatter-gather latency when one shard answers in 2s and others in 20ms?
151. Design the resilience stack for a payment dependency.
152. Why must breaker timeout be less than client timeout?
153. When is retry safe on HTTP POST in payments?
154. How would you design a retry budget with full jitter for a payment client under intermittent 503s?
155. Read fallback vs write fallback policies at checkout?
156. How does bulkhead prevent cascade without fixing root cause?
157. What SLO would you set for tier-1 checkout API?
158. How do error budgets gate feature releases?
159. How would you choose consumer-driven contract testing over E2E for a twelve-service checkout graph?
160. How do idempotent consumers interact with at-least-once delivery?
161. Design saga compensation for failed inventory reservation.
162. How ensure orchestrator durability with outbox?
163. What happens when half-open probes overload recovering service?
164. Graceful degradation for recommendations without faking payments?
165. How test timeout chains in CI for microservice graph?
166. Payment provider latency doubled — how would you tune retries, timeouts, and circuit breakers together?
167. Walk me through designing idempotency keys that survive client retries and broker redelivery.
168. How would you implement graceful degradation when the recommendation service is down but checkout must complete?
169. Design a saga compensation path when inventory release succeeds but payment refund fails.
170. How would you set SLOs and error budgets for a tier-1 API owned by three different teams?
171. What happens if circuit breaker half-open probes arrive faster than the recovering service can handle?
172. How would you test chaos experiments on payment flows without risking real money movement?
173. Walk me through bulkhead isolation when one slow dependency threatens the entire thread pool.
174. How would you design fallback behavior for tax calculation when the vendor API is unavailable?
175. Design disaster recovery RTO/RPO targets when checkout spans five regions and three vendors.
176. How would you ensure at-least-once consumers remain safe when duplicate events arrive hours apart?
177. What failure modes appear when retry budgets are per-service but the blast radius is cross-service?
178. How would you run a game day that validates failover without customer-visible errors?
179. Walk me through hedged requests for read paths — when do they help vs amplify load?
180. How would you design timeout budgets across a six-hop synchronous checkout chain?
181. Design health checks that do not mark a pod ready while downstream warmup is incomplete.
182. How would you handle poison messages in a payment settlement queue without losing ordering?
183. What happens if your outbox relay falls behind during a regional database failover?
184. How would you implement adaptive concurrency limits based on downstream error rates?
185. Walk me through error budget policy when product wants to ship during an ongoing reliability debt.
186. How would you design a dead-letter workflow that ops can replay without double-charging customers?
187. Design resilience for a third-party KYC API with unpredictable 30s timeouts during peak hours.
188. How would you validate circuit breaker thresholds using historical p99 instead of guesses?
189. What tradeoffs do you accept between fail-open rate limiting and fail-closed during Redis outage?
190. How would you coordinate graceful shutdown so in-flight sagas complete before pod termination?
191. Checkout p99 spiked — walk through triage steps.
192. Consumer lag growing — what do you check first?
193. Poison message blocking partition — mitigation?
194. Split-brain after DB failover — detection and fix?
195. Retry storm after partial outage — containment?
196. Mesh control plane down — what still works?
197. CDC lag at cutover gate — go/no-go criteria?
198. Stale service registry causing intermittent 503?
199. Cascading timeout across five-hop synchronous chain?
200. Outbox relay stopped — business impact and fix?
201. Hot partition on order topic — symptoms and fix?
202. JWKS fetch failure causing auth outage at gateway?
203. Canary regression — rollback decision criteria?
204. Projection lag causing stale UI after write?
205. Checkout p99 jumped from 200ms to 4s — walk me through your first 15 minutes of triage.
206. Kafka consumer lag is growing 10K messages/min — what do you check before scaling consumers?
207. Redis cluster reports UNHEALTHY — how would you isolate whether it is network, memory, or failover?
208. Database primary failed over — how would you detect split-brain and protect in-flight transactions?
209. Pods are OOMKilled every 10 minutes after a deploy — walk me through your investigation.
210. CrashLoopBackOff on payment-service after a config change — what is your structured debug path?
211. Connection pool exhaustion causes 503s — how would you distinguish client leaks from traffic spike?
212. TLS certificate expired on the API gateway at 2am — what is immediate mitigation and long-term fix?
213. DNS resolution intermittently fails for internal services — how would you narrow root cause?
214. Thread pool starvation in order-service — what metrics and traces prove the bottleneck?
215. GC pause times exceed 2s on checkout JVMs — how would you correlate with latency SLO breach?
216. Istio sidecar routing sends 30% traffic to a draining pod — walk me through mesh triage.
217. Canary deployment shows 5× error rate on 5% traffic — what are your rollback decision criteria?
218. Event replay job duplicated customer emails — how would you stop blast radius and repair state?
219. Memory leak in a long-running consumer — how would you profile without stopping production traffic?
220. API gateway returns 401 for all users — JWKS fetch is timing out; what do you check first?
221. CDC connector lag blocks strangler cutover — what go/no-go signals do you require?
222. Projection worker fell 6 hours behind — how would you explain stale UI to product and fix backlog?
223. Mesh control plane is down — what still works and what must you disable immediately?
224. Retry storm after partial outage amplified load 8× — how would you contain it in production?
225. Hot partition on order-events topic — symptoms, immediate fix, and permanent remediation?
226. How do RED metrics differ from USE for a gRPC service?
227. What fields belong in structured logs for correlation?
228. Head vs tail sampling tradeoffs for payment traces?
229. How propagate traceparent through Kafka record headers?
230. Golden signals for async pipeline vs sync API?
231. Alert on consumer lag vs CPU for worker autoscale?
232. Dashboard minimum for new microservice production launch?
233. How link logs to traces in OpenTelemetry collector pipeline?
234. What SLO burn rate alert fires before user-visible outage?
235. How detect missing trace context at service boundary?
236. Checkout error rate doubled but CPU is flat — how would you use metrics, logs, and traces to find root cause?
237. Walk me through designing RED dashboards for a new gRPC service before launch day.
238. How would you debug missing trace spans across Kafka consumers and HTTP callbacks?
239. Prometheus cardinality exploded after a deploy — how would you find the offending label?
240. Jaeger shows 8s gaps in traces — how would you determine whether sampling or instrumentation is wrong?
241. How would you correlate Loki logs to Tempo traces when trace_id is missing in half the log lines?
242. Design alert routing so on-call is paged for user-visible SLO burn, not every pod restart.
243. How would you investigate p99 latency regression when per-service metrics all look healthy?
244. Walk me through OpenTelemetry collector pipeline design for 200 microservices.
245. How would you choose head vs tail sampling when payment traces must be debuggable but volume is huge?
246. Grafana dashboards show green but customers complain — what signals are you likely missing?
247. How would you detect metric label churn that will break Prometheus in three months?
248. Design a runbook-driven incident timeline using logs, traces, and deployment events.
249. How would you debug high-cardinality custom metrics from a well-meaning feature team?
250. Walk me through burn-rate alerting that fires 30 minutes before an SLO breach, not after.
251. How would you instrument async pipelines so lag is visible before consumers fall hours behind?
252. What happens if your tracing backend is down during a production incident — what is your fallback?
253. How would you validate that correlation IDs propagate through mesh, gateway, and batch jobs?
254. Design log retention and sampling when compliance requires 90 days but cost must stay bounded.
255. How would you use exemplars to jump from a latency spike graph to the exact slow trace?
256. Walk me through debugging a canary regression using only observability data, no code diff yet.
257. How would you onboard a new service to observability standards in one sprint without boilerplate drift?
258. Design SLO dashboards that executives understand without hiding operator-critical detail.
259. How would you detect silent failures where HTTP 200 is returned but business logic partially failed?
260. Walk me through post-incident observability gaps when nobody could answer 'what changed at 14:03?'
261. mTLS mesh vs edge TLS only — threat model difference?
262. How rotate JWT signing keys without downtime?
263. Service-to-service auth: OAuth client credentials vs mesh SPIFFE?
264. Secrets in env vs Vault sidecar injection tradeoffs?
265. How prevent BFF from becoming over-privileged aggregator?
266. Zero-trust between services in same VPC — justify?
267. How audit mesh authorization policy changes?
268. API gateway WAF vs service-level input validation division?
269. A service account key leaked in a public repo — walk me through containment and rotation without downtime.
270. How would you design break-glass access for production debugging without permanent over-privilege?
271. mTLS rollout caused 12% traffic failures — how would you troubleshoot mesh certificate trust chains?
272. How would you audit which services can call payment APIs after six months of organic growth?
273. Design secret rotation for database credentials used by 40 microservices without coordinated deploys.
274. How would you prevent SSRF from a BFF that proxies partner webhook callbacks?
275. Walk me through threat modeling when moving from VPC peering to zero-trust service identity.
276. How would you detect and block credential stuffing at the gateway without blocking mobile apps?
277. Design OAuth scope governance so teams cannot request admin scopes by default.
278. How would you respond when WAF rules block legitimate traffic during a marketing campaign?
279. Walk me through securing Kafka topics when producers span three business units.
280. How would you validate that no service logs PAN or PII after a rushed feature launch?
281. First bounded context to extract from monolith — criteria?
282. Dual-write risks during strangler migration phases?
283. Feature flag rollback during canary failure?
284. Blue-green vs canary for schema-breaking API change?
285. How reverse-sync legacy DB during database decomposition rollback?
286. Anti-corruption layer testing strategy during strangler?
287. Team topology changes required before service extraction?
288. How measure migration progress beyond lines of code moved?
289. Strangler cutover is tonight — CDC lag spiked to 45 minutes; what is your go/no-go decision framework?
290. How would you roll back a database decomposition when reverse-sync has not been tested at production volume?
291. Walk me through dual-write detection when legacy and new order tables diverge silently.
292. How would you migrate authentication from monolith sessions to JWT without forcing all users to re-login?
293. Design a feature-flag strategy for routing 1% traffic to a new fulfillment service safely.
294. How would you measure migration success when error rates are flat but operational cost doubled?
295. Walk me through anti-corruption layer testing when legacy ERP schema changes weekly.
296. How would you sequence service extraction when billing depends on inventory but inventory depends on catalog?
297. Design zero-downtime schema migration for a column type change on a 2B-row orders table.
298. How would you communicate migration risk to executives when technical rollback is possible but business rollback is not?
299. Walk me through team topology changes required before extracting the payments bounded context.
300. How would you handle a strangler phase where two systems both emit OrderCreated events?
