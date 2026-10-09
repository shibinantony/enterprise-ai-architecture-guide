# Platform selection: enterprise fit, outcomes, and economics

Compare the platform against the redesigned business process. This framework turns the [cloud comparison](cross-cloud-comparison.md) and [pricing analysis](pricing-and-economics.md) into an enterprise decision. It does not assign a universal provider ranking.

## Establish enterprise context

Record the existing identity plane, systems of record, data platform, regulatory and contractual requirements, developer capability, operational maturity, distribution channels, model/framework choice, sovereignty/network constraints, and commercial commitments.

These dependencies determine integration effort and operating fit. A nominally cheaper model endpoint can become the more expensive service if it requires data movement, new skills, duplicated operations, or an additional user channel.

## Compare the same service boundary

Compare model APIs with model APIs, custom-code runtimes with custom-code runtimes, retrieval services with retrieval services, and packaged workplace products with similarly scoped products. State what each price or feature includes.

Use two trials: a controlled trial with the same model and workload where supported, and a native-optimized trial where each cloud uses its best-fit design. The former isolates some platform differences; the latter tests achievable process value. Neither eliminates the need to evaluate actual task quality and operating behavior.

## Mandatory conditions

Check required processing locations, data terms, identity, object access, transaction integrity, service support, recovery, revocation, and relevant obligations before scoring. A high average score cannot compensate for a mandatory condition that is not met.

Distinguish unavailable, untested, preview, and accepted with limitations. Have qualified enterprise owners determine actual requirements; this guide is not a compliance determination.

## Weighted decision model

Example weights total 100. Agree them before trials and adjust to the business context.

| Dimension | Weight | Evidence |
|---|---:|---|
| Business task quality and experience | 25 | Verified outcomes, handoff quality, user acceptance |
| Data and application fit | 20 | Existing sources, live integrations, freshness, identity compatibility |
| Full service economics | 20 | Cost per verified outcome including human and operating effort |
| Reliability and operational fit | 15 | Failure recovery, telemetry, capacity, support, regional availability |
| Delivery and team capability | 10 | Skills, development flow, release process, maintainability |
| Portability and commercial flexibility | 10 | Exit exercise, contract dependencies, migration effort |

Mandatory security and business controls remain gates rather than points that can be traded away.

Score 0–5: 0 unavailable; 1 assertion only; 2 partial demonstration; 3 acceptance test passed with limits; 4 relevant operating evidence plus tests; 5 sustained evidence at required conditions. Record confidence and evidence with the score.

```text
Weighted score out of 100 = sum(weight * score / 5)
```

Recalculate under plausible alternative weights. If small changes reverse the outcome, make the dependency on business priorities or missing evidence explicit.

## Common trial workload

Use the same eligible case population, outcome criteria, knowledge corpus, tool contracts, load profile, observation window, and cost boundary. Include normal cases, ambiguity, missing/stale data, malicious retrieved instructions, unauthorized objects, duplicates, expired approvals, dependency failures, and timeout after possible commit.

Measure outcome quality, end-to-end latency, human review, full cost, and ability to diagnose and recover. Record tokens and tool calls across every loop rather than charging one nominal prompt per case. Report counts and uncertainty as well as rates.

## Portability and exit

MCP supports protocol interoperability; identity, deployment, networking, data, security, telemetry, and distribution remain platform-dependent. Even the protocol layer requires compatible versions, transports, schemas, and extensions.

Recreate a bounded workflow on a second host using supported contracts. Re-run task, denial, failure, and recovery cases. Measure the work to replace identity, state, observability, and deployment dependencies. Document contractual restrictions and non-exportable assets.

Protocol connection success alone does not prove equivalent operation. Avoid weakening a necessary capability solely to make implementations identical.

## Final decision record

Use the [platform template](../templates/platform-evaluation.md). Record selected scope and configuration, mandatory gate results, common trial evidence, full cost, rejected alternatives, residual limitations, owner, review date, and reconsideration triggers.

Choose the cloud and service configuration that best supports the enterprise's process and operating context. Explain the trade-off rather than declaring a permanent winner.
