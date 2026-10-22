# Heap Types

### Heap Types

A different option besides static types is *heap-allocated types*, or *heap types* for brevity, which line up closely with classes produced through Python’s `class` statement. The `Py_TPFLAGS_HEAPTYPE` flag is set on heap types.

You achieve this by populating a [`PyType_Spec`](https://docs.python.org/3.14/c-api/type.html#c.PyType_Spec) structure and invoking [`PyType_FromSpec()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_FromSpec), [`PyType_FromSpecWithBases()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_FromSpecWithBases), [`PyType_FromModuleAndSpec()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_FromModuleAndSpec), or [`PyType_FromMetaclass()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_FromMetaclass).

[Subject index](INDEX.md) · [Previous source contract](static-types.md) · [Following source contract](pynumbermethods-to-pynumbermethods-nb-divmod.md)
