# Python 3.14.0 beta 1 / library / ctypes

[gh-133290](https://github.com/python/cpython/issues/133290): Resolve an attribute caching bug that appeared when assigning [`ctypes._Pointer._type_`](https://docs.python.org/3.14/library/ctypes.html#ctypes._Pointer._type_) via the undocumented, deprecated `ctypes.SetPointerType()` function together with the undocumented `set_type()` method.

[gh-100926](https://github.com/python/cpython/issues/100926): Relocate the [`ctypes.POINTER()`](https://docs.python.org/3.14/library/ctypes.html#ctypes.POINTER) types cache away from a global internal store (`_pointer_type_cache`) onto the [`ctypes._CData.__pointer_type__`](https://docs.python.org/3.14/library/ctypes.html#ctypes._CData.__pointer_type__) attribute belonging to the matching [`ctypes`](https://docs.python.org/3.14/library/ctypes.html#module-ctypes) types. That keeps the cache from expanding without bound under certain conditions.

[gh-132417](https://github.com/python/cpython/issues/132417): Repair a `NULL` pointer dereference triggered when a C function invoked through [`ctypes`](https://docs.python.org/3.14/library/ctypes.html#module-ctypes) whose `restype` is [`py_object`](https://docs.python.org/3.14/library/ctypes.html#ctypes.py_object) hands back `NULL`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
