# Type Object Structures

### Type Object Structures

Among the most consequential structures in Python's object system is the one used to declare a fresh type: the [`PyTypeObject`](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) structure. You can manipulate type objects through any of the `PyObject_*` or `PyType_*` functions, though they expose little of direct interest to ordinary Python programs. Because these objects underpin the behavior of every object, they matter a great deal both to the interpreter and to any extension module defining its own types.

Relative to the ordinary built-in types, type objects are quite sizable. That bulk comes from the many values each one holds — predominantly C function pointers, where every pointer supplies one fragment of the type's behavior. This section walks through the type object's fields one by one, presenting them in the same sequence they appear within the structure.

Beyond the quick reference that follows, the Examples section offers an at-a-glance look at what [`PyTypeObject`](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) means and how it is used.

[Subject index](INDEX.md) · [Following source contract](tp-slots.md)
