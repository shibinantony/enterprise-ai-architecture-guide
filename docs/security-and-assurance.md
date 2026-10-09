# Security and assurance: constrain what an agent can cause

An agent's useful permissions are also its potential blast radius. Review the complete path from an untrusted request to a committed business change. A convincing answer or a successful tool response is insufficient evidence that the action was authorized, correct or committed.

**Status:** proposed reference control design, reviewed against the public sources linked below on **2026-10-09 UTC**. This is an implementation starting point, not a security certification. Protocol-specific requirements refer to the linked specification version; deployed clients, servers and SDKs need their own compatibility review.

## Establish the enforcement boundaries

The orchestrator proposes an operation. Trusted execution code validates it. The MCP server checks the caller's authority for the requested resource. The system of record enforces business invariants when it commits the transaction. A gateway may consolidate controls, but direct or alternative access paths must preserve them. Default denial and authorization on every request are established application-security principles. [OWASP authorization guidance](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html)

Credentials, risk classifications and approval records belong outside model-generated content. A prompt instruction, tool description, `readOnlyHint` or model confidence score cannot grant permission. MCP tool metadata supports discovery; it does not demonstrate that a server's implementation behaves as described. [MCP tools, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/server/tools)

**Limit credential concentration.** Prefer independently scoped workload or agent identities, short-lived credentials, and delegated user authority where the process requires it. Retrieve necessary secrets through a managed secret service; prevent broadly privileged credentials from being inherited by every tool process. Document unavoidable shared identities and compensating controls. Test revocation, rotation, and attempted cross-tool access. These are proposed deployment controls, not properties supplied by the protocol.

