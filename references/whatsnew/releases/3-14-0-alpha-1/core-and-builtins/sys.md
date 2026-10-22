# Python 3.14.0 alpha 1 / core and builtins / sys

[gh-122029](https://github.com/python/cpython/issues/122029): Produce `c_call` events from [`sys.setprofile()`](https://docs.python.org/3.14/library/sys.html#sys.setprofile) whenever a `PyMethodObject` that points at a `PyCFunction` gets called.

[gh-113993](https://github.com/python/cpython/issues/113993): Per the documentation, strings interned via [`sys.intern()`](https://docs.python.org/3.14/library/sys.html#sys.intern) are once again garbage-collected after they fall out of use. Strings interned by way of the C function [`PyUnicode_InternInPlace()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_InternInPlace) stay immortal. The string interning mechanism's internals have changed. That change may bear on performance as well as on the identities of [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) objects.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
