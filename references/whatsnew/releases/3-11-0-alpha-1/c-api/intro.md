# Python 3.11.0 alpha 1 / c api / intro

[bpo-45116](https://bugs.python.org/issue?@action=redirect&bpo=45116): Introduce the [`Py_ALWAYS_INLINE`](https://docs.python.org/3.14/c-api/intro.html#c.Py_ALWAYS_INLINE) macro that requests the compiler always inline a static inline function. A compiler is free to disregard it and choose not to inline the function. Victor Stinner wrote the patch.

[bpo-45094](https://bugs.python.org/issue?@action=redirect&bpo=45094): Introduce the [`Py_NO_INLINE`](https://docs.python.org/3.14/c-api/intro.html#c.Py_NO_INLINE) macro that switches off inlining for a function. Victor Stinner authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
