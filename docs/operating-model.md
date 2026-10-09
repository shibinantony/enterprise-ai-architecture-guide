# Operating model: organize people and capabilities around value

Enterprise AI succeeds when a redesigned process produces better outcomes and somebody owns the complete service. The product team cannot stop at a convincing demonstration, the platform team cannot stop at an available endpoint, and the business owner cannot stop at approving a budget. Delivery and operations must share a definition of completed work.

This is a proposed operating model, reviewed on **2026-10-09 UTC**. It connects [Day 0 process redesign](day-0-business-process.md), [Day 1 implementation](day-1-build-and-launch.md) and [Day 2 improvement](day-2-operate-and-improve.md). Adapt the team structure to the organization; retain clear decision rights and evidence of value.

## Build a team that owns the process

Organize around a product or process outcome, supported by reusable platform and domain capabilities. Assign a named accountable owner for every deployed service. Functional specialists can contribute across teams, but a user should not have to navigate the organizational chart to resolve a failed case.

| Team or role | Owns | Working agreement |
| --- | --- | --- |
| Business/process owner | Outcome definition, eligible cases, decision policy and benefit realization | Decides which work to eliminate, simplify, assist or automate; funds exception handling |
| Product and process team | End-to-end journey, delivery backlog, acceptance and adoption | Includes frontline specialists; prioritizes useful completion over agent activity |
| Domain capability/data owners | Authoritative records, supported APIs, content quality and transaction rules | Publish freshness, permission, compatibility and recovery contracts |
| Platform team | Reusable identity, runtime, integration, evaluation and telemetry services | Offers supported patterns and self-service paths with clear costs and limits |
| Experience and change leads | Usability, communications, training and role transition | Test whether users understand outcomes, uncertainty and human handoffs |
| Technical service/operations owner | Reliability, dependency health, support, incidents and reconciliation | Accepts the service before launch and maintains operational readiness |
| Evaluation and assurance specialists | Measurement design, independent challenge and control evidence | Assess the real workload and expose uncertainty; do not manufacture a pass |

The designated risk authority accepts residual risk; the release authority approves a deployment within defined scope. A service owner may hold either role only where that authority is explicitly assigned. Smaller teams can combine roles while preserving the independence their highest-consequence decisions require. NIST supports documented responsibilities, executive accountability and differentiated human oversight; this particular team design is our application of that guidance. [NIST AI RMF Core, GOVERN 2–3](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/)

## Treat changes to work as part of delivery

Ask what each role does after the intervention. In service recovery, specialists may spend less time copying order facts and more time resolving disputed evidence, unusual remedies and dissatisfied users. That change requires a usable case view, explicit authority and time to learn. Renaming a manual step as an approval can leave the original investigation work intact.

Design the human handoff as a product feature. It should present current state, relevant evidence, proposed options, unresolved questions and the decision required. Show whether an action is proposed, committed or awaiting reconciliation. Give the reviewer a practical way to disagree, correct a fact, request more evidence or route the case.

Involve frontline staff in process mapping and pilots. Track the work that moves elsewhere: extra review, support tickets, knowledge maintenance and exception management. Do not count a transfer of effort from one team to another as a saving. Plan how released capacity will be redeployed before reporting benefits.

## Develop skills and a learning culture

Different roles need different competence. Process specialists need to challenge evidence and interpret uncertainty. Product teams need to distinguish a good answer from a completed outcome. Engineers need retrieval, integration, evaluation and failure-recovery skills. Operations staff need to diagnose the chain from request to model, tool, workflow and business record.

Use realistic exercises: a stale policy, an ambiguous request, an unavailable system, a rejected recommendation and a timeout after a possible commit. Assess whether the person can complete the exception, not whether they attended a training session. Maintain ordinary operating procedures alongside reusable agent skills; a skill file cannot replace domain knowledge or a supported application contract.

Create a culture in which reporting a failed case improves the service rather than undermines a success narrative. Reward useful corrections, simplification and retirement of ineffective features. Avoid incentives based only on adoption, autonomous completion or tool-call volume. An appropriate escalation can be the best business result.

## Join delivery ownership to operational ownership

The first delivery slice should include a supported failure path and the person responsible for it. Before launch, agree service objectives, dependency owners, review capacity, budgets, escalation rules and reconciliation procedures. Operations should participate in design and testing, rather than inherit a finished application with an incomplete runbook.

Maintain one improvement backlog across process, data, experience and technology. A slow resolution may come from an approval queue or a missing source record; a different model will not necessarily fix it. Classify recurring failures by root cause and fund the responsible team to address them.

