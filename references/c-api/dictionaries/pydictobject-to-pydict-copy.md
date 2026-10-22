# dictionaries C API: `PyDictObject`, `PyDict_Type`, `PyDict_Check()`, `PyDict_CheckExact()`, `PyDict_New()`, `PyDictProxy_New()`, `PyDictProxy_Type`, `PyDict_Clear()`, `PyDict_Contains()`, `PyDict_ContainsString()`, `PyDict_Copy()`

### Dictionary Objects

 type PyDictObject

A [`PyObject`](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) subtype standing for a Python dictionary object.

 [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) PyDict_Type

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

A [`PyTypeObject`](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) instance standing for the Python dictionary type. At the Python level this is identical to the [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict) object.

 int PyDict_Check([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *p)

* Thread safety: [Atomic](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-atomic).*

Yields true when *p* is a dict object, or an instance of any subtype of dict. The call never fails.

 int PyDict_CheckExact([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *p)

* Thread safety: [Atomic](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-atomic).*

Yields true when *p* is a dict object while not being an instance of any dict subtype. The call never fails.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyDict_New()

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).** Thread safety: [Atomic](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-atomic).*

Hand back a fresh empty dictionary; on failure the result is `NULL`.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyDictProxy_New([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *mapping)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Produce a [`types.MappingProxyType`](https://docs.python.org/3.14/library/types.html#types.MappingProxyType) object wrapping a mapping so that it behaves read-only. The typical purpose is to expose a view that blocks edits to the dictionary backing non-dynamic class types.

 [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) PyDictProxy_Type

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

The type object behind mapping proxy objects produced via `PyDictProxy_New()`, as well as the read-only `__dict__` attribute carried by many built-in types. An instance of `PyDictProxy_Type` exposes a live, read-only window onto a backing dictionary: edits made to that backing dictionary show up through the proxy, yet the proxy on its own rejects any mutation. In Python this maps to [`types.MappingProxyType`](https://docs.python.org/3.14/library/types.html#types.MappingProxyType).

 void PyDict_Clear([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *p)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).** Thread safety: [Atomic](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-atomic).*

Strip every key-value pair out of an existing dictionary.

 int PyDict_Contains([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *p, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *key)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).** Thread safety: [Safe for concurrent use on the same object](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-shared).*

Check whether dictionary *p* holds *key*. When some entry within *p* matches *key*, the result is `1`; otherwise it is `0`. A `-1` result signals an error. The Python equivalent is the expression `key in p`.

Note

On [free threading](https://docs.python.org/3.14/glossary.html#term-free-threaded-build) the call is atomic whenever *key* is a [`str`](https://docs.python.org/3.14/library/stdtypes.html#str), [`int`](https://docs.python.org/3.14/library/functions.html#int), [`float`](https://docs.python.org/3.14/library/functions.html#float), [`bool`](https://docs.python.org/3.14/library/functions.html#bool) or [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes).

 int PyDict_ContainsString([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *p, const char *key)

* Thread safety: [Atomic](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-atomic).*

Behaves like `PyDict_Contains()`, except *key* arrives as a const char* UTF-8 encoded bytes string in place of a [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)*.

Added in version 3.13.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyDict_Copy([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *p)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).** Thread safety: [Atomic](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-atomic).*

Hand back a fresh dictionary holding the very same key-value pairs found in *p*.

[Subject index](INDEX.md) · [Following source contract](pydict-setitem-to-pydict-getitemwitherror.md)
