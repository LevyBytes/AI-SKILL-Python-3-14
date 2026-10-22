# int PyDict_Merge(PyObject *a, PyObject *b, int override)

int PyDict_Merge([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *a, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *b, int override)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).** Thread safety: [Safe for concurrent use on the same object](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-shared).*

Step through the mapping object *b*, folding its key-value pairs into dictionary *a*. The object *b* can be a dictionary or anything else that implements [`PyMapping_Keys()`](https://docs.python.org/3.14/c-api/mapping.html#c.PyMapping_Keys) along with [`PyObject_GetItem()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_GetItem). When *override* is true, a pair already in *a* gets overwritten if *b* holds the same key; otherwise a pair is added only where *a* lacks that key. Yield `0` when it succeeds, or `-1` should an exception arise.

Note

On the [free-threaded build](https://docs.python.org/3.14/glossary.html#term-free-threaded-build), should *b* be a [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict) using the standard iterator, both *a* and *b* stay locked for as long as the operation runs. Where *b* is a mapping that is not a dict, the lock covers *a* alone; another thread may modify *b* at the same time.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pydictobject-to-pydict-copy.md) · [Following source contract](pydict-next.md) · [Following source contract](pydict-update-to-pydict-unwatch.md)
