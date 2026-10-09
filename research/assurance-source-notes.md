# Assurance research notes

**Reviewed:** 2026-10-09 UTC. The review clock returned 2026-10-09 11:20:57 UTC. Only public primary sources informed the two documents below.

**Outputs:** [Security and assurance](../docs/security-and-assurance.md), [Operating model](../docs/operating-model.md), and the supporting [Governance and business realignment](../docs/governance-and-business-realignment.md) chapter. Edition 0.2 places these within a broader value-led architecture and adoption guide.

## Source register

| Source | Scope used | Interpretation boundary |
| --- | --- | --- |
| [NIST AI RMF Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/) | Lifecycle risk functions; responsibility, inventory and decommissioning | Voluntary framework; our role matrix, gates and metrics are a proposed operational design, not a formal conformance mapping |
| [NIST AI 600-1: Generative AI Profile](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf) | Pre-deployment evidence, capability-claim limits and evaluation context | Companion guidance published in 2024; not an agent-specific certification standard or a guarantee that test results generalize |
| [MCP authorization, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization) | Token validation and intended audience | Applies within the specification's transport and authorization scope; downstream business authorization remains an application responsibility |
| [MCP security guidance, 2026-07-28](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices) | Confused deputy, network destinations, state handles and local execution | Pair with the exact deployed protocol version and normative authorization requirements |
| [MCP tools, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/server/tools) | Metadata trust and tool contract | Tool annotations cannot demonstrate implementation behavior or grant business authority |
| [OWASP MCP Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/MCP_Security_Cheat_Sheet.html) | Tool metadata integrity, isolation and injection exposure | Living guidance; definition hashes detect metadata changes, not a malicious implementation behind unchanged metadata |
| [OWASP AI Agent Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/AI_Agent_Security_Cheat_Sheet.html) | Action boundaries, approval integrity and resource limits | Guidance includes illustrative examples; we do not endorse copying example code as a production control |
| [OWASP LLM Prompt Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html) | Threat coverage and limitations of layered defenses | Filtering and structured context do not establish that arbitrary text is trustworthy |
| [OWASP Transaction Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Transaction_Authorization_Cheat_Sheet.html) | Server enforcement and operation-specific authorization | Proposed approval records and transaction recovery extend this principle to agent actions; they are not MCP features |
| [OWASP Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) | Default denial and per-request permission checks | Application control guidance, not a specification of enterprise business policy |
| [OWASP Logging Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html) | Sensitive-data exclusions and protected evidence | Logging alone does not prove a transaction committed or that an action was authorized |

## Version and evidence caveats

- The current MCP security page resolved to the dated **2026-07-28** documentation. Its state-handle section describes a stateless protocol and explicitly points readers of **2025-11-25 and earlier** to the older session guidance. Do not generalize a session model across versions. [MCP state-handle guidance](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices#state-handle-hijacking)
- OWASP pages are living documents. Recheck guidance before implementation; a review date does not make linked content immutable. For a production assessment, preserve approved source snapshots or revision references in the organization's evidence repository.
- The threat matrix, risk tiers, decision rights, execution sequence and outcome formulas are editorial synthesis. They describe a proposed architecture and operating discipline, not externally measured results. No deployment, penetration test or business-value experiment was performed for these documents.
- Idempotency, reconciliation, transaction-bound approval and downstream commit validation require implementation. MCP does not supply end-to-end exactly-once business execution.
- No legal requirements, universal financial thresholds or domain-specific mandatory human-review rules are asserted. Applicable obligations require the organization's own domain and jurisdiction assessment.
- Research deliberately excludes adoption statistics, product rankings, unverified security claims and internal implementation material. Examples describe generic capabilities and synthetic evaluation conditions.

## Refresh triggers

Re-review when the deployed protocol or SDK changes; when authentication, transport or tool semantics change; when assurance sources publish material revisions; or when a new workflow introduces a different class of consequence. Record the new review date and explain any changed claim or control assumption.
