# dictionaries C API: `PyDict_Items()`, `PyDict_Keys()`, `PyDict_Values()`, `PyDict_Size()`, `PyDict_GET_SIZE()`

[PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyDict_Items([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *p)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).** Thread safety: [Atomic](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-atomic).*

Hand back a [`PyListObject`](https://docs.python.org/3.14/c-api/list.html#c.PyListObject) holding every item from the dictionary.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyDict_Keys([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *p)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).** Thread safety: [Atomic](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-atomic).*

Hand back a [`PyListObject`](https://docs.python.org/3.14/c-api/list.html#c.PyListObject) holding every key from the dictionary.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyDict_Values([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *p)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).** Thread safety: [Atomic](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-atomic).*

Hand back a [`PyListObject`](https://docs.python.org/3.14/c-api/list.html#c.PyListObject) holding every value from the dictionary *p*.

 [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) PyDict_Size([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *p)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).** Thread safety: [Atomic](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-atomic).*

Hand back how many items the dictionary holds. For a dictionary this matches `len(p)`.

 [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) PyDict_GET_SIZE([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *p)

* Thread safety: [Atomic](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-atomic).*

Much like `PyDict_Size()`, only with no error checking.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pydictobject-to-pydict-copy.md) · [Previous source contract](pydict-getitemstring-to-pydict-popstring.md) · [Following source contract](pydict-next.md)
