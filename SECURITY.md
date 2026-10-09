# Security and sensitive information

This repository contains research and a local policy simulator. It does not operate an agent service or accept customer data.

If you find an exposed credential, personal record, or sensitive organizational information, do not reproduce it in a public issue. Use the repository's private vulnerability reporting option if it is enabled. Otherwise, use a maintainer-provided private channel; a public request for a private channel should contain no sensitive details.

For ordinary documentation or example defects, describe the problem with synthetic inputs and a minimal reproduction. Do not submit live endpoints, credentials, customer records, or exploitable details about an unrelated deployed system.

Passing the example tests does not establish production security. See the [example boundaries](examples/service-recovery/README.md) and [security and assurance guidance](docs/security-and-assurance.md).
