# Python 3.8.0 alpha 4 / tests / functions and types

[bpo-36719](https://bugs.python.org/issue?@action=redirect&bpo=36719): Uncollectable objects are now always spotted by regrtest. Formerly that check ran only under `--findleaks`. It now functions alongside `-jN/--multiprocess N` as well. `--findleaks` is now a deprecated alias for `--fail-env-changed`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
