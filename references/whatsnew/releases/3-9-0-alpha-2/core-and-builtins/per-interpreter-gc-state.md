# Python 3.9.0 alpha 2 / core and builtins / garbage collector state held per interpreter pyinterpreterstate gc instead globally

[bpo-36854](https://bugs.python.org/issue?@action=redirect&bpo=36854): Garbage collector state is now held per interpreter (`PyInterpreterState.gc`) instead of globally (`_PyRuntimeState.gc`).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
