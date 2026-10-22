# Python 3.14.0 beta 2 / library / asyncio

[gh-114177](https://github.com/python/cpython/issues/114177): Adjust [`asyncio`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio) so it leaves subprocess pipes open, since closing them would error when the event loop is already shut.

[gh-86802](https://github.com/python/cpython/issues/86802): Repaired an asyncio memory leak in cancelled shield tasks. For shielded tasks whose shield got cancelled, any leftover exceptions are now logged via the exception handler. Contributed by Christian Harries.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
