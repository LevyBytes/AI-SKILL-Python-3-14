# exceptions C API: `PyErr_GetExcInfo()`, `PyErr_SetExcInfo()`

void PyErr_GetExcInfo([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) **ptype, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) **pvalue, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) **ptraceback)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.7.*

Fetch the legacy-style view of the exception info, the same one reported by [`sys.exc_info()`](https://docs.python.org/3.14/library/sys.html#sys.exc_info). This points at an exception that was *already caught*, not one that has just been raised. Hands back new references for all three objects, each of which may be `NULL`. Leaves the exception info state untouched. This function survives for backwards compatibility. Favor `PyErr_GetHandledException()` instead.

Note

Code aiming to handle exceptions does not usually call this function. It is instead handy where code has to briefly stash and reinstate the exception state. Reach for `PyErr_SetExcInfo()` to reinstate or clear that exception state.

Added in version 3.3.

 void PyErr_SetExcInfo([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *type, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *value, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *traceback)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.7.*

Establish the exception info, the same view reported by `sys.exc_info()`. This points at an exception that was *already caught*, not one that has just been raised. The function steals the references of its arguments. Hand in `NULL` for all three arguments to clear the exception state. This function survives for backwards compatibility. Favor `PyErr_SetHandledException()` instead.

Note

Code aiming to handle exceptions does not usually call this function. It is instead handy where code has to briefly stash and reinstate the exception state. Reach for `PyErr_GetExcInfo()` to read that exception state.

Added in version 3.3.

Changed in version 3.11: Now unused, the `type` and `traceback` arguments are permitted to be NULL, since the interpreter at this point obtains them from the exception instance (that is, the `value` argument). References of all three arguments are still stolen by the function.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pyerr-occurred-to-pyerr-setraisedexception.md) · [Previous source contract](pyerr-fetch-to-pyerr-sethandledexception.md) · [Following source contract](pyerr-checksignals-to-pysignal-setwakeupfd.md)