Manage reusable components as services. Tool consumers need notice of breaking changes, a supported version window and an escalation route. Model, prompt, skill, policy and retrieval changes need impact assessment proportional to the behavior they can change. Use the [security and assurance evidence](security-and-assurance.md) when the change affects access or business action.

## Give each review a decision

The following cadence is illustrative; combine it with the [Day 2 operating practices](day-2-operate-and-improve.md).

| Cadence | Primary decision | Accountable participant |
| --- | --- | --- |
| During live operation | Contain a failure, restore service or route unfinished work | On-call/service operations |
| Daily in a pilot | Adjust reviewer capacity, fix user friction or pause a failing case class | Product and process leads |
| Weekly | Prioritize recurring outcome, data and integration problems | Cross-functional service team |
| Monthly | Confirm benefits, costs and actual capacity redeployment; change investment | Business owner with finance and operations |
| At portfolio review | Reuse, expand, consolidate or retire capabilities | Business and platform leadership |
| On material change | Determine which evaluations and approvals must be renewed | Relevant owners and release authority |

Every review ends with an action, owner and date or an explicit decision to continue observation. A dashboard without a decision path is another reporting workload.

## Measure value with stable denominators

Choose the cohort, eligibility rules, follow-up window and baseline before the pilot. Report counts, uncertainty, unresolved cases and changes in case mix. These definitions are proposed measures, not performance targets or claimed results.

| Measure | Definition |
| --- | --- |
| Verified outcome rate | Eligible cases meeting the agreed business outcome without disqualifying rework in the follow-up window / all eligible cases entering the cohort. Report how many have completed that window. |
| Adoption for eligible work | Eligible cases actually handled through the new service / all cases eligible to use it. Report abandonment separately; logins are not completed work. |
| Exception rate | Eligible cases requiring an unplanned human decision, correction or recovery / all eligible cases. Separate these from planned approvals and report exception reasons. |
| Human effort per eligible case | Total execution, review, exception and attributable support minutes / all eligible cases. Include failed attempts and work shifted to other teams. |
| Time to verified resolution | Median and 95th percentile from intake to accepted outcome, including queues. Report unresolved cases and their age to expose completion-only bias. |
| Cost per verified outcome | Total attributable operating cost for the cohort / verified outcomes. Include unsuccessful work, inference, tools, retrieval, infrastructure, telemetry, review and allocated shared services; report build cost separately. |
| Net capacity released | Human hours required by a comparable baseline cohort minus actual human hours for the new cohort, adjusted for volume and complexity. Distinguish available time, redeployed time and eliminated expense. |
| Recovery effectiveness | Cases requiring recovery that reach the approved state within the recovery target / all cases requiring recovery. Keep unresolved and unrecoverable cases in the denominator. |
| Capability reuse | Newly released workflows using an existing supported domain capability without a new domain integration / all newly released workflows. Report adapter, assurance and support effort alongside the ratio. |

Segment results where aggregate averages could hide difficult cases or affected user groups. Use a matched or concurrent baseline where feasible. If a denominator is zero, report the measure as not applicable rather than zero cost or perfect quality. Use [pricing and economics](pricing-and-economics.md) to connect these measures to an explicit service-cost model.

## Test the Agent Factory economic hypothesis

An *Agent Factory* is a repeatable delivery and operating approach: common intake, supported capabilities, reusable procedures, evaluation assets and deployment patterns. Its economic hypothesis is that successive workflows require less incremental effort because they reuse approved foundations.

Test that hypothesis. Record lead time, integration effort, assurance effort and support cost for each additional workflow. Compare with a credible standalone approach, accounting for shared-platform build and maintenance. Reuse can fail economically when coordination, generic abstraction or incompatible requirements cost more than the duplication avoided.

Start with the foundations required by a real workflow and a credible next consumer. Fund owners for shared assets; do not build an unfunded catalog that consumers cannot rely on. Standardize proven contracts and recurring needs, while allowing a simpler local solution when shared infrastructure adds little value.

## Keep transformation and stewardship connected

Continue the service because verified outcomes justify its cost and accepted risk, not because it has already consumed investment. Narrow scope when exceptions exceed support capacity. Retire it when the process changes, the benefit disappears or dependencies can no longer be supported, including migration of unfinished work and withdrawal of access.

The final [governance and business realignment chapter](governance-and-business-realignment.md) brings people, technology and operating philosophy together so that authority and evidence support the redesigned process throughout its life.
