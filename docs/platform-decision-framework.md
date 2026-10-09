# Platform decisions without provider rankings

This chapter proposes an evaluation method. It makes no product feature, market leadership, price, or production-readiness claims. Evaluate an actual service configuration and supported version, with the same workload and acceptance criteria across candidates.

## Choose an approach before a platform

| Approach | Useful when | Cost or constraint to investigate |
|---|---|---|
| Conventional workflow | Steps and decisions are fully specified | Flexibility for genuinely ambiguous requests |
| Agent within an existing application | A clear owner and narrow process already exist | Duplication of shared controls and support |
| Managed agent service | Standard lifecycle and operations meet requirements | Feature maturity, control visibility, service limits, and exit cost |
| Composable runtime and services | Isolation, integration, or control needs are unusual | Engineering effort, operational burden, and fragmented accountability |

MCP may be useful in several approaches. It is not a reason to replace an adequate API integration or force an unnecessary gateway into a simple workflow.

## Apply veto criteria first

Reject a candidate if it cannot satisfy a mandatory requirement. A high average score cannot compensate for a missing legal, contractual, security, or operational condition.

Typical veto criteria are approved processing boundaries, supported identity delegation, enforceable object access, auditable material actions, required availability and recovery, supported deployment lifecycle, acceptable data terms, and a credible revocation mechanism. Have qualified owners determine the actual obligations for the use case; this guide supplies no jurisdiction-specific compliance determination.

## Weighted scorecard

The following weights are illustrative and total 100. Agree weights and disqualifiers before running trials. Retain test evidence and unresolved assumptions with each score.

| Dimension | Weight | Evidence to request |
|---|---:|---|
| Identity, delegation, and object authorization | 20 | Cross-tenant denial, token audience checks, delegated scope, timely revocation |
| Transaction and policy integrity | 20 | Limits, independent approval, idempotency, concurrency, state validation |
| Data controls and isolation | 15 | Pre-retrieval filters, egress enforcement, retention, tenant isolation |
| Evaluation and operational assurance | 15 | Reproducible evaluations, trace correlation, incident exercises, rollback |
| Integration and behavior portability | 10 | Same contract and denial cases across independently implemented hosts |
| Full service economics | 10 | Comparable cost per verified outcome, including review and control costs |
| Delivery and support fit | 10 | Team capability, supported features, escalation path, upgrade commitments |

Use scores from 0 to 5: **0** unavailable; **1** assertion only; **2** partial demonstration; **3** acceptance test passed with documented limits; **4** relevant operational evidence plus tests; **5** sustained evidence at the required scale and conditions. Unsupported or preview capabilities cannot receive a production-evidence score merely because a demo succeeds.

```text
Weighted score out of 100 = sum(weight * score / 5)
```

Track evidence confidence separately as low, medium, or high. A score without evidence is provisional. Re-run sensitivity analysis with different weights; if small changes reverse the result, the decision rests on business priorities or missing evidence and should say so.

Use the [evaluation template](../templates/platform-evaluation.md) to preserve the actual decision.

## A common evaluation workload

Choose a synthetic process representative of the intended production pattern. Include a valid request, ambiguity requiring clarification, unauthorized object access, malicious retrieved instructions, stale state, duplicate invocation, expired approval, policy outage, downstream timeout after commit, and tool revocation.

Run the same frozen cases, input distribution, concurrency, data scope, and cost-accounting window. Record versions and configurations. Use enough repeated trials to characterize variability; a single successful run says little about probabilistic tool selection.

Separate five measurements:

1. Did the workflow reach the independently accepted business outcome?
2. Did every protected action obey the declared authority and transaction controls?
3. What was the end-to-end latency, including queues and human review?
4. What did each accepted outcome cost, including failures and rework?
5. Could operations detect, explain, stop, and recover the observed failure?

Report counts and uncertainty alongside percentages. Distinguish a control test that was not run from one that passed. Keep model-generated quality judgments separate from authoritative transaction checks and independent human acceptance.

## Test the exit strategy

Protocol compatibility is one part of portability. The [MCP foundations](mcp-foundations.md) chapter distinguishes protocol, behavior, authority, operations, and economics.

A practical exit exercise should export tool contracts, policy definitions, workflow configuration, evaluation datasets, and permissible evidence. Reconstruct the bounded workflow in another host and deployment environment. Re-run denial, recovery, and operating tests. Measure the changes needed for identity, network controls, state, telemetry, and support.

Document assets that cannot be exported, contractual restrictions, service-specific behavior, retraining needs, and migration effort. Avoid an unsupported claim of full portability, and avoid weakening essential controls merely to make every implementation identical.

## Build, buy, or reuse

Prefer reuse when the existing capability has an accountable owner, a supported contract, and controls that match the proposed use. Buying may reduce operational work while retaining integration and assurance obligations. Building may satisfy uncommon requirements but creates long-term support, patching, and recovery responsibilities.

The final decision record should name the rejected alternatives, unresolved dependencies, residual risks, owner, review date, and conditions that would trigger reconsideration. Record the reason a choice fits the enterprise's workload; do not substitute a universal platform ranking for that explanation.
