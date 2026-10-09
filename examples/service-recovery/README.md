# Synthetic service recovery: from proposal to policy decision

This runnable example is a **decision-policy simulator**, not an MCP server, approval service, or production enforcement point. It has no network calls, dependencies, credentials, persistent ledger, or real integration. Every identifier is fictional; **demo credits are non-monetary units** with no exchange value. The thresholds are invented risk appetite choices, not industry guidance.

The business question is narrow: may an agent propose a service-recovery credit for a delayed order? A model can propose an action; a trusted service must decide whether that action is authorized, and the system of record must validate and commit it. Even a correct proposal is insufficient authority to execute.

For the larger process, see the [three-tool design walkthrough](../../docs/from-prompt-to-enterprise-service.md). It adds order lookup, loyalty-based proposals, shipping, approval, and outcome verification as a conceptual design. Its illustrative policy differs from this simulator; those additional behaviors are not implemented here.

## Run from the repository root

Use Python 3.9 or later:

```console
python examples/service-recovery/evaluator.py
python -m unittest discover -s examples/service-recovery -p "test_*.py" -v
```

The first command evaluates four independent fixtures against the same snapshot: `allow`, `require_approval`, a cap denial, and a forged-approval denial. Each line reports whether the outcome matches the fixture. Exit code `0` means all fixture expectations matched; `1` means a mismatch; `2` means a file could not be processed. No order balance changes.

## Files and boundaries

| File | Purpose |
| --- | --- |
| [tool-contract.json](tool-contract.json) | Illustrative MCP-style tool description and input schema; no server or transport implementation. |
| [policy.json](policy.json) | Explicit, synthetic eligibility and limit policy. |
| [synthetic-trace.json](synthetic-trace.json) | Mock trusted context, untrusted proposals, expected outcomes, and an unimplemented production sequence. |
| [evaluator.py](evaluator.py) | Deterministic snapshot checks using the Python standard library. |
| [test_evaluator.py](test_evaluator.py) | Adversarial inputs, boundary values, ownership, and state checks. |

`evaluate(policy, trusted_context, proposal)` deliberately separates three inputs. The policy must come from a reviewed configuration source. `trusted_context.identity` represents identity and delegated customer scope verified outside the model. `trusted_context.order` represents a fresh authoritative read. The proposal may come from a model or tool output and carries no authority.

Calling an object `trusted_context` does not make it trustworthy. In this local fixture it is ordinary editable JSON. The simulator cannot authenticate a caller, prove delegation, verify a policy signature, or establish that an order snapshot is current. A production adapter must supply those assurances and prevent an untrusted caller from supplying these inputs.

The proposal cannot provide a tenant, customer scope, order status, cumulative credits, or approval flag. Unknown fields, missing fields, unsupported policy identifiers, and malformed types fail closed. Amounts must be positive Python integers; booleans, numeric strings, and floats are rejected. JSON loading also rejects duplicate keys and non-finite numeric constants. The illustrative schema and policy are distinct: the evaluator implements business checks directly and does not load a general JSON Schema validator.

## Decision table

All checks are cumulative; approval cannot override a denial.

| Condition | Outcome |
| --- | --- |
| Tenant, customer ownership, or requested order does not match trusted context | `deny` |
| Expected order version differs from supplied authoritative snapshot | `deny` |
| Status is not `DELAYED` or reason is not `WEATHER_DISRUPTION` | `deny` |
| Destination is not `original_account` | `deny` |
| Amount exceeds 50, or prior credits plus amount exceed 100 | `deny` |
| All checks pass and amount is 26 through 50 | `require_approval` |
| All checks pass and amount is 1 through 25 | `allow` |

Limits are in demo credits. `original_account` is a fixed routing selector; an authoritative service would resolve the account without accepting an arbitrary destination from the model. The simulator does not perform that resolution.

`require_approval` means execution must wait. There is no `approved: true` shortcut. Production approval must be independently verified, appropriately authorized, time limited, and bound to the exact principal, tenant, action, arguments, and policy/state context. A stale or modified request requires renewed validation. `allow` means only that a supplied snapshot passed these checks; it is not an execution token.

## What the production transaction still needs

The state-version check demonstrates optimistic concurrency intent, not concurrency safety. A production service must revalidate eligibility and cumulative limits at commit, using locking, compare-and-swap, or another transaction design appropriate to its system of record. Two requests that separately pass against the same snapshot must not consume the same remaining allowance.

The idempotency key is checked for syntax only. A real ledger must atomically bind it to the principal, tenant, resource, operation, and canonical arguments; return the recorded outcome for an identical retry; and reject key reuse with changed arguments. The commit and cumulative-credit update must share an appropriate atomic boundary. Retry, timeout, partial-failure, and recovery behavior need integration tests.

The fixture is neither an audit trail nor cryptographic proof. Production evidence needs a recorded policy decision, verified approval where applicable, request and transaction correlation, committed outcome, access controls, redaction, retention, and suitable integrity protection. Avoid logging sensitive tool results merely because they are available.

The director-level acceptance criterion is therefore broader than passing these tests: an accountable service owner must demonstrate that identity, delegation, policy delivery, transaction integrity, approval verification, and evidence controls actually hold at the execution boundary. This example makes the decision boundary inspectable; it does not certify a deployable platform.
