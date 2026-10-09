"""Reproduce illustrative agent economics offline with exact decimal arithmetic.

Rates are a dated public-price snapshot. Workloads and non-rate TCO inputs are
synthetic. This is neither an invoice estimator nor a deployment benchmark.
"""

import argparse
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
MILLION = Decimal(1000000)
HOUR = Decimal(3600)
GIB_IN_DECIMAL_GB = Decimal(1073741824) / Decimal(1000000000)


def number(value, *, minimum=Decimal(0), maximum=None):
    """Reject missing, boolean, negative, and non-finite quantities."""
    if type(value) not in (str, int, Decimal):
        raise ValueError("Use integers or decimal strings, not booleans/floats")
    try:
        parsed = Decimal(value)
    except InvalidOperation as error:
        raise ValueError("Invalid decimal") from error
    if not parsed.is_finite() or parsed < minimum:
        raise ValueError("Invalid or out-of-range number")
    if maximum is not None and parsed > maximum:
        raise ValueError("Number exceeds maximum")
    return parsed


def money(value):
    return format(value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP), "f")


def model_cost(model, common, scenario):
    attempts = number(common["tasks_per_month"]) * number(
        scenario["attempts_per_task"], minimum=Decimal(1))
    input_tokens = attempts * number(scenario["input_tokens_per_attempt"])
    output_tokens = attempts * number(scenario["output_tokens_per_attempt"])
    cost = (input_tokens * number(model["input_usd_per_million_tokens"])
            + output_tokens * number(model["output_usd_per_million_tokens"])) / MILLION
    return {"input_tokens": input_tokens, "output_tokens": output_tokens,
            "attempts": attempts, "cost": cost}


def runtime_cost(runtime, common, scenario, idle_tail_seconds, *, aws_gb_as_gib=False):
    attempts = number(common["tasks_per_month"]) * number(
        scenario["attempts_per_task"], minimum=Decimal(1))
    wall_seconds = number(scenario["session_seconds_per_attempt"])
    tail = number(idle_tail_seconds) if runtime["bill_idle_tail"] else Decimal(0)
    cpu_fraction = number(scenario["cpu_active_fraction"], maximum=Decimal(1))
    if runtime["metering"] == "allocated":
        cpu_seconds = wall_seconds + tail
    elif runtime["metering"] == "active_cpu":
        # The scenario assumes no background CPU during the post-request tail.
        cpu_seconds = wall_seconds * cpu_fraction
    else:
        raise ValueError("Unknown runtime metering mode")
    memory_units = number(common["memory_gib"])
    if runtime["memory_unit"] == "GB":
        if not aws_gb_as_gib:
            memory_units *= GIB_IN_DECIMAL_GB
    elif runtime["memory_unit"] != "GiB":
        raise ValueError("Unknown memory unit")
    cpu_hours = attempts * number(common["vcpus"]) * cpu_seconds / HOUR
    memory_hours = attempts * memory_units * (wall_seconds + tail) / HOUR
    cost = (cpu_hours * number(runtime["vcpu_usd_per_hour"])
            + memory_hours * number(runtime["memory_usd_per_unit_hour"]))
    return {"cpu_hours": cpu_hours, "native_memory_unit_hours": memory_hours,
            "cost": cost}


def calculate(provider, rates, common, scenario, *, aws_gb_as_gib=False):
    if rates["schema_version"] != 1 or rates["currency"] != "USD":
        raise ValueError("Unsupported rates schema or currency")
    if number(common["cache_read_fraction"]) != 0 or number(common["batch_fraction"]) != 0:
        raise ValueError("This baseline does not implement cache/batch accounting")
    details = rates["providers"][provider]  # Unknown providers fail; never use a zero fallback.
    token = model_cost(details["model"], common, scenario)
    floor_runtime = runtime_cost(details["runtime"], common, scenario, 0,
                                 aws_gb_as_gib=aws_gb_as_gib)
    runtime = runtime_cost(details["runtime"], common, scenario,
                           scenario["idle_tail_seconds"][provider],
                           aws_gb_as_gib=aws_gb_as_gib)
    tasks = number(common["tasks_per_month"], minimum=Decimal(1))
    accepted = tasks * number(scenario["accepted_fraction"], minimum=Decimal("0.000001"),
                             maximum=Decimal(1))
    review = (tasks * number(scenario["review_fraction"], maximum=Decimal(1))
              * number(scenario["review_minutes"]) / Decimal(60)
              * number(common["reviewer_usd_per_hour"]))
    operations = number(scenario["operations_hours"]) * number(common["operations_usd_per_hour"])
    build = number(scenario["build_usd"]) / number(
        common["build_amortization_months"], minimum=Decimal(1))
    ancillary = tasks * number(scenario["ancillary_usd_per_task"])
    fixed = number(scenario["fixed_platform_usd"])
    evaluation = token["cost"] * number(scenario["evaluation_token_budget_fraction"])
    subtotal = token["cost"] + runtime["cost"] + review + operations + build + ancillary + fixed + evaluation
    contingency = subtotal * number(scenario["contingency_fraction"], maximum=Decimal(1))
    total = subtotal + contingency
    capacity = (accepted * number(common["gross_minutes_released_per_accepted_task"])
                / Decimal(60) * number(common["reviewer_usd_per_hour"])
                * number(common["capacity_realization_fraction"], maximum=Decimal(1)))
    return {
        "provider": provider,
        "attempts": format(token["attempts"], "f"),
        "input_tokens": format(token["input_tokens"], "f"),
        "output_tokens": format(token["output_tokens"], "f"),
        "model_usd": money(token["cost"]),
        "runtime_no_tail_usd": money(floor_runtime["cost"]),
        "model_runtime_lower_bound_usd": money(token["cost"] + floor_runtime["cost"]),
        "runtime_with_scenario_tail_usd": money(runtime["cost"]),
        "review_usd": money(review),
        "operations_usd": money(operations),
        "amortized_build_usd": money(build),
        "ancillary_variable_allowance_usd": money(ancillary),
        "fixed_platform_allowance_usd": money(fixed),
        "evaluation_token_allowance_usd": money(evaluation),
        "contingency_usd": money(contingency),
        "synthetic_tco_usd": money(total),
        "accepted_tasks": format(accepted, "f"),
        "synthetic_usd_per_accepted_task": format(total / accepted, ".4f"),
        "synthetic_gross_realized_capacity_value_usd": money(capacity),
        "aws_memory_interpretation": "binary sensitivity" if aws_gb_as_gib else "decimal GB assumption",
    }


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--rates", type=Path, default=HERE / "rates.json")
    parser.add_argument("--scenarios", type=Path, default=HERE / "scenarios.json")
    parser.add_argument("--aws-gb-as-gib", action="store_true",
                        help="Test the alternative interpretation of AWS's published GB label")
    args = parser.parse_args()
    try:
        rates, assumptions = load(args.rates), load(args.scenarios)
        if assumptions["schema_version"] != 1:
            raise ValueError("Unsupported scenario schema")
        results = []
        for scenario_name, scenario in assumptions["scenarios"].items():
            for provider in rates["providers"]:
                results.append({"scenario": scenario_name, **calculate(
                    provider, rates, assumptions["common"], scenario,
                    aws_gb_as_gib=args.aws_gb_as_gib)})
        print(json.dumps({"checked_on": rates["checked_on"], "currency": "USD",
                          "notice": assumptions["notice"], "results": results}, indent=2))
        return 0
    except (OSError, ValueError, KeyError, TypeError) as error:
        parser.exit(2, "Calculation failed: " + str(error) + "\n")


if __name__ == "__main__":
    raise SystemExit(main())
