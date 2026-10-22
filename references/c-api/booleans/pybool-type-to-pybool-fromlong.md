# Boolean Objects

# Bool

### Boolean Objects

Under the hood, Python builds its booleans as a subclass derived from integers. Just two of them exist — `Py_False` together with `Py_True`. Given that, the usual routines for allocating and freeing objects have no bearing on booleans. What you do get, though, are the macros listed below.

 [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) PyBool_Type

*Included in the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Standing in for Python’s boolean type, this [`PyTypeObject`](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) instance is one and the same as what Python code knows as [`bool`](https://docs.python.org/3.14/library/functions.html#bool).

 int PyBool_Check([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o)

Yields true whenever *o* carries the type `PyBool_Type`. Calling it never fails.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *Py_False

Python’s `False` singleton. It exposes no methods of its own and counts as [immortal](https://docs.python.org/3.14/glossary.html#term-immortal).

Changed in version 3.12: `Py_False` became [immortal](https://docs.python.org/3.14/glossary.html#term-immortal).

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *Py_True

Python’s `True` singleton. Carrying no methods of its own, it likewise ranks as [immortal](https://docs.python.org/3.14/glossary.html#term-immortal).

Changed in version 3.12: `Py_True` was made [immortal](https://docs.python.org/3.14/glossary.html#term-immortal).

 Py_RETURN_FALSE

Hand back `Py_False` as a function’s result.

 Py_RETURN_TRUE

Hand back `Py_True` as a function’s result.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyBool_FromLong(long v)

*Returns a fresh reference. Included in the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Gives back either `Py_True` or `Py_False`, according to whether *v* is truthy.

[Subject index](INDEX.md)
