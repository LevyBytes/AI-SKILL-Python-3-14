# Python 3.11.0 alpha 7 / core and builtins / collections and iteration

[bpo-39829](https://bugs.python.org/issue?@action=redirect&bpo=39829): The `__len__()` call during list initialization was dropped and the initializing logic shifted into `list_extend`. Jeremiah Pascual supplied the patch.

[bpo-47162](https://bugs.python.org/issue?@action=redirect&bpo=47162): Faulty function-pointer casts — those differing in argument count or types — are something WebAssembly cannot tolerate. To soften this, Python may now route through call trampolines. Set `PY_CALL_TRAMPOLINE` to switch call trampolines on.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
