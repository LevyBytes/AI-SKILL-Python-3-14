# Python 3.11.0 alpha 7 / c api / sys

[bpo-46850](https://bugs.python.org/issue?@action=redirect&bpo=46850): The private undocumented `_PyEval_CallTracing()` function is dropped from the C API. Use the public [`sys.call_tracing()`](https://docs.python.org/3.14/library/sys.html#sys.call_tracing) function instead. Victor Stinner wrote the patch.

[bpo-46850](https://bugs.python.org/issue?@action=redirect&bpo=46850): The private undocumented `_PyEval_GetCoroutineOriginTrackingDepth()` function is dropped from the C API. Use the public [`sys.get_coroutine_origin_tracking_depth()`](https://docs.python.org/3.14/library/sys.html#sys.get_coroutine_origin_tracking_depth) function instead. Victor Stinner wrote the patch.

[bpo-46850](https://bugs.python.org/issue?@action=redirect&bpo=46850): The following private undocumented functions are dropped from the C API:

  - `_PyEval_GetAsyncGenFirstiter()`

  - `_PyEval_GetAsyncGenFinalizer()`

  - `_PyEval_SetAsyncGenFirstiter()`

  - `_PyEval_SetAsyncGenFinalizer()`

Use the public [`sys.get_asyncgen_hooks()`](https://docs.python.org/3.14/library/sys.html#sys.get_asyncgen_hooks) and [`sys.set_asyncgen_hooks()`](https://docs.python.org/3.14/library/sys.html#sys.set_asyncgen_hooks) functions instead. Victor Stinner wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
