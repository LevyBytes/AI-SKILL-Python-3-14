# unicode C API: `PyUnicode_Type`, `PyUnicodeIter_Type`

### Unicode Type

Listed here are the fundamental Unicode object types that back the Unicode implementation inside Python:

 [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) PyUnicode_Type

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

This particular [`PyTypeObject`](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) stands for Python's Unicode type. Python-level code sees it as [`str`](https://docs.python.org/3.14/library/stdtypes.html#str).

 [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) PyUnicodeIter_Type

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

This particular [`PyTypeObject`](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) stands for Python's Unicode iterator type, which serves to walk over Unicode string objects.

[Subject index](INDEX.md) · [Previous source contract](unicode-objects.md) · [Following source contract](py-ucs4-to-py-ucs1.md)
