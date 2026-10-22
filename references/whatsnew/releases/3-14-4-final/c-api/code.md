# Python 3.14.4 final / c api / code

[gh-144981](https://github.com/python/cpython/issues/144981): On the [free threaded](https://docs.python.org/3.14/glossary.html#term-free-threading) build, [`PyUnstable_Code_SetExtra()`](https://docs.python.org/3.14/c-api/code.html#c.PyUnstable_Code_SetExtra), [`PyUnstable_Code_GetExtra()`](https://docs.python.org/3.14/c-api/code.html#c.PyUnstable_Code_GetExtra), and [`PyUnstable_Eval_RequestCodeExtraIndex()`](https://docs.python.org/3.14/c-api/code.html#c.PyUnstable_Eval_RequestCodeExtraIndex) have been made thread-safe.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
