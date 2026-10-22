# Python 3.9.0 alpha 4 / core and builtins / structures

[bpo-39573](https://bugs.python.org/issue?@action=redirect&bpo=39573): Revise the clinic tool so it relies on [`Py_IS_TYPE()`](https://docs.python.org/3.14/c-api/structures.html#c.Py_IS_TYPE). Donghee Na contributed the patch.

[bpo-39573](https://bugs.python.org/issue?@action=redirect&bpo=39573): Introduce the [`Py_IS_TYPE()`](https://docs.python.org/3.14/c-api/structures.html#c.Py_IS_TYPE) static inline helper to test whether the object *o* type matches *type*.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
