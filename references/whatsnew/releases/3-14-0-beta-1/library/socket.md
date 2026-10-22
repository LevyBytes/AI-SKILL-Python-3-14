# Python 3.14.0 beta 1 / library / socket

[gh-132734](https://github.com/python/cpython/issues/132734): Add new constants for Bluetooth [`sockets`](https://docs.python.org/3.14/library/socket.html#module-socket).

[gh-129719](https://github.com/python/cpython/issues/129719): On Linux, the socket module's `socket.CAN_RAW_ERR_FILTER` constant, absent ever since Python 3.11, has been restored.

[gh-85302](https://github.com/python/cpython/issues/85302): Provide [`BTPROTO_SCO`](https://docs.python.org/3.14/library/socket.html#socket.BTPROTO_SCO) support for sockets running on FreeBSD.

[gh-132099](https://github.com/python/cpython/issues/132099): On Linux, the Bluetooth socket using the [`BTPROTO_HCI`](https://docs.python.org/3.14/library/socket.html#socket.BTPROTO_HCI) protocol will now take an address given as an integer `device_id`, and no longer requires a tuple `(device_id,)`.

[gh-70145](https://github.com/python/cpython/issues/70145): Provide channel support within the Bluetooth HCI protocol ([`BTPROTO_HCI`](https://docs.python.org/3.14/library/socket.html#socket.BTPROTO_HCI)).

[gh-132429](https://github.com/python/cpython/issues/132429): Repair Bluetooth socket handling on NetBSD and DragonFly BSD. Provide *cid* and *bdaddr_type* support within the BTPROTO_L2CAP address on FreeBSD. Hand back *cid* from `getsockname()` for BTPROTO_L2CAP whenever it is non-zero.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
