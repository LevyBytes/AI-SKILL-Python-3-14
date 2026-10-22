# Python 3.11.0 beta 1 / core and builtins / numeric behavior

[bpo-46509](https://bugs.python.org/issue?@action=redirect&bpo=46509): Provide type-specialized variants of `Py_DECREF()`, then apply them for `float`, `int`, `str`, `bool`, and `None` so that pointer-chasing is skipped at runtime wherever types are already settled at C compile time.

[gh-91421](https://github.com/python/cpython/issues/91421): Resolve a possible integer overflow inside _Py_DecodeUTF8Ex.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
