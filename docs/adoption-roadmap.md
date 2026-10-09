# Adoption roadmap: Day 0, Day 1, and Day 2

Day 0, Day 1, and Day 2 describe lifecycle stages. They overlap: operating and adoption work starts during design, and process redesign continues after launch. The schedule below is illustrative, not a delivery commitment.

## Stage map

| Stage | Main question | Accountable outcome |
|---|---|---|
| [Day 0](day-0-business-process.md): before adoption | What should change, and why? | A funded future process, baseline, prepared data, team, and value hypothesis |
| [Day 1](day-1-build-and-launch.md): implementation | Can we deliver the complete service? | Integrated, evaluated service with trained users and launch readiness |
| [Day 2](day-2-operate-and-improve.md): sustained operation | Is it delivering value reliably? | Verified outcomes, adoption, viable economics, and continuous improvement |

## The first working week

| Day | Work | Concrete output |
|---|---|---|
| 1 | Sponsor, process owner, frontline, and architecture discovery | Outcome, scope, affected users, current pain |
| 2 | Map current workflow, handoffs, systems, queues, exceptions | Baseline plan and current-state process |
| 3 | Eliminate, simplify, standardize, assist, and automate decisions | Future workflow and changed responsibilities |
| 4 | Assess knowledge, live data, APIs, identity, network, and channel | Readiness gaps and initial architecture alternatives |
| 5 | Estimate value and cost range; set acceptance and stop criteria | Service charter and a decision to fund, reshape, or stop |

These are workshop milestones. Missing access, unresolved ownership, or unavailable evidence can require additional work before the next stage.

## Illustrative 90-day delivery sequence

| Period | Work across business and technology | Exit evidence |
|---|---|---|
| Days 1–15 | Process redesign, baseline, roles, data assessment, platform shortlist | Sponsor accepts the future process and value hypothesis |
| Days 16–30 | Data and tool contracts, vertical slice, model/retrieval baseline, evaluation set, deployment foundations | End-to-end feasibility and owned readiness gaps |
| Days 31–45 | Integrate in user workflow, run restricted pilot, train users, measure review and rework | Accepted task quality and usable handoff; honest cost estimate |
| Days 46–60 | Add justified bounded actions, transaction/recovery tests, operational telemetry | Application integrity and support evidence for the declared scope |
| Days 61–75 | Load, failure and recovery exercises; rollout/rollback; staffing and adoption readiness | Release authority approves constrained production |
| Days 76–90 | Observe outcomes, adoption and costs; improve the process; assess reusable assets | Decision to expand, continue observation, redesign, or retire |

If a required gate fails, change scope or timing. Do not lower the gate to preserve a presentation date. Production observations must be long enough to cover relevant process cycles; a 90-day calendar alone does not establish value.

## Parallel workstreams

- **Business and change:** process owner, product decisions, baseline, user research, role redesign, training, adoption.
- **Data and integration:** authoritative sources, quality, permissions, retrieval, APIs, transactions.
- **AI and application:** model selection, orchestration, experience, evaluations, handoffs.
- **Platform and operations:** environments, deployment, identity, network, capacity, telemetry, support.
- **Economics and assurance:** price evidence, cost attribution, benefit realization, decision authority, required control tests.

## Leadership review

The sponsor owns investment and outcome. The process owner owns the future workflow. Technical and data owners accept their service responsibilities. The designated risk authority accepts residual risk; the release authority decides production scope.

Use the [process canvas](../templates/process-redesign-canvas.md), [release review](../templates/release-review.md), and [value scorecard](../templates/value-scorecard.md). Governance supports these business decisions throughout the lifecycle and is explained in the [final chapter](governance-and-business-realignment.md).
