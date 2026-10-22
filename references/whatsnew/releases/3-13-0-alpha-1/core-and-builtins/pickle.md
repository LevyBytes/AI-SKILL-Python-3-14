# Python 3.13.0 alpha 1 / core and builtins / pickle

[gh-93627](https://github.com/python/cpython/issues/93627): Bring the Python pickle module implementation in line with the C implementation of the pickle module. For objects that set reduction methods such as [`__reduce_ex__()`](https://docs.python.org/3.14/library/pickle.html#object.__reduce_ex__) or [`__reduce__()`](https://docs.python.org/3.14/library/pickle.html#object.__reduce__) to `None`, attempting to pickle them now yields a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
