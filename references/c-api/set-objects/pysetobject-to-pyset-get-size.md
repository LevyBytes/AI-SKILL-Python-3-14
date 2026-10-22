# set objects C API: Set types, construction and size queries

type PySetObject

A subtype of [`PyObject`](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) that carries the internal state behind both [`set`](https://docs.python.org/3.14/library/stdtypes.html#set) and [`frozenset`](https://docs.python.org/3.14/library/stdtypes.html#frozenset) objects. Resembling a [`PyDictObject`](https://docs.python.org/3.14/c-api/dict.html#c.PyDictObject), it keeps a fixed footprint for small sets (comparable to how tuples store data) and refers out to a separately allocated, variable-length region of memory for medium and large sets (comparable to how lists store data). Treat none of this structure's fields as public; every one of them may change. Reach the data only through the documented API instead of poking at the values held in the structure directly.

 [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) PySet_Type

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

An instance of [`PyTypeObject`](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) that stands for the Python [`set`](https://docs.python.org/3.14/library/stdtypes.html#set) type.

 [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) PyFrozenSet_Type

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

An instance of [`PyTypeObject`](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) that stands for the Python [`frozenset`](https://docs.python.org/3.14/library/stdtypes.html#frozenset) type.

The type-check macros below accept pointers to any Python object. In the same way, the constructor functions accept any iterable Python object.

 int PySet_Check([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *p)

Reports true whenever *p* counts as a [`set`](https://docs.python.org/3.14/library/stdtypes.html#set), whether directly or via a subtype instance. The call can never fail.

 int PyFrozenSet_Check([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *p)

Reports true whenever *p* counts as a [`frozenset`](https://docs.python.org/3.14/library/stdtypes.html#frozenset), whether directly or via a subtype instance. The call can never fail.

 int PyAnySet_Check([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *p)

Reports true whenever *p* counts as a [`set`](https://docs.python.org/3.14/library/stdtypes.html#set), a [`frozenset`](https://docs.python.org/3.14/library/stdtypes.html#frozenset), or any subtype instance of those. The call can never fail.

 int PySet_CheckExact([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *p)

Reports true whenever *p* is precisely a [`set`](https://docs.python.org/3.14/library/stdtypes.html#set) and not merely a subtype instance. The call can never fail.

Added in version 3.10.

 int PyAnySet_CheckExact([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *p)

Reports true whenever *p* is precisely a [`set`](https://docs.python.org/3.14/library/stdtypes.html#set) or precisely a [`frozenset`](https://docs.python.org/3.14/library/stdtypes.html#frozenset), excluding subtype instances. The call can never fail.

 int PyFrozenSet_CheckExact([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *p)

Reports true whenever *p* is precisely a [`frozenset`](https://docs.python.org/3.14/library/stdtypes.html#frozenset) and not merely a subtype instance. The call can never fail.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PySet_New([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *iterable)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).** Thread safety: [Safe for concurrent use on the same object](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-shared).*

Yield a fresh [`set`](https://docs.python.org/3.14/library/stdtypes.html#set) holding the objects yielded by the *iterable*. Passing `NULL` for *iterable* builds a new empty set. The result is the new set when it succeeds, or `NULL` when it fails. A [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) is raised if *iterable* turns out not to be iterable. This constructor also serves to clone a set (`c=set(s)`).

Note

On [free threading](https://docs.python.org/3.14/glossary.html#term-free-threaded-build), the operation is atomic whenever *iterable* is a [`set`](https://docs.python.org/3.14/library/stdtypes.html#set), [`frozenset`](https://docs.python.org/3.14/library/stdtypes.html#frozenset) or [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict).

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyFrozenSet_New([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *iterable)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).** Thread safety: [Safe for concurrent use on the same object](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-shared).*

Yield a fresh [`frozenset`](https://docs.python.org/3.14/library/stdtypes.html#frozenset) holding the objects yielded by the *iterable*. Passing `NULL` for *iterable* builds a new empty frozenset. The result is the new set when it succeeds, or `NULL` when it fails. A [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) is raised if *iterable* turns out not to be iterable.

Note

On [free threading](https://docs.python.org/3.14/glossary.html#term-free-threaded-build), the operation is atomic whenever *iterable* is a [`set`](https://docs.python.org/3.14/library/stdtypes.html#set), [`frozenset`](https://docs.python.org/3.14/library/stdtypes.html#frozenset) or [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict).

The functions and macros below are usable on instances of [`set`](https://docs.python.org/3.14/library/stdtypes.html#set) or [`frozenset`](https://docs.python.org/3.14/library/stdtypes.html#frozenset), as well as instances of their subtypes.

 [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) PySet_Size([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *anyset)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).** Thread safety: [Atomic](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-atomic).*

Yield the length of a [`set`](https://docs.python.org/3.14/library/stdtypes.html#set) or [`frozenset`](https://docs.python.org/3.14/library/stdtypes.html#frozenset) object. The equivalent of `len(anyset)`. A [`SystemError`](https://docs.python.org/3.14/library/exceptions.html#SystemError) is raised when *anyset* is neither a `set`, a `frozenset`, nor an instance of a subtype.

 [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) PySet_GET_SIZE([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *anyset)

* Thread safety: [Atomic](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-atomic).*

The macro variant of `PySet_Size()`, skipping the error checking.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](set-objects.md) · [Following source contract](pyset-contains-to-pyset-clear.md)
