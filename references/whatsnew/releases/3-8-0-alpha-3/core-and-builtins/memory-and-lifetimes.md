# Python 3.8.0 alpha 3 / core and builtins / memory and lifetimes

[bpo-36333](https://bugs.python.org/issue?@action=redirect&bpo=36333): Plug a leak in _PyRuntimeState_Fini. Stéphane Wirtel contributed this.

[bpo-30040](https://bugs.python.org/issue?@action=redirect&bpo=30040): A freshly created empty dict now uses less memory than before. Previously it consumed more than an empty dict produced via `dict.clear()`. On top of that, building and tearing down an empty dict is roughly 2x quicker. Inada Naoki wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
