# Python 3.9.0 alpha 5 / core and builtins / per interpreter tracing state

[bpo-39984](https://bugs.python.org/issue?@action=redirect&bpo=39984): subinterpreters: Shift `_PyRuntimeState.ceval.tracing_possible` over to `PyInterpreterState.ceval.tracing_possible`, so each interpreter holds its own variable.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
