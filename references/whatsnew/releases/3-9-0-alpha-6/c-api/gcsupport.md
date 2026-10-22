# Python 3.9.0 alpha 6 / c api / gcsupport

[bpo-40170](https://bugs.python.org/issue?@action=redirect&bpo=40170): Turn the [`PyObject_IS_GC()`](https://docs.python.org/3.14/c-api/gcsupport.html#c.PyObject_IS_GC) macro into a function so implementation details stay hidden.

[bpo-40241](https://bugs.python.org/issue?@action=redirect&bpo=40241): The [`PyObject_GC_IsTracked()`](https://docs.python.org/3.14/c-api/gcsupport.html#c.PyObject_GC_IsTracked) and [`PyObject_GC_IsFinalized()`](https://docs.python.org/3.14/c-api/gcsupport.html#c.PyObject_GC_IsFinalized) functions join the public API, letting callers ask whether the garbage collector is presently tracking certain Python objects or has already finalized them. Pablo Galindo wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
