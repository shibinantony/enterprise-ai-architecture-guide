# Enterprise AI as a business transformation and architecture decision

## The investment thesis

Enterprise LLM and agent platforms can make interpretation, synthesis, creation, and interaction practical at a scale that would otherwise require substantial manual effort. The opportunity becomes a business result when the surrounding process changes.

A faster draft has limited value if it waits in the same approval queue. A capable agent cannot resolve an order if the enterprise lacks reliable data or clear authority to offer a remedy. Leadership must redesign the work and deliver the service, with the AI platform as an enabling capability.

Google Cloud is this guide's detailed implementation example. Azure and AWS are compared against the same logical architecture and workload. Different models, regions, deployment modes, and commercial packages are distinguished explicitly.

## The value portfolio

| Opportunity | AI contribution | Enterprise change | Outcome measure |
|---|---|---|---|
| Customer resolution | Interpret requests, assemble facts, explain remedies | Consolidate case ownership and integrate actions | Verified resolution, repeat contacts, time to outcome |
| Employee knowledge | Search and synthesize permitted content | Maintain content and embed access in work | Task completion and search effort |
| Document operations | Extract, classify, compare, prepare documents | Standardize inputs and exceptions | Accepted throughput, error, rework |
| Software engineering | Draft code, explain systems, propose tests | Improve review, testing, and delivery flow | Accepted changes, lead time, escaped defects |
| Operational decisions | Summarize events, query records, compare options | Establish data freshness and decision ownership | Decision latency and subsequent outcome |
| New service experiences | Language, voice, multimodal access | Redesign the journey and support model | Completion or conversion with quality |

These are opportunities to test, not promised benefits. Measure the full process, including work transferred to other teams.

## Choose the right amount of agency

Use a **model call** for a bounded transformation, **retrieval** for enterprise knowledge, and **tools** for live facts or actions. Use a **deterministic workflow** when steps and rules are known. Add **agent reasoning** when variable intent or evidence genuinely changes the next step. Multiple agents need a measurable specialization or parallelism benefit that exceeds their coordination cost.

A disruption service can combine these patterns without becoming autonomous at every step. AI interprets the request and prepares a response; applications supply live state, determine eligible remedies, and commit the transaction. See [value and capabilities](value-and-capabilities.md).

## Day 0: prepare the business

Agree the problem, baseline, future process, data readiness, target experience, team, and economic hypothesis. Decide which steps to eliminate, simplify, standardize, assist, automate, or retain as human judgment.

Identify how roles change. Specialists may investigate fewer routine cases but handle more ambiguity. Knowledge owners need time to maintain content. Supervisors need outcome and exception measures rather than activity counts. Training must prepare users to challenge and correct output.

The output is a service charter with a future workflow, not a collection of demos. See [Day 0](day-0-business-process.md).

## Day 1: deliver a complete service

Build one representative path from user request to verified result, including data, integration, human handoff, and measurement. Evaluate the AI behavior and test access, correctness, concurrency, errors, load, recovery, and usability.

Prepare support and train the pilot group before launch. A local demonstration establishes feasibility; production readiness and adoption require additional evidence. See [Day 1](day-1-build-and-launch.md) and the [architecture](reference-architecture.md).

## Day 2: sustain outcomes

Operate reliability, task quality, cost, data freshness, dependencies, incidents, adoption, and benefit realization. Count unresolved cases and work displaced into exception queues as carefully as successful completions.

Reuse supported tools, data products, evaluation assets, and delivery patterns where their economics justify it. A large agent inventory is not itself a business outcome. See [Day 2](day-2-operate-and-improve.md).

## Economics beyond a token price

Include runtime, retrieval, data preparation, integrations, network, evaluation, observability, human review, support, and change management. Distinguish initial investment from recurring service cost.

```text
Cost per verified outcome = attributable service cost / verified outcomes

Realized period value = attributable business benefit
                        - recurring service cost
                        - agreed allocation of investment and transition cost
```

Benefits can be cash savings, redeployed capacity, incremental margin, improved service, or reduced expected loss. Avoid counting the same minutes saved as both reduced expense and redeployed capacity. Keep unverified benefits as scenarios.

The [pricing chapter](pricing-and-economics.md) provides dated rates and reproducible calculations. A cheaper inference rate may require more calls, context, retries, or review to achieve the same business quality.

## Leadership decisions

| Decision | Evidence required | Deliverable |
|---|---|---|
| Where to invest | Process pain, baseline, feasible intervention, owner | Prioritized opportunity |
| What to change | Future process, journey, data, roles, adoption plan | Service charter |
| What to build or buy | Architecture, equivalent alternatives, economics | Funded delivery plan |
| When to launch | End-to-end quality, trained users, support, fallback | Bounded production service |
| When to expand | Adoption, outcomes, sustainable economics | Wider scope or reusable capability |
| When to stop | Poor value, harmful behavior, unsupported dependencies, inadequate demand | Redesign or retirement |

Governance makes these decisions clear and sustainable. It belongs within business process realignment: people understand responsibilities, technology implements boundaries, and leadership rewards useful outcomes and learning. The [final chapter](governance-and-business-realignment.md) develops that relationship.
