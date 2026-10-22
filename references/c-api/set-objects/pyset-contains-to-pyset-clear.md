# set objects C API: `PySet_Contains()`, `PySet_Add()`, `PySet_Discard()`, `PySet_Pop()`, `PySet_Clear()`

int PySet_Contains([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *anyset, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *key)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).** Thread safety: [Safe for concurrent use on the same object](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-shared).*

Yield `1` when found, `0` when not found, and `-1` when an error occurs. In contrast to the Python [`__contains__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__contains__) method, this function will not silently turn unhashable sets into temporary frozensets. A [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) is raised when the *key* is unhashable. A [`SystemError`](https://docs.python.org/3.14/library/exceptions.html#SystemError) is raised when *anyset* is neither a [`set`](https://docs.python.org/3.14/library/stdtypes.html#set), a [`frozenset`](https://docs.python.org/3.14/library/stdtypes.html#frozenset), nor an instance of a subtype.

Note

On [free threading](https://docs.python.org/3.14/glossary.html#term-free-threaded-build), the operation is atomic whenever *key* is [`str`](https://docs.python.org/3.14/library/stdtypes.html#str), [`int`](https://docs.python.org/3.14/library/functions.html#int), [`float`](https://docs.python.org/3.14/library/functions.html#float), [`bool`](https://docs.python.org/3.14/library/functions.html#bool) or [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes).

 int PySet_Add([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *set, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *key)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).** Thread safety: [Safe for concurrent use on the same object](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-shared).*

Insert *key* into a [`set`](https://docs.python.org/3.14/library/stdtypes.html#set) instance. This also operates on [`frozenset`](https://docs.python.org/3.14/library/stdtypes.html#frozenset) instances (as with [`PyTuple_SetItem()`](https://docs.python.org/3.14/c-api/tuple.html#c.PyTuple_SetItem), it lets you populate the contents of freshly created frozensets before any other code can see them). Yield `0` on success or `-1` on failure. A [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) is raised when the *key* is unhashable. A [`MemoryError`](https://docs.python.org/3.14/library/exceptions.html#MemoryError) is raised when there is no space to expand. A [`SystemError`](https://docs.python.org/3.14/library/exceptions.html#SystemError) is raised when *set* is not an instance of `set` or its subtype.

Note

On [free threading](https://docs.python.org/3.14/glossary.html#term-free-threaded-build), the operation is atomic whenever *key* is [`str`](https://docs.python.org/3.14/library/stdtypes.html#str), [`int`](https://docs.python.org/3.14/library/functions.html#int), [`float`](https://docs.python.org/3.14/library/functions.html#float), [`bool`](https://docs.python.org/3.14/library/functions.html#bool) or [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes).

The functions below apply to instances of [`set`](https://docs.python.org/3.14/library/stdtypes.html#set) or its subtypes, but not to instances of [`frozenset`](https://docs.python.org/3.14/library/stdtypes.html#frozenset) or its subtypes.

 int PySet_Discard([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *set, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *key)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).** Thread safety: [Safe for concurrent use on the same object](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-shared).*

Yield `1` when found and removed, `0` when not found (nothing happens), and `-1` when an error occurs. No [`KeyError`](https://docs.python.org/3.14/library/exceptions.html#KeyError) is raised for absent keys. A [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) is raised when the *key* is unhashable. In contrast to the Python [`discard()`](https://docs.python.org/3.14/library/stdtypes.html#set.discard) method, this function will not silently turn unhashable sets into temporary frozensets. A [`SystemError`](https://docs.python.org/3.14/library/exceptions.html#SystemError) is raised when *set* is not an instance of [`set`](https://docs.python.org/3.14/library/stdtypes.html#set) or its subtype.

Note

On [free threading](https://docs.python.org/3.14/glossary.html#term-free-threaded-build), the operation is atomic whenever *key* is [`str`](https://docs.python.org/3.14/library/stdtypes.html#str), [`int`](https://docs.python.org/3.14/library/functions.html#int), [`float`](https://docs.python.org/3.14/library/functions.html#float), [`bool`](https://docs.python.org/3.14/library/functions.html#bool) or [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes).

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PySet_Pop([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *set)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).** Thread safety: [Atomic](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-atomic).*

Yield a new reference to some arbitrary object within the *set*, removing that object from the *set* in the process. Yield `NULL` on failure. A [`KeyError`](https://docs.python.org/3.14/library/exceptions.html#KeyError) is raised when the set is empty. A [`SystemError`](https://docs.python.org/3.14/library/exceptions.html#SystemError) is raised when *set* is not an instance of [`set`](https://docs.python.org/3.14/library/stdtypes.html#set) or its subtype.

 int PySet_Clear([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *set)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).** Thread safety: [Atomic](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-atomic).*

Remove every element from an existing set. Yield `0` on success. Yield `-1` and raise [`SystemError`](https://docs.python.org/3.14/library/exceptions.html#SystemError) when *set* is not an instance of [`set`](https://docs.python.org/3.14/library/stdtypes.html#set) or its subtype.

Note

Under the [free-threaded build](https://docs.python.org/3.14/glossary.html#term-free-threaded-build), the set is made empty before its entries get cleared, which means other threads see an empty set rather than any intermediate state.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](set-objects.md) · [Owning structure and shared ABI conditions](pysetobject-to-pyset-get-size.md) · [Following source contract](pyset-minsize.md)
