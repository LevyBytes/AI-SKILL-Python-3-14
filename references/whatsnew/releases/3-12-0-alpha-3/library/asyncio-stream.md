# Python 3.12.0 alpha 3 / library / asyncio stream

[gh-88863](https://github.com/python/cpython/issues/88863): When [`asyncio.open_connection()`](https://docs.python.org/3.14/library/asyncio-stream.html#asyncio.open_connection) raises, sever the reference cycles formed by the local exception and the future instance (whose member var holds that exception instance), preventing apparent memory leaks. Dong Uk, Kang supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
