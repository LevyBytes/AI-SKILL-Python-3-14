# What's New In Python 3.7 / socketserver - socketserver

### socketserver

[`socketserver.ThreadingMixIn.server_close`](https://docs.python.org/3.14/library/socketserver.html#socketserver.BaseServer.server_close) now holds off until every non-daemon thread has finished. `socketserver.ForkingMixIn.server_close` now holds off until all of the child processes finish.

A new [`socketserver.ForkingMixIn.block_on_close`](https://docs.python.org/3.14/library/socketserver.html#socketserver.ThreadingMixIn.block_on_close) class attribute was added to the [`socketserver.ForkingMixIn`](https://docs.python.org/3.14/library/socketserver.html#socketserver.ForkingMixIn) and [`socketserver.ThreadingMixIn`](https://docs.python.org/3.14/library/socketserver.html#socketserver.ThreadingMixIn) classes. Setting that attribute to `False` restores the pre-3.7 behaviour.

[Subject index](INDEX.md) · [Previous source section](socket.md) · [Next source section](sqlite3.md) · [Release/subject declaration](summary-release-highlights.md)
