# Python 3.13.0 alpha 2 / library / asyncio stream

[gh-110894](https://github.com/python/cpython/issues/110894): For exceptions raised in `client_connected_cb` of [`asyncio.start_server()`](https://docs.python.org/3.14/library/asyncio-stream.html#asyncio.start_server), the loop exception handler is now invoked so that applications get a chance to deal with them. Kumar Aditya wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
