# Python 3.11.0 alpha 7 / core and builtins / frame

[bpo-42197](https://bugs.python.org/issue?@action=redirect&bpo=42197): Profiling and tracing no longer invoke `PyFrame_FastToLocalsWithError()` or `PyFrame_LocalsToFast()`. To read the `f_locals` attribute on a [`PyFrameObject`](https://docs.python.org/3.14/c-api/frame.html#c.PyFrameObject), C code can instead call [`PyFrame_GetLocals()`](https://docs.python.org/3.14/c-api/frame.html#c.PyFrame_GetLocals).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
