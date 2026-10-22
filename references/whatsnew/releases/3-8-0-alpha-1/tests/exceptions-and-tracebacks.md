# Python 3.8.0 alpha 1 / tests / exceptions and tracebacks

[bpo-34279](https://bugs.python.org/issue?@action=redirect&bpo=34279): `test.support.run_unittest()` will no longer raise `TestDidNotRun` when the result holds skipped tests. That exception now fires only if nothing ran and nothing was skipped.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
