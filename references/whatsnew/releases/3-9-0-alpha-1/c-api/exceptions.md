# Python 3.9.0 alpha 1 / c api / exceptions

[bpo-38644](https://bugs.python.org/issue?@action=redirect&bpo=38644): Supply [`Py_EnterRecursiveCall()`](https://docs.python.org/3.14/c-api/exceptions.html#c.Py_EnterRecursiveCall) and [`Py_LeaveRecursiveCall()`](https://docs.python.org/3.14/c-api/exceptions.html#c.Py_LeaveRecursiveCall) as ordinary functions for the limited API. They used to be macros, yet those macros failed under the limited API, which has no access to the `PyThreadState.recursion_depth` field. The stable ABI loses `_Py_CheckRecursionLimit`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
