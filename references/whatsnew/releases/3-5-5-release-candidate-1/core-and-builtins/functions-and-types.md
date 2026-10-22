# Python 3.5.5 release candidate 1 / core and builtins / functions and types

[bpo-31095](https://bugs.python.org/issue?@action=redirect&bpo=31095): Repair a potential crash during GC stemming from a `tp_dealloc` that omits the call to `PyObject_GC_UnTrack()`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
