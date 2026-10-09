# Topic coverage: from MCP learning to enterprise delivery

This map connects the guide's foundational ideas with the decisions and artifacts needed to deliver an enterprise AI service. Follow the main [reading path](../README.md) for a value-led narrative; use this table to examine a particular architectural concern.

| Core topic | Where it is developed | What the reader should be able to assess |
| --- | --- | --- |
| Business intent becomes observable action | [Three-tool walkthrough](../docs/from-prompt-to-enterprise-service.md) | Trace a request through current facts, a proposed remedy, execution authority, and a verified business result |
| Reasoning, capability execution, and business authority | [MCP foundations](../docs/mcp-foundations.md) and [transaction-authority decision](../decisions/001-enforce-authority-at-execution.md) | Identify what the model proposes, what the interface exposes, and what the application permits |
| Rules, reusable skills, and tools | [MCP distinctions](../docs/mcp-foundations.md) and [worked procedure](../docs/from-prompt-to-enterprise-service.md) | Separate behavioral guidance, a task procedure, an executable contract, and enforced policy |
| Integration reuse and capability discovery | [MCP foundations](../docs/mcp-foundations.md) and [capability registration](../templates/capability-registration.md) | Treat supported domain capabilities as reusable assets with consumers, ownership, and compatibility obligations |
| Practical use-case breadth | [Industry portfolio](../docs/use-case-portfolio.md) | Connect service, IT, engineering, finance, health/pharma, manufacturing, and assurance problems to bounded capabilities and outcomes |
| Benefits and their conditions | [Value and capabilities](../docs/value-and-capabilities.md), [MCP foundations](../docs/mcp-foundations.md), and [value scorecard](../templates/value-scorecard.md) | Test whether reuse, composition, faster delivery, or better work actually produces accepted outcomes |
| Attack surface and failure modes | [Security and assurance](../docs/security-and-assurance.md) | Examine injection, tool tampering, confused delegation, credentials, excess autonomy, uncertain commits, and corresponding evidence |
| Google Cloud construction-to-operation path | [GCP deep dive](../docs/gcp-enterprise-architecture.md) | Distinguish development tooling, ADK application, model/data services, production tools, runtime, and operations |
| Microsoft Azure alternative | [Equivalent-layer comparison](../docs/cross-cloud-comparison.md) | Assess Foundry hosting, remote tools, Toolbox, identity, data, user channels, and approval responsibilities |
| AWS alternative | [Equivalent-layer comparison](../docs/cross-cloud-comparison.md) | Assess AgentCore Runtime and Gateway, server hosting, model/data services, identity, workflow, and operating responsibilities |
| Platform choice and portability | [Platform decision framework](../docs/platform-decision-framework.md), [comparison](../docs/cross-cloud-comparison.md), and [MCP foundations](../docs/mcp-foundations.md) | Evaluate existing identity, records, data, skills, channels, location requirements, commercial constraints, and exit cost |
| Complete production architecture | [Reference architecture](../docs/reference-architecture.md) | Connect business and experience layers to reasoning, knowledge, action, control, infrastructure, and operations |
| Proportionate authority and tool lifecycle | [Governance within business realignment](../docs/governance-and-business-realignment.md) | Assign consequence tiers, ownership, permission, evidence, change, suspension, and retirement responsibilities |
| Reusable platform economics | [Operating model](../docs/operating-model.md) and [pricing](../docs/pricing-and-economics.md) | Separate integration investment, marginal workflow cost, runtime/model consumption, human work, and realized value |
| Director-level decisions | [Executive brief](../docs/executive-brief.md) and [review questions](../docs/governance-and-business-realignment.md) | Turn business, data, authority, quality, operational, and investment questions into named decisions and evidence |
| End-to-end adoption and sustained value | [Day 0](../docs/day-0-business-process.md), [Day 1](../docs/day-1-build-and-launch.md), [Day 2](../docs/day-2-operate-and-improve.md), and [roadmap](../docs/adoption-roadmap.md) | Redesign work, prepare people and data, deliver a complete service, and improve or retire it using measured outcomes |

## What each type of artifact establishes

The walkthrough preserves a small, understandable three-tool pattern. Its loyalty amounts and shipping choices are fictional design inputs. The [runnable simulator](../examples/service-recovery/README.md) demonstrates a narrower policy decision with different explicitly documented limits; it does not implement the walkthrough, an MCP server, approval verification, or a transaction ledger.

The cloud chapters map that pattern to documented product capabilities. They do not report deployed implementations or prove that every component supports the same protocol revision. The [cost calculator](../examples/cost-model/README.md) reproduces explicit assumptions and sourced list rates; it does not establish a measured provider bill or universal price winner.

The adoption and operating chapters extend technical feasibility into business delivery. Governance completes this account through people, technology, and management philosophy: who owns the result, what authority is delegated, how evidence changes decisions, and how the organization learns. It supports the business outcome throughout the lifecycle.

See the [research method](README.md) for evidence classes, source registers, review dates, and maintenance rules.
