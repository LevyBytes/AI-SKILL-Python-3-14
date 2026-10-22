# Python 3.13.0 alpha 3 / library / asyncio

[gh-113214](https://github.com/python/cpython/issues/113214): Resolved an `AttributeError` happening during asyncio SSL protocol aborts in SSL-over-SSL scenarios.

[gh-112989](https://github.com/python/cpython/issues/112989): Cut the overhead of opening socket connections through the [`asyncio`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio) SelectorEventLoop.

[gh-112800](https://github.com/python/cpython/issues/112800): Stop [`asyncio`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio) `SubprocessTransport.close()` from raising `PermissionError` when it is used against setuid executables.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
