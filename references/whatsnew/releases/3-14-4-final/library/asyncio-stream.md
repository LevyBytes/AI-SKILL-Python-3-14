# Python 3.14.4 final / library / asyncio stream

[gh-142352](https://github.com/python/cpython/issues/142352): [`asyncio.StreamWriter.start_tls()`](https://docs.python.org/3.14/library/asyncio-stream.html#asyncio.StreamWriter.start_tls) now moves any data already buffered in [`StreamReader`](https://docs.python.org/3.14/library/asyncio-stream.html#asyncio.StreamReader) over to the SSL layer. This stops data from being lost when a connection is promoted to TLS in the middle of a stream — for instance, while adding PROXY protocol support.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
