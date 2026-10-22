# How do I use Py_BuildValue() to create a tuple of arbitrary length?

### How do I use Py_BuildValue() to create a tuple of arbitrary length?

That isn't possible. Reach for [`PyTuple_Pack()`](https://docs.python.org/3.14/c-api/tuple.html#c.PyTuple_Pack) in its place.

[Subject index](INDEX.md)
