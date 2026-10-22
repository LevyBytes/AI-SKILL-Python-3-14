# Python 3.14.0 alpha 1 / library / functools

[gh-119127](https://github.com/python/cpython/issues/119127): The positional arguments of [`functools.partial()`](https://docs.python.org/3.14/library/functools.html#functools.partial) objects can now carry placeholders through [`functools.Placeholder`](https://docs.python.org/3.14/library/functools.html#functools.Placeholder).

[gh-121025](https://github.com/python/cpython/issues/121025): Polish the [`__repr__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__repr__) output of [`functools.partialmethod`](https://docs.python.org/3.14/library/functools.html#functools.partialmethod). Patch by Bénédikt Tran.

[gh-121027](https://github.com/python/cpython/issues/121027): Emit a future warning from `functools.partial.__get__()`. Upcoming Python releases will turn [`functools.partial`](https://docs.python.org/3.14/library/functools.html#functools.partial) into a method descriptor.

[gh-121027](https://github.com/python/cpython/issues/121027): Turn the [`functools.partial`](https://docs.python.org/3.14/library/functools.html#functools.partial) object into a method descriptor.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
