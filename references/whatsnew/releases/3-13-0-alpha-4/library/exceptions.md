# Python 3.13.0 alpha 4 / library / exceptions

[gh-75128](https://github.com/python/cpython/issues/75128): Pass over an [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) inside `asyncio.BaseEventLoop.create_server()` whenever IPv6 is present yet the interface cannot truly back it.

[gh-104522](https://github.com/python/cpython/issues/104522): An [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) thrown while launching a subprocess now carries a *filename* attribute equal to *cwd* solely when the failure stemmed from an unsuccessful try at changing the working directory.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
