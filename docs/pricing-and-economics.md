# Pricing and economics: buy an accepted business outcome

For the workload below, the same model's token charge is **$1,404 per month on each cloud's selected rate card**. Compute adds tens to hundreds of dollars; the synthetic operating model adds tens of thousands. A director should therefore choose an acceptable delivery model and measure the complete cost of a successful task before negotiating small differences in runtime rates.

This chapter separates three things: sourced public prices, calculated workload costs, and invented planning assumptions. Prices were researched on **2026-10-09**, in **USD**, excluding tax, negotiated discounts, commitments, and free allowances. Source publication dates and unresolved details remain visible in the [evidence ledger](../research/pricing-source-notes.md). Nothing here is a measured quality benchmark or a supplier quote.

## 1. Start with value and an acceptance condition

For service recovery, define success as a correctly resolved case with an authorized outcome, an understandable response, and no avoidable repeat contact. A faster answer that creates another case is not the outcome being purchased.

Track cost per **accepted task**, elapsed resolution time, repeat-contact rate, escalation rate, and customer outcome together. Separate four possible benefits: released staff capacity, fewer errors or losses, faster throughput, and improved experience. A reduction in staff minutes is capacity value; it becomes cash savings only when an actual spending decision changes. Assign an owner and baseline to each benefit.

The economic test is whether measurable benefit exceeds the complete operating and change cost under a credible downside scenario. This preserves room for agents that improve service without reducing headcount, and rejects cheap demonstrations that create expensive supervision or rework.

## 2. A defensible same-model comparison

Claude Haiku 4.5 provides a common model family across the three platforms. The selected modes are online, global, standard/pay-as-you-go inference, with every request below 200,000 input tokens. They are not regional-sovereignty equivalents. Current availability documentation supports these endpoints; model access and quotas still require account-level validation. [Google model card](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/claude/haiku-4-5), [Microsoft model availability](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/claude-models), [AWS model card](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-anthropic-claude-haiku-4-5.html).

| Platform | Exact model / selected deployment | Input / million tokens | Output / million tokens |
| --- | --- | ---: | ---: |
| Google Cloud | `claude-haiku-4-5`; global endpoint | $1.00 | $5.00 |
| Microsoft Azure | `claude-haiku-4-5`; Global Standard, Anthropic-hosted version 1; East US 2 resource endpoint | $1.00 | $5.00 |
| AWS | `global.anthropic.claude-haiku-4-5-20251001-v1:0`; Bedrock Standard Global Cross-Region, us-east-1 source | $1.00 | $5.00 |

