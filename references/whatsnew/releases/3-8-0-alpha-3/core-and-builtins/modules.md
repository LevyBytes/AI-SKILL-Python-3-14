# Python 3.8.0 alpha 3 / core and builtins / modules

[bpo-36124](https://bugs.python.org/issue?@action=redirect&bpo=36124): Introduce a fresh interpreter-specific dict and surface it through the C-API via PyInterpreterState_GetDict(). This mirrors PyThreadState_GetDict(). That said, extension modules ought to keep relying on PyModule_GetState() for their own per-interpreter state.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
