# Python 3.12.0 beta 1 / library / asyncio protocol

[gh-103462](https://github.com/python/cpython/issues/103462): Corrected a problem where using [`writelines()`](https://docs.python.org/3.14/library/asyncio-protocol.html#asyncio.WriteTransport.writelines) within [`asyncio`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio) to transmit very large payloads exceeding what a single call to [`socket.socket.send()`](https://docs.python.org/3.14/library/socket.html#socket.socket.send) or [`socket.socket.sendmsg()`](https://docs.python.org/3.14/library/socket.html#socket.socket.sendmsg) can write left the remaining buffer unsent.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
