# Value and capabilities: choosing the right amount of AI

Start with the part of the process that needs better interpretation, knowledge access, creation, decision support, or coordination. The architecture follows from that need. An agent platform is useful when its capabilities address a real constraint.

This chapter proposes a capability and value model. Concrete product features and primary sources are in the [GCP deep dive](gcp-enterprise-architecture.md) and [cross-cloud comparison](cross-cloud-comparison.md).

## Enterprise capability map

| Capability | Work supported | Dependencies | Acceptance test |
|---|---|---|---|
| Language understanding | Interpret requests, classify issues, identify missing information | Representative terminology, examples, taxonomy | Correct interpretation across ordinary and ambiguous cases |
| Generation and summarization | Prepare correspondence, briefs, reports, candidate code | Relevant context and an output contract | Faithful output accepted for the intended task |
| Enterprise retrieval | Answer questions from permitted knowledge | Content ownership, access metadata, indexing, freshness | Relevant evidence and an answer supported by that evidence |
| Structured-data interaction | Investigate order, inventory, or service state | Authoritative queries and APIs | Correct records and calculations within the permitted scope |
| Multimodal understanding | Interpret documents, diagrams, images, voice, or video where supported | Modality-specific preparation and model support | Correct task outcome on representative input quality |
| Tool use | Read live facts or initiate application operations | Typed contracts, identity, integration, error semantics | Correct operation and arguments with a verified result |
| Adaptive orchestration | Choose the next step in an ambiguous case | Bounded tools, process state, completion criteria | Completion within quality, cost, and latency limits |
| Shared platform services | Reuse deployment, integration, evaluation, operations | Ownership, compatibility, funding, support | Lower delivery effort without degraded service outcomes |

Use deterministic services for totals, balances, eligibility rules, and commitments. Forecasting, optimization, rules engines, or classical ML may be more suitable for numerical prediction and constrained planning than an LLM.

## Pattern selection

| Process need | Starting pattern | Add complexity when |
|---|---|---|
| Fixed rules and sequence | Conventional workflow | Interpretation is a material bottleneck |
| Bounded classification or drafting | Model call within an application | Enterprise evidence or live state is needed |
| Questions over enterprise knowledge | Retrieval-augmented application | The task also requires business actions |
| Known actions in a known sequence | Workflow with typed tools | The next step varies materially by case |
| Ambiguous investigation | Single bounded agent | Independent work packages justify specialization |
| Independent specialist tasks | Coordinated agents or services | Evaluation demonstrates a benefit over the simpler design |

These patterns can coexist. A model can assist one step inside a conventional workflow without owning the whole process.

## Service recovery as a business capability

A customer reports a delayed delivery. AI interprets varied language, organizes evidence, identifies ambiguity, and drafts a response. The order service supplies current state. A domain service determines eligible remedies. A transaction service commits the chosen action. Specialists handle disputed facts or exceptional circumstances.

The desired change is fewer fragmented handoffs and faster verified resolution. A case is complete only when its outcome is confirmed and communicated. The agent loop is an implementation choice within that redesigned process.

## Retrieval, live data, and memory

Retrieval supplies knowledge such as service policy. Quality depends on preparation, document structure, access filtering, retrieval strategy, ranking, and freshness. A citation does not make a stale or irrelevant source useful.

Live APIs supply operational facts such as current order status. They need access checks, stable contracts, fresh-state semantics, and clear failure behavior. An indexed snapshot may be useful for discovery but insufficient for a fulfillment or financial commitment.

Session context supports the current interaction. Durable memory can preserve task-relevant preferences or context, but creates correction, retention, ownership, and isolation responsibilities. Introduce it when it improves a defined task and the lifecycle can be managed.

## Retrieve, tune, or route

Start with a baseline prompt and representative evaluation cases. Add retrieval for changing or organization-specific facts. Improve tools and structured context for live state. Consider tuning where a supported model and representative dataset can address persistent behavior or formatting problems. Tuning does not replace current data access or application integration.

Model routing can allocate simpler work to a lower-cost model and difficult work to a more capable one. Base routing on measured task outcomes, not only self-reported model confidence. Evaluate fallback cost, latency, and error propagation across the full route.

Long context may help when relevant information is spread across a large artifact. It also increases consumption and may obscure decisive evidence. Compare long-context reading with retrieval on the actual task.

## When multiple agents justify their cost

Possible reasons include independent parallel work, specialist tools, separate ownership boundaries, or comparing independently generated alternatives. Costs include repeated context, additional calls, coordination failures, inconsistent state, and harder debugging.

Begin service recovery with one orchestrator and explicit tools. A separate investigation agent needs a meaningful independent work package and a measurable handoff benefit. Define shared state, communication, timeout, duplicate handling, escalation, and one accountable owner of the final outcome.

## Design the value experiment

Define eligible cases before the trial. Measure baseline queue time, handling effort, errors, repeat work, and outcome. Compare current work, the proposed service, and a simpler automation option where appropriate.

Leading indicators include retrieval relevance, answer acceptance, tool success, and adoption. Connect them to resolved cases, accepted throughput, reduced repeat contacts, or realized margin. Chatbot usage alone does not demonstrate value.

Segment straightforward cases, ambiguity, missing data, unusual input quality, and exceptions. Record unresolved cases and work shifted outside the measured team. Avoid interpreting theoretical time savings as realized cash savings.

## Buy, build, and distribute

An existing workplace or contact-center product may satisfy a common need faster than a custom application. A custom service may create differentiated value through specialized data, integration, workflow, or experience. A managed runtime can reduce infrastructure work while leaving application and business responsibilities with the enterprise.

Compare actual units: per-seat product, consumption-based model API, managed agent runtime, and self-managed infrastructure have different scopes. The [cloud comparison](cross-cloud-comparison.md) separates these layers.

The [industry use-case portfolio](use-case-portfolio.md) applies these choices to customer service, IT operations, engineering, financial services, healthcare/pharma, manufacturing, and assurance. The [three-tool walkthrough](from-prompt-to-enterprise-service.md) follows one bounded process all the way from a question to a verified outcome.

The first delivery should be the smallest complete service a real user can adopt and a business owner can evaluate. [Day 0](day-0-business-process.md) turns that principle into a process design.
