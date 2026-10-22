# Python 3.12.0 alpha 1 / library / asyncio streams streamreaderprotocol holds strong reference task spawns preventing task being

[gh-90467](https://github.com/python/cpython/issues/90467): `asyncio.streams.StreamReaderProtocol` now holds a strong reference to the task it spawns, preventing that task from being garbage collected.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
