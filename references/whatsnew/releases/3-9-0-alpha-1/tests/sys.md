# Python 3.9.0 alpha 1 / tests / sys

[bpo-37069](https://bugs.python.org/issue?@action=redirect&bpo=37069): regrtest now relies on [`sys.unraisablehook()`](https://docs.python.org/3.14/library/sys.html#sys.unraisablehook) to label a test as "environment altered" (ENV_CHANGED) whenever it produces an "unraisable exception". On top of that, regrtest emits a warning in such a case.

Run `python3 -m test --fail-env-changed` so unraisable exceptions surfacing in tests are caught.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
