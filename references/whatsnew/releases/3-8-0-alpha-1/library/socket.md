# Python 3.8.0 alpha 1 / library / socket

[bpo-32394](https://bugs.python.org/issue?@action=redirect&bpo=32394): socket: At run time on older Windows releases, drop the TCP_FASTOPEN,TCP_KEEPCNT,TCP_KEEPIDLE,TCP_KEEPINTVL flags.

[bpo-34521](https://bugs.python.org/issue?@action=redirect&bpo=34521): Within `multiprocessing.reduction.recvfds()`, the ancillary data size is now derived from [`socket.CMSG_SPACE()`](https://docs.python.org/3.14/library/socket.html#socket.CMSG_SPACE) rather than [`socket.CMSG_LEN()`](https://docs.python.org/3.14/library/socket.html#socket.CMSG_LEN), since [**RFC 3542**](https://datatracker.ietf.org/doc/html/rfc3542.html) mandates the former for applications that aim to be portable.

[bpo-34638](https://bugs.python.org/issue?@action=redirect&bpo=34638): A weak reference to the stream reader is now kept so the strong reference loop between reader and protocol is broken. This makes it possible to spot and close the socket when the stream is dropped (garbage collected) absent any `close()` call.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
