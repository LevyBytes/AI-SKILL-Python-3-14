# Python 3.14.0 alpha 1 / core and builtins / frame

[gh-123923](https://github.com/python/cpython/issues/123923): Inside the internal [`_PyInterpreterFrame`](https://docs.python.org/3.14/c-api/frame.html#c._PyInterpreterFrame) struct, the `f_executable` field now holds a tagged pointer. Any profiler or debugger reading this field should clear the least significant bit in order to recover the [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)* pointer.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
