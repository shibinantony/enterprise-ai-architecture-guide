# Contributing

Contributions should improve the accuracy, usefulness, or clarity of this provider-neutral guide.

## Content expectations

- Use public primary sources for protocol, security, and standards claims. Give exact links and versions or review dates.
- Distinguish source-backed facts, proposed architecture, synthetic demonstrations, and measured results.
- Explain a concrete process problem, control boundary, or decision. Avoid unsupported rankings and product promotion.
- Keep examples fictional. Do not submit employer or client materials, personal data, credentials, internal architecture, or private evidence links.
- Discuss limitations, failure behavior, ownership, and recovery alongside the normal flow.
- Report actual test results and evidence gaps. Do not describe a simulator as a production service.

No repository license has been selected for this edition. Resolve contribution and reuse terms with the maintainer before contributing material that needs a specific license.

## Local checks

Run from the repository root with Python 3.9 or later:

```console
python tools/verify_repository.py
python examples/service-recovery/evaluator.py
python -m unittest discover -s examples/service-recovery -p "test_*.py" -v
```

The repository checker validates local links, JSON syntax, and common publication hazards. It is a heuristic check and cannot establish that content is safe to publish. Review the complete proposed diff and any commit metadata before publication.

## Review record

Explain the problem, resulting change, supporting sources, relevant checks, and limitations. Update the source register and change log when changing research claims. Public issue reports and pull requests must contain only information appropriate for public disclosure.
