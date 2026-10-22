# Python 3.9.0 alpha 1 / core and builtins / gcsupport

[bpo-38392](https://bugs.python.org/issue?@action=redirect&bpo=38392): While in debug mode, [`PyObject_GC_Track()`](https://docs.python.org/3.14/c-api/gcsupport.html#c.PyObject_GC_Track) henceforth invokes the object type's `tp_traverse()` to confirm the object is sound: it verifies that whatever objects `tp_traverse()` visits remain valid.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
