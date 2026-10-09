# Use-case portfolio: invest in business capabilities

An enterprise portfolio should connect a process problem to a reusable capability and a measurable outcome. The patterns below are proposed designs, not reports of deployments, proven returns, or financial, clinical or regulatory advice. Suitability depends on local process evidence, authority and operational readiness.

The strategic distinction is between helping people understand evidence, coordinating work across systems, and committing business changes. Each adds different value and requires different prerequisites. Start with the [Day 0 process redesign](day-0-business-process.md), then compare candidate investments using the same outcome definitions and full [economics](pricing-and-economics.md).

## 1. Service disruption and customer recovery

**Business problem and AI benefit.** A service representative must reconcile an order, disruption evidence, customer entitlements and remedy policy. AI can assemble the context, explain options and draft an appropriate response while a domain service determines permitted remedies.

**Authoritative path.** Order-status and entitlement tools read the order and customer systems; a remedy tool validates current state and commits through the service or payment system. Retrieved policy must carry its version and effective date.

**Process and people.** Give representatives a prepared case and explicit exception reasons; retain a service owner for unresolved commitments.

**Measure and boundary.** Measure verified resolutions per eligible disruption case, resolution time and reopened cases. Permit bounded remedies only under enforced policy; route exceptional, disputed or uncertain outcomes to a person. A drafted apology is not a resolved case.

## 2. IT operations and service management

**Business problem and AI benefit.** Incident evidence is distributed across tickets, telemetry, deployment history and known-error records. AI can construct a timeline and propose a supported diagnostic or remediation sequence.

**Authoritative path.** Read tools access incident management and monitoring; approved workflow tools invoke narrowly scoped operational actions. The change system and affected service record the resulting state.

**Process and people.** Preserve the incident command role, service ownership and escalation paths. Define who validates recovery and who handles a failed remediation.

**Measure and boundary.** Measure time to verified service restoration, recurrence and unsuccessful changes, segmented by incident severity. Start with observation and diagnosis. Production changes require the service's change authority, preconditions and recovery plan; apparent correlation in logs is insufficient evidence to execute a fix.

## 3. Software engineering and delivery

**Business problem and AI benefit.** Engineers spend effort connecting requirements, code, failing tests and documentation. AI can prepare a change proposal with traceable rationale and relevant test evidence.

**Authoritative path.** Repository, work-item, test, vulnerability-scanning and delivery tools provide evidence; changes enter the repository review process and trusted build pipeline. Deployment logs establish observed behavior after release.

**Process and people.** Allocate reviewer capacity, maintain code ownership and teach developers to challenge generated assumptions. The delivery team retains ownership after merge.

**Measure and boundary.** Measure accepted changes without follow-up defects, delivery lead time and reviewer effort per accepted change. Generated code and agent-operated tests remain untrusted inputs. Protect credentials and runners; merging and deploying require separately established authority. Count reviewed delivery outcomes, not generated lines of code.

## 4. Banking operations, payment investigation and KYC evidence

**Business problem and AI benefit.** Investigators must reconcile payment events or assemble know-your-customer evidence from multiple records. AI can organize timelines, identify missing documents and prepare a cited case summary or policy exception request.

**Authoritative path.** Account, payment-status, document and approved-policy tools retrieve permitted records; case-management tools preserve source references and route work. Payment corrections use a separately authorized transaction service.

**Process and people.** Define evidence acceptance criteria, specialist review responsibilities and a route for contradictory or incomplete records.

**Measure and boundary.** Measure complete, accepted case packages per eligible case, rework and investigator time. This pattern prepares evidence; it does not delegate eligibility, credit, enforcement or regulatory determinations to a model. Access to payment evidence does not confer authority to move money.

## 5. Healthcare and pharmaceutical operations

**Business problem and AI benefit.** Quality teams must connect controlled procedures, event reports and supporting records. AI can assist document retrieval, manufacturing-deviation triage, clinical-operations administration, pharmacovigilance case preparation and submission assembly.

