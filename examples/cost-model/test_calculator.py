"""Check units, retry multiplication, missing rates, and economic sensitivities."""

from copy import deepcopy
from decimal import Decimal
from pathlib import Path
import unittest

from calculator import calculate, load, model_cost, number, runtime_cost


HERE = Path(__file__).resolve().parent


class CostModelTests(unittest.TestCase):
    def setUp(self):
        self.rates = load(HERE / "rates.json")
        self.inputs = load(HERE / "scenarios.json")
        self.common = self.inputs["common"]
        self.base = self.inputs["scenarios"]["base"]

    def test_same_model_base_tokens_and_cost_match_all_clouds(self):
        for provider in self.rates["providers"].values():
            result = model_cost(provider["model"], self.common, self.base)
            self.assertEqual(result["input_tokens"], Decimal(864000000))
            self.assertEqual(result["output_tokens"], Decimal(108000000))
            self.assertEqual(result["cost"], Decimal(1404))

    def test_azure_hour_and_memory_units(self):
        result = runtime_cost(self.rates["providers"]["azure"]["runtime"],
                              self.common, self.base, 0)
        self.assertEqual(result["cpu_hours"], Decimal(900))
        self.assertEqual(result["native_memory_unit_hours"], Decimal(1800))
        self.assertEqual(result["cost"], Decimal("110.7000"))

    def test_idle_tail_is_provider_specific(self):
        azure = runtime_cost(self.rates["providers"]["azure"]["runtime"],
                             self.common, self.base, 120)
        google = runtime_cost(self.rates["providers"]["gcp"]["runtime"],
                              self.common, self.base, 120)
        self.assertEqual(azure["cost"], Decimal("553.5000"))
        self.assertEqual(google["cost"], Decimal("92.700"))
        azure_default_tail = runtime_cost(self.rates["providers"]["azure"]["runtime"],
                                          self.common, self.base, 900)
        self.assertEqual(azure_default_tail["cost"], Decimal("3431.7000"))

    def test_aws_active_cpu_and_explicit_memory_conversion(self):
        runtime = self.rates["providers"]["aws"]["runtime"]
        result = runtime_cost(runtime, self.common, self.base, 0)
        alternate = runtime_cost(runtime, self.common, self.base, 0, aws_gb_as_gib=True)
        self.assertEqual(result["cpu_hours"], Decimal(270))
        self.assertEqual(result["cost"], Decimal("42.42934842624"))
        self.assertEqual(alternate["cost"], Decimal("41.17500"))

    def test_review_cost_and_accepted_task_denominator(self):
        result = calculate("azure", self.rates, self.common, self.base)
        self.assertEqual(result["review_usd"], "11250.00")
        self.assertEqual(result["accepted_tasks"], "95000.00")
        self.assertEqual(result["synthetic_gross_realized_capacity_value_usd"], "142500.00")
        self.assertEqual(result["model_runtime_lower_bound_usd"], "1514.70")
        self.assertGreater(Decimal(result["synthetic_tco_usd"]), Decimal("30000"))

    def test_cost_rises_across_synthetic_scenarios(self):
        for provider in self.rates["providers"]:
            values = [Decimal(calculate(provider, self.rates, self.common,
                                        self.inputs["scenarios"][name])["synthetic_tco_usd"])
                      for name in ("low", "base", "high")]
            self.assertLess(values[0], values[1])
            self.assertLess(values[1], values[2])

    def test_missing_price_is_an_error_not_free(self):
        del self.rates["providers"]["azure"]["model"]["input_usd_per_million_tokens"]
        with self.assertRaises(KeyError):
            calculate("azure", self.rates, self.common, self.base)

    def test_invalid_quantities_are_rejected(self):
        for value in [True, False, None, -1, "NaN", "Infinity", 1.5, "oops"]:
            with self.subTest(value=value), self.assertRaises(ValueError):
                number(value)
        self.base["review_fraction"] = "1.01"
        with self.assertRaises(ValueError):
            calculate("gcp", self.rates, self.common, self.base)

    def test_cache_assumption_cannot_silently_change_formula(self):
        self.common["cache_read_fraction"] = "0.5"
        with self.assertRaises(ValueError):
            calculate("gcp", self.rates, self.common, self.base)

    def test_inputs_are_not_mutated(self):
        original = deepcopy((self.rates, self.common, self.base))
        calculate("aws", self.rates, self.common, self.base)
        self.assertEqual((self.rates, self.common, self.base), original)


if __name__ == "__main__":
    unittest.main()
