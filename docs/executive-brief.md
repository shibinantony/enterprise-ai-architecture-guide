# From prompting to governed agency

## Executive thesis

An enterprise agent is an operational service that interprets intent and uses tools to pursue a business outcome. Its value comes from the complete service: accurate interpretation, legitimate authority, reliable execution, and evidence that the intended result occurred.

The strategic shift is from funding isolated assistants to managing a portfolio of reusable capabilities. MCP can support this shift by standardizing how applications discover and request capabilities. It does not replace the organization's responsibility for business decisions, access, transactions, or recovery. [MCP specification](https://modelcontextprotocol.io/specification/2026-07-28)

The recommendation in this guide is to fund one bounded workflow and the smallest shared foundation it needs. Expansion should depend on measured outcomes and control evidence. Building a large platform before establishing demand risks creating expensive infrastructure without a durable service portfolio.

## Start with the process problem

Consider a fictional service team handling delivery disruptions. Staff repeatedly retrieve an order, check eligibility, determine an allowed remedy, apply it, and explain the result. Some requests are ambiguous; the compensation calculation and authority boundaries should be precise.

An agent can interpret the request, gather relevant evidence, and propose a resolution. A policy service evaluates the proposal. The business system validates current state and commits the approved action. The user receives a response grounded in the committed result, including unresolved uncertainty when execution cannot be confirmed.

This decomposition matters more than the choice of model. It assigns ambiguity to reasoning and business invariants to enforceable services.

| Process characteristic | Likely starting approach | Reason |
|---|---|---|
| Stable inputs and fixed decision steps | Conventional workflow or API automation | Easier to test and operate when interpretation adds little value |
| Varied language, bounded task, verifiable outcome | Agent-assisted workflow | Interpretation may reduce manual work while actions remain constrained |
| High consequence, disputed evidence, difficult reversal | Decision support with qualified review | Preserve accountable judgment and a complete evidence record |
| No authoritative data or unclear process ownership | Improve the process and data first | An agent cannot repair missing authority or an undefined outcome |

These are selection heuristics. A real decision needs process data and accountable acceptance of residual risk.

## Four planes, distinct responsibilities

**Reasoning plane:** interprets intent, selects relevant information, and proposes actions. It includes the model, host, workflow, procedures, and bounded memory.

**Knowledge plane:** supplies approved context with provenance, access restrictions, and freshness. It includes documents, retrieval, and reads from business records. Retrieved text remains data; it cannot grant authority.

**Action plane:** exposes bounded operations and validates transactions against authoritative state. It includes MCP servers, domain services, APIs, and systems of record.

**Control plane:** manages registration, ownership, identities, policy versions, release decisions, evaluation, and revocation. Its decisions must be enforced in the execution path. A registry entry or a diagram alone provides no protection.

The [reference architecture](reference-architecture.md) explains how these planes interact without assuming that all controls must reside in one product or gateway.

## The strategic asset is a governed capability

A reusable capability includes more than a connector. It needs a stable contract, narrow authority, a business owner, compatibility tests, support commitments, data handling rules, and a retirement path.

For example, `propose_service_recovery` is easier to govern when its target records, permitted destinations, limits, failure modes, and evidence obligations are explicit. A generic tool that can execute arbitrary scripts may be flexible, but shifts substantial risk and review cost into every consuming workflow.

Standardized integration can reduce duplication. Reuse is economically beneficial only if the shared service's maintenance, assurance, and coordination costs are lower than the duplication it avoids. That proposition should be tested rather than assumed.

## A business case that includes control costs

Compare the proposed service with a measured baseline over comparable cases and time periods. Preserve the same definition of a successfully resolved case, including downstream rework and reversals.

```text
Net period value = realized process benefit
                   - incremental operating cost
                   - amortized build and control cost
                   - measured loss and remediation cost

Cost per verified outcome = total attributable service cost
                            / independently accepted outcomes
```

These are planning formulas, not empirical findings. Avoid presenting theoretical hours saved as realized cash savings. Track redeployed capacity separately from eliminated expense, and do not subtract the same incident cost twice. Estimate uncertain losses using scenarios and sensitivity analysis; a short pilot with no incidents does not establish a low long-term loss rate.

Include model consumption, hosting, retrieval, integration maintenance, evaluation, human review, observability, security, support, and recovery. Compare against simpler automation as well as current manual work. Shared platform costs need a declared allocation rule.

The [operating model](operating-model.md) defines denominators for outcome, cost, exception, recovery, and reuse measures.

## Investment and stop decisions

| Decision | Evidence required | Accountable decision-maker |
|---|---|---|
| Fund discovery | Process volume, baseline, owner, expected outcome, credible data access | Business sponsor |
| Fund a pilot | Bounded authority, threat model, evaluation plan, recovery design, cost envelope | Sponsor with architecture and control owners |
| Permit constrained production | Tested enforcement and failure paths, support readiness, accepted residual risks | Designated service release authority |
| Expand autonomy or scope | Sustained outcome quality, known exception behavior, capacity and control evidence | Business owner with risk and operations |
| Pause or retire | Harm, control failure, poor economics, unavailable support, or loss of lawful access | Service owner under defined escalation rules |

Define these authorities before implementation. An architecture board may evaluate design without owning business outcomes; a security review cannot substitute for an operational owner.

## What the director should ask

1. Which process outcome improves, and how will it be independently verified?
2. Why is agent reasoning needed for this process?
3. Under whose identity and delegated authority will each action occur?
4. Where are object access, limits, approval, and current-state validation enforced?
5. What happens when an action times out after it may have committed?
6. Who can stop new actions, reconcile incomplete work, and support affected users?
7. What evidence would cause us to reject expansion or retire the service?
8. Which reusable capabilities have a funded owner and another credible consumer?

NIST's AI Risk Management Framework provides a useful voluntary structure for governing, mapping, measuring, and managing AI risks. The release gates and investment model in this guide are proposed applications of those ideas, not NIST certification criteria. [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework)

## Recommended first commitment

Select one process with a clear owner, authoritative data, measurable outcomes, and a manageable exception path. Begin with assisted decisions or restricted reads. Add bounded actions only after enforcement and recovery tests pass. Use the resulting evidence to decide what to standardize and what to stop.

The proposed [90-day plan](adoption-roadmap.md) expresses this as decision gates, with time boxes that should be adjusted to the organization's delivery and assurance obligations.
