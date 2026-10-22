# lists C API: `PyList_SetItem()`, `PyList_SET_ITEM()`, `PyList_Insert()`, `PyList_Append()`, `PyList_GetSlice()`, `PyList_SetSlice()`, `PyList_Extend()`, `PyList_Clear()`

int PyList_SetItem([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *list, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) index, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *item)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).** Thread safety: [Atomic](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-atomic).*

Stores *item* at slot *index* of the list. A `0` comes back when this works. Where *index* lies beyond the valid range, the call yields `-1` and raises an [`IndexError`](https://docs.python.org/3.14/library/exceptions.html#IndexError) exception.

Note

A reference to *item* is “stolen” by this call, and the reference to whatever element previously occupied that slot is dropped.

 void PyList_SET_ITEM([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *list, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) i, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o)

* Thread safety: [Safe to call from multiple threads with external synchronization only](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-compatible).*

A macro version of `PyList_SetItem()` that skips error validation. You would generally reach for it only while populating brand-new lists that hold nothing yet.

A range check runs as an assertion whenever Python is compiled in [debug mode](https://docs.python.org/3.14/using/configure.html#debug-build) or [`with assertions`](https://docs.python.org/3.14/using/configure.html#cmdoption-with-assertions).

Note

A reference to *item* is “stolen” by this macro, and — in contrast to `PyList_SetItem()` — it does *not* release any reference to an element being overwritten; whatever reference sat in *list* at slot *i* gets leaked.

Note

Within the [free-threaded build](https://docs.python.org/3.14/glossary.html#term-free-threaded-build), there is no built-in synchronization behind this macro. Reach for it mainly while populating fresh lists that no other thread holds a reference to. Should the list possibly be shared, turn to `PyList_SetItem()` instead, as it relies on a [per-object lock](https://docs.python.org/3.14/glossary.html#term-per-object-lock).

 int PyList_Insert([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *list, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) index, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *item)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).** Thread safety: [Safe for concurrent use on the same object](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-shared).*

Places *item* into *list* just ahead of slot *index*. A `0` comes back when it works, while a failure yields `-1` together with a raised exception. This mirrors `list.insert(index, item)`.

 int PyList_Append([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *list, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *item)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).** Thread safety: [Atomic](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-atomic).*

Tacks the object *item* onto the tail of *list*. A `0` comes back when it works, while a failure yields `-1` along with a raised exception. This mirrors `list.append(item)`.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyList_GetSlice([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *list, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) low, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) high)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).** Thread safety: [Atomic](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-atomic).*

Produces a list gathering the elements of *list* that sit *between* *low* and *high*. Where it fails, the call yields `NULL` and raises an exception. This mirrors `list[low:high]`. Counting backward from the tail is not allowed.

 int PyList_SetSlice([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *list, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) low, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) high, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *itemlist)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).** Thread safety: [Safe for concurrent use on the same object](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-shared).*

Replaces the *list* slice running from *low* to *high* with what *itemlist* holds. This mirrors `list[low:high] = itemlist`. You may pass `NULL` for *itemlist*, which assigns an empty list (i.e. deletes the slice). A `0` comes back on success and `-1` on failure. Counting backward from the tail is not allowed.

Note

Within the [free-threaded build](https://docs.python.org/3.14/glossary.html#term-free-threaded-build), should *itemlist* be a [`list`](https://docs.python.org/3.14/library/stdtypes.html#list), the operation holds locks on both *list* and *itemlist* throughout. With any other iterable (or with `NULL`), the lock covers *list* alone.

 int PyList_Extend([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *list, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *iterable)

* Thread safety: [Safe for concurrent use on the same object](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-shared).*

Grows *list* by appending whatever *iterable* contains. It amounts to `PyList_SetSlice(list, PY_SSIZE_T_MAX, PY_SSIZE_T_MAX, iterable)` and matches `list.extend(iterable)` or `list += iterable`.

When *list* is not a [`list`](https://docs.python.org/3.14/library/stdtypes.html#list) object, an exception is raised and `-1` comes back. Otherwise 0 is returned on success.

Added in version 3.13.

Note

Within the [free-threaded build](https://docs.python.org/3.14/glossary.html#term-free-threaded-build), should *iterable* be a [`list`](https://docs.python.org/3.14/library/stdtypes.html#list), [`set`](https://docs.python.org/3.14/library/stdtypes.html#set), [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict), or a dict view, the operation locks both *list* and *iterable* (or the dict behind it) throughout. With other iterables, only *list* gets locked, and *iterable* might be changed at the same time by a separate thread.

 int PyList_Clear([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *list)

* Thread safety: [Atomic](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-atomic).*

Empties *list* of every element. It amounts to `PyList_SetSlice(list, 0, PY_SSIZE_T_MAX, NULL)` and matches `list.clear()` or `del list[:]`.

When *list* is not a [`list`](https://docs.python.org/3.14/library/stdtypes.html#list) object, an exception is raised and `-1` comes back. Otherwise 0 is returned on success.

Added in version 3.13.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pylistobject-to-pylist-get-item.md) · [Following source contract](pylist-sort-to-pylist-astuple.md)
