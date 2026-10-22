# Python 3.14.6 final / core and builtins / asyncio

[gh-150107](https://github.com/python/cpython/issues/150107): [`asyncio`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio): the `sendfile()` and `sock_sendfile()` event loop methods now invoke `file.seek(offset)` whenever *file* exposes a `seek()` method, even where *offset* equals `0` (the default value).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
