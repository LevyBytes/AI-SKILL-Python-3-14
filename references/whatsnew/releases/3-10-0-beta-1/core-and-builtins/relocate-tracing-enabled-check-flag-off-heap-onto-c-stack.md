# Python 3.10.0 beta 1 / core and builtins / relocate tracing enabled check flag off heap onto c stack

[bpo-43760](https://bugs.python.org/issue?@action=redirect&bpo=43760): Relocate the tracing-enabled check flag off the heap and onto the C stack. Interpreter dispatch ought to get quicker as a result.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
