# Python 3.12.0 alpha 1 / c api / typeobj

[gh-95589](https://github.com/python/cpython/issues/95589): Extension classes that assign `tp_dictoffset` and `tp_weaklistoffset` forfeit multiple-inheritance support, though they are now safe. The recommendation for extension classes is to rely on [`Py_TPFLAGS_MANAGED_DICT`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_TPFLAGS_MANAGED_DICT) and [`Py_TPFLAGS_MANAGED_WEAKREF`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_TPFLAGS_MANAGED_WEAKREF) instead.

[gh-93274](https://github.com/python/cpython/issues/93274): The vectorcall implementation API ([`Py_TPFLAGS_HAVE_VECTORCALL`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_TPFLAGS_HAVE_VECTORCALL), [`PyVectorcall_NARGS()`](https://docs.python.org/3.14/c-api/call.html#c.PyVectorcall_NARGS) and [`PyVectorcall_Call()`](https://docs.python.org/3.14/c-api/call.html#c.PyVectorcall_Call)) has joined the limited API and stable ABI.

[gh-93012](https://github.com/python/cpython/issues/93012): Whenever a class reassigns its [`__call__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__call__) method, the [`Py_TPFLAGS_HAVE_VECTORCALL`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_TPFLAGS_HAVE_VECTORCALL) flag is now stripped from it. That renders vectorcall safe on mutable types (that is, heap types lacking the `immutable` flag). A mutable type that never overrides [`tp_call`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_call) now picks up the `Py_TPFLAGS_HAVE_VECTORCALL` flag by inheritance.

[gh-95388](https://github.com/python/cpython/issues/95388): Building [`immutable types`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_TPFLAGS_IMMUTABLETYPE) on top of mutable bases is now deprecated, with plans to forbid it in Python 3.14.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
