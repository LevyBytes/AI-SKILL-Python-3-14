# Python 3.12.0 alpha 1 / library / linecache

[gh-92336](https://github.com/python/cpython/issues/92336): A defect where [`linecache.getline()`](https://docs.python.org/3.14/library/linecache.html#linecache.getline) broke on bad files with a [`UnicodeDecodeError`](https://docs.python.org/3.14/library/exceptions.html#UnicodeDecodeError) or [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError) is fixed. It now hands back an empty string just as the documentation says.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
