# Python 3.10.0 alpha 1 / core and builtins / stefan behnel pointed out cf feature version gets consulted even pycf only ast

[bpo-35975](https://bugs.python.org/issue?@action=redirect&bpo=35975): Stefan Behnel pointed out that cf_feature_version gets consulted even with PyCF_ONLY_AST unset. That clashes with both the intent and the documented behavior, so a fix landed.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
