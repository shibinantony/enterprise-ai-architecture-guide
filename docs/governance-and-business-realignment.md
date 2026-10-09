# Governance and business realignment: sustain the redesigned process

Governance earns its place when it helps an enterprise deliver useful outcomes repeatedly, recognize failure and change direction. An agent that accelerates an obsolete handoff can preserve the wrong process. A platform that enforces access perfectly can still deliver little value. Review process purpose, human responsibility and technical behavior together.

This final chapter proposes a practical alignment model, reviewed on **2026-10-09 UTC**. It builds on [Day 0 redesign](day-0-business-process.md), [Day 1 launch](day-1-build-and-launch.md), [Day 2 improvement](day-2-operate-and-improve.md) and the [operating model](operating-model.md). The tiers and review practices below are illustrative; they are not legal classifications or certification criteria.

## Align people, technology and operating philosophy

| Dimension | Alignment question | Evidence in the redesigned service |
| --- | --- | --- |
| People | Who benefits, who decides and who handles failure? | Accountable process owner, informed users, trained reviewers, supported exceptions and an accessible correction route |
| Technology | Can the system perform and verify the permitted work? | Authoritative data, narrow tools, enforced authority, durable transactions, evaluations and recoverable operations |
| Philosophy | What should this organization delegate, and on what grounds? | Explicit purpose, limits on autonomy, a preference for justified simplicity and willingness to stop when evidence contradicts the benefit case |

These dimensions constrain each other. A technically possible action may lack a legitimate business mandate. A proposed human approval may be ineffective because no reviewer has time or sufficient information. A target for maximum automation may discourage useful escalation. Resolve such contradictions in the process design rather than burying them in a prompt.

NIST's AI RMF organizes risk work around Govern, Map, Measure and Manage across the lifecycle. It provides supporting guidance for accountability and stakeholder engagement; this chapter supplies a proposed service-level application, not a complete framework assessment. [NIST AI RMF Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/)

## Define the service mandate before expanding autonomy

Write a concise mandate: intended outcome, eligible work, affected people, permitted data, allowable actions, exclusions, human decision rights and stop conditions. The process owner approves the business purpose; designated authorities approve data access, residual risk and release within their responsibilities.

Consider fictional service recovery. An agent can collect facts and explain an eligible remedy. A domain service determines eligibility and limits. An authorized reviewer decides an exception. The business application commits the remedy and supplies its status. Nobody should infer a completed resolution from a fluent explanation or from an approval that has not yet been executed.

Choose autonomy by activity. Retrieval, drafting, recommendation and execution can have different boundaries within one workflow. Expand a boundary only when outcome quality, authority enforcement, reviewer capacity and recovery evidence support it. A high-confidence answer is not an authorization decision, and a low-risk tool can become consequential through repeated or combined use.

## Classify consequences, then allocate assurance

Evaluate data sensitivity, affected rights, scale, reversibility, timing and downstream effects. A read can expose protected information; a reversible database change can already have triggered an irreversible external consequence. Use the highest credible consequence to determine review depth.

| Illustrative tier | Activity | Starting treatment |
| --- | --- | --- |
| 0: bounded public retrieval | Find approved public information | Source quality, schema checks, basic monitoring and resource limits |
| 1: restricted retrieval | Read a permitted internal record | Authenticated identity, record filtering, minimization and access evidence |
| 2: bounded reversible change | Create a low-impact work item | Current-state validation, idempotency, notification and tested recovery |
| 3: material business action | Commit an obligation, refund or access change | Explicit business authority, aggregate limits, transaction-bound approval where required and commit evidence |
| 4: critical consequence | Support a safety-sensitive or rights-affecting decision | Formal domain assessment, qualified decision authority and validated operating limits; support-only mode as the starting position |

