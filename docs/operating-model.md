# Operating model: govern a service, measure an outcome

An enterprise agent should enter the portfolio as an accountable service with a defined purpose, permitted authority, operating budget and exit path. A reusable tool catalog is valuable only when its services remain supported, observable and fit for the workflows that consume them.

**Status:** proposed operating model, informed by the public sources linked below and reviewed on **2026-10-09 UTC**. Roles, tiers, gates and measures are design recommendations. They are not regulatory classifications, external certification criteria or proof of compliance.

## Start with a decision worth improving

Before selecting a platform, document the process problem, affected people, existing performance, cost of an incorrect action and available recovery. Compare an agent with a conventional workflow, search interface or improved API. Use agency where variable interpretation helps and where the action boundary can be controlled.

A service charter should state:

- The outcome and eligible case population, including explicit exclusions.
- Permitted data, tools, targets, action limits and required approvals.
- The accountable business owner and technical service owner.
- Success, suspension and retirement criteria agreed before the pilot.
- The operational fallback, human review capacity and escalation route.

NIST organizes AI risk work around Govern, Map, Measure and Manage, with governance operating throughout the lifecycle. This guide applies that structure to an agent service; it does not reproduce or claim a complete NIST assessment. [NIST AI RMF Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/)

## Make decision rights explicit

One person holds each accountable role for a service; several teams may deliver the work. Higher-impact services need appropriate separation between implementation, risk acceptance and release approval.

| Decision | Accountable role | Required contribution or evidence |
| --- | --- | --- |
| Whether the outcome justifies investment | Business service owner | Baseline, affected-user needs, benefit hypothesis and cost ceiling |
| What the agent may access or change | Business process owner | Authority matrix, policy limits and data-owner concurrence |
| How the capability is engineered and supported | Technical service owner | Architecture, dependencies, service objectives and support coverage |
| Whether a tool contract is fit for shared use | Domain capability owner | Schema, authorization, version support, invariants and recovery contract |
| Whether residual risk is acceptable | Designated risk authority | Independent challenge, open findings, compensating controls and expiry |
| Whether a release enters or expands production | Release authority | Tested version manifest, approved scope and rollback readiness |
| Whether execution must stop during an incident | Incident commander or delegated on-call owner | Tested suspension access, evidence preservation and communication plan |

The business owner remains accountable for the service outcome after approval. Human reviewers need authority, time and sufficient evidence; placing a person in an overloaded queue does not establish effective oversight.

## Use risk tiers to allocate assurance effort

These tiers are illustrative. Classification depends on impact, data sensitivity, scale, reversibility, affected rights and operating context. A read operation can be high impact when it exposes protected information; an apparently reversible action can have irreversible downstream effects.

| Tier | Illustrative activity | Starting assurance posture |
| --- | --- | --- |
| 0: bounded public retrieval | Find an approved public product document | Provenance, input/output checks and resource limits |
| 1: restricted retrieval | Read a permitted internal service record | Identity, record-level authorization, minimization and access evidence |
| 2: bounded reversible change | Create a low-impact internal work item | Business validation, idempotency, notification and demonstrated recovery |
| 3: material action | Change access or commit a significant obligation | Transaction-specific authority, enforced limits, independent review where required and commit evidence |
| 4: critical consequence | Support a safety-sensitive or rights-affecting decision | Formal domain assessment; qualified decision authority; validated operating limits; support-only mode as the starting position |

