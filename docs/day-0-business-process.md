# Day 0: redesign the process and prepare the enterprise

Day 0 covers the work before implementation: understanding the process, choosing the intervention, preparing data and integration, defining the future organization, and establishing a value case. It can take days or months. Platform selection should be informed by this work.

## 1. Agree the outcome and baseline

Define the affected customer or employee, process boundary, eligible population, and independently verifiable outcome. For service recovery, the process starts with a disruption or request and ends with confirmed resolution and communication. A generated answer is an intermediate output.

Baseline demand, case mix, backlog, queue time, handling time, repeat contacts, errors, rework, and cost. Record the follow-up window needed to declare a case resolved. Use comparable cohorts and periods; seasonality or a different case mix can distort the result.

## 2. Discover the actual work

Interview frontline specialists, supervisors, users, data owners, application teams, and operations. Walk through work in an approved environment. Identify informal spreadsheets, repeated searches, unclear ownership, undocumented exceptions, and queues. Keep that private evidence out of the public repository.

For every step, record trigger, input, decision, system, responsible role, delay, failure, and output. Distinguish necessary decisions from historical workarounds. Classify the step as **eliminate, simplify, standardize, assist, automate, or retain as human judgment**.

AI should not preserve redundant approvals or duplicated data entry merely because they exist today. Equally, human judgment is not automatically waste.

## 3. Define the future process

This is a fictional redesign, with no measured benefit claimed:

| Step | Current pattern | Future pattern | Organizational change |
|---|---|---|---|
| Intake | Read and re-enter the request | AI suggests intent and missing information within the case application | Specialist resolves ambiguity; one case record remains authoritative |
| Investigation | Search systems and copy records | Tools gather permitted live facts; retrieval supplies current policy | Data and application owners supply supported, fresh contracts |
| Remedy selection | Interpret policy and calculate an option | Domain service determines eligible options; AI explains them | Process owner standardizes rules and exception categories |
| Exception decision | Email chains and unclear authority | Named reviewer receives a complete case and specific decision | Supervisor owns capacity, delegation, and escalation |
| Fulfillment | Manual action with uncertain retries | Application commits the action and returns a durable result | Domain team owns integrity and reconciliation |
| Communication | Draft from partial records | AI drafts from confirmed facts and outcome | User can correct; disputed cases remain visible |
| Improvement | Irregular collection of problems | Corrections and exceptions feed a managed backlog | Process owner prioritizes root-cause improvements |

Draw a responsibility map or swimlane. A human handoff should include evidence, current state, options, unresolved questions, and the decision needed. Reviewers should not repeat the entire investigation just to understand the case.

## 4. Resolve policy and decision rights

Resolve conflicting business rules before implementation. Define actions that can be delegated, review conditions, specialist-only decisions, time limits, notification, reversal, complaints, and exception routing. These decisions shape the workflow.

A remedy limit belongs in an authoritative service. An instruction to explain uncertainty shapes behavior and is evaluated through testing and user research. Both matter, but they operate differently. The [governance chapter](governance-and-business-realignment.md) connects these choices to people, technology, and management philosophy.

## 5. Prepare data and integration

| Question | Day 0 deliverable |
|---|---|
| What is authoritative? | Source and ownership inventory for each fact and document |
| Is it reliable? | Completeness, duplication, stale-content, and quality backlog |
| Who may see it? | Access model preserved in retrieval and APIs |
| How current must it be? | Freshness requirements and update/removal design |
| How will it be accessed? | Search, query, API, and event contracts |
| How will quality be tested? | Approved reference cases and expected evidence |
| Who repairs it? | Content stewardship and integration support |

Documents, relational facts, events, and transaction state have different consistency and access needs. Do not place all enterprise data into a vector index by default. Include preparation and API remediation in the plan.

## 6. Design an experience people will adopt

Choose the existing application, portal, contact-center desktop, collaboration channel, or new experience that best fits the work. A separate chatbot can create another handoff if users must transfer its output into the operational system.

Design completion, uncertainty, correction, escalation, and status displays. Distinguish proposed from committed actions. Include accessibility, language needs, training, and support for affected users.

## 7. Establish economics and delivery readiness

Estimate eligible volume, adoption, success, review effort, exception demand, and net capacity change. State how released capacity would be redeployed. Include transition work and parallel running of old and new processes.

Estimate consumption using representative model, retrieval, tool, and runtime traces; refine the range during the pilot. The [pricing chapter](pricing-and-economics.md) supplies a method, not an enterprise quote.

Fund the process owner, product owner, delivery team, ongoing operations, and change work. Identify procurement, access, network, application-release, and training dependencies on the critical path.

## 8. Prepare people and management practices

Explain what changes in each role, what remains a human responsibility, and how errors are handled. Give frontline users time to practice and a reliable way to challenge output. Train reviewers to inspect evidence instead of approving fluent explanations reflexively.

Measure work created by AI: review, exceptions, content maintenance, evaluation, and support. Plan job redesign with appropriate employee and management stakeholders. Projected minutes saved are not automatically a headcount decision.

## Day 0 exit

The sponsor should be able to explain the future process without naming a model. Architects should map every fact, decision, action, and handoff to an owner and system.

Required artifacts: baseline, future workflow, [redesign canvas](../templates/process-redesign-canvas.md), charter, data readiness assessment, architecture, cost range, adoption plan, and pilot criteria. Open gaps need owners and resolution plans.

Proceed when a bounded useful service can be built and evaluated. Rework the plan if ownership is absent, data is inaccessible, benefits depend on unplanned organizational change, or simpler automation meets the need more effectively.
