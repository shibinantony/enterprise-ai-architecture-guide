# A 90-day adoption plan with decision gates

This is an illustrative planning sequence, not a delivery commitment. Procurement, data access, control validation, and domain obligations can extend the schedule. Failure to meet a gate should change scope or timing, rather than lower the gate.

## Days 1–15: define the service

Select a frequent, bounded process with a business owner and a verifiable outcome. Compare conventional automation with an agent-assisted approach. Measure case volumes, outcomes, exceptions, handling effort, and downstream rework before introducing automation.

Complete [use-case intake](../templates/use-case-intake.md). Identify authoritative systems, permitted data, intended users, action limits, consequence severity, and an initial cost envelope.

**Gate:** the sponsor accepts the process baseline and outcome definition; architecture confirms that the proposed agent role has a credible advantage; the control owners agree on the initial risk treatment.

**Stop or reshape if:** authority is unclear, required data cannot be used, outcomes cannot be verified, or a simpler workflow meets the need at lower cost and risk.

## Days 16–30: establish contracts and offline evidence

Define narrow tool contracts and an initial capability register. Draw trust boundaries. Implement policy decisions independently of model instructions. Build an evaluation set covering normal, ambiguous, unauthorized, adversarial, and failure cases.

Use synthetic data first. The [service-recovery example](../examples/service-recovery/README.md) demonstrates a small local policy boundary; actual integrations need identity, state, approval, and transaction tests that the example does not supply.

**Gate:** required control cases pass in the intended test environment; the tool owner accepts the contract, versioning strategy, support obligations, and data scope.

**Stop or reshape if:** the design requires broad credentials or unbounded execution that the team cannot constrain and support.

## Days 31–45: run a restricted pilot

Begin with restricted retrieval and draft recommendations, or shadow decisions where appropriate. Verify that shadow mode cannot reach mutating endpoints and still respects approved data boundaries. Compare outcomes against the baseline using independent review.

Measure corrections, abstentions, review burden, latency, and cost. Inspect where users over-trust fluent answers or cannot understand an exception. Tune the procedure and interface; changing model settings alone may not solve the process issue.

**Gate:** the business owner accepts task quality and user behavior; the evaluation owner documents coverage and remaining uncertainty.

## Days 46–60: add bounded actions

Enable only the smallest justified action set. Enforce identity and object scope, verified approval where required, aggregate limits, concurrency controls, and idempotency at the execution boundary. Reconcile every action to a committed business result.

Exercise denial, stale state, duplicate retries, timeouts after possible commit, revocation, and recovery. Train reviewers on the authority they hold and how to reject or escalate requests.

**Gate:** security, domain, and operations owners accept the evidence for the declared action limits; the designated risk authority accepts residual risk, and the service owner accepts operational responsibilities. The release authority records the permitted scope.

## Days 61–75: demonstrate operational readiness

Run incident and recovery exercises with the actual support team. Test the mechanism for stopping new actions and accounting for in-flight work. Set service indicators for verified outcomes, exceptions, latency, cost, and recovery. Validate retention and restricted evidence access.

Complete the [release review](../templates/release-review.md) and document fallback ownership. Demonstrate model, tool, workflow, and policy upgrade evaluation rather than assuming compatibility.

**Gate:** the designated release authority approves constrained production or records specific blocking conditions.

## Days 76–90: decide whether to expand

Review actual operating costs and independently accepted outcomes. Compare against the original baseline and a simpler alternative. Separate observed benefits from projected benefits and report the sample size and observation period.

Identify shared capabilities with a funded owner and a credible second consumer. Standardize these assets selectively. Increase autonomy only after evaluating the new action scope, failure consequences, and support load.

**Decision:** expand, continue bounded observation, redesign, or retire. Record the conditions for the next review.

## Minimum artifacts by the end

| Artifact | Accountable owner |
|---|---|
| Business baseline, outcome definition, and economic assessment | Business owner |
| Reference architecture and decision records | Architecture owner |
| Capability register and supported tool contracts | Tool owners |
| Threat model, evaluation cases, and release evidence | Control and evaluation owners |
| Incident, revocation, reconciliation, and retirement procedures | Operations owner |
| Accepted residual risks and production scope | Service release authority |

The operating roles may be combined in a small team, but high-consequence approvals require the independence and separation of duties defined by the organization's own controls.
