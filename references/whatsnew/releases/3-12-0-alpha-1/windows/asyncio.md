# Python 3.12.0 alpha 1 / windows / asyncio

[gh-92841](https://github.com/python/cpython/issues/92841): When the interpreter shuts down following asynchronous socket traffic, [`asyncio`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio) no longer raises `RuntimeError: Event loop is closed`. The patch came from Oleg Iarygin.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
