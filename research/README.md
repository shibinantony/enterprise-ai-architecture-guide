# Research method and evidence map

## Scope

This guide connects business value, process redesign, enterprise architecture, hyperscaler capabilities, pricing, delivery, operations, and organizational change. Google Cloud is the detailed implementation path; Azure and AWS are compared at equivalent logical layers.

The primary-source review date is **2026-10-09 UTC**. This is a focused technical and commercial-documentation review, not a systematic literature review, production case study, or cloud benchmark.

Use the [topic coverage map](topic-coverage.md) to locate the practical examples, technical foundations, strategic decisions, and operating guidance. The [three-tool walkthrough](../docs/from-prompt-to-enterprise-service.md) and [industry portfolio](../docs/use-case-portfolio.md) are proposed designs, not reported deployments.

## Evidence registers

| Register | What it supports |
|---|---|
| [Google Cloud](gcp-source-notes.md) | Current service names, architecture components, development/deployment paths, limitations |
| [Cross-cloud comparison](cross-cloud-source-notes.md) | Equivalent layers, runtime differences, data, integration, identity, operations, distribution |
| [Pricing](pricing-source-notes.md) | Exact public rates, deployment modes, units, dates, lifecycle and billing caveats |
| [MCP](mcp-source-notes.md) | Protocol facts pinned to the 2026-07-28 revision |
| [Assurance](assurance-source-notes.md) | Supporting risk, identity, security, and organizational guidance |

The [NIST zero trust architecture](https://csrc.nist.gov/pubs/sp/800/207/final) supports the resource-oriented access discussion in the reference architecture. The business process, team design, adoption sequence, scorecards, and economic scenarios are this guide's proposed analytical framework.

## Evidence classes

| Class | Meaning |
|---|---|
| Documented capability | Official service or protocol documentation; deployed support still depends on version, region, and configuration |
| Sourced price | Public list rate for a named SKU, unit, location/deployment scope, and review date |
| Proposed architecture | A design recommendation, with alternatives and implementation responsibilities |
| Illustrative assumption | Invented workload, volume, staffing, price allocation, or benefit input used to explain a calculation |
| Synthetic demonstration | Local code and fictional records; no deployed platform or real transaction |
| Observed result | A local check actually executed, with stated scope; not evidence of production behavior |

No provider is ranked universally. Matching a model name or nominal resource size does not eliminate differences in serving, billing, data processing, support, or task behavior.

## Comparison method

Use one business workload and common acceptance criteria. Separate a controlled same-model trial from a native-optimized design comparison. Separate model inference, agent hosting, retrieval/data, integration, distribution, and operations so products at different layers are not treated as direct substitutes.

Prices are compared with explicit usage assumptions. Token estimates include the whole modeled task rather than one nominal message. Missing or unpriced items must remain visible rather than silently count as free. A total-cost scenario includes synthetic inputs and is not a provider quote.

## Research limits

No hyperscaler workload was deployed, performance tested, or billed for this guide. Public pricing does not establish negotiated rates, enterprise discounts, taxes, support fees, exact invoice behavior, or future availability. Model retirement, region, quota, and preview/GA status require revalidation before procurement or deployment.

Official pages can disagree or describe different modes. The registers record material ambiguities instead of silently resolving them in favor of a platform. Mutable pages and APIs may change after review; preserve approved evidence in an enterprise decision record.

No confidential proposal, private customer evidence, internal architecture, personal records, or employer/client lineage is used. Business scenarios are fictional. No achieved ROI or universal legal compliance is claimed.

## Maintenance

Refresh product and price evidence before a purchasing decision and when the target configuration changes. Recheck model lifecycle dates, serving location, runtime mode, units, minima, and version compatibility. Update the rate file, calculator expectations, chapter, and source register together.

Maintain source-backed claims separately from recommendations and forecasts. Record changes in [CHANGELOG.md](../CHANGELOG.md). See [CONTRIBUTING.md](../CONTRIBUTING.md).
