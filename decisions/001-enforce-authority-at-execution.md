# ADR-001: enforce business authority at execution

- **Status:** proposed reference decision; adoption requires local review.
- **Date:** 2026-10-09.
- **Scope:** bounded enterprise agent actions exposed through tool services.

## Context

The host can select a tool and produce well-formed arguments while lacking authority for the target object or action. Instructions and tool descriptions can also be influenced by untrusted content. Protocol-level access is necessary but does not express every domain invariant.

## Decision

Keep verified identity and delegation outside model-supplied arguments. Evaluate policy on the actual request. Enforce object authorization and business invariants in the tool/domain service and system of record. Use independent, transaction-bound approvals when required. Revalidate state and aggregate limits at commit.

A gateway may centralize common checks, but it is not the sole source of truth for domain authorization. Prevent bypass paths or enforce equivalent checks on every path. Record the policy decision and committed outcome with appropriate minimization and integrity controls.

## Alternatives considered

| Alternative | Why it is insufficient on its own |
|---|---|
| Prompt-only constraints | Instructions cannot guarantee access or transaction invariants |
| Host-only checking | Other callers or compromised host execution can bypass the check |
| Gateway-only checking | Edge metadata may lack fresh domain state; direct paths can bypass it |
| API permission only | Permission to call an endpoint does not establish object ownership, limits, or approval |

## Consequences

Domain services require engineering and operational ownership. Policy outages need explicit fail behavior. Independent approval, idempotency, and business commit may span systems and require recovery design. Consistency between layers must be tested rather than inferred from shared terminology.

The benefit is a control boundary that remains enforceable when the host, model, or workflow changes.

## Acceptance evidence

Demonstrate unauthorized object denial, changed-argument approval rejection, stale-state rejection, concurrent aggregate-limit enforcement, safe duplicate retry, timeout reconciliation, and tool revocation. Inspect direct and alternate invocation paths as well as the normal agent path.

## Revisit when

The action's consequence, tenancy model, delegation design, system of record, policy semantics, or recovery commitments change.

## References

[Reference architecture](../docs/reference-architecture.md), [MCP authorization specification](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization), [NIST SP 800-207](https://csrc.nist.gov/pubs/sp/800/207/final).
