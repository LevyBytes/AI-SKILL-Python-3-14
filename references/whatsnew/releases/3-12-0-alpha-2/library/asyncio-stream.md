# Python 3.12.0 alpha 2 / library / asyncio stream

[gh-98703](https://github.com/python/cpython/issues/98703): Make [`asyncio.StreamWriter.drain()`](https://docs.python.org/3.14/library/asyncio-stream.html#asyncio.StreamWriter.drain) invoke the `protocol.connection_lost` callback just a single time on Windows.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