The highest credible consequence governs review depth. Tiers neither grant authority nor prescribe universal monetary thresholds. Approval and execution controls should be implemented outside model interpretation. [OWASP AI agent security guidance](https://cheatsheetseries.owasp.org/cheatsheets/AI_Agent_Security_Cheat_Sheet.html)

## Release through evidence gates

| Gate | Evidence required | Decision |
| --- | --- | --- |
| 1. Qualify | Charter, baseline, alternative approaches, eligible population and impact assessment | Fund discovery or stop |
| 2. Bound | Data flow, threat model, tool owners, action policy, recovery and identity design | Authorize an isolated prototype |
| 3. Validate | Scenario results, security-control tests, error analysis, cost estimate and unresolved risks | Permit a limited pilot or remediate |
| 4. Pilot | Restricted population, staffed review, production telemetry, incident drill and measured outcomes | Expand, adjust or suspend |
| 5. Operate | Service objectives, recurring review, change controls, support and budget ownership | Continue within approved limits |
| 6. Retire | Dependency migration, access revocation, data disposition and closure evidence | Remove from service |

Each gate produces an explicit decision, named approver, approved scope, expiry or next review, and links to controlled evidence. Incomplete evidence is visible rather than replaced by a narrative assurance claim. Evaluation results should match the intended deployment context; narrow demonstrations cannot establish general reliability. [NIST Generative AI Profile, MEASURE 2.5 and Appendix A.1.4](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf)

A model, tool, policy, skill, data-source or permission change triggers impact assessment. Record which evidence remains applicable and which tests must be repeated. A minor version label is not evidence of low risk. Emergency changes require a bounded exception, accountable approver and retrospective review.

## Measure outcomes with defined denominators

Set targets before the pilot and publish the cohort, time window, exclusions and data source with every result. A proposed monthly scorecard follows. These are measurement definitions, not claimed benchmarks or promised returns.

| Measure | Definition and interpretation |
| --- | --- |
| Verified outcome rate | Eligible cases reaching the predefined business outcome without disqualifying rework during the follow-up window / all eligible cases entering the measured cohort. Report pending cases and window maturity separately. |
| Autonomous resolution rate | Eligible cases completed correctly without human execution or review / all eligible cases in the cohort. Also report the reviewed-case share so automation does not hide oversight work. |
| Exception rate | Eligible cases requiring unplanned manual intervention, escalation, or recovery / all eligible cases in the cohort. Count each case once and report planned approval reviews separately. |
| Material unauthorized-action rate | Confirmed unauthorized committed actions / all committed material actions. Report attempted-but-denied actions separately and count incidents even when later reversed. |
| Recovery success | Failed or incorrect actions restored to the approved state within the recovery target / all actions requiring recovery. Include unresolved and unrecoverable cases in the denominator. |
| Time to verified resolution | Median and 95th percentile from eligible-case intake to verified outcome, including queue and review time. Report unresolved cases and their age to prevent completion-only bias. |
| Cost per verified outcome | Total attributable operating cost for the cohort / verified outcomes in that cohort. Include unsuccessful attempts, inference, tools, runtime, monitoring, human review and allocated shared-service cost. Report one-time build cost separately. |
| Net capacity released | Baseline human hours for a comparable cohort minus actual execution, review, exception and support hours. Show volume and case-mix adjustments; released time is not automatically cash savings. |
| Capability reuse | New workflows using an existing approved capability without a new domain integration / all new workflows released in the period. Report adapter and assurance effort alongside the ratio. |

For rates, report numerator and denominator; for small samples, include uncertainty and avoid precise-looking rankings. Segment outcomes by relevant case complexity and risk. Compare against a concurrent or carefully matched baseline where feasible, because changing demand can otherwise look like an automation benefit.

Use cost and quality together. A cheaper completion that increases rework, delays a person or causes an unauthorized action is not a successful outcome. Include unresolved complaints and sampled user feedback in portfolio review.

## Fund reusable capabilities without obscuring their cost

Maintain a domain-owned capability catalog with consumer list, service objectives, policy contract, supported versions and deprecation dates. Fund shared identity, assurance, evaluation and observability deliberately. Allocate shared-service cost transparently so a low apparent per-call price does not conceal central operating effort.

Expand only when measured benefits exceed incremental delivery, oversight and operating costs within accepted risk. Tool count and agent count are inventory measures, not benefit measures.

## Suspend and retire deliberately

Define triggers such as unsupported dependencies, repeated control failures, deteriorating outcomes or an uneconomic cost base. Suspension should stop new actions while preserving reconciliation and incident access. Retirement includes notifying consumers, migrating or cancelling queued work, reconciling pending transactions, revoking credentials, removing discovery entries and applying the approved retention or deletion schedule.

Keep closure evidence and update the capability inventory so retired versions cannot be redeployed accidentally. Safe decommissioning and system inventory are explicit parts of the NIST governance core. [NIST AI RMF Core, GOVERN 1.6–1.7](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/)

Use [security and assurance](security-and-assurance.md) to turn the charter's boundaries into controls and acceptance evidence. See the [source review notes](../research/assurance-source-notes.md) for research scope and version caveats.
