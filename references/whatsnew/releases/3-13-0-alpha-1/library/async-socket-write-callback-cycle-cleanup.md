# Python 3.13.0 alpha 1 / library / address ref cycle asyncio selectorsockettransport dropping write ready within close

[gh-106503](https://github.com/python/cpython/issues/106503): Address a ref cycle in `asyncio._SelectorSocketTransport` by dropping `_write_ready` within `close`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
