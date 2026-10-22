# dictionaries C API: `PyDict_GetItemString()`, `PyDict_GetItemStringRef()`, `PyDict_SetDefault()`, `PyDict_SetDefaultRef()`, `PyDict_Pop()`, `PyDict_PopString()`

[PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyDict_GetItemString([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *p, const char *key)

*Return value: Borrowed reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).** Thread safety: [Safe to call from multiple threads with external synchronization only](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-compatible).*

Behaves like `PyDict_GetItem()`, except *key* arrives as a const char* UTF-8 encoded bytes string in place of a [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)*.

Note

Any exceptions thrown while this invokes the [`__hash__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__hash__) and [`__eq__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__eq__) methods, or while building the temporary [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) object, are quietly dropped. Reach instead for the `PyDict_GetItemWithError()` function paired with your own [`PyUnicode_FromString()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_FromString) *key*.

Note

Within the [free-threaded build](https://docs.python.org/3.14/glossary.html#term-free-threaded-build), the [borrowed reference](https://docs.python.org/3.14/glossary.html#term-borrowed-reference) handed back can turn invalid should another thread mutate the dictionary at the same time. Reach for `PyDict_GetItemStringRef()` instead, since it hands back a [strong reference](https://docs.python.org/3.14/glossary.html#term-strong-reference).

 int PyDict_GetItemStringRef([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *p, const char *key, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) **result)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.13.** Thread safety: [Atomic](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-atomic).*

Much like `PyDict_GetItemRef()`, except *key* arrives as a const char* UTF-8 encoded bytes string in place of a [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)*.

Added in version 3.13.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyDict_SetDefault([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *p, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *key, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *defaultobj)

*Return value: Borrowed reference.** Thread safety: [Safe to call from multiple threads with external synchronization only](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-compatible).*

This mirrors the Python-level [`dict.setdefault()`](https://docs.python.org/3.14/library/stdtypes.html#dict.setdefault). When *key* exists, the matching value out of dictionary *p* is returned. When the key is absent from the dict, it gets added with the value *defaultobj*, and *defaultobj* is returned. Rather than computing the hash of *key* separately for the lookup and for the insertion, this function runs the hash function on *key* a single time.

Added in version 3.4.

Note

Within the [free-threaded build](https://docs.python.org/3.14/glossary.html#term-free-threaded-build), the [borrowed reference](https://docs.python.org/3.14/glossary.html#term-borrowed-reference) handed back can turn invalid should another thread mutate the dictionary at the same time. Reach for `PyDict_SetDefaultRef()` instead, since it hands back a [strong reference](https://docs.python.org/3.14/glossary.html#term-strong-reference).

 int PyDict_SetDefaultRef([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *p, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *key, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *default_value, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) **result)

* Thread safety: [Safe for concurrent use on the same object](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-shared).*

Place *default_value* into dictionary *p* under the key *key* when that key is not yet present in the dictionary. Provided *result* is not `NULL`, **result* is then set to a [strong reference](https://docs.python.org/3.14/glossary.html#term-strong-reference) pointing either at *default_value*, when the key was absent, or at the value already there, when *key* was already present in the dictionary. Returns `1` when the key existed and *default_value* was not inserted, or `0` when the key was absent and *default_value* got inserted. Upon failure it returns `-1`, sets an exception, and sets `*result` to `NULL`.

To be explicit: should a strong reference to *default_value* already be in your hands ahead of this call, then upon its return you hold a strong reference both to *default_value* and to **result* (when that is not `NULL`). The two can name the same object, in which case you carry two distinct references to it.

Note

On [free threading](https://docs.python.org/3.14/glossary.html#term-free-threaded-build) the call is atomic whenever *key* is a [`str`](https://docs.python.org/3.14/library/stdtypes.html#str), [`int`](https://docs.python.org/3.14/library/functions.html#int), [`float`](https://docs.python.org/3.14/library/functions.html#float), [`bool`](https://docs.python.org/3.14/library/functions.html#bool) or [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes).

Added in version 3.13.

 int PyDict_Pop([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *p, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *key, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) **result)

* Thread safety: [Safe for concurrent use on the same object](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-shared).*

Take *key* out of dictionary *p* and, when wanted, hand back the value that was removed. No [`KeyError`](https://docs.python.org/3.14/library/exceptions.html#KeyError) is raised should the key be absent.

- When the key exists, point **result* at a fresh reference to the removed value provided *result* is not `NULL`, and return `1`.

- When the key is absent, point **result* at `NULL` provided *result* is not `NULL`, and return `0`.

- When an error occurs, raise an exception and return `-1`.

Comparable to [`dict.pop()`](https://docs.python.org/3.14/library/stdtypes.html#dict.pop), yet lacking the default value and not raising [`KeyError`](https://docs.python.org/3.14/library/exceptions.html#KeyError) when the key is absent.

Note

On [free threading](https://docs.python.org/3.14/glossary.html#term-free-threaded-build) the call is atomic whenever *key* is a [`str`](https://docs.python.org/3.14/library/stdtypes.html#str), [`int`](https://docs.python.org/3.14/library/functions.html#int), [`float`](https://docs.python.org/3.14/library/functions.html#float), [`bool`](https://docs.python.org/3.14/library/functions.html#bool) or [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes).

Added in version 3.13.

 int PyDict_PopString([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *p, const char *key, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) **result)

* Thread safety: [Atomic](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-atomic).*

Much like `PyDict_Pop()`, except *key* arrives as a const char* UTF-8 encoded bytes string in place of a [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)*.

Added in version 3.13.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pydictobject-to-pydict-copy.md) · [Previous source contract](pydict-setitem-to-pydict-getitemwitherror.md) · [Following source contract](pydict-items-to-pydict-get-size.md)