Google publishes these amounts in its [model price table](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing). Azure's selected offer rates tokens using [Anthropic's current model prices and Foundry CCU conversion](https://platform.claude.com/docs/en/about-claude/pricing#claude-in-microsoft-foundry-pricing). AWS figures are supported by the [model vendor's dated platform price sheet](https://www-cdn.anthropic.com/files/4zrzovbb/website/3684c2faafb97418665782cea0001f439f74b1d2.pdf), with [AWS-maintained June 2026 guidance](https://github.com/aws-solutions-library-samples/guidance-for-claude-code-with-amazon-bedrock/blob/main/assets/docs/COST_ESTIMATES.md) as corroboration. The AWS tariff needs offer revalidation: its dynamically rendered current pricing rows were not independently extracted.

Google lists retirement **not sooner than October 15, 2026**. This makes Haiku 4.5 useful as a dated comparison anchor, not a recommendation for a new long-lived deployment. Matching model names also does not prove identical quality, latency, token accounting, or service behavior. Test the same corpus and acceptance rubric on each endpoint.

Caching, batch processing, priority tiers, provisioned throughput, images, audio, and search charges are excluded from this baseline. Cache reads, cache creation, TTL, and eligible prefix length need separate accounting; an advertised cache discount cannot be applied to every input token. An asynchronous batch price is not an interactive-agent price. If substituting native models, label the result a **different-model rate scenario**, then evaluate quality and token usage again.

## 3. Standardize the work before multiplying rates

The base scenario submits 100,000 tasks per month. Each attempted task uses 8,000 aggregate input tokens and 1,000 aggregate output tokens across its complete agent loop. These totals include repeated conversation history, tool definitions, retrieved content, tool results, and any billable reasoning output. They are not a single user prompt multiplied by an arbitrary call count.

Assume 8% of tasks incur one complete additional attempt: 108,000 attempts. Each attempt starts an independent session, so any post-request tail applies once per attempt. This deliberately simple retry assumption multiplies both token and runtime usage once. A production model should replace it with measured partial retries, session reuse, fallbacks, and failed-call billing.

```text
Input  = 100,000 × 1.08 × 8,000 = 864 million tokens
Output = 100,000 × 1.08 × 1,000 = 108 million tokens
Model  = 864 × $1 + 108 × $5 = $1,404 per month
```

Every cloud receives the same submitted tasks and token totals. This isolates the selected prices. It does not claim an actual deployment will consume identical tokens. The 95% accepted-outcome assumption later in this chapter is also synthetic; a paid attempt can fail acceptance.

## 4. Runtime: compare resource demand and billing behavior

Use one vCPU, 2 GiB memory, and 30 seconds per attempted task, with CPU actually busy for 30% of that interval. This means 900 session-hours, 900 allocated vCPU-hours, 270 consumed vCPU-hours, and 1,800 GiB-hours before any post-request lifetime.

| Runtime and price scope | CPU / hour | Memory / hour | No-tail base runtime |
| --- | ---: | ---: | ---: |
| Google Agent Runtime, published standard USD Scale rate | $0.085 / vCPU | $0.009 / GiB | $92.70 |
| Azure Foundry Hosted, eastus2 Consumption | $0.0994 / vCPU | $0.0118 / GiB | $110.70 |
| AWS AgentCore microVM **v1**, commercial consumption | $0.0895 / vCPU | $0.00945 / GB | $41.18–$42.43 |

Google bills allocated runtime resources and excludes waiting between turns. AWS v1 charges consumed CPU; memory remains relevant during session lifetime. Azure uses per-session sandboxes. These are different meters applied to the same declared demand, not proof that equal configured machines deliver equal performance. [Google runtime pricing](https://cloud.google.com/products/gemini-enterprise-agent-platform/pricing), [AWS runtime pricing](https://aws.amazon.com/bedrock/agentcore/pricing/), [Azure lifecycle](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/hosted-agents).

Azure amounts come from the public [Retail Prices API lookup](https://prices.azure.com/api/retail/prices?$filter=contains(productName,%27Agent%27)%20and%20armRegionName%20eq%20%27eastus2%27&currencyCode=%27USD%27), not an unrelated container service. Its [pricing page](https://azure.microsoft.com/en-us/pricing/details/foundry-agent-service/) provides the vCPU-hour/GiB-hour labels; the API supplies the amounts. Public meter identifiers are preserved in the rate file.

AWS labels memory **GB**, while the others say **GiB**. The calculator defaults to 2 GiB = 2.147483648 decimal GB; an alternative binary interpretation produces the lower end of the range. The source did not resolve that billing-definition detail. Preserve it as a procurement question rather than silently equating units. AWS v2 has different published rates and reclamation behavior and is excluded.

With no post-request tail, model plus runtime is **$1,496.70 Google, $1,514.70 Azure, and $1,446.43 AWS** using the decimal assumption. These are **partial cost floors under the stated list-rate assumptions**, not complete bills. Startup, system overhead, extra resources, and billable session lifetime remain material.

Azure's documented idle timeout is 2–60 minutes, default 15. Under an allocation-duration assumption, 120 extra seconds per base attempt raises its runtime line to **$553.50**; 900 seconds raises it to **$3,431.70**. The base synthetic TCO uses 120 seconds for Azure and AWS v1, with zero background CPU during that tail; Google waiting between turns remains excluded. Confirm actual billed lifecycle behavior in a pilot. Do not use a 30-second response latency as a 30-second invoice duration.

## 5. The bill of materials extends beyond inference

Record each required component, its billable unit, quantity, ownership, and quote status. The following costs are omitted from the partial floor and must be priced or explicitly budgeted:

| Cost family | Quantities to obtain |
| --- | --- |
| Data and retrieval | Document ingestion, parsing/OCR, embedding refresh, index capacity, retrieval and reranking calls |
| Tools and grounding | Gateway operations, external APIs, web search, connector licences, browser/code sessions, downstream transactions |
| State and storage | Session history, memory generation, checkpoints, object/vector storage, backups and retention |
| Networking and security | Private endpoints, NAT, egress, key operations, policy services and inspection |
| Assurance and telemetry | Evaluation-model tokens, native evaluator fees, trace/log ingestion, retention, queries and incident investigation |
| People and change | Review, exceptions, on-call operations, connector maintenance, release validation, training and retirement |

Azure explicitly separates tool and knowledge costs from native prompt/workflow agent charges. AWS separately meters AgentCore capabilities and observability. Google prices compute, memory, and storage across its agent services. A bundled orchestration fee therefore does not establish a free workflow. Any unpriced or preview-dependent component remains **quote required**; do not put zero in the budget merely because a page shows a dash.

## 6. Full synthetic TCO sensitivity

The following **invented** scenarios hold submitted volume at 100,000 tasks. They change complexity and operating burden, not provider capability. The same human and platform assumptions apply across clouds so the table does not manufacture an operating advantage for a supplier.

| Planning input | Low | Base | High |
| --- | ---: | ---: | ---: |
| Attempts per task | 1.02 | 1.08 | 1.20 |
| Aggregate input/output tokens per attempt | 4,000 / 500 | 8,000 / 1,000 | 16,000 / 2,000 |
| Active session seconds / CPU-busy share | 15 / 20% | 30 / 30% | 60 / 50% |
| Azure/AWS post-request tail, seconds | 0 | 120 | 900 |
| Accepted outcomes | 98% | 95% | 90% |
| Tasks reviewed / minutes per review | 2% / 2 | 5% / 3 | 12% / 5 |
| Operations hours per month | 40 | 80 | 160 |
| Initial build, amortized over 12 months | $30,000 | $60,000 | $120,000 |
| Variable ancillary allowance / submitted task | $0.005 | $0.015 | $0.040 |
| Fixed platform allowance / month | $500 | $1,500 | $4,000 |
| Extra evaluation token budget | 1% | 5% | 10% |
| Contingency on modeled subtotal | 10% | 20% | 30% |

Review labor is $45/hour; operations labor is $75/hour. These loaded rates are assumptions. Variable and fixed allowances cover unitemized technology services from the preceding table; they are placeholders to replace with a priced bill of materials, not vendor charges. Evaluation uses a percentage of production token cost; native evaluation fees belong in the ancillary allowance. Contingency is uncertainty provision, not expenditure already incurred.

```text
Monthly TCO = model + runtime including declared tail + review
            + operations + amortized build + ancillary allowances
            + evaluation token allowance + contingency
```

| Calculated monthly synthetic TCO | Low | Base | High |
| --- | ---: | ---: | ---: |
| Google Cloud | $11,234.75 | $32,180.28 | $102,229.40 |
| Microsoft Azure | $11,244.10 | $32,733.24 | $107,078.40 |
| AWS, v1 and decimal-GB assumption | $11,204.45 | $32,207.62 | $102,922.17 |

Base cost per accepted task is **$0.3387, $0.3446, and $0.3390**, respectively. These small cross-cloud differences are dominated by the declared workload, tail, and staffing assumptions. They do not establish a cheapest production platform. Most economic uncertainty sits between low and high, not between provider columns.

## 7. Decisions that change the business case

In the base case, review alone costs **$11,250/month**. One additional percentage point of tasks requiring a three-minute review adds **$2,250** before contingency. A 10% reduction in this scenario's model charge saves **$140.40**. Improving task design, retrieval relevance, and review quality can therefore matter more than a modest token discount. Do not remove necessary review to make the spreadsheet attractive.

For a benefit illustration, assume each accepted task releases four gross minutes valued at $45/hour and only half of that capacity is realized. At 95,000 accepted tasks, modeled gross realized capacity value is **$142,500/month**, before the modeled operating costs. This is not booked savings. Validate released time, redeployment, incremental revenue, and rework with the process owner; avoid counting the same benefit in several use cases. Build cost is already amortized in TCO and must not be counted again as a recurring charge.

A sensible approval sequence is: establish the manual baseline; run the same representative tasks on candidate endpoints; collect accepted outcomes and actual usage; reconcile modeled cost to billing; replace allowances with quotes; then choose the platform whose full cost and operating fit support the outcome. Keep task, token, tool-call, runtime, and review budgets visible during rollout. Reassess after changes in model, retrieval corpus, prompt, tool schema, or autonomy.

## 8. Reproduce and refresh

The [offline calculator](../examples/cost-model/README.md) uses decimal arithmetic and contains meaningful unit, retry, missing-price, and sensitivity tests. From the repository root:

```console
python examples/cost-model/calculator.py
python -m unittest discover -s examples/cost-model -p "test_*.py" -v
python examples/cost-model/calculator.py --aws-gb-as-gib
```

Update rates, lifecycle evidence, regional scope, and workload assumptions together. Keep unverified quantities visible. The useful decision artifact is a reproducible cost per accepted outcome with an accountable benefit owner, not a timeless ranking of clouds.
