# Python 3.12.0 alpha 1 / c api / collections and iteration

[gh-92678](https://github.com/python/cpython/issues/92678): Bring back the 3.10 semantics governing multiple inheritance for those C extension classes whose dictionary sits at the tail of the struct.

[gh-92678](https://github.com/python/cpython/issues/92678): Support C extensions using managed dictionaries by setting the `Py_TPFLAGS_MANAGED_DICT` flag.

[gh-92678](https://github.com/python/cpython/issues/92678): Introduces the unstable C-API helpers `_PyObject_VisitManagedDict` and `_PyObject_ClearManagedDict` so that C extensions can let the VM look after their objects' dictionaries.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
