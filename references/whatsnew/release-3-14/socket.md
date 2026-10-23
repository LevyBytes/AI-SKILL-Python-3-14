# What's new in Python 3.14 / socket - socket

### socket

- Enhance and correct Bluetooth-socket support.

  - Repair Bluetooth-socket handling under NetBSD plus DragonFly BSD. (Serhiy Storchaka authored this work, tracked at [gh-132429](https://github.com/python/cpython/issues/132429).)

  - Mend the [`BTPROTO_HCI`](https://docs.python.org/3.14/library/socket.html#socket.BTPROTO_HCI) path when running on FreeBSD. (Victor Stinner authored this work, tracked at [gh-111178](https://github.com/python/cpython/issues/111178).)

  - Bring [`BTPROTO_SCO`](https://docs.python.org/3.14/library/socket.html#socket.BTPROTO_SCO) handling to FreeBSD. (Serhiy Storchaka authored this work, tracked at [gh-85302](https://github.com/python/cpython/issues/85302).)

  - Let the [`BTPROTO_L2CAP`](https://docs.python.org/3.14/library/socket.html#socket.BTPROTO_L2CAP) address on FreeBSD take *cid* alongside *bdaddr_type*. (Serhiy Storchaka authored this work, tracked at [gh-132429](https://github.com/python/cpython/issues/132429).)

  - Let the [`BTPROTO_HCI`](https://docs.python.org/3.14/library/socket.html#socket.BTPROTO_HCI) address on Linux take a *channel* entry. (Serhiy Storchaka authored this work, tracked at [gh-70145](https://github.com/python/cpython/issues/70145).)

  - Allow a plain integer to serve as the [`BTPROTO_HCI`](https://docs.python.org/3.14/library/socket.html#socket.BTPROTO_HCI) address on Linux. (Serhiy Storchaka authored this work, tracked at [gh-132099](https://github.com/python/cpython/issues/132099).)

  - Return *cid* out of [`getsockname()`](https://docs.python.org/3.14/library/socket.html#socket.socket.getsockname) for the [`BTPROTO_L2CAP`](https://docs.python.org/3.14/library/socket.html#socket.BTPROTO_L2CAP) case. (Serhiy Storchaka authored this work, tracked at [gh-132429](https://github.com/python/cpython/issues/132429).)

  - Bring in a batch of fresh constants. (Serhiy Storchaka authored this work, tracked at [gh-132734](https://github.com/python/cpython/issues/132734).)

[Subject index](INDEX.md) · [Previous source section](re.md) · [Next source section](ssl.md) · [Release/subject declaration](summary-release-highlights.md)
