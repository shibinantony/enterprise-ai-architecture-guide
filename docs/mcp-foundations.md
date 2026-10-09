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
| Behavioral instruction | How should the agent behave? | Explain uncertainty before suggesting a resolution | Host and evaluation process; text alone cannot guarantee compliance |
| Skill or procedure | How should this task be performed? | Gather evidence, classify a case, propose a resolution | Workflow implementation, supported by instructions |
| Tool contract | What operation can be requested? | `create_service_case` with a defined input schema | MCP server and downstream service |
| Business policy | Is this request permitted here and now? | Caller owns the case and has approval for the proposed action | Authoritative policy and transaction enforcement |

This is the guide's architecture model, not a set of four MCP primitives. A Markdown instruction is not equivalent to an access-control rule. A procedure can reference policy without being the system that enforces it.

Skills can also be distributed through the optional **Skills over MCP** extension. It defines discovery and retrieval of instructions and supporting files; host support must be checked. Merely reading a skill does not activate it. [Skills extension](https://modelcontextprotocol.io/extensions/skills/overview)

## Discovery is not a grant of authority

Clients can use `tools/list` to discover tools and `tools/call` to request execution. Listings may change over time and may depend on the authorization presented with the request. A tool's presence in a list is not sufficient evidence that every argument, target record, or business action is allowed. The tools specification requires server access controls and input validation. [Tools specification](https://modelcontextprotocol.io/specification/2026-07-28/server/tools)

**Architecture recommendation:** evaluate authority at execution using the authenticated principal, target object, requested action, current policy, and relevant business state. Recheck approvals when material arguments change. Reject unknown operations and unauthorized objects; do not rely on hiding tool names.

A narrow tool name does not prove a narrow capability. A generic script runner or unrestricted query tool can expose much more authority than its short description suggests. Review the actual execution permissions and reachable systems before assigning its risk tier.

## Authorization exists, but has a defined scope

MCP includes an authorization specification for HTTP transports. Authorization support is optional at the protocol level; HTTP implementations that support it should follow that specification. Stdio implementations should use credentials from their execution environment instead of adopting the HTTP flow. [Authorization specification](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)

In that flow, the protected MCP server is an OAuth resource server. Tokens must be validated for the intended MCP server, and the specification forbids accepting or forwarding tokens meant for other resources. This does not define an organization's refund thresholds, separation of duties, or account ownership rules. [Authorization specification](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)

**Architecture recommendation:** define three separate boundaries: client-to-MCP access, MCP-to-downstream access, and business authorization for the target transaction. Use approved delegation or service credentials for the downstream boundary. For local processes, explicitly restrict inherited secrets and operating-system permissions; local execution is not inherently trusted.

The official security guidance addresses confused-deputy attacks, token passthrough, and server-side request forgery during authorization discovery. These require specific identity and network controls, beyond a model instruction to behave safely. [Security best practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices)

## Version and transport are design inputs

The standard transports are stdio and Streamable HTTP. Transport bindings carry the same protocol semantics using different delivery mechanisms. [Transport overview](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports)

Revision **2026-07-28** removes the earlier initialization handshake and protocol-level sessions. Requests carry version and capability metadata; servers implement `server/discover`. Change notifications use an opted-in `subscriptions/listen` stream. Earlier examples using `initialize` or `Mcp-Session-Id` describe a different revision. [Key changes](https://modelcontextprotocol.io/specification/2026-07-28/changelog)

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
