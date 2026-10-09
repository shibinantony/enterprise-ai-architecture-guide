# Pricing evidence ledger

Checked **2026-10-09**. Public primary sources only. Amounts are USD list rates, not customer quotes. A check date does not change a source's publication date. Rates, billing units, deployment modes, and source links are also recorded in [rates.json](../examples/cost-model/rates.json); workloads and TCO allowances live separately in [scenarios.json](../examples/cost-model/scenarios.json).

## Model-price evidence

| Source | What was verified | Evidence limitation |
| --- | --- | --- |
| [Google model pricing](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing) | Claude Haiku 4.5 global online input $1.00 and output $5.00 per million tokens; regional rows differ. | The old Vertex AI pricing URL redirects here. Avoid stale cached preview-price snippets. |
| [Google Haiku 4.5 model card](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/claude/haiku-4-5) | `claude-haiku-4-5`; GA; global endpoint; 200K input context; retirement not sooner than 2026-10-15. | Earliest retirement is close to this research date; no long-term availability promise. |
| [Anthropic platform-specific price sheet, dated 2026-05-27](https://www-cdn.anthropic.com/files/4zrzovbb/website/3684c2faafb97418665782cea0001f439f74b1d2.pdf) | Printed page 6: Bedrock Haiku 4.5 global $1/$5; geographic/in-region $1.10/$5.50. Printed pages 10 and 12 corroborate Google and Foundry global $1/$5. | Older dated commercial evidence; not an independently refreshed AWS offer on the check date. |
| [AWS-maintained cost guide](https://github.com/aws-solutions-library-samples/guidance-for-claude-code-with-amazon-bedrock/blob/main/assets/docs/COST_ESTIMATES.md) | Haiku 4.5 $1/$5 per million, cached input $0.10. | Guide says June 2026 estimates; corroboration, not a binding current tariff. |
| [AWS model card](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-anthropic-claude-haiku-4-5.html) | Global inference profile `global.anthropic.claude-haiku-4-5-20251001-v1:0`; Standard mode and us-east-1 global source endpoint supported. | Global inference may leave the source region. The model card distinguishes `bedrock-runtime` from `bedrock-mantle`; the example uses the former. |
| [Microsoft model availability](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/claude-models) | `claude-haiku-4-5` lists both hosting versions GA; Global Standard supported. | The example selects Anthropic-hosted version 1. Hosting, contracting, and residency are distinct from model-name parity. |
| [Current Anthropic pricing and Foundry billing](https://platform.claude.com/docs/en/about-claude/pricing#claude-in-microsoft-foundry-pricing), [Microsoft CCU documentation](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/claude-models-billing) | Foundry usage is rated at model/feature prices and converted to Claude Consumption Units; current Haiku 4.5 input/output rate is $1/$5 per million. | Customer discounts and offer terms can change the payable amount. CCUs are an invoice unit, not tokens. |

The current AWS pricing page's extracted HTML did not expose the Haiku rows. A read-only request to the public `AmazonBedrock` price-list file completed, but the selected model-name filter returned no matching product; this was **not** interpreted as a missing product, a zero price, or price verification. AWS's row therefore retains its older source dates and explicitly requires offer revalidation. The same-model comparison is a transparent rate-card scenario, not a guaranteed October tariff.

## Runtime evidence

| Source | Verified fact | Interpretation used |
| --- | --- | --- |
| [Google Agent Platform pricing](https://cloud.google.com/products/gemini-enterprise-agent-platform/pricing) | Standard Agent Compute $0.085/vCPU-hour and Agent Memory $0.009/GiB-hour; allocated resources; idle intervals between turns excluded. | Public page's indexed official text was readable; direct full-page fetches failed. Free monthly allowances are deliberately excluded from the comparison. |
| [AWS AgentCore pricing](https://aws.amazon.com/bedrock/agentcore/pricing/) | Runtime microVM v1 $0.0895/vCPU-hour and $0.00945/GB-hour; v2 $0.1276 and $0.0169; CPU based on consumption, not allocated wall time. | Only v1 is calculated. GB is preserved as published. Decimal versus binary interpretation is an explicit calculator sensitivity. |
| [AWS usage metrics](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-runtime-metrics.html) | CPU-hour and memory-GB-hour usage metrics are available; telemetry and authoritative billing can differ. | Reconcile a pilot against billed meters; monitoring graphs alone do not establish invoice equivalence. |
| [Foundry Agent Service pricing](https://azure.microsoft.com/en-us/pricing/details/foundry-agent-service/) | Hosted CPU unit is vCPU-hour; memory unit is GiB-hour. | Static HTML displayed `$-`, not a rate. Unit labels resolve the retail API's generic `1 Hour` field. |
| [Foundry hosted-agent lifecycle](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/hosted-agents) | Per-session sandbox; active-session CPU/memory billing; idle timeout configurable from 2 to 60 minutes, default 15. | Calculator includes declared post-request tails. This is a conservative allocation-duration assumption to validate against a bill, not measured metering behavior. |

## Exact Azure retail lookup

The unauthenticated [Microsoft Retail Prices API query](https://prices.azure.com/api/retail/prices?$filter=contains(productName,%27Agent%27)%20and%20armRegionName%20eq%20%27eastus2%27&currencyCode=%27USD%27) returned 14 records and `NextPageLink: null` on the check date. Filtered relevant public records:

| Field | CPU | Memory |
| --- | --- | --- |
| Product / SKU / type | Foundry Agents / Hosted / Consumption | Foundry Agents / Hosted / Consumption |
| Region / currency | eastus2 / USD | eastus2 / USD |
| Meter | Hosted vCPU Usage | Hosted Memory Usage |
| Retail price | 0.0994 | 0.0118 |
| API unit | 1 Hour | 1 Hour |
| Effective from | 2026-02-01 | 2026-02-01 |
| Meter ID | bc9e699b-af61-53a1-97e8-66bac4f5b115 | 9553cdec-3a26-54dc-bebd-ca28a87ad5e9 |

These IDs are public catalog identifiers. No customer account was queried. [API documentation](https://learn.microsoft.com/en-us/rest/api/cost-management/retail-prices/azure-retail-prices) explains the retail endpoint and filters. The rates are not borrowed from Azure Container Apps or another unrelated compute service.

## Revalidation rules

Before procurement, verify model lifecycle, hosting version, approved inference geography, regional runtime availability, memory-unit definition, quotas, marketplace offer, active-session accounting, discounts, and omitted service meters. Preserve a fresh quote or catalog snapshot with its date. Unpriced features remain **quote required**; preview status alone never means free. No deployment, latency test, quality test, or actual cloud bill was produced for this research.
