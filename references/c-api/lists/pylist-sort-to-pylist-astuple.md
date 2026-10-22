# lists C API: `PyList_Sort()`, `PyList_Reverse()`, `PyList_AsTuple()`

int PyList_Sort([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *list)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).** Thread safety: [Safe for concurrent use on the same object](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-shared).*

Orders the elements of *list* in place. A `0` comes back on success and `-1` on failure. This matches `list.sort()`.

Note

Within the [free-threaded build](https://docs.python.org/3.14/glossary.html#term-free-threaded-build), comparing elements through [`__lt__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__lt__) may run arbitrary Python code, and while that runs the [per-object lock](https://docs.python.org/3.14/glossary.html#term-per-object-lock) can be let go of for a moment. With the built-in types ([`str`](https://docs.python.org/3.14/library/stdtypes.html#str), [`int`](https://docs.python.org/3.14/library/functions.html#int), [`float`](https://docs.python.org/3.14/library/functions.html#float)), the lock stays held throughout the comparison.

 int PyList_Reverse([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *list)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).** Thread safety: [Safe for concurrent use on the same object](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-shared).*

Flips the order of the elements in *list* in place. A `0` comes back on success and `-1` on failure. This matches `list.reverse()`.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyList_AsTuple([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *list)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).** Thread safety: [Atomic](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-atomic).*

Builds a fresh tuple object holding everything that *list* contains; the same as `tuple(list)`.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pylistobject-to-pylist-get-item.md) · [Previous source contract](pylist-setitem-to-pylist-clear.md)
