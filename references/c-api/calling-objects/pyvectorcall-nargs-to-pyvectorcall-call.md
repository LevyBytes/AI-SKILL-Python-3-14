# Vectorcall Support API

### Vectorcall Support API

 [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) PyVectorcall_NARGS(size_t nargsf)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.12.*

When handed a vectorcall *nargsf* argument, hand back the genuine argument count. As things stand this matches:

```c
(Py_ssize_t)(nargsf & ~PY_VECTORCALL_ARGUMENTS_OFFSET)

```

Even so, route through the `PyVectorcall_NARGS` function so that later extensions remain possible.

Added in version 3.8.

 vectorcallfunc PyVectorcall_Function([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *op)

Should *op* lack vectorcall support — whether the type as a whole or just that one instance — give back *NULL*. In every other case, give back the vectorcall function pointer kept inside *op*. No exception is ever raised by this routine.

Its primary value is in testing whether *op* supports vectorcall at all, which you determine by evaluating `PyVectorcall_Function(op) != NULL`.

Added in version 3.9.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyVectorcall_Call([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *callable, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *tuple, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *dict)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.12.*

Invoke the `vectorcallfunc` of *callable*, supplying the positional and keyword arguments through a tuple and a dict respectively.

You are looking at a special-purpose function meant to occupy the [`tp_call`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_call) slot or serve inside a `tp_call` implementation. It neither inspects the [`Py_TPFLAGS_HAVE_VECTORCALL`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_TPFLAGS_HAVE_VECTORCALL) flag nor drops back to `tp_call`.

Added in version 3.8.

[Subject index](INDEX.md) · [Previous source contract](recursion-control.md) · [Following source contract](pyobject-call-to-pyobject-callfunction.md)
