# Objects, Types and Reference Counts

### Objects, Types and Reference Counts

The bulk of Python/C API functions take one or more arguments and hand back a return value typed [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)*. That type is a pointer aimed at an opaque data type that stands for some arbitrary Python object. Given that the Python language handles every Python object type alike in most circumstances (think assignments, scope rules, and argument passing), representing them all with one shared C type is only natural. Nearly every Python object resides on the heap: you never declare an automatic or static variable typed [`PyObject`](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) — only pointer variables typed PyObject* may be declared. The lone exception is the type objects; because they must never be freed, they take the form of static [`PyTypeObject`](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) objects.

Every Python object (Python integers included) carries a *type* together with a *reference count*. The type of an object dictates the kind of object it is (for instance, an integer, a list, or a user-defined function; plenty more exist, as spelled out in [The standard type hierarchy](https://docs.python.org/3.14/reference/datamodel.html#types)). Each of the well-known types comes with a macro for testing whether a given object is of that type; as an illustration, `PyList_Check(a)` evaluates true precisely when the object *a* points to is a Python list.

[Subject index](INDEX.md) · [Previous source contract](py-aligned-to-py-va-copy.md) · [Following source contract](reference-counts.md)
