# Python 3.7.0 alpha 4 / library / asyncio

[bpo-32327](https://bugs.python.org/issue?@action=redirect&bpo=32327): Turn the asyncio functions documented as coroutines into actual coroutines. These functions are affected: loop.sock_sendall, loop.sock_recv, loop.sock_accept, loop.getaddrinfo, loop.getnameinfo.

[bpo-29711](https://bugs.python.org/issue?@action=redirect&bpo=29711): Repair `stop_serving` in the asyncio proactor loop killing every listening server

[bpo-29970](https://bugs.python.org/issue?@action=redirect&bpo=29970): Tear down the asyncio SSLProtocol connection when the handshake fails to finish inside 10 seconds.

[bpo-32253](https://bugs.python.org/issue?@action=redirect&bpo=32253): For asyncio synchronization primitives, deprecate `yield from lock`, `await lock`, `with (yield from lock)` and `with await lock`.

[bpo-32193](https://bugs.python.org/issue?@action=redirect&bpo=32193): Move asyncio onto *async/await* syntax. The older `yield from` style still works as well.

[bpo-23749](https://bugs.python.org/issue?@action=redirect&bpo=23749): asyncio: Provide loop.start_tls()

[bpo-32415](https://bugs.python.org/issue?@action=redirect&bpo=32415): asyncio: Provide Task.get_loop() and Future.get_loop()

[bpo-26133](https://bugs.python.org/issue?@action=redirect&bpo=26133): On interpreter shutdown, refrain from unsubscribing signals within the asyncio UNIX event loop.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
