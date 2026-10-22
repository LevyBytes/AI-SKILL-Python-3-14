# Python 3.14.0 alpha 4 / core and builtins / compiler and parser

[gh-124483](https://github.com/python/cpython/issues/124483): Treat `Py_DECREF` and its variants as escaping while producing opcode and uop metadata. This keeps a `__del__` method from steering the JIT into incorrect behavior.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