**Separate OAuth consent from business approval.** For an MCP proxy acting on third-party APIs, the official confused-deputy guidance requires consent tied to the requesting client, registered redirect validation, and protected, expiring, single-use authorization state. Consent to connect an application does not approve a particular refund or deployment. Exercise both boundaries independently. [MCP confused-deputy guidance](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices#confused-deputy-problem)

## Threats, controls and evidence

The following matrix is this guide's proposed application of published guidance. Tests use synthetic records in isolated environments; production attack payloads and sensitive evidence belong in restricted systems.

| Threat and consequence | Preventive control | Detection and recovery | Release evidence |
| --- | --- | --- | --- |
| Retrieved instructions redirect the agent into an unauthorized action | Treat documents, messages and tool results as untrusted data; minimize exposed tools; authorize subsequent calls independently of model output | Detect unexpected destinations or actions; suspend the workflow and invalidate affected memory | Indirect and multi-turn injection cases cannot cross the permitted action boundary |
| A tool description or package changes after review | Approve a specific server origin, artifact and schema; separate tools by trust and function | Detect metadata and artifact changes; quarantine and restore a reviewed release | Changed schema is blocked; unchanged schema with altered behavior is tested separately |
| A valid token is used for the wrong service or resource | Validate issuer, audience, expiry and scope; bind resource access to verified caller identity; use separate downstream credentials | Alert on token-validation failures and unusual resource access; revoke affected grants | Wrong audience, expired token and cross-principal resource requests fail |
| An injected URL reaches an internal endpoint or exports confidential fields | Constrain destinations at the network layer; check redirects and resolved destinations; retrieve only necessary fields | Monitor outbound destinations and transfer size; block the route and investigate exposure | Redirect, DNS-change and sensitive-field export cases fail without logging the secret |
| A local server compromises its host | Restrict process identity, filesystem mounts, network and credentials; review executable provenance | Detect forbidden host access; isolate the process and rotate exposed credentials | Sandbox tests show denied file, process and outbound access |
| An approval is reused or its target changes | Bind approval to a canonical operation and consume it once at execution; reauthorize changed actions | Alert on stale, mismatched or repeated approvals; cancel pending work | Concurrent replay, expired approval and changed-argument tests cannot commit |
| A timeout causes duplicate or inconsistent business changes | Scope idempotency to principal and business operation; persist request digest and outcome; enforce invariants atomically in the system of record | Reconcile unknown outcomes before retry; repair through an approved compensating process | A lost response after commit produces one business effect on retry; changed payload with the same key fails |
| An agent loops, escalates privileges or exhausts a budget | Bound tool calls, elapsed time, concurrency and spend; restrict delegation | Measure limits centrally; trip a circuit breaker and route unfinished work to an owner | Recursive and dependency-failure tests terminate within the configured limits |

Injection controls draw on [OWASP prompt-injection guidance](https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html). Metadata, isolation and supply-chain controls draw on [OWASP MCP security guidance](https://cheatsheetseries.owasp.org/cheatsheets/MCP_Security_Cheat_Sheet.html). Identity requirements come from [MCP authorization](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization); network and local-server threats are described in [MCP security guidance](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices). The approval and resource-limit patterns are informed by [OWASP agent security guidance](https://cheatsheetseries.owasp.org/cheatsheets/AI_Agent_Security_Cheat_Sheet.html). Transaction recovery is a proposed application design, not an MCP delivery guarantee.

Filtering, delimiters and sanitization can reduce exposure and identify some attacks; none establishes that arbitrary retrieved text is safe. Structured fields may still contain hostile instructions. Evaluate whether the independent action boundary holds when the model follows an attack, as well as whether the model resists it. [OWASP MCP security guidance](https://cheatsheetseries.owasp.org/cheatsheets/MCP_Security_Cheat_Sheet.html)

For executable tools, the proposed supply-chain baseline is an immutable approved artifact, pinned dependencies and tool contracts, verified integrity/provenance, and rescanning when relevant vulnerabilities or dependencies change. Use package signatures and runtime attestation where supported and justified by the threat model. Neither proves that a tool is appropriate for a particular business action; behavior and authorization still require evaluation.

## Make human approval a transaction control

Use a trusted approval interface that presents the actual target, material parameters, consequences and evidence. A model-written statement that a person approved an action has no authority. Transaction authorization should be enforced server-side and tied to a specific operation. [OWASP transaction authorization guidance](https://cheatsheetseries.owasp.org/cheatsheets/Transaction_Authorization_Cheat_Sheet.html)

Proposed execution design:

1. Create an immutable proposal containing the principal, tool/version, target, normalized arguments, policy decision/version and relevant record preconditions.
2. Present that proposal to an authorized reviewer. Record the approver, digest, expiry and unique approval identifier in a protected store.
3. Immediately before execution, validate current authorization, proposal digest, expiry and record preconditions. Atomically claim the approval for this operation; reject concurrent claims.
4. Pass a stable idempotency key to the system of record. Store pending, committed, failed or unknown outcome separately. Reconcile an unknown result before any retry.
5. If material parameters, authority or preconditions change, create a new proposal. Never transfer an approval to a different operation.

Claiming approval and committing in a different system are not automatically one transaction. Design the intermediate failure states explicitly. Approval establishes permission, while idempotency prevents duplicate effects; both are needed. If a downstream service lacks deduplication or reliable status lookup, restrict autonomous writes until an acceptable recovery design exists.

## Collect evidence without creating another data leak

Record correlation and transaction identifiers, authenticated actor references, agent/tool/policy versions, authorization result, approval reference, timing, outcome and reconciliation status. Retain the source of each record and its integrity protection. Link the server's execution receipt to the system-of-record commit receipt; a client trace alone proves only what the client observed.

Keep tokens, secrets and unrestricted prompt/tool payloads out of routine telemetry. Use redacted metadata and restricted evidence stores, with access controls, retention periods and deletion procedures appropriate to the data. Logging needs its own threat model. [OWASP logging guidance](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html)

## Require an assurance argument before release

For every material claim, retain **claim → control → test → observed result → owner → residual limitation**. Test normal tasks, boundary values, denied tasks, dependencies failing before and after commit, approval races, resource isolation and realistic injection sequences. Version the evaluation dataset with the agent, model, tools and policy. Record sample sizes, repeats and case-level failures; an aggregate pass rate must not conceal a severe boundary failure.

Pre-deployment testing and evidence shared with release authorities are supported by the NIST Generative AI Profile. Its discussion also cautions that laboratory tests may not generalize to deployment conditions. A passed test suite therefore supports a bounded release decision rather than a claim of complete safety. [NIST AI 600-1, sections MEASURE 2.3, MEASURE 2.5 and Appendix A.1.4](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf)

Assign a named owner to residual risks and define suspension triggers. Any observed unauthorized material action, tenant boundary failure or uncontained data export should block expansion and trigger incident review under the organization's approved response process.

Continue with the [operating model](operating-model.md) for decision rights, release gates and outcome measurement. [Source review notes](../research/assurance-source-notes.md) document the scope and limitations of the research.
