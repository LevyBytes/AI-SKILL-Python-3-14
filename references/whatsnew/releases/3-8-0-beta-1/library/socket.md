# Python 3.8.0 beta 1 / library / socket

[bpo-37027](https://bugs.python.org/issue?@action=redirect&bpo=37027): Hands back a proxy socket object that is safe to use from transport.get_extra_info(‘socket’)

[bpo-31922](https://bugs.python.org/issue?@action=redirect&bpo=31922): `asyncio.AbstractEventLoop.create_datagram_endpoint()`: Skips connecting the UDP socket while broadcast is permitted. Doing so makes it possible to take in replies following a UDP broadcast.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
