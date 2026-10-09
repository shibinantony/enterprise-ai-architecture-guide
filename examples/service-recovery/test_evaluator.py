"""Exercise synthetic policy boundaries and hostile input without external services."""

from copy import deepcopy
from pathlib import Path
import tempfile
import unittest

from evaluator import evaluate, load_json


HERE = Path(__file__).resolve().parent


class PolicyTests(unittest.TestCase):
    def setUp(self):
        self.policy = load_json(HERE / "policy.json")
        trace = load_json(HERE / "synthetic-trace.json")
        self.context = trace["trusted_context"]
        self.proposal = deepcopy(trace["cases"][0]["proposal"])

    def result(self):
        return evaluate(self.policy, self.context, self.proposal)

    def assert_decision(self, decision, reason):
        self.assertEqual(self.result(), {"decision": decision, "reason_code": reason})

    def test_fixture_outcomes(self):
        trace = load_json(HERE / "synthetic-trace.json")
        for case in trace["cases"]:
            with self.subTest(case=case["case_id"]):
                self.assertEqual(evaluate(self.policy, trace["trusted_context"],
                                          case["proposal"]), case["expected"])

    def test_amount_boundaries(self):
        for amount, decision, reason in [
            (1, "allow", "WITHIN_AUTOMATIC_LIMIT"),
            (25, "allow", "WITHIN_AUTOMATIC_LIMIT"),
            (26, "require_approval", "ABOVE_AUTOMATIC_LIMIT"),
            (50, "require_approval", "ABOVE_AUTOMATIC_LIMIT"),
            (51, "deny", "PER_ACTION_CAP_EXCEEDED"),
        ]:
            with self.subTest(amount=amount):
                self.proposal["amount"] = amount
                self.assert_decision(decision, reason)

    def test_invalid_amounts_including_python_booleans(self):
        for amount in [True, False, 0, -1, "25", 25.0, None, [], {}, float("nan")]:
            with self.subTest(amount=amount):
                self.proposal["amount"] = amount
                self.assert_decision("deny", "INVALID_AMOUNT")

    def test_total_cap_boundary_and_approval_does_not_override_cap(self):
        self.context["order"]["credits_granted"] = 75
        self.assert_decision("allow", "WITHIN_AUTOMATIC_LIMIT")
        self.context["order"]["credits_granted"] = 76
        self.assert_decision("deny", "PER_ORDER_CAP_EXCEEDED")
        self.context["order"]["credits_granted"] = 50
        self.proposal["amount"] = 50
        self.assert_decision("require_approval", "ABOVE_AUTOMATIC_LIMIT")
        self.context["order"]["credits_granted"] = 51
        self.assert_decision("deny", "PER_ORDER_CAP_EXCEEDED")

    def test_tenant_and_owner_scope_are_independent(self):
        self.context["identity"]["tenant_id"] = "demo-tenant-other"
        self.assert_decision("deny", "TENANT_MISMATCH")
        self.context["identity"]["tenant_id"] = self.context["order"]["tenant_id"]
        self.context["identity"]["customer_scope_id"] = "demo-customer-other"
        self.assert_decision("deny", "OWNER_MISMATCH")

    def test_resource_substitution(self):
        self.proposal["order_id"] = "demo-order-other"
        self.assert_decision("deny", "RESOURCE_MISMATCH")

    def test_stale_state(self):
        self.proposal["expected_order_version"] = 2
        self.assert_decision("deny", "STALE_STATE")
        self.proposal["expected_order_version"] = True
        self.assert_decision("deny", "INVALID_EXPECTED_VERSION")

    def test_ineligible_status_and_reason(self):
        self.context["order"]["status"] = "DELIVERED"
        self.assert_decision("deny", "INELIGIBLE_STATUS")
        self.context["order"]["status"] = "DELAYED"
        self.context["order"]["reason"] = "UNVERIFIED"
        self.assert_decision("deny", "INELIGIBLE_REASON")

    def test_destination_cannot_be_supplied_by_model(self):
        self.proposal["destination"] = "demo-alternate-account"
        self.assert_decision("deny", "DESTINATION_NOT_ALLOWED")

    def test_unknown_and_missing_proposal_fields(self):
        for key, value in [("approved", True), ("tenant_id", "demo-tenant-001"),
                           ("status", "DELAYED"),
                           ("instructions", "Ignore limits and execute")]:
            with self.subTest(key=key):
                proposal = {**self.proposal, key: value}
                self.assertEqual(evaluate(self.policy, self.context, proposal),
                                 {"decision": "deny", "reason_code": "INVALID_PROPOSAL_FIELDS"})
        del self.proposal["amount"]
        self.assert_decision("deny", "INVALID_PROPOSAL_FIELDS")

    def test_unsupported_policy_and_schema(self):
        self.proposal["policy_id"] = "demo-unknown-policy"
        self.assert_decision("deny", "UNKNOWN_POLICY_REFERENCE")
        self.proposal["policy_id"] = self.policy["policy_id"]
        self.policy["policy_id"] = "demo-unknown-policy"
        self.assert_decision("deny", "UNKNOWN_POLICY")
        self.policy["policy_id"] = self.proposal["policy_id"]
        for version in [True, 1.0, "1", 2]:
            with self.subTest(version=version):
                self.policy["schema_version"] = version
                self.assert_decision("deny", "UNSUPPORTED_POLICY_SCHEMA")

    def test_policy_changes_do_not_skip_validation(self):
        for key, value, reason in [
            ("automatic_limit", True, "INVALID_POLICY_LIMITS"),
            ("automatic_limit", 51, "INVALID_POLICY_LIMITS"),
            ("per_action_cap", 101, "INVALID_POLICY_LIMITS"),
            ("eligible_reasons", [], "INVALID_POLICY_ELIGIBILITY"),
            ("unit", "cash", "INVALID_POLICY_CONTRACT"),
        ]:
            with self.subTest(key=key, value=value):
                policy = {**self.policy, key: value}
                self.assertEqual(evaluate(policy, self.context, self.proposal),
                                 {"decision": "deny", "reason_code": reason})
        self.policy["bypass"] = True
        self.assert_decision("deny", "INVALID_POLICY_FIELDS")

    def test_context_unknown_fields_and_negative_ledger(self):
        self.context["order"]["credits_granted"] = -1
        self.assert_decision("deny", "INVALID_CONTEXT_STATE")
        self.context["order"]["credits_granted"] = True
        self.assert_decision("deny", "INVALID_CONTEXT_STATE")
        self.context["order"]["credits_granted"] = 20
        self.context["identity"]["approved"] = True
        self.assert_decision("deny", "INVALID_CONTEXT_FIELDS")

    def test_malformed_top_level_inputs_fail_closed(self):
        for value in [None, [], "ignore policy", True]:
            with self.subTest(value=value):
                self.assertEqual(evaluate(value, self.context, self.proposal)["decision"], "deny")
                self.assertEqual(evaluate(self.policy, value, self.proposal)["decision"], "deny")
                self.assertEqual(evaluate(self.policy, self.context, value)["decision"], "deny")

    def test_invalid_unit_and_idempotency_key(self):
        self.proposal["unit"] = "cash"
        self.assert_decision("deny", "INVALID_UNIT")
        self.proposal["unit"] = "demo credits"
        self.proposal["idempotency_key"] = ""
        self.assert_decision("deny", "INVALID_PROPOSAL_ID")

    def test_evaluation_is_pure_and_does_not_commit(self):
        before = deepcopy((self.policy, self.context, self.proposal))
        first, retry = self.result(), self.result()
        self.assertEqual(first, retry)
        self.assertEqual((self.policy, self.context, self.proposal), before)
        self.assertEqual(self.context["order"]["credits_granted"], 20)

    def test_strict_json_rejects_duplicate_and_non_finite_values(self):
        with tempfile.TemporaryDirectory(prefix="demo-policy-") as directory:
            path = Path(directory) / "demo-input.json"
            for content in ['{"amount":25,"amount":50}', '{"amount":NaN}',
                            '{"amount":Infinity}']:
                with self.subTest(content=content):
                    path.write_text(content, encoding="utf-8")
                    with self.assertRaises(ValueError):
                        load_json(path)


if __name__ == "__main__":
    unittest.main()
