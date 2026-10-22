# Python 3.10.0 alpha 7 / c api / refcounting

[bpo-43688](https://bugs.python.org/issue?@action=redirect&bpo=43688): When Python is compiled in debug mode (that is, with the `Py_DEBUG` macro defined), the limited C API is now usable. Within the limited C API, [`Py_INCREF()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_INCREF) and [`Py_DECREF()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_DECREF) are now realized as opaque function calls instead of reaching straight into the [`PyObject.ob_refcnt`](https://docs.python.org/3.14/c-api/structures.html#c.PyObject.ob_refcnt) member, provided Python is built in debug mode and the `Py_LIMITED_API` macro is aimed at Python 3.10 or later. Supporting the limited C API in debug mode became feasible because, ever since Python 3.8, the [`PyObject`](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) structure is identical across release and debug builds (refer to [bpo-36465](https://bugs.python.org/issue?@action=redirect&bpo=36465)).

The `--with-trace-refs` special build (the `Py_TRACE_REFS` macro) still does not support the limited C API.

Victor Stinner wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
