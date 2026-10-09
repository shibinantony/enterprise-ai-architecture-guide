"""Simulate a synthetic service-recovery policy; never authorize a real commit.

The caller supplies independently trusted policy and identity/order context.
This module cannot establish their authenticity. Model/tool proposals are a
separate untrusted input. No credentials, network, persistence, or approval
verification are implemented.
"""

import argparse
import json
from pathlib import Path
import re


POLICY_ID = "demo-service-recovery-v1"
POLICY_KEYS = {
    "schema_version", "policy_id", "tool_name", "unit", "automatic_limit",
    "per_action_cap", "per_order_total_cap", "eligible_statuses",
    "eligible_reasons", "allowed_destination",
}
PROPOSAL_KEYS = {
    "policy_id", "order_id", "amount", "unit", "destination",
    "idempotency_key", "expected_order_version",
}
IDENTITY_KEYS = {"agent_id", "tenant_id", "customer_scope_id"}
ORDER_KEYS = {
    "order_id", "tenant_id", "customer_id", "status", "reason",
    "credits_granted", "version",
}


def _keys(value, expected):
    return type(value) is dict and set(value) == expected


def _integer(value, minimum):
    # bool is a subclass of int in Python; it must not be accepted as an amount.
    return type(value) is int and value >= minimum


def _demo_id(value):
    return (
        type(value) is str
        and len(value) <= 80
        and re.fullmatch(r"demo-[a-z0-9]+(?:-[a-z0-9]+)*", value) is not None
    )


def _code(value):
    return (
        type(value) is str
        and re.fullmatch(r"[A-Z][A-Z0-9_]{0,63}", value) is not None
    )


def _code_list(value):
    return (
        type(value) is list
        and len(value) > 0
        and all(_code(item) for item in value)
        and len(value) == len(set(value))
    )


def _policy_error(policy):
    if not _keys(policy, POLICY_KEYS):
        return "INVALID_POLICY_FIELDS"
    if type(policy["schema_version"]) is not int or policy["schema_version"] != 1:
        return "UNSUPPORTED_POLICY_SCHEMA"
    if policy["policy_id"] != POLICY_ID:
        return "UNKNOWN_POLICY"
    if (
        policy["tool_name"] != "grant_service_recovery"
        or policy["unit"] != "demo credits"
        or policy["allowed_destination"] != "original_account"
    ):
        return "INVALID_POLICY_CONTRACT"
    if not all(_integer(policy[key], 1) for key in (
        "automatic_limit", "per_action_cap", "per_order_total_cap"
    )):
        return "INVALID_POLICY_LIMITS"
    if not (
        policy["automatic_limit"] <= policy["per_action_cap"]
        <= policy["per_order_total_cap"]
    ):
        return "INVALID_POLICY_LIMITS"
    if not all(_code_list(policy[key]) for key in (
        "eligible_statuses", "eligible_reasons"
    )):
        return "INVALID_POLICY_ELIGIBILITY"
    return None


def _context_error(context):
    if not _keys(context, {"identity", "order"}):
        return "INVALID_CONTEXT_FIELDS"
    identity, order = context["identity"], context["order"]
    if not _keys(identity, IDENTITY_KEYS) or not _keys(order, ORDER_KEYS):
        return "INVALID_CONTEXT_FIELDS"
    if not all(_demo_id(value) for value in identity.values()):
        return "INVALID_CONTEXT_ID"
    if not all(_demo_id(order[key]) for key in (
        "order_id", "tenant_id", "customer_id"
    )):
        return "INVALID_CONTEXT_ID"
    if not all(_code(order[key]) for key in ("status", "reason")):
        return "INVALID_CONTEXT_STATE"
    if not _integer(order["credits_granted"], 0) or not _integer(order["version"], 1):
        return "INVALID_CONTEXT_STATE"
    return None


