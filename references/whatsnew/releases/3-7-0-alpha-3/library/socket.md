# Python 3.7.0 alpha 3 / library / socket

[bpo-32154](https://bugs.python.org/issue?@action=redirect&bpo=32154): The `asyncio.windows_utils.socketpair()` function is gone: call [`socket.socketpair()`](https://docs.python.org/3.14/library/socket.html#socket.socketpair) directly, which every platform has carried since Python 3.5 (formerly it was missing on Windows). On Python 3.5 and later, `asyncio.windows_utils.socketpair()` had merely been an alias of `socket.socketpair`.

[bpo-28369](https://bugs.python.org/issue?@action=redirect&bpo=28369): Improves the add_reader/writer test confirming that a socket is not in use by some transport. Formerly only the cases where add_reader/writer received an int FD were covered. The check is now done correctly for every file-like object.

[bpo-31927](https://bugs.python.org/issue?@action=redirect&bpo=31927): Repairs compilation of the socket module on NetBSD 8. Also fixes an assertion failure, plus the reading of arbitrary data, when an AF_BLUETOOTH address is parsed on NetBSD and DragonFly BSD.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
