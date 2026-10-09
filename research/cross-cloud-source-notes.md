# Cross-cloud comparison: source register and evidence boundaries

**Research snapshot:** 2026-10-09 UTC. Review began at **2026-10-09 11:39:38 UTC**, verified by the session clock. Sources below are official provider documentation inspected for [the comparison chapter](../docs/cross-cloud-comparison.md). These are live pages, not immutable archival snapshots.

## Method

Compare the same logical layers and one proposed synthetic business workflow. Separate a controlled runtime/integration trial from a native-optimized service trial. Product descriptions establish advertised capabilities; they do not establish measured accuracy, latency, reliability, portability or business return. No implementation was deployed or tested for this chapter. Fit recommendations, benchmark design and Day 0/1/2 sequencing are editorial analysis.

## Google Cloud evidence

| Official source | Claim scope and constraint |
| --- | --- |
| [Agent Runtime](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/runtime), [agent deployment](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/deploy-an-agent) | Current runtime name, managed hosting, container/framework contract and ADK integration. Runtime overview displayed updated 2026-10-07; deployment examples retain the `reasoningEngines` resource path. |
| [Model Garden](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/model-garden/explore-models) | Discovery and serving paths; catalog membership does not establish identical feature or regional availability. |
| [RAG Engine](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/rag-engine/rag-overview) | Private-data ingestion/retrieval components; deployment mode and region must be checked independently. |
| [BigQuery with MCP Toolbox](https://docs.cloud.google.com/bigquery/docs/pre-built-tools-with-mcp-toolbox) | Structured analytical access; tutorial scope is not a production transaction or authorization design. |
| [Agent Gateway](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-overview) | Ingress/egress modes, protocol mediation and connectivity conditions. No universal protocol-conformance claim is inferred. |
| [Managing runtime access](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/manage-agent-access) | Service-account and agent-identity choices; agent identity labelled preview in this guide at review. |
| [Workflows](https://docs.cloud.google.com/workflows/docs/overview) | Defined service orchestration, waits, retries and callbacks. Proposed business state machine is our design. |
| [Agent evaluation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/optimize/evaluation/evaluate-agents) | Development, regression and online evaluation modes; judge output is not authoritative transaction evidence. |
| [Agent observability](https://docs.cloud.google.com/gemini-enterprise-agent-platform/optimize/observability/overview) | OpenTelemetry and Cloud Observability integration; instrumentation/configuration still required. |
| [Revisions and traffic](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/manage-revisions-and-traffic) | Immutable revisions and traffic splitting; page explicitly labels feature preview and `v1beta1`. |
| [Sharing custom agents](https://docs.cloud.google.com/gemini/enterprise/docs/share-custom-agents) | Gemini Enterprise distribution for registered compatible agents; not included by implication in runtime hosting. |
| [Agent locations](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/agent-locations) | Per-feature location constraints; explicitly separates infrastructure residency from model-processing location. |

## Microsoft Azure evidence

| Official source | Claim scope and constraint |
| --- | --- |
| [What is Microsoft Foundry?](https://learn.microsoft.com/en-us/azure/foundry/what-is-foundry) | Current brand, classic/new resource and API distinctions. Page displayed updated 2026-09-24. |
| [Foundry Agent Service](https://learn.microsoft.com/en-us/azure/foundry/agents/overview) | Prompt versus hosted agent responsibility; this comparison selects hosted agents for code-level parity. |
| [Hosted agents](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/hosted-agents) | Session isolation, dedicated identity, immutable versions and one-version endpoint. Page displayed updated 2026-09-11; it distinguishes background work from process resilience. |
| [Foundry Models](https://learn.microsoft.com/en-us/azure/foundry/concepts/foundry-models-overview) | Deployment choices, model lifecycle and regional/feature variation. |
| [Foundry IQ](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/what-is-foundry-iq) | Azure AI Search foundation, knowledge sources and relationship to Fabric/Work IQ. Feature status differs by API version and portal. |
| [Toolbox](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/toolbox-overview) | Managed MCP tool distribution, authentication, versioning and tool-support table. Tool search and skills are labelled preview; no blanket GA assertion is made. |
| [Networking options](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/networking-options) | Inbound and outbound choices; a private endpoint by itself does not establish isolated egress. |
| [Durable Functions](https://learn.microsoft.com/en-us/azure/durable-task/durable-functions/durable-functions-overview) | Stateful orchestration and checkpoint/recovery responsibilities. |
| [Agent evaluators](https://learn.microsoft.com/en-us/azure/foundry/concepts/evaluation-evaluators/agent-evaluators?view=foundry) | Outcome/tool metrics and explicit limitations for some tool types. |
| [Agent tracing](https://learn.microsoft.com/en-us/azure/foundry/observability/concepts/trace-agent-concept) | Tracing/Application Insights path; it does not establish equivalent retention or instrumentation across implementations. |
| [Publishing to Copilot and Teams](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/publish-copilot) | Channel path with administrative prerequisites; runtime availability does not imply workplace entitlement. |

## AWS evidence

| Official source | Claim scope and constraint |
| --- | --- |
| [AgentCore overview](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html) | Separates AgentCore capabilities from model inference and end-user applications. |
| [AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) | Framework/model flexibility, invocation interfaces and microVM/Instances choices; modes have different lifetime/isolation characteristics. |
| [Bedrock model compatibility](https://docs.aws.amazon.com/bedrock/latest/userguide/models.html) | Model, API, endpoint and regional support must be checked as a combination. |
| [Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html) | Retrieval and grounded response generation; transactional state remains separately authoritative. |
| [Structured knowledge stores](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-build-structured.html) | Natural-language query conversion and supported structured retrieval; not an arbitrary database-write facility. |
| [AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) | Gateway/tool capability boundary. |
| [MCP targets](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-target-MCPservers.html) | Supported protocol revisions and authentication details; version-update availability has account-specific qualifications. |
| [Runtime authentication](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-oauth.html) | Inbound and outbound authority are different configuration surfaces. |
| [Runtime VPC connectivity](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agentcore-vpc.html) | Private-resource connectivity and separate private API access; account networking still requires design. |
| [Step Functions workflow types](https://docs.aws.amazon.com/step-functions/latest/dg/choosing-workflow-type.html) | Standard/Express duration and execution semantics; explicit retries and downstream effects still require application reasoning. |
| [Evaluation types](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations-types.html) | Online, on-demand and batch evaluation paths. |
| [Observability configuration](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-configure.html) | CloudWatch, ADOT and explicit setup requirements; built-in metrics do not mean every application event is captured. |
| [Runtime versions/endpoints](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agent-runtime-versioning.html) | Immutable versions; default endpoint movement differs from pinned named endpoints. |
| [AgentCore regions](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agentcore-regions.html) | Per-capability matrix; Runtime Instances, Memory and other services need their own checks. |
| [Evaluation cross-region inference](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations-cross-region-inference.html) | Processing location can differ from stored-data location. A regional endpoint is insufficient evidence for a no-cross-region requirement. |

## Conflicts and limits retained in the analysis

1. **Google perimeter wording:** the runtime-access page says VPC Service Controls is not supported with Agent Gateway, while the gateway overview describes perimeter enforcement when an agent connectivity template routes through a VPC attachment. We preserve this as an unresolved mode/version support question, not an unconditional supported/unsupported verdict.
2. **Microsoft maturity wording:** current hosted-agent documentation describes substantial capabilities without a blanket preview heading, while other networking pages still use older preview wording. We make feature-specific claims and require an actual support/region check; absence of a preview label is not treated as proof of a contractual production commitment.
3. **Runtime state versus protocol state:** cloud session persistence is not MCP protocol-session semantics. No inference about universal support for MCP 2026-07-28 is made from a runtime's MCP marketing statement.
4. **Model and price scope:** the chapter does not compare native model benchmarks or quote rates. A shared-model trial must confirm the exact version, inference route, lifecycle and parameters; a native-optimized comparison measures a complete service instead.
5. **Provider assertions:** statements about managed scaling, isolation or instrumentation are documented product behavior, not independently verified properties of a deployed configuration. Review source revisions, quotas and applicable terms when selecting a service.

Refresh this register when product names, API paths, feature status, regional availability or deployment modes change, and preserve approved configuration-specific evidence with the actual implementation decision.
