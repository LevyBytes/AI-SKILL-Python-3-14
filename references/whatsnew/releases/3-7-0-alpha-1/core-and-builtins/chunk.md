# Python 3.7.0 alpha 1 / core and builtins / chunk

[bpo-28411](https://bugs.python.org/issue?@action=redirect&bpo=28411): Move to the abstract API when handling `PyInterpreterState.modules`. That paves the way for later support across every dict subclass and additional Mapping implementations. A `PyImport_GetModule()` function is also added so that a chunk of duplicated code can be removed.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
