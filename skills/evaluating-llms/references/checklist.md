# Domain checklist

## Common failure patterns

- Optimizing on the test set and calling it generalization.
- Using a language model judge without calibration.
- Inventing a success rate because examples look convincing.

## Review questions

- No held-out leakage or silent removal of failures.
- Metrics include denominator and scope.
- Critical safety failures cannot be hidden by a high average score.

## Worked boundary

No model runtime is available. Produce runnable cases and a grading protocol, with all behavioral outcomes explicitly not-run.

This is authored engineering guidance, not a legal opinion, live observation or certification. Validate jurisdiction-specific, version-specific and environment-specific requirements from authoritative sources.
