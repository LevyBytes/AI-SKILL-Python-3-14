# Python 3.12.0 beta 1 / core and builtins / functions and types

[gh-102500](https://github.com/python/cpython/issues/102500): Expose the buffer protocol to Python code through the new `__buffer__` and `__release_buffer__` magic methods. Consult [**PEP 688**](https://peps.python.org/pep-0688/) for the particulars. Jelle Zijlstra wrote the patch.

[gh-102213](https://github.com/python/cpython/issues/102213): Address a slowdown that occurred when reading an object's attributes while `__getattr__` is defined.

[gh-98003](https://github.com/python/cpython/issues/98003): Complex function calls now run faster and use up no C stack space.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
