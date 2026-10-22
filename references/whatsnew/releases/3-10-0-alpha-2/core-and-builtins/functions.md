# Python 3.10.0 alpha 2 / core and builtins / functions

[bpo-41974](https://bugs.python.org/issue?@action=redirect&bpo=41974): Took out the special methods `__int__`, `__float__`, `__floordiv__`, `__mod__`, `__divmod__`, `__rfloordiv__`, `__rmod__` and `__rdivmod__` belonging to the [`complex`](https://docs.python.org/3.14/library/functions.html#complex) class. Each of them invariably raised a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
