# Python 3.13.0 alpha 1 / c api / object

[gh-106572](https://github.com/python/cpython/issues/106572): The [`PyObject_DelAttr()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_DelAttr) and [`PyObject_DelAttrString()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_DelAttrString) macros become functions. Victor Stinner wrote the patch.

[gh-106521](https://github.com/python/cpython/issues/106521): The [`PyObject_GetOptionalAttr()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_GetOptionalAttr) and [`PyObject_GetOptionalAttrString()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_GetOptionalAttrString) functions are added.

[gh-108511](https://github.com/python/cpython/issues/108511): The functions [`PyObject_HasAttrWithError()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_HasAttrWithError), [`PyObject_HasAttrStringWithError()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_HasAttrStringWithError), [`PyMapping_HasKeyWithError()`](https://docs.python.org/3.14/c-api/mapping.html#c.PyMapping_HasKeyWithError) and [`PyMapping_HasKeyStringWithError()`](https://docs.python.org/3.14/c-api/mapping.html#c.PyMapping_HasKeyStringWithError) are added.

[gh-107073](https://github.com/python/cpython/issues/107073): The new [`PyObject_VisitManagedDict()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_VisitManagedDict) and [`PyObject_ClearManagedDict()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_ClearManagedDict) functions have to be invoked from the traverse and clear functions of any type that carries the [`Py_TPFLAGS_MANAGED_DICT`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_TPFLAGS_MANAGED_DICT) flag. Victor Stinner wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
