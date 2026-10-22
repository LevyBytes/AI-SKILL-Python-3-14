# Python 3.10.0 alpha 4 / c api / functions and types

[bpo-42591](https://bugs.python.org/issue?@action=redirect&bpo=42591): Exported the `Py_FrozenMain()` function: a fix for a Python 3.9.0 regression. Because Python 3.9 turns on `-fvisibility=hidden`, the function went unexported as it was never marked for export explicitly.

[bpo-32381](https://bugs.python.org/issue?@action=redirect&bpo=32381): Dropped the private `_Py_fopen()` function, which is no longer required. Reach for `_Py_wfopen()` or `_Py_fopen_obj()` in its place. Victor Stinner wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
