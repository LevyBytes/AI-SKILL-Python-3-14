# Python 3.11.0 alpha 7 / library / asyncio eventloop

[bpo-27929](https://bugs.python.org/issue?@action=redirect&bpo=27929): Adjust [`asyncio.loop.sock_connect()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.sock_connect) so it resolves names solely for the [`socket.AF_INET`](https://docs.python.org/3.14/library/socket.html#socket.AF_INET) or [`socket.AF_INET6`](https://docs.python.org/3.14/library/socket.html#socket.AF_INET6) families. Other families — [`socket.AF_BLUETOOTH`](https://docs.python.org/3.14/library/socket.html#socket.AF_BLUETOOTH) and [`socket.AF_UNIX`](https://docs.python.org/3.14/library/socket.html#socket.AF_UNIX) among them — may have no use for resolution.

[bpo-46955](https://bugs.python.org/issue?@action=redirect&bpo=46955): Surface `asyncio.base_events.Server` under the name [`asyncio.Server`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.Server). Stefan Zabka supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
