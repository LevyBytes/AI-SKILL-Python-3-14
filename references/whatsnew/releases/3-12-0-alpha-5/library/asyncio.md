# Python 3.12.0 alpha 5 / library / asyncio

[gh-100573](https://github.com/python/cpython/issues/100573): Close a Windows [`asyncio`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio) bug with named pipes whereby a client calling `os.stat()` against the pipe would throw the server into an error that blocked any later requests.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
