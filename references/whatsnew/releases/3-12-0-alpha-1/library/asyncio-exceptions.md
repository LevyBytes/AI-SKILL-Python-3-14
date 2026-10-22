# Python 3.12.0 alpha 1 / library / asyncio exceptions

[gh-95704](https://github.com/python/cpython/issues/95704): Should a task trap [`asyncio.CancelledError`](https://docs.python.org/3.14/library/asyncio-exceptions.html#asyncio.CancelledError) and then throw a different error, that different error ought not be quietly discarded in general.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
