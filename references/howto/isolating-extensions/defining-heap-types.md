# Defining Heap Types

### Defining Heap Types

You build heap types by populating a [`PyType_Spec`](https://docs.python.org/3.14/c-api/type.html#c.PyType_Spec) structure — a description or ?blueprint? of a class — then invoking [`PyType_FromModuleAndSpec()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_FromModuleAndSpec) to assemble a new class object.

Note

Additional functions, such as [`PyType_FromSpec()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_FromSpec), can likewise build heap types, but [`PyType_FromModuleAndSpec()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_FromModuleAndSpec) ties the module to the class, granting access to module state from methods.

As a rule, store the class in *both* the module state (for secure access from C) and the module's `__dict__` (for access from Python code).

[Subject index](INDEX.md) · [Previous source context](changing-static-types-to-heap-types.md) · [Following source context](garbage-collection-protocol.md)
