# asyncio.eventloop: Async server listening sockets

sockets

List of socket-like objects, `asyncio.trsock.TransportSocket`, which the server is listening on.

Changed in version 3.7: Before Python 3.7, `Server.sockets` handed back its internal list of server sockets as-is; from 3.7 onward what you get is a copy of that list.

[Subject index](INDEX.md) · [Previous](asyncio-server-close-to-asyncio-server-wait-closed.md) · [Continue](asyncio-selectoreventloop-class.md) · [Owning module, declaration or section: asyncio.Server](asyncio-server-class.md) · [Owning module, declaration or section: Server objects](asyncio-server-class.md)
