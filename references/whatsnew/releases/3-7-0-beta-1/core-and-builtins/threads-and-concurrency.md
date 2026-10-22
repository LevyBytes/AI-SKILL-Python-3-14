# Python 3.7.0 beta 1 / core and builtins / threads and concurrency

[bpo-20891](https://bugs.python.org/issue?@action=redirect&bpo=20891): Py_Initialize() now builds the GIL. The GIL is no longer built "on demand", which fixes a race condition arising when PyGILState_Ensure() gets called from a non-Python thread.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
