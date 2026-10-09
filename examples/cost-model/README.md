# Reproduce the pricing and economics scenarios

This offline Python standard-library calculator uses a **2026-10-09 public-rate snapshot** and **invented workloads/TCO allowances**. It makes no cloud requests, deploys nothing, and needs no credentials or packages. The output is a planning calculation, not a measured benchmark or a quote.

From the repository root, with Python 3.9 or later:

```console
python examples/cost-model/calculator.py
python -m unittest discover -s examples/cost-model -p "test_*.py" -v
python examples/cost-model/calculator.py --aws-gb-as-gib
```

Read [the pricing chapter](../../docs/pricing-and-economics.md) before interpreting the results. [rates.json](rates.json) separates sourced list prices, model identifiers, endpoint modes, units, dates, and public catalog meter IDs from [scenarios.json](scenarios.json), whose quantities and allowances are entirely synthetic. The calculator uses decimal arithmetic and rounds monetary display values only at output.

The same Claude Haiku 4.5 model family and global online pricing mode anchor all three model rows. No quality equivalence between different models is asserted. Actual behavior and billable token counts still need testing on each endpoint. Google lists an earliest possible retirement of 2026-10-15; this dated example is not a recommendation to begin a long-lived deployment on that model.

The base workload is 100,000 submitted tasks, 1.08 full attempts per task, 8,000 aggregate input tokens and 1,000 aggregate output tokens per attempt. Aggregates include all agent-loop calls, repeated context, tool schemas/results, and billable reasoning output. Retries multiply the aggregate once. Every attempt starts an independent session and incurs one selected post-request tail; retries sharing a session need a different session-count model. Caching and batching are zero in every case; unsupported nonzero values fail explicitly.

Runtime modeling distinguishes allocated resources from consumed CPU. The no-tail line excludes post-request lifetime and other resources, so it is only a lower bound under the specified list-rate assumptions. Synthetic TCO includes the scenario's idle tail, human review, operations, amortized build, variable ancillary allowance, fixed platform allowance, evaluation-token allowance, and contingency. Allowances are not vendor prices. No free tiers, discounts, taxes, or currency conversion are applied.

AWS publishes memory as **GB-hours**, while Google and Azure publish **GiB-hours**. The default explicitly converts 2 GiB to 2.147483648 decimal GB. The final command tests treating the AWS GB label as a binary unit instead. This is an unresolved billing-definition sensitivity, not an asserted definition of AWS's invoice meter. Verify that definition and the v1/v2 runtime choice before using a procurement estimate.

Missing prices raise an error rather than becoming zero. Tests cover token aggregation, retries, hour conversion, provider-specific idle behavior, memory-unit sensitivity, human review, the accepted-task denominator, invalid quantities, and input immutability. Refresh rates and sources together, then rerun tests and update the chapter's tables.
