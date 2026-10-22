# Python 3.6.4 release candidate 1 / core and builtins / memory and lifetimes

[bpo-30817](https://bugs.python.org/issue?@action=redirect&bpo=30817): `PyErr_PrintEx()` now clears the ignored exception that `_PySys_SetObjectId()` might raise, for instance when memory is exhausted.

[bpo-30696](https://bugs.python.org/issue?@action=redirect&bpo=30696): Stop the interactive interpreter from looping forever when memory runs out.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
