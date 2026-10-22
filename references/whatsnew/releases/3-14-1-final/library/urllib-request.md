# Python 3.14.1 final / library / urllib request

[gh-140691](https://github.com/python/cpython/issues/140691): Within [`urllib.request`](https://docs.python.org/3.14/library/urllib.request.html#module-urllib.request), should a FTP URL fail to open because no data connection can be established, the socket of the control connection is now shut to head off a [`ResourceWarning`](https://docs.python.org/3.14/library/exceptions.html#ResourceWarning).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
