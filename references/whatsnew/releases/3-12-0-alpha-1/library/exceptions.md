# Python 3.12.0 alpha 1 / library / exceptions

[gh-88123](https://github.com/python/cpython/issues/88123): Provide an `Enum.__contains__` that hands back `True` or `False`, superseding the deprecated behaviour that would occasionally raise a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError).

[gh-97825](https://github.com/python/cpython/issues/97825): Resolves an [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError) raised when [`subprocess.check_output()`](https://docs.python.org/3.14/library/subprocess.html#subprocess.check_output) runs with the argument `input=None` alongside either *encoding* or *errors*.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
