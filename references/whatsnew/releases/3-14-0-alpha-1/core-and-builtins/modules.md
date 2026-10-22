# Python 3.14.0 alpha 1 / core and builtins / modules

[gh-119180](https://github.com/python/cpython/issues/119180): Give functions, classes, and modules an `__annotate__` attribute, part of the [**PEP 649**](https://peps.python.org/pep-0649/) work. Jelle Zijlstra wrote the patch.

[gh-116510](https://github.com/python/cpython/issues/116510): A bug capable of crashing when sub-interpreters employ “basic” single-phase extension modules is fixed. Shared objects might point at PyGC_Head nodes that had already been freed during interpreter cleanup.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
