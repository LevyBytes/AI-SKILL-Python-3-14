# Python 3.13.0 alpha 2 / library / asyncio eventloop

[gh-79033](https://github.com/python/cpython/issues/79033): Yet another fix for [`asyncio.Server.wait_closed()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.Server.wait_closed). The call now waits until two requirements both hold: the server has been closed *and* no active connections remain. (Consequently, in certain situations where 3.12.0 would *incorrectly* return at once, the call will instead block — notably whenever no connections are active but the server hasn't yet been closed.)

[gh-111246](https://github.com/python/cpython/issues/111246): Closing a server created via [`asyncio.loop.create_unix_server()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.create_unix_server) now causes its Unix socket to be deleted automatically.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
