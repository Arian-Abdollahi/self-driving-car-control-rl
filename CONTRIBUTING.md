# Contributing

This is an experimental, simulation-only project. Pull requests should be narrowly scoped, documented, and verified against an appropriate Webots version.

- Preserve phase-specific controller behavior when refactoring shared utilities.
- Keep third-party copyright notices intact.
- Do not commit generated models, logs, native binaries or proprietary data unless redistribution is explicitly permitted.
- For code changes run `python -m unittest discover -s tests -v`; for behavior changes also attach simulator versions, random seeds, scenarios, and evaluation metrics.
- Describe which phase and which Webots/SUMO environment you tested. Passing static checks alone is not a runtime validation.
