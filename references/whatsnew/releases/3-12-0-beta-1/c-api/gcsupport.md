# Python 3.12.0 beta 1 / c api / gcsupport

[gh-103743](https://github.com/python/cpython/issues/103743): Introduce the [`PyUnstable_Object_GC_NewWithExtraData()`](https://docs.python.org/3.14/c-api/gcsupport.html#c.PyUnstable_Object_GC_NewWithExtraData) function, handy for reserving extra memory past an object to hold data Python does not manage.

[gh-101408](https://github.com/python/cpython/issues/101408): [`PyObject_GC_Resize`](https://docs.python.org/3.14/c-api/gcsupport.html#c.PyObject_GC_Resize) ought to factor in preheader size where that applies. Donghee Na wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
