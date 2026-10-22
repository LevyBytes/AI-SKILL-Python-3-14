# Python 3.13.0 alpha 4 / library / csv

[gh-113796](https://github.com/python/cpython/issues/113796): Layer in extra validation within the [`csv.Dialect`](https://docs.python.org/3.14/library/csv.html#csv.Dialect) constructor. A [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) now gets raised should one identical character be assigned to differing roles.

[gh-113732](https://github.com/python/cpython/issues/113732): Correct the handling of [`QUOTE_NOTNULL`](https://docs.python.org/3.14/library/csv.html#csv.QUOTE_NOTNULL) and [`QUOTE_STRINGS`](https://docs.python.org/3.14/library/csv.html#csv.QUOTE_STRINGS) inside [`csv.reader()`](https://docs.python.org/3.14/library/csv.html#csv.reader).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
