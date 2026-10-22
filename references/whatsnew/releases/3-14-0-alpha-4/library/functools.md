# Python 3.14.0 alpha 4 / library / functools

[gh-83662](https://github.com/python/cpython/issues/83662): Supplied the absent `__class_getitem__` method on the Python implementation of [`functools.partial()`](https://docs.python.org/3.14/library/functools.html#functools.partial) so it lines up with the C version. That mostly matters for other Python implementations such as PyPy and GraalPy, given that CPython normally falls back on the C implementation of that function.

[gh-121676](https://github.com/python/cpython/issues/121676): Marked as deprecated the practice of calling the Python implementation of [`functools.reduce()`](https://docs.python.org/3.14/library/functools.html#functools.reduce) with `function` or `sequence` passed as a [keyword argument](https://docs.python.org/3.14/glossary.html#term-keyword-argument). Python 3.16 will disallow this so as to align with the C implementation.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
