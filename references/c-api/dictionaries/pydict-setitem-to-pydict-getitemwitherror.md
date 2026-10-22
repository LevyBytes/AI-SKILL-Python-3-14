# dictionaries C API: `PyDict_SetItem()`, `PyDict_SetItemString()`, `PyDict_DelItem()`, `PyDict_DelItemString()`, `PyDict_GetItemRef()`, `PyDict_GetItem()`, `PyDict_GetItemWithError()`

int PyDict_SetItem([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *p, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *key, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *val)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).** Thread safety: [Safe for concurrent use on the same object](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-shared).*

Store *val* under the key *key* in dictionary *p*. The *key* has to be [hashable](https://docs.python.org/3.14/glossary.html#term-hashable); when it is not, a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) is raised. Yields `0` when it works and `-1` when it fails. The function *does not* steal a reference to *val*.

Note

On [free threading](https://docs.python.org/3.14/glossary.html#term-free-threaded-build) the call is atomic whenever *key* is a [`str`](https://docs.python.org/3.14/library/stdtypes.html#str), [`int`](https://docs.python.org/3.14/library/functions.html#int), [`float`](https://docs.python.org/3.14/library/functions.html#float), [`bool`](https://docs.python.org/3.14/library/functions.html#bool) or [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes).

 int PyDict_SetItemString([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *p, const char *key, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *val)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).** Thread safety: [Atomic](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-atomic).*

Behaves like `PyDict_SetItem()`, except *key* arrives as a const char* UTF-8 encoded bytes string in place of a [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)*.

 int PyDict_DelItem([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *p, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *key)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).** Thread safety: [Safe for concurrent use on the same object](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-shared).*

Delete from dictionary *p* the entry keyed by *key*. The *key* has to be [hashable](https://docs.python.org/3.14/glossary.html#term-hashable); when it is not, a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) is raised. When *key* does not appear in the dictionary, a [`KeyError`](https://docs.python.org/3.14/library/exceptions.html#KeyError) is raised. Yields `0` when it works and `-1` when it fails.

Note

On [free threading](https://docs.python.org/3.14/glossary.html#term-free-threaded-build) the call is atomic whenever *key* is a [`str`](https://docs.python.org/3.14/library/stdtypes.html#str), [`int`](https://docs.python.org/3.14/library/functions.html#int), [`float`](https://docs.python.org/3.14/library/functions.html#float), [`bool`](https://docs.python.org/3.14/library/functions.html#bool) or [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes).

 int PyDict_DelItemString([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *p, const char *key)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).** Thread safety: [Atomic](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-atomic).*

Behaves like `PyDict_DelItem()`, except *key* arrives as a const char* UTF-8 encoded bytes string in place of a [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)*.

 int PyDict_GetItemRef([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *p, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *key, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) **result)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.13.** Thread safety: [Safe for concurrent use on the same object](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-shared).*

Hand back a fresh [strong reference](https://docs.python.org/3.14/glossary.html#term-strong-reference) to the object stored under *key* in dictionary *p*:

- When the key exists, point **result* at a fresh [strong reference](https://docs.python.org/3.14/glossary.html#term-strong-reference) to that value and return `1`.

- When the key is absent, point **result* at `NULL` and return `0`.

- When an error occurs, raise an exception, point **result* at `NULL` and return `-1`.

Note

On [free threading](https://docs.python.org/3.14/glossary.html#term-free-threaded-build) the call is atomic whenever *key* is a [`str`](https://docs.python.org/3.14/library/stdtypes.html#str), [`int`](https://docs.python.org/3.14/library/functions.html#int), [`float`](https://docs.python.org/3.14/library/functions.html#float), [`bool`](https://docs.python.org/3.14/library/functions.html#bool) or [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes).

Added in version 3.13.

See also the [`PyObject_GetItem()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_GetItem) function.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyDict_GetItem([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *p, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *key)

*Return value: Borrowed reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).** Thread safety: [Safe to call from multiple threads with external synchronization only](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-compatible).*

Hand back a [borrowed reference](https://docs.python.org/3.14/glossary.html#term-borrowed-reference) to the object stored under *key* in dictionary *p*. Should that key *key* be absent, the result is `NULL` and *no* exception gets set.

Note

Any exceptions thrown while this invokes the [`__hash__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__hash__) and [`__eq__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__eq__) methods are quietly dropped. Reach for the `PyDict_GetItemWithError()` function in preference.

Note

Within the [free-threaded build](https://docs.python.org/3.14/glossary.html#term-free-threaded-build), the [borrowed reference](https://docs.python.org/3.14/glossary.html#term-borrowed-reference) handed back can turn invalid should another thread mutate the dictionary at the same time. Reach for `PyDict_GetItemRef()` instead, since it hands back a [strong reference](https://docs.python.org/3.14/glossary.html#term-strong-reference).

Changed in version 3.10: Invoking this API without an [attached thread state](https://docs.python.org/3.14/glossary.html#term-attached-thread-state) used to be permitted for historical reasons. That is permitted no longer.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyDict_GetItemWithError([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *p, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *key)

*Return value: Borrowed reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).** Thread safety: [Safe to call from multiple threads with external synchronization only](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-compatible).*

A flavor of `PyDict_GetItem()` that leaves exceptions intact. Hands back `NULL` **with** an exception set when an exception arose. Hands back `NULL` **without** an exception set when the key was not there.

Note

Within the [free-threaded build](https://docs.python.org/3.14/glossary.html#term-free-threaded-build), the [borrowed reference](https://docs.python.org/3.14/glossary.html#term-borrowed-reference) handed back can turn invalid should another thread mutate the dictionary at the same time. Reach for `PyDict_GetItemRef()` instead, since it hands back a [strong reference](https://docs.python.org/3.14/glossary.html#term-strong-reference).

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pydictobject-to-pydict-copy.md) · [Following source contract](pydict-getitemstring-to-pydict-popstring.md)
