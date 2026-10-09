# Day 1: build, integrate, evaluate, and launch

Day 1 turns the Day 0 process design into a working service. It includes software engineering, data engineering, application integration, user preparation, and operational readiness. The aim is an end-to-end slice that a real user can complete and the business can evaluate.

## 1. Establish the implementation contract

Translate the future process into acceptance cases, input/output contracts, workload expectations, service objectives, exception routes, and outcome measures. Freeze an initial evaluation set before prompt tuning so the team can distinguish improvement from fitting familiar examples.

Choose the model, data pattern, runtime, integration design, and channel from the [architecture](reference-architecture.md). Record why each component is required. Use the [GCP chapter](gcp-enterprise-architecture.md) for the detailed mapping and the [cloud comparison](cross-cloud-comparison.md) to challenge the choice.

## 2. Prepare environments and data

Provision development, evaluation, and production configurations with separate identities, approved networking, budgets, quotas, secret access, and deployment permissions. Use infrastructure as code where supported. Pin dependencies and record supported model, SDK, protocol, and tool versions.

Implement document ingestion, access metadata, quality checks, indexing, and freshness. Create supported live-data APIs rather than depending on manual exports. Keep representative evaluation data appropriately isolated and minimized.

## 3. Build the smallest complete process

For service recovery, the first slice should cover authenticated intake, intent interpretation, permitted evidence and current order retrieval, eligible options, a specialist handoff when needed, a confirmed result, and user communication.

Begin with draft recommendations or restricted reads if transaction integration is not ready. Clearly label that scope; do not describe a draft-only prototype as an automated resolution service.

Use typed domain services for calculations and business actions. Maintain explicit workflow state and stable operation identifiers. Build the failure path at the same time as the successful path.

## 4. Evaluate each layer and the full task

| Test layer | Representative questions |
|---|---|
| Interpretation | Is the intent correct, and does missing information trigger clarification? |
| Retrieval | Is evidence relevant, permitted, current, and complete enough? |
| Response | Is the output faithful, useful, and appropriately uncertain? |
| Tool use | Are operation, arguments, target record, and sequence correct? |
| Transaction | Are state, authorization, cumulative limits, idempotency, and concurrency correct? |
| Process | Does the case reach the accepted outcome without hidden rework? |
| Experience | Can the user understand status, correct mistakes, and complete an exception? |
| Operations | Can the team detect, diagnose, stop, reconcile, and recover failures? |
| Economics | What are the full cost and latency per verified outcome? |

Combine deterministic checks, domain-expert review, appropriately validated model-assisted scoring, load tests, and failure injection. A model judge is not an authoritative check of whether a transaction committed. Report case counts, variation, exclusions, and limitations.

## 5. Build the delivery pipeline

Version application code, prompt/procedure configuration, tools, data/index configuration, policy, and evaluation assets. Run unit and contract checks, representative task evaluations, and required security tests before promotion. Compare cost and quality regressions together.

Deploy through a supported progressive-release mechanism or an application-level routing strategy. Verify provider-specific rollout behavior; cloud runtimes do not all implement identical revision or traffic-splitting semantics. Have a tested rollback and a method to reconcile in-flight work.

## 6. Prepare users, support, and launch

Co-design the pilot with frontline staff. Train on normal cases, uncertainty, correction, and escalation. Staff the review queue and support path. Provide a clear explanation of what the service does and how users can challenge its outcome.

Run user acceptance against the future process, not just the chat interface. Rehearse model downtime, stale knowledge, tool failure, a possibly committed transaction with a lost response, and reviewer backlog.

## Launch decision

Use the [release review](../templates/release-review.md) to record process scope, outcome quality, data readiness, user training, support ownership, operating cost, unresolved issues, and required controls. The designated business, release, and risk authorities make their respective decisions.

Launch to a restricted population with clear success and stop conditions. Preserve the baseline and report the actual pilot result. Move into [Day 2](day-2-operate-and-improve.md) immediately when users depend on the service.
