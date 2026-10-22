# Python 3.9.0 alpha 1 / library / socket

[bpo-28724](https://bugs.python.org/issue?@action=redirect&bpo=28724): The [`socket.send_fds()`](https://docs.python.org/3.14/library/socket.html#socket.send_fds) and `socket.recv.fds()` methods are now part of the socket module. Joannah Nanjekye, Shinya Okano and Victor Stinner contributed this.

[bpo-11953](https://bugs.python.org/issue?@action=redirect&bpo=11953): Filling out the WSA* error codes within [`socket`](https://docs.python.org/3.14/library/socket.html#module-socket).

[bpo-37811](https://bugs.python.org/issue?@action=redirect&bpo=37811): Fixed the `socket` module's `socket.connect(address)` function, which could not make a connection after an interrupted system call. The issue showed up on every OS whose `poll(2)` system call accepts only non-negative integers along with -1 as the timeout value.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
