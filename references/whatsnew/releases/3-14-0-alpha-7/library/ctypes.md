# Python 3.14.0 alpha 7 / library / ctypes

[gh-128715](https://github.com/python/cpython/issues/128715): The class behind [`Structure`](https://docs.python.org/3.14/library/ctypes.html#ctypes.Structure)/[`Union`](https://docs.python.org/3.14/library/ctypes.html#ctypes.Union) field descriptors is now reachable as [`CField`](https://docs.python.org/3.14/library/ctypes.html#ctypes.CField), gaining new attributes that help with debugging and introspection.

[gh-132168](https://github.com/python/cpython/issues/132168): Subscription is now supported by the [`ctypes.py_object`](https://docs.python.org/3.14/library/ctypes.html#ctypes.py_object) type, turning it into a [generic type](https://docs.python.org/3.14/glossary.html#term-generic-type).

[gh-131974](https://github.com/python/cpython/issues/131974): Several thread-safety problems in [`ctypes`](https://docs.python.org/3.14/library/ctypes.html#module-ctypes) on the [free threaded](https://docs.python.org/3.14/glossary.html#term-free-threading) build have been fixed.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
