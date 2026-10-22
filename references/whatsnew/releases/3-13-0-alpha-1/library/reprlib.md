# Python 3.13.0 alpha 1 / library / reprlib

[gh-109818](https://github.com/python/cpython/issues/109818): Corrected [`reprlib.recursive_repr()`](https://docs.python.org/3.14/library/reprlib.html#reprlib.recursive_repr) so it no longer fails to copy `__type_params__` from the function it decorates.

[gh-107409](https://github.com/python/cpython/issues/107409): Assign the `__wrapped__` attribute within [`reprlib.recursive_repr()`](https://docs.python.org/3.14/library/reprlib.html#reprlib.recursive_repr).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
