# Python 3.12.0 alpha 4 / library / break reference cycle asyncio selectorsockettransport clearing read ready cb during close

[gh-100348](https://github.com/python/cpython/issues/100348): Break a reference cycle in `asyncio._SelectorSocketTransport` by clearing `_read_ready_cb` during `close`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
