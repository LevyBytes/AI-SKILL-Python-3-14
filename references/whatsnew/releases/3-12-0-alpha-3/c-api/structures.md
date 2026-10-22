# Python 3.12.0 alpha 3 / c api / structures

[gh-47146](https://github.com/python/cpython/issues/47146): The `structmember.h` header is now deprecated. Whatever of its contents aren't deprecated become available simply by including `Python.h`, gaining a `Py_` prefix wherever one was absent. (The deprecated contents are [`T_OBJECT`](https://docs.python.org/3.14/c-api/structures.html#c.T_OBJECT), [`T_NONE`](https://docs.python.org/3.14/c-api/structures.html#c.T_NONE), and the no-op flags.) Petr Viktorin wrote the patch, building on earlier work from Alexander Belopolsky and Matthias Braun.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
