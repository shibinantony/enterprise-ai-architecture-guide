# Research method and evidence map

## Purpose and method

This guide develops a provider-neutral architecture and operating model for MCP-enabled enterprise agents. The source review used publicly available primary standards and guidance, reviewed on **2026-10-09 UTC**. It is a focused technical review, not a systematic literature review or empirical comparison of commercial platforms.

The protocol baseline is **MCP 2026-07-28**, which the official latest-specification link resolved to at review time. Versioned links are preferred. Mutable guidance and extensions are recorded with a review date; their contents may subsequently change.

Sources were selected for direct relevance to protocol semantics, identity, security, and organizational risk. Product marketing, confidential materials, and unverified quantitative claims were excluded. No provider ranking or endorsement is implied by a protocol or standards citation.

## Evidence classes

| Class | Meaning in this repository |
|---|---|
| Protocol fact | A claim tied to a specified version of the official MCP documentation |
| External guidance | Advice from a named primary standards or security organization; applicability requires judgment |
| Proposed design | The guide's architecture, control pattern, tier, metric, template, or decision framework |
| Synthetic demonstration | Locally executable examples using fictional data; no production integration |
| Unvalidated hypothesis | Expected value or reuse benefits that require enterprise measurement |

Recommendations are written as design choices rather than attributed mandates. Risk tiers, scores, thresholds, and time boxes are illustrative. This repository claims no legal compliance, accreditation, production safety certification, or measured business return.

## Claim-to-source map

| Topic | Evidence | Scope and limitation |
|---|---|---|
| Host/client/server, tools, resources, prompts | [MCP source register](mcp-source-notes.md) | Protocol and intended interaction patterns; not business authority |
| HTTP authorization and token boundaries | [MCP source register](mcp-source-notes.md) | Transport-scoped requirements; not a complete enterprise policy model |
| Revision and compatibility changes | [MCP source register](mcp-source-notes.md) | 2026-07-28 baseline; actual host/SDK support needs testing |
| Prompt injection, confused deputy, excessive agency | [Assurance source register](assurance-source-notes.md) | Threat guidance; adopting a checklist does not prove protection |
| Organizational AI risk management | [Assurance source register](assurance-source-notes.md) | Voluntary risk framework; not certification or sector-specific legal advice |
| Explicit trust boundaries | [NIST SP 800-207](https://csrc.nist.gov/pubs/sp/800/207/final) | Zero trust architecture guidance; agent-specific mapping is proposed here |
| Return on investment, platform choice, adoption sequence | [Executive brief](../docs/executive-brief.md), [decision framework](../docs/platform-decision-framework.md), [roadmap](../docs/adoption-roadmap.md) | Original analytical frameworks; no measured results claimed |
| Policy decision behavior | [Synthetic example](../examples/service-recovery/README.md) | Local fixture and unit tests; no identity or transaction integration |

## Limitations and open questions

The review does not benchmark tool-selection accuracy, cost, scale, or human review behavior. It does not establish current support for the selected protocol revision in any commercial service or SDK. It does not determine jurisdiction-specific obligations or acceptable residual risk for a particular organization.

Important research questions remain:

- How much integration reuse survives differences in identity, policy, and operating requirements?
- Which approval interfaces help reviewers detect incorrect or manipulated proposals?
- How should evaluations estimate rare but consequential failures under realistic workloads?
- Which evidence is sufficient for investigation without excessive collection of sensitive data?
- How do operating costs and exception rates change as autonomy and tool breadth increase?

Answer these with controlled experiments and operational evidence before making broader claims.

## Maintenance

Review versioned protocol claims before every guide release. Recheck mutable security guidance and extensions. Record substantive changes in [CHANGELOG.md](../CHANGELOG.md). Update claims and examples together when a compatibility assumption changes. Do not silently rewrite a version-specific statement to use a mutable latest link.

Contributions should add an exact primary URL, source version or publication date where available, review date, supported claim, and limitation. See [CONTRIBUTING.md](../CONTRIBUTING.md).