def _proposal_error(proposal):
    if not _keys(proposal, PROPOSAL_KEYS):
        return "INVALID_PROPOSAL_FIELDS"
    if proposal["policy_id"] != POLICY_ID:
        return "UNKNOWN_POLICY_REFERENCE"
    if not _demo_id(proposal["order_id"]) or not _demo_id(proposal["idempotency_key"]):
        return "INVALID_PROPOSAL_ID"
    if not _integer(proposal["amount"], 1):
        return "INVALID_AMOUNT"
    if not _integer(proposal["expected_order_version"], 1):
        return "INVALID_EXPECTED_VERSION"
    if proposal["unit"] != "demo credits":
        return "INVALID_UNIT"
    if type(proposal["destination"]) is not str:
        return "INVALID_DESTINATION"
    return None


def evaluate(policy, trusted_context, proposal):
    """Return allow, deny, or require_approval against a supplied snapshot.

    An allow result is a simulated policy outcome, never an execution token.
    Unknown/missing fields, unknown policies, and malformed types fail closed.
    The label trusted_context is an interface assumption, not a trust mechanism.
    """
    for validation in (_policy_error(policy), _context_error(trusted_context),
                       _proposal_error(proposal)):
        if validation:
            return {"decision": "deny", "reason_code": validation}

    identity, order = trusted_context["identity"], trusted_context["order"]
    denials = [
        (identity["tenant_id"] != order["tenant_id"], "TENANT_MISMATCH"),
        (identity["customer_scope_id"] != order["customer_id"], "OWNER_MISMATCH"),
        (proposal["order_id"] != order["order_id"], "RESOURCE_MISMATCH"),
        (proposal["expected_order_version"] != order["version"], "STALE_STATE"),
        (order["status"] not in policy["eligible_statuses"], "INELIGIBLE_STATUS"),
        (order["reason"] not in policy["eligible_reasons"], "INELIGIBLE_REASON"),
        (proposal["destination"] != policy["allowed_destination"],
         "DESTINATION_NOT_ALLOWED"),
        (proposal["amount"] > policy["per_action_cap"], "PER_ACTION_CAP_EXCEEDED"),
        (order["credits_granted"] + proposal["amount"] > policy["per_order_total_cap"],
         "PER_ORDER_CAP_EXCEEDED"),
    ]
    for denied, reason in denials:
        if denied:
            return {"decision": "deny", "reason_code": reason}
    if proposal["amount"] > policy["automatic_limit"]:
        return {"decision": "require_approval", "reason_code": "ABOVE_AUTOMATIC_LIMIT"}
    return {"decision": "allow", "reason_code": "WITHIN_AUTOMATIC_LIMIT"}


def _unique_object(pairs):
    """Reject duplicate JSON keys instead of silently accepting the last value."""
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("Duplicate JSON key")
        result[key] = value
    return result


def _reject_constant(value):
    raise ValueError("Non-finite JSON number")


def load_json(path):
    """Read strict JSON, rejecting duplicate fields and non-finite values."""
    with Path(path).open(encoding="utf-8") as source:
        return json.load(source, object_pairs_hook=_unique_object,
                         parse_constant=_reject_constant)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--policy", type=Path,
                        default=Path(__file__).with_name("policy.json"))
    parser.add_argument("--trace", type=Path,
                        default=Path(__file__).with_name("synthetic-trace.json"))
    args = parser.parse_args()
    try:
        policy, trace = load_json(args.policy), load_json(args.trace)
        mismatches = 0
        for case in trace["cases"]:
            result = evaluate(policy, trace["trusted_context"], case["proposal"])
            matches = result == case["expected"]
            mismatches += not matches
            print(json.dumps({"case_id": case["case_id"], **result,
                              "matches_expected": matches}, sort_keys=True))
        return 1 if mismatches else 0
    except (OSError, ValueError, KeyError, TypeError) as error:
        print(json.dumps({"decision": "deny", "reason_code": "INVALID_INPUT_FILE",
                          "error_type": type(error).__name__}))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
