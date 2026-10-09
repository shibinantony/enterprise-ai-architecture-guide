# Day 2: operate the service, realize value, and scale

Day 2 manages the complete service after launch. Availability is necessary, but an available service that gives poor answers, creates rework, or is ignored by users does not deliver the intended value.

## Operate four linked views

| View | What to observe | What it informs |
|---|---|---|
| Business outcome | Verified completion, repeat contacts, backlog, rework, user impact | Whether the process improved |
| User adoption | Eligible task usage, abandonment, corrections, successful handoffs | Whether the experience and training work |
| Service health | Dependency failures, latency, queues, freshness, transaction status | Reliability and operational response |
| Economics | Cost per outcome, token/call growth, review and support effort | Optimization and expansion decisions |

Keep numerator, denominator, cohort, and time window consistent. Segment by task complexity and user group where appropriate. Report unresolved cases and maturity of follow-up windows.

## Set service objectives

Set business and technical objectives together: verified outcome quality, time to resolution, answer latency where relevant, data freshness, exception aging, availability, and cost envelope. Distinguish model-call latency from the user's full wait, including queues and review.

Define thresholds and responsible responders before launch. An error budget or expansion pause should reflect service consequence and business need. Avoid inventing a universal target such as a fixed accuracy percentage for every process.

## Run a practical operating cadence

| Cadence | Work | Owner |
|---|---|---|
| Continuous | Alert on outages, abnormal spend, stuck work, serious outcome or access failures | On-call and service operations |
| Daily during pilot | Review unresolved cases, corrections, queue capacity, user friction, cost anomalies | Product and process team |
| Weekly | Inspect evaluation failures, content gaps, tool reliability, adoption, improvement backlog | Cross-functional delivery team |
| Monthly | Review value against baseline, unit economics, capacity redeployment, service objectives | Business owner and finance partner |
| On material change | Re-evaluate model, prompt, tool, data, policy, infrastructure, or permissions | Relevant owners and release authority |
| At portfolio review | Expand, reuse, consolidate, renegotiate, or retire | Platform and business leadership |

Adjust this proposed cadence to service scale and criticality. A meeting schedule does not substitute for clear action ownership.

## Manage change and drift

Failures can arise from model changes, new user behavior, outdated knowledge, changed APIs, evolving business policy, or an altered case mix. Diagnose the layer before changing the prompt.

Use production observations to build new approved evaluation cases. Protect a representative holdout set. Re-test impacted paths before deploying a model or tool upgrade. Track deprecation and retirement dates early enough to evaluate replacements rather than make an emergency migration.

Preserve a version record across application, model/configuration, workflow, tool contracts, data/index, policy, and evaluation. A minor version label does not prove a minor business impact.

## Reliability and incident response

Correlate requests, retrieval, model calls, tools, human handoffs, and transaction receipts. Use minimized telemetry and controlled access to sensitive evidence. Classify failures by effect: unavailable response, incorrect advice, unauthorized access, incorrect action, duplicate action, or unresolved commitment.

Stop the affected action path when needed, preserve case state, communicate the next responsible step, and reconcile in-flight transactions. An application rollback does not reverse an already committed business operation. Use the approved domain repair or compensation process.

Exercise fallback with the actual support team. A manual fallback is viable only if staff have capacity, current information, and the required authority.

## Optimize cost without sacrificing outcomes

Investigate excessive context, repeated retrieval, unnecessary loops, retries, idle sessions, over-provisioning, and review burden. Consider shorter context, caching where permitted, batch work for asynchronous tasks, model routing, and simpler orchestration.

Re-measure quality after each optimization. Lower tokens can remove decisive evidence; reduced review can shift costs into later remediation. The [cost model](../examples/cost-model/README.md) makes assumptions visible, but actual service traces and invoices are required for realized economics.

## Expand through supported reuse

Standardize assets with proven consumers: data products, tool contracts, procedures, evaluation harnesses, deployment paths, observability, and identity patterns. Give shared assets an owner, service objective, funded maintenance, and change contract.

Measure the marginal delivery and operating effort of the next workflow, including adapters, testing, and support. Do not call a capability reusable merely because its code was copied. Keep the domain team accountable for the business outcome.

## Retire deliberately

Retire or redesign a service when demand, outcomes, economics, supportability, or obligations no longer justify it. Migrate consumers, resolve queued work, reconcile transactions, revoke access, update discovery, and apply the approved data-retention plan.

The [operating model](operating-model.md) assigns these responsibilities. The [final governance chapter](governance-and-business-realignment.md) ties them to decision rights and management philosophy.
