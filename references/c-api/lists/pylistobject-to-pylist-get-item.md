# lists C API: `PyListObject`, `PyList_Type`, `PyList_Check()`, `PyList_CheckExact()`, `PyList_New()`, `PyList_Size()`, `PyList_GET_SIZE()`, `PyList_GetItemRef()`, `PyList_GetItem()`, `PyList_GET_ITEM()`

# List

### List Objects

 type PyListObject

A Python list is the object that this [`PyObject`](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) subtype stands for.

 [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) PyList_Type

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Standing in for the list type itself, this [`PyTypeObject`](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) instance is identical to the [`list`](https://docs.python.org/3.14/library/stdtypes.html#list) you see from Python code.

 int PyList_Check([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *p)

* Thread safety: [Atomic](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-atomic).*

Yields true when *p* is either a list object or an instance belonging to some subtype of the list type. A call here can never fail.

 int PyList_CheckExact([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *p)

* Thread safety: [Atomic](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-atomic).*

Yields true when *p* is a list object yet not an instance of any subtype of the list type. A call here can never fail.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyList_New([Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) len)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).** Thread safety: [Atomic](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-atomic).*

On success you get back a freshly built list whose length is *len*; otherwise the result is `NULL`.

Note

Whenever *len* exceeds zero, every slot of the new list object holds `NULL` at first. Because of that, refrain from calling abstract API helpers like [`PySequence_SetItem()`](https://docs.python.org/3.14/c-api/sequence.html#c.PySequence_SetItem), and do not hand the object to Python code, until each slot has been filled with a genuine object via `PyList_SetItem()` or `PyList_SET_ITEM()`. Only these two calls are safe to use while the list remains partly built: `PyList_SetItem()` and `PyList_SET_ITEM()`.

 [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) PyList_Size([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *list)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).** Thread safety: [Atomic](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-atomic).*

Gives the number of elements held by the list object *list*, matching what `len(list)` reports for a list object.

 [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) PyList_GET_SIZE([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *list)

* Thread safety: [Atomic](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-atomic).*

Behaves like `PyList_Size()` while skipping any validation of errors.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyList_GetItemRef([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *list, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) index)

*Return value: New reference.** Belongs to the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) as of version 3.13.** Thread safety: [Atomic](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-atomic).*

Hands back whatever object sits at slot *index* within the list that *list* points to. That position has to be zero or higher, since counting backward from the tail is not allowed. Should *index* fall outside the valid range (`<0 or >=len(list)`), the call yields `NULL` and raises an [`IndexError`](https://docs.python.org/3.14/library/exceptions.html#IndexError) exception.

Added in version 3.13.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyList_GetItem([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *list, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) index)

*Return value: Borrowed reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).** Thread safety: [Safe to call from multiple threads with external synchronization only](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-compatible).*

Works the same way as `PyList_GetItemRef()`, except that it hands you a [borrowed reference](https://docs.python.org/3.14/glossary.html#term-borrowed-reference) rather than a [strong reference](https://docs.python.org/3.14/glossary.html#term-strong-reference).

Note

Within the [free-threaded build](https://docs.python.org/3.14/glossary.html#term-free-threaded-build), that [borrowed reference](https://docs.python.org/3.14/glossary.html#term-borrowed-reference) you receive can stop being valid once a different thread mutates the list at the same time. Lean toward `PyList_GetItemRef()`, since it yields a [strong reference](https://docs.python.org/3.14/glossary.html#term-strong-reference).

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyList_GET_ITEM([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *list, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) i)

*Return value: Borrowed reference.** Thread safety: [Safe to call from multiple threads with external synchronization only](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-compatible).*

Behaves like `PyList_GetItem()` while leaving out any validation of errors.

Note

Within the [free-threaded build](https://docs.python.org/3.14/glossary.html#term-free-threaded-build), that [borrowed reference](https://docs.python.org/3.14/glossary.html#term-borrowed-reference) you receive can stop being valid once a different thread mutates the list at the same time. Lean toward `PyList_GetItemRef()`, since it yields a [strong reference](https://docs.python.org/3.14/glossary.html#term-strong-reference).

[Subject index](INDEX.md) · [Following source contract](pylist-setitem-to-pylist-clear.md)