Tier assignment grants no permission. Set monetary, volume, time and approval thresholds from the actual process and risk appetite. Any numbers used in examples are design inputs, not universal safe limits or regulatory requirements. OWASP similarly distinguishes agent action risk from the independent authorization required to execute it. [OWASP agent security guidance](https://cheatsheetseries.owasp.org/cheatsheets/AI_Agent_Security_Cheat_Sheet.html)

## Register capabilities as supported business assets

Registration should make a capability consumable and accountable. For each tool or tool service, record its purpose; business, technical and data owners; supported schema and artifact versions; reachable systems; data and action classifications; permitted callers and records; identity/delegation model; policy and approval rules; evidence contract; support commitments; and retirement triggers.

Add transaction details for mutating tools: preconditions, cumulative limits, idempotency scope, duplicate behavior, uncertain-outcome lookup and repair. Include the consumers that depend on the capability, so changing or revoking it becomes a managed business event. Use the [capability registration template](../templates/capability-registration.md).

Do not confuse presence in a registry with permission to act. A catalog tells teams what a reviewed capability is intended to do; execution services must still check the current request. Reusable skills describe procedures, while deterministic services enforce the rules that cannot depend on model interpretation.

## Put authority where the action occurs

The host proposes an operation. Trusted execution code validates it. The tool/domain service authorizes the caller and target; the system of record checks current state and commits the transaction. Gateways can consolidate common checks, but alternate paths must preserve the same business boundary.

Where human approval is needed, bind it to the actual principal, operation, target, canonical arguments, relevant state, expiry and policy context. Verify and consume it through trusted code. Changing the destination or material parameters requires renewed approval. A model-supplied confirmation flag is not proof. Approval and a downstream commit may span systems, so design idempotency and reconciliation explicitly. [OWASP transaction authorization](https://cheatsheetseries.owasp.org/cheatsheets/Transaction_Authorization_Cheat_Sheet.html)

Retrieved instructions and tool responses remain untrusted data. Filtering cannot establish their safety. Bound subsequent actions independently, constrain egress and preserve only justified evidence. The [security and assurance chapter](security-and-assurance.md) maps threats to preventive, detective and recovery controls and the tests that support them.

## Make release and continuous review evidence-based

Before release, connect each material claim to a control, test, observed result and owner. Test representative work, denied actions, ambiguous cases, malicious retrieved content, changed approvals, stale state, retries and dependencies failing after a possible commit. Verify the user journey and human exception path alongside the software.

The release record identifies the tested model, host, workflow, skill, tool, policy, data configuration and evaluation set. Record approved scope, unresolved limitations, the residual-risk acceptance authority, expiry/review triggers and the person able to stop new actions. Use the [release template](../templates/release-review.md).

During operation, compare outcomes and costs with the accepted baseline. Investigate process drift as well as model drift: new products, changed policies, demand spikes or a different user population may invalidate prior evidence. Pre-deployment testing has limits when conditions differ from deployment; NIST's Generative AI Profile makes that limitation explicit. [NIST AI 600-1, MEASURE 2.5 and Appendix A.1.4](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf)

Suspension stops new actions while preserving investigation and reconciliation. Retirement includes migrating unfinished work, withdrawing identities and tool access, updating consumers and applying retention/deletion decisions. Reopening a retired service requires an explicit decision, not an accidental redeployment.

## Ask director-level questions that lead to decisions

Use these prompts to expose missing decisions and evidence. Assign the unanswered item to an owner; a meeting that repeats the questions without resolving them adds little value.

| Review area | Purposeful questions |
| --- | --- |
| Business | Which verified outcome improves, for which eligible cases? Why is agency preferable to a simpler workflow, and what evidence would stop expansion? |
| Data | Which records and documents are necessary and authoritative? Where are permission filtering, freshness, provenance and permitted processing boundaries enforced? |
| Authority | Under whose identity and delegation does the action occur? Who sets individual and aggregate limits, and which exact transaction requires approval? |
| Integration | Who supports each tool and its compatibility contract? What happens when a dependency fails after an action may already have committed? |
| Security | Can malicious content redirect access or export data? What independent controls constrain credentials, destinations and execution, and how quickly can they be revoked? |
| Quality | Which normal, exceptional and adversarial cases were evaluated? How are severe failures, sample size and uncovered conditions reported rather than hidden in an average? |
| Operations | Can staff connect a request to a verified outcome and repair an incomplete case? Are latency, review queues, cost and incident ownership visible across the service? |
| Governance | Who owns outcomes and accepts residual risk? What triggers reassessment, suspension or retirement, and who has authority to carry out that decision? |

Business approval should consider the [full economic model](pricing-and-economics.md), including integration, shared services, review, support and rework. Hours released become value only when the organization uses them productively or removes the associated expense. Reuse remains a hypothesis to measure, not a benefit guaranteed by adopting MCP or creating more agents.

The enduring asset is a service the enterprise can understand, improve and change responsibly: people know their role, technology enforces its mandate, and investment follows demonstrated process value. Governance preserves that alignment as capabilities and business needs evolve.
