# Python 3.13.0 alpha 1 / library / dataclasses

[gh-110273](https://github.com/python/cpython/issues/110273): [`dataclasses.replace()`](https://docs.python.org/3.14/library/dataclasses.html#dataclasses.replace) now signals TypeError rather than ValueError when a keyword argument is given for a field declared with init=False, or when a keyword argument for a required InitVar field is omitted.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
