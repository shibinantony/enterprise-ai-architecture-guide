# MCP primary-source register

**Reviewed:** 2026-10-09 UTC. **Protocol baseline:** 2026-07-28. The review clock returned `2026-10-09 11:20:55 UTC`. The official `latest` URL resolved to the versioned specification below during review.

This register supports [MCP foundations](../docs/mcp-foundations.md). It records public primary sources only. No employer, customer, private deployment, or training-exercise evidence is used. Statements labeled **architecture recommendation** in the guide are the guide's proposed design choices, not additional protocol requirements.

| ID | Exact primary source | Version or status at review | Supported claims | Limits |
|---|---|---|---|---|
| MCP-01 | [Specification](https://modelcontextprotocol.io/specification/2026-07-28) | 2026-07-28 | JSON-RPC; participant roles; core features; implementer security responsibilities | Standard adoption does not prove deployed controls or compliance |
| MCP-02 | [Architecture overview](https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture) | Documentation for 2026-07-28 | Host/client/server separation; local and remote execution; protocol does not dictate model use | Explanatory documentation, not an enterprise reference architecture |
| MCP-03 | [Tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools) | 2026-07-28 | Listing and invocation; schemas; interaction flexibility; changing authorization-dependent lists; server access controls | Discovery does not grant transaction authority; metadata is not security attestation |
| MCP-04 | [Resources](https://modelcontextprotocol.io/specification/2026-07-28/server/resources) | 2026-07-28 | URI-addressed context and application-driven interaction pattern | Does not mandate a particular user interface or establish data trust |
| MCP-05 | [Prompts](https://modelcontextprotocol.io/specification/2026-07-28/server/prompts) | 2026-07-28 | Server-provided templates, arguments, discovery, and flexible interaction | User-controlled selection does not mean user-authored content |
| MCP-06 | [Authorization](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization) | 2026-07-28 | Optional authorization support; HTTP scope; stdio distinction; resource-server role; token audience checks | Not an organization-specific policy model; OAuth 2.1 is cited as an IETF draft in this revision |
| MCP-07 | [Security Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices) | Documentation for 2026-07-28 | Confused-deputy, token-passthrough, and authorization-discovery SSRF threats and mitigations | Threat descriptions do not establish the vulnerability of any particular deployment |
| MCP-08 | [Transport overview](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports) | 2026-07-28 | Stdio and Streamable HTTP bindings; shared protocol semantics | Choosing a transport does not establish isolation, availability, or transaction integrity |
| MCP-09 | [Key Changes](https://modelcontextprotocol.io/specification/2026-07-28/changelog) | Changes from 2025-11-25 to 2026-07-28 | Removed handshake and protocol sessions; request metadata; discovery; subscription changes | A migration inventory, not evidence that every SDK or host implements the revision |
| MCP-10 | [Skills](https://modelcontextprotocol.io/extensions/skills/overview) | Official extension; linked proposal marked Final; implementation support developing | Optional skill discovery/retrieval; host activation responsibilities | Separate from core primitives; verify actual client/server support and extension revision |

## Interpretation rules

- Pin citations to the revision discussed. Recheck the official [version index](https://modelcontextprotocol.io/specification/latest) before implementation or a substantive guide update.
- Distinguish normative language in the specification from explanatory guidance and this repository's recommendations. Preserve whether a source says required, recommended, or optional.
- Do not infer that OAuth scopes encode every business rule, that a visible tool is authorized for every record, or that an MCP server is inherently trusted.
- Treat cross-host compatibility, operational portability, return on investment, and control effectiveness as hypotheses requiring measurements. These pages do not provide such measurements.
- The review covered published documentation, not running implementations. No security certification, interoperability test, performance benchmark, or production deployment is claimed.

## Maintenance trigger

Review these sources when the supported protocol revision, transport, SDK, host, authentication flow, or optional extension changes. Update the review date and affected claims together. If implementations remain on an older revision, document that compatibility decision explicitly instead of silently combining old and new wire behavior.
