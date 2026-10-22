# Python 3.13.0 alpha 3 / library / logging

[gh-113538](https://github.com/python/cpython/issues/113538): Within `asyncio.StreamReaderProtocol.connection_made()` there is a callback that logs an error whenever the task wrapping the “connected callback” fails. That callback would itself fail once the task got cancelled. Guard against this by first checking whether the task was cancelled. When it was, close the transport yet skip logging an error.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
