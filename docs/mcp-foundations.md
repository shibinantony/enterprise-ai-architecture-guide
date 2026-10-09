# MCP foundations for enterprise decisions

Reviewed: **2026-10-09 UTC**. Protocol baseline: **2026-07-28**. This chapter explains the standard and identifies additional architecture recommendations. It is not an implementation conformance checklist. The [source register](../research/mcp-source-notes.md) records scope and limitations.

## The enterprise question

An enterprise agent creates value when it can turn a valid business request into an authorized, observable outcome. Connecting a model to an application is only one part of that chain. The organization still owns the decision about who may act, on which records, under what conditions, and with what recovery path.

MCP provides a common protocol for exchanging context and invoking capabilities. It uses JSON-RPC 2.0 and distinguishes hosts, clients, and servers. Its specification also identifies security and consent responsibilities that implementations must address; adopting the protocol does not automatically enforce them. [MCP specification](https://modelcontextprotocol.io/specification/2026-07-28)

The strategic opportunity is reusable capability contracts. The strategic risk is mistaking a successful tool call for a legitimate business action.

## The participants and primitives

A **host** is the application coordinating the experience and model use. An **MCP client** is the host component communicating with a server. An **MCP server** exposes context and capabilities; it may execute locally or remotely. MCP does not prescribe how the host reasons or manages model context. [Architecture overview](https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture)

| Primitive | What it represents | Architectural use |
|---|---|---|
| [Tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools) | Named executable operations with input schemas | Retrieve a record or request a business operation |
| [Resources](https://modelcontextprotocol.io/specification/2026-07-28/server/resources) | Context identified by a URI | Supply a document, schema, or other data |
| [Prompts](https://modelcontextprotocol.io/specification/2026-07-28/server/prompts) | Parameterized message templates exposed by a server | Offer a reusable interaction starting point |

The specification describes tools as model-controlled, resources as application-driven, and prompts as user-controlled. These are intended interaction patterns, not a mandatory interface design. An implementation can apply a deterministic workflow, explicit user selection, or model-assisted selection. [Tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools), [resources](https://modelcontextprotocol.io/specification/2026-07-28/server/resources), [prompts](https://modelcontextprotocol.io/specification/2026-07-28/server/prompts)

**Architecture recommendation:** use model reasoning where ambiguity creates value; keep eligibility, financial limits, record ownership, and transaction validation in services that can be tested independently of the model.

## Four things that must remain distinct

| Concern | Question answered | Example | Enforcement responsibility |
|---|---|---|---|
| Workspace or agent rule | What should apply throughout its configured scope? | Never describe an action as completed without a system receipt | Host and evaluation process; text alone cannot guarantee compliance |
| Skill or procedure | How should this task be performed? | Gather evidence, classify a case, propose a resolution | Workflow implementation, supported by instructions |
| Tool contract | What operation can be requested? | `create_service_case` with a defined input schema | MCP server and downstream service |
| Business policy | Is this request permitted here and now? | Caller owns the case and has approval for the proposed action | Authoritative policy and transaction enforcement |

This is the guide's architecture model, not a set of four MCP primitives. Here, a **rule** means a persistent behavioral instruction within an explicitly configured host or workspace scope. Discovery, precedence, and filenames depend on the host; MCP does not standardize workspace rules. A Markdown instruction is not equivalent to an access-control rule. A procedure can reference policy without being the system that enforces it.

The separate **Agent Skills** format packages a procedure in a directory with a `SKILL.md` file containing metadata and instructions. Supporting scripts, references, and assets are optional. Its progressive-disclosure approach exposes descriptive metadata first, then instructions and supporting material when needed. This can make procedures reusable without placing every procedure in every prompt; actual host support still matters. [Agent Skills specification](https://agentskills.io/specification)

Skills can also be distributed through the optional **Skills over MCP** extension, which defines discovery and retrieval of instructions and supporting files. Hosts implementing it must treat skill content as untrusted and obtain per-skill user approval for host-side code execution or permission grants. Reading a nested skill as supporting content does not activate it. [Skills extension](https://modelcontextprotocol.io/extensions/skills/overview)

For the fictional service-recovery process, the separation becomes concrete:

| Layer | Proposed responsibility |
|---|---|
| Rule | Show an unresolved or pending state until a business-system receipt confirms completion |
| Skill | Verify the order, gather applicable policy and evidence, prepare a remedy, route exceptions, and explain the confirmed outcome |
| Read tool | `get_order_status` retrieves the current record within the caller's permitted scope |
| Action tool | `issue_disruption_compensation` requests a specific change through a supported transaction service |
| Enforced policy | The transaction service checks current eligibility, cumulative limits, required approval, and duplicate execution |

The [three-tool walkthrough](from-prompt-to-enterprise-service.md) adds loyalty lookup and follows these responsibilities through to a verified outcome. These are proposed contracts, not implemented tools in this repository. Keep changeable thresholds in versioned business policy; the skill should consult that policy rather than maintain a conflicting copy. Evaluate the procedure's sequencing separately from the tool's contract and the transaction's invariants.

## Discovery is not a grant of authority

Clients can use `tools/list` to discover tools and `tools/call` to request execution. Listings may change over time and may depend on the authorization presented with the request. A tool's presence in a list is not sufficient evidence that every argument, target record, or business action is allowed. The tools specification requires server access controls and input validation. [Tools specification](https://modelcontextprotocol.io/specification/2026-07-28/server/tools)

**Architecture recommendation:** evaluate authority at execution using the authenticated principal, target object, requested action, current policy, and relevant business state. Recheck approvals when material arguments change. Reject unknown operations and unauthorized objects; do not rely on hiding tool names.

A narrow tool name does not prove a narrow capability. A generic script runner or unrestricted query tool can expose much more authority than its short description suggests. Review the actual execution permissions and reachable systems before assigning its risk tier.

## Turn integrations into supported capabilities

When service recovery and shipment enquiry both need order facts, one supported order capability can avoid building two separate domain integrations. Each consumer still needs compatible client behavior, identity mapping, task evaluations, and support. Reuse is an architectural and economic outcome to measure, not an automatic result of adopting MCP.

A proposed enterprise catalog could start with a few real consumers:

| Domain | Illustrative capabilities | Potential consumers |
|---|---|---|
| Orders | `get_order_status`, `retrieve_delivery_events` | Service recovery, shipment enquiry |
| Cases | `create_service_case`, `get_case_status` | Service recovery, support triage |
| Policy | `retrieve_applicable_policy` | Service recovery, exception preparation |

The catalog is an organizational inventory; `tools/list` is protocol discovery from a particular server. Neither supplies permission to act. A gateway may provide a common access path, but direct connections to supported domain servers can also serve the design.

Register the owner, purpose, schemas, permitted callers, authentication contract, error meanings, compatibility window, evidence requirements, and support commitment. For mutations, add preconditions, idempotency scope, outcome lookup, and repair behavior. Record consumers before a breaking change or retirement. The [capability registration template](../templates/capability-registration.md) makes this reviewable.

| Potential benefit | What makes it real | Qualification |
|---|---|---|
| Standardization | Common discovery and invocation contracts | Business semantics and authorization still need design |
| Reuse | Several workflows consume one maintained domain integration | Count adaptation, assurance, and support costs |
| Composition | Procedures combine independently supported tools | Test cross-tool state, failures, and partial completion |
| Faster experimentation | A local or remote server exposes a bounded capability | A prototype connection is not production readiness |
| Easier model change | Tool contracts survive a model substitution | Retest selection, arguments, outcomes, latency, and cost |

Fund a shared capability when a current use case and a credible next consumer justify it. Track incremental integration effort and accepted outcomes; avoid making catalog size the success measure. The [operating model](operating-model.md) develops this reusable-platform economic hypothesis.

## Authorization exists, but has a defined scope

MCP includes an authorization specification for HTTP transports. Authorization support is optional at the protocol level; HTTP implementations that support it should follow that specification. Stdio implementations should use credentials from their execution environment instead of adopting the HTTP flow. [Authorization specification](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)

In that flow, the protected MCP server is an OAuth resource server. Tokens must be validated for the intended MCP server, and the specification forbids accepting or forwarding tokens meant for other resources. This does not define an organization's refund thresholds, separation of duties, or account ownership rules. [Authorization specification](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)

**Architecture recommendation:** define three separate boundaries: client-to-MCP access, MCP-to-downstream access, and business authorization for the target transaction. Use approved delegation or service credentials for the downstream boundary. For local processes, explicitly restrict inherited secrets and operating-system permissions; local execution is not inherently trusted.

The official security guidance addresses confused-deputy attacks, token passthrough, and server-side request forgery during authorization discovery. These require specific identity and network controls, beyond a model instruction to behave safely. [Security best practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices)

## Version and transport are design inputs

The standard transports are stdio and Streamable HTTP. Transport bindings carry the same protocol semantics using different delivery mechanisms. [Transport overview](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports)

Revision **2026-07-28** removes the earlier initialization handshake and protocol-level sessions. Requests carry version and capability metadata; servers implement `server/discover`. Change notifications use an opted-in `subscriptions/listen` stream. Examples requiring `initialize` or protocol-managed `Mcp-Session-Id` describe an earlier revision. A hosting platform may retain an affinity header for its own routing; see the [cloud comparison](cross-cloud-comparison.md) for that separate responsibility. [Key changes](https://modelcontextprotocol.io/specification/2026-07-28/changelog)

**Architecture recommendation:** pin a compatibility matrix covering client, server, SDK, transport, protocol revision, and extensions. Validate it before upgrades. Keep business workflow state in explicit application records. Use business idempotency keys and reconciliation for mutations; a protocol request identifier is not evidence of exactly-once execution.

## Portability is a testable claim

MCP standardizes part of the integration contract. It does not specify an enterprise's deployment architecture, commercial model, operating procedures, or regulatory obligations. The following is an architecture assessment framework, not a guarantee in the standard:

| Portability layer | What to verify |
|---|---|
| Protocol | Compatible revisions, transports, schemas, errors, and extensions |
| Behavior | Comparable tool selection, argument quality, and task outcomes across hosts and models |
| Authority | Equivalent delegation, object access, approval, and revocation behavior |
| Operations | Equivalent network isolation, telemetry, deployment, incident response, and recovery |
| Economics | Full migration and operating costs, including adaptation and reassessment |

Demonstrate portability by running the same bounded workflow against the same capability contracts from two independently implemented hosts, then testing failure and denial paths. Record remaining dependencies. A second successful connection alone does not demonstrate operational portability.

## What a director should require

Before funding expansion, require an accountable business owner, a measurable process outcome, a defined action boundary, evidence of enforced authorization, and a tested exception path. Require a release record that identifies the model, host, server, tool schema, workflow, policy, and evaluation versions.

The investment decision is whether a reusable capability improves outcomes at an acceptable operating cost and residual risk. MCP makes an important integration boundary explicit; the enterprise must make that boundary governable.
