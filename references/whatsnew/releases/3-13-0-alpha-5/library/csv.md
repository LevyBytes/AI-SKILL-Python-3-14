# Python 3.13.0 alpha 5 / library / csv

[gh-67044](https://github.com/python/cpython/issues/67044): [`csv.writer()`](https://docs.python.org/3.14/library/csv.html#csv.writer) now invariably quotes or escapes `'\r'` and `'\n'`, no matter the *lineterminator* value.

[gh-115712](https://github.com/python/cpython/issues/115712): Bring back support for a space delimiter together with `skipinitialspace=True` inside [`csv`](https://docs.python.org/3.14/library/csv.html#module-csv). [`csv.writer()`](https://docs.python.org/3.14/library/csv.html#csv.writer) now quotes empty fields when the delimiter is a space and skipinitialspace is true, and raises an exception whenever quoting cannot happen.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
