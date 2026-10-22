# Python 3.10.0 alpha 1 / c api / null unicode constructor deprecation warnings

[bpo-36346](https://bugs.python.org/issue?@action=redirect&bpo=36346): Emits a DeprecationWarning for `PyUnicode_FromUnicode(NULL, size)` and `PyUnicode_FromStringAndSize(NULL, size)` whenever `size > 0`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
