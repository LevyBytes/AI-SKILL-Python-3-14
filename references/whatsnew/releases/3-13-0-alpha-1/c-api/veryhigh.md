# Python 3.13.0 alpha 1 / c api / veryhigh

[gh-104668](https://github.com/python/cpython/issues/104668): Avoid invoking [`PyOS_InputHook`](https://docs.python.org/3.14/c-api/veryhigh.html#c.PyOS_InputHook) or [`PyOS_ReadlineFunctionPointer`](https://docs.python.org/3.14/c-api/veryhigh.html#c.PyOS_ReadlineFunctionPointer) within subinterpreters, because the callbacks registered there usually find it hard to steer clear of global state. The change also keeps extensions from accidentally executing inside a subinterpreter they were never built for (or have yet to be loaded within).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
