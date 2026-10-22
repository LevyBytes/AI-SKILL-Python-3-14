# How do I extract C values from a Python object?

### How do I extract C values from a Python object?

It varies with the object's type. For a tuple, [`PyTuple_Size()`](https://docs.python.org/3.14/c-api/tuple.html#c.PyTuple_Size) yields the length while [`PyTuple_GetItem()`](https://docs.python.org/3.14/c-api/tuple.html#c.PyTuple_GetItem) fetches whatever sits at a given index. Lists come with their own counterparts, namely [`PyList_Size()`](https://docs.python.org/3.14/c-api/list.html#c.PyList_Size) and [`PyList_GetItem()`](https://docs.python.org/3.14/c-api/list.html#c.PyList_GetItem).

When dealing with bytes, [`PyBytes_Size()`](https://docs.python.org/3.14/c-api/bytes.html#c.PyBytes_Size) gives the length and [`PyBytes_AsStringAndSize()`](https://docs.python.org/3.14/c-api/bytes.html#c.PyBytes_AsStringAndSize) supplies a pointer to the value together with that length. Bear in mind that Python bytes objects can hold null bytes, so steer away from C's `strlen()`.

Before checking an object's type, confirm it isn't `NULL`, and only then turn to [`PyBytes_Check()`](https://docs.python.org/3.14/c-api/bytes.html#c.PyBytes_Check), [`PyTuple_Check()`](https://docs.python.org/3.14/c-api/tuple.html#c.PyTuple_Check), [`PyList_Check()`](https://docs.python.org/3.14/c-api/list.html#c.PyList_Check), and the rest.

A high-level API for Python objects exists too, delivered through what's termed the ‘abstract' interface — consult `Include/abstract.h` for the rest. With it you can work against any Python sequence via calls such as [`PySequence_Length()`](https://docs.python.org/3.14/c-api/sequence.html#c.PySequence_Length), [`PySequence_GetItem()`](https://docs.python.org/3.14/c-api/sequence.html#c.PySequence_GetItem), and so forth, plus a host of other handy protocols — numbers ([`PyNumber_Index()`](https://docs.python.org/3.14/c-api/number.html#c.PyNumber_Index) and friends) and mappings through the PyMapping APIs among them.

[Subject index](INDEX.md)
