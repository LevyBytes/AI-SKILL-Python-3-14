# Python 3.10.0 alpha 6 / c api / exceptions

[bpo-43270](https://bugs.python.org/issue?@action=redirect&bpo=43270): The private `_PyErr_OCCURRED()` macro is gone; reach for the public [`PyErr_Occurred()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_Occurred) function instead.

[bpo-40170](https://bugs.python.org/issue?@action=redirect&bpo=40170): To keep implementation details hidden, [`PyExceptionClass_Name()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyExceptionClass_Name) is from now on declared exclusively as a function. Previously the macro reached straight into [`PyTypeObject.tp_name`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_name). Erlend E. Aasland authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
