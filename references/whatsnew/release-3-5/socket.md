# What’s New In Python 3.5 / socket - os, socket

### socket

In place of a system clock, functions carrying timeouts now rely on a monotonic clock. Victor Stinner landed this (see [bpo-22043](https://bugs.python.org/issue?@action=redirect&bpo=22043)).

By leaning on the fast [`os.sendfile()`](https://docs.python.org/3.14/library/os.html#os.sendfile) function on UNIX, the new [`socket.sendfile()`](https://docs.python.org/3.14/library/socket.html#socket.socket.sendfile) method can push a file out over a socket — making uploads roughly 2 to 3 times quicker than ordinary [`socket.send()`](https://docs.python.org/3.14/library/socket.html#socket.socket.send) would manage. Giampaolo Rodola’ added this (see [bpo-17552](https://bugs.python.org/issue?@action=redirect&bpo=17552)).

Every time data is sent or received, the [`socket.sendall()`](https://docs.python.org/3.14/library/socket.html#socket.socket.sendall) method no longer restarts the socket timeout. That timeout now represents the longest overall span permitted to transmit all of the data. Victor Stinner contributed this (see [bpo-23853](https://bugs.python.org/issue?@action=redirect&bpo=23853)).

For the [`socket.listen()`](https://docs.python.org/3.14/library/socket.html#socket.socket.listen) method, the *backlog* argument has become optional. When omitted it falls back to whichever of [`SOMAXCONN`](https://docs.python.org/3.14/library/socket.html#socket.SOMAXCONN) or `128` is smaller. Charles-François Natali landed this (see [bpo-21455](https://bugs.python.org/issue?@action=redirect&bpo=21455)).

[Subject index](INDEX.md) · [Previous source section](sndhdr.md) · [Next source section](ssl-memory-bio-support.md) · [Release/subject declaration](summary-release-highlights.md)
