# Python 3.14.0 alpha 7 / library / textwrap

[gh-107369](https://github.com/python/cpython/issues/107369): The performance of [`textwrap.indent()`](https://docs.python.org/3.14/library/textwrap.html#textwrap.indent) improved by roughly 1.3x on average. Adam Turner contributed the patch.

[gh-131792](https://github.com/python/cpython/issues/131792): The performance of [`textwrap.dedent()`](https://docs.python.org/3.14/library/textwrap.html#textwrap.dedent) rose by about 2.4x on average (reaching up to 4x for large inputs), and a bug was repaired in which blank lines holding whitespace characters apart from space or horizontal tab failed to be normalised to the newline. The patch came from Adam Turner, Marius Juston, and Pieter Eendebak.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
