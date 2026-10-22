# Python 3.11.0 alpha 4 / build / python

[bpo-44133](https://bugs.python.org/issue?@action=redirect&bpo=44133): When Python is built without [`--enable-shared`](https://docs.python.org/3.14/using/configure.html#cmdoption-enable-shared), the `python` program now links against object files rather than against the Python static library (libpython.a), guaranteeing every symbol gets exported. Earlier the linker dropped certain symbols, such as the `Py_FrozenMain()` function. Victor Stinner wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
