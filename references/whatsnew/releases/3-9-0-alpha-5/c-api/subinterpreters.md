# Python 3.9.0 alpha 5 / c api / subinterpreters

[bpo-39947](https://bugs.python.org/issue?@action=redirect&bpo=39947): Add the [`PyInterpreterState_Get()`](https://docs.python.org/3.14/c-api/subinterpreters.html#c.PyInterpreterState_Get) function into the limited C API.

[bpo-38500](https://bugs.python.org/issue?@action=redirect&bpo=38500): Introduce a private API for reading and writing the frame evaluation function: the [`_PyInterpreterState_GetEvalFrameFunc()`](https://docs.python.org/3.14/c-api/subinterpreters.html#c._PyInterpreterState_GetEvalFrameFunc) and [`_PyInterpreterState_SetEvalFrameFunc()`](https://docs.python.org/3.14/c-api/subinterpreters.html#c._PyInterpreterState_SetEvalFrameFunc) C functions are added. A *tstate* parameter is now accepted by the [`_PyFrameEvalFunction`](https://docs.python.org/3.14/c-api/subinterpreters.html#c._PyFrameEvalFunction) function type.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
