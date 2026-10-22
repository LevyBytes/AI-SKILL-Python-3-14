# Python 3.7.0 beta 3 / core and builtins / memory and lifetimes

[bpo-33005](https://bugs.python.org/issue?@action=redirect&bpo=33005): Resolve a crash on fork while using a custom memory allocator (for example via the PYTHONMALLOC env var). _PyGILState_Reinit() and _PyInterpreterState_Enable() now rely on the default RAW memory allocator to allocate a fresh interpreters mutex during fork.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
