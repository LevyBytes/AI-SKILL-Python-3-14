# Python 3.7.0 alpha 3 / library / asyncio

[bpo-31632](https://bugs.python.org/issue?@action=redirect&bpo=31632): Correct the set_protocol() method on the _SSLProtocolTransport class within the asyncio module. Earlier, that method altered the wrong reference to the protocol.

[bpo-31245](https://bugs.python.org/issue?@action=redirect&bpo=31245): AF_UNIX socket support was added to the asyncio `create_datagram_endpoint`.

[bpo-32069](https://bugs.python.org/issue?@action=redirect&bpo=32069): Removes the legacy SSL transport from asyncio, since ssl.MemoryBIO is what gets used in every case anyway.

[bpo-32066](https://bugs.python.org/issue?@action=redirect&bpo=32066): asyncio: Accept pathlib.Path within create_unix_connection; the sock arg ought to be optional

[bpo-32015](https://bugs.python.org/issue?@action=redirect&bpo=32015): Resolves an asyncio loop that spun whenever the socket was reconnected while an async read/write to or from the socket was being awaited.

[bpo-31970](https://bugs.python.org/issue?@action=redirect&bpo=31970): Cuts the performance cost of asyncio debug mode.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
