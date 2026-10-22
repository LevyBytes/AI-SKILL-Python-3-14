# Python 3.11.0 alpha 1 / core and builtins / make pyaiter check verify only anext present not aiter

[bpo-45123](https://bugs.python.org/issue?@action=redirect&bpo=45123): Make PyAiter_Check verify only that __anext__ is present (and not __aiter__). Rename PyAiter_Check to PyAIter_Check, PyObject_GetAiter -> PyObject_GetAIter.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
