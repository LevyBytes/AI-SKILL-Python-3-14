# Python 3.11.0 alpha 4 / core and builtins / subinterpreters

[bpo-46070](https://bugs.python.org/issue?@action=redirect&bpo=46070): [`Py_EndInterpreter()`](https://docs.python.org/3.14/c-api/subinterpreters.html#c.Py_EndInterpreter) now deliberately untracks every object the GC is currently tracking. Earlier, if another interpreter later used such an object, calling [`PyObject_GC_UnTrack()`](https://docs.python.org/3.14/c-api/gcsupport.html#c.PyObject_GC_UnTrack) on it crashed whenever the previous or next object in the `PyGC_Head` structure had turned into a dangling pointer. Victor Stinner wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
