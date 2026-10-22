# Python next / library / socket

[gh-143988](https://github.com/python/cpython/issues/143988): Resolved segfaults within [`socket.socket.sendmsg()`](https://docs.python.org/3.14/library/socket.html#socket.socket.sendmsg) plus [`socket.socket.recvmsg_into()`](https://docs.python.org/3.14/library/socket.html#socket.socket.recvmsg_into) that could surface whenever buffer sequences undergo concurrent mutation.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
