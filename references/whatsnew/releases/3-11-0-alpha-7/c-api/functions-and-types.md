# Python 3.11.0 alpha 7 / c api / functions and types

[bpo-40421](https://bugs.python.org/issue?@action=redirect&bpo=40421): The `PyFrame_GetBuiltins`, `PyFrame_GetGenerator` and `PyFrame_GetGlobals` C-API functions are added so that frame object attributes can be reached safely from C code.

[bpo-46850](https://bugs.python.org/issue?@action=redirect&bpo=46850): The private `_PyFrameEvalFunction` type, together with the private `_PyInterpreterState_GetEvalFrameFunc()` and `_PyInterpreterState_SetEvalFrameFunc()` functions, is relocated into the internal C API. That `_PyFrameEvalFunction` callback function type now takes the `_PyInterpreterFrame` type, which belongs to the internal C API. Victor Stinner wrote the patch.

[bpo-46850](https://bugs.python.org/issue?@action=redirect&bpo=46850): The private undocumented `_PyEval_EvalFrameDefault()` function is relocated into the internal C API. That function now takes the `_PyInterpreterFrame` type, which belongs to the internal C API. Victor Stinner wrote the patch.

[bpo-46987](https://bugs.python.org/issue?@action=redirect&bpo=46987): The private `_PySys_GetObjectId()` and `_PySys_SetObjectId()` functions are removed. Donghee Na wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
