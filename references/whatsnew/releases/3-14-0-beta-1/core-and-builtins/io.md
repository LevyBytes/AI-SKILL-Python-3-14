# Python 3.14.0 beta 1 / core and builtins / io

[gh-132952](https://github.com/python/cpython/issues/132952): Startup under the `-S` argument is sped up by importing the private `_io` module rather than [`io`](https://docs.python.org/3.14/library/io.html#module-io). A performance regression added earlier during Python 3.14 development is thereby fixed, returning performance to the Python 3.13 level.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