**Authoritative path.** Controlled-document, quality, safety-case and operational systems provide versioned evidence; proposed updates return through their approved workflows. Preserve original reports, provenance and unresolved contradictions.

**Process and people.** Assign qualified reviewers, train teams to recognize omissions and establish urgent escalation routes before introducing automated preparation.

**Measure and boundary.** Measure accepted complete packages per eligible event, correction rate and time to qualified review. Assess the applicable validation and record requirements locally. Clinical decisions, safety assessments and submission authorization remain with designated qualified authorities in this proposed pattern; fluent summaries must not conceal missing evidence.

## 6. Manufacturing and supply-chain operations

**Business problem and AI benefit.** A shortage or quality deviation can require coordinated decisions across procurement, engineering, production and logistics. AI can explain dependencies and prepare alternatives using current operational evidence.

**Authoritative path.** Enterprise resource planning (ERP), product lifecycle management (PLM), manufacturing execution (MES), asset, supplier and logistics tools expose bounded capabilities. Engineering changes, purchase commitments and production adjustments commit through their responsible systems.

**Process and people.** Establish a cross-functional exception owner and a shared handoff record. Resolve conflicting part, revision and inventory identifiers before scaling.

**Measure and boundary.** Measure verified exception resolution, avoidable expediting cost and downstream rework per eligible case. Planning suggestions require feasibility validation. Safety-related changes and material commitments require appropriate engineering or operational authority; an agent cannot infer permission from visibility of a production schedule.

## 7. Assurance and capability operations

**Business problem and AI benefit.** Platform teams must assemble evidence across tool versions, evaluations and incidents. AI can prepare registration records, summarize findings and identify missing evidence for review.

**Authoritative path.** Registry, schema-validation, artifact-scanning, policy and execution-evidence services support tools such as `register_capability`, `retrieve_risk_assessment` and `retrieve_execution_evidence`. Version approval and revocation are separate privileged capabilities.

**Process and people.** Tool owners maintain evidence; designated reviewers decide exceptions. Operations owns revocation and recovery when consumers are affected.

**Measure and boundary.** Measure review time, escaped defects and verified containment time. Evidence retrieval is distinct from certification: the agent cannot approve its own release. Emergency suspension can follow a pre-authorized rule with an accountable responder and restoration criteria.

## Build a domain capability catalog

Catalog business contracts rather than duplicating a connector for every assistant. These names are illustrative; read and write permissions remain separate.

| Domain | Reusable capabilities | Authoritative owner |
| --- | --- | --- |
| Customer and service | Retrieve entitlement, read case, propose remedy, commit approved remedy | Customer/service process owner |
| Operations | Read incident, retrieve telemetry, request approved remediation | Service owner |
| Engineering | Read revision, run isolated validation, submit change proposal | Engineering owner |
| Enterprise records | Retrieve versioned document, validate record references | Data/document owner |
| Transactions | Read status, validate preconditions, commit, reconcile outcome | Transaction-system owner |
| Assurance | Retrieve evidence, register version, suspend access | Platform and assurance owners |

Reuse requires stable semantics, permitted consumers, ownership, versions and support commitments. A shared retrieval interface does not grant every workflow access to the same records. The [capability template](../templates/capability-registration.md) makes these contracts reviewable.

## Prioritize reuse and outcomes together

Evidence assembly is a useful first candidate where records are accessible and reviewers can validate completeness. Cross-system coordination follows when handoffs and exception ownership are defined. Business actions become candidates when preconditions, authority, reconciliation and recovery are reliable. These are dependency-based choices, not a universal industry ranking.

Score each investment on addressable case volume, current human effort, outcome value, error consequence, evidence quality and integration cost. Prefer a capability with funded consumers and a domain owner over an abstract platform component. Test the reuse hypothesis by measuring the second workflow's incremental build and support cost, including changes imposed on existing consumers.

Use simpler automation when rules, inputs and outputs are stable and deterministic. Use search or a dashboard when finding information solves the problem. Repair poor records and unclear process ownership before adding orchestration. An agent earns its place only when interpretation or adaptive coordination improves the measured process enough to cover review, operation and failure costs.
