# What’s New in Python 2.7 / Port-Specific Changes: FreeBSD - socket

### Port-Specific Changes: FreeBSD

- The `SO_SETFIB` constant from FreeBSD 7.1, paired with the [`socket()`](https://docs.python.org/3.14/library/socket.html#socket.socket) methods [`getsockopt()`](https://docs.python.org/3.14/library/socket.html#socket.socket.getsockopt)/[`setsockopt()`](https://docs.python.org/3.14/library/socket.html#socket.socket.setsockopt) for choosing a different routing table, is now offered by the [`socket`](https://docs.python.org/3.14/library/socket.html#module-socket) module. (Added by Kyle VanderBeek; [bpo-8235](https://bugs.python.org/issue?@action=redirect&bpo=8235).)

[Subject index](INDEX.md) · [Previous source section](port-specific-changes-mac-os-x.md) · [Next source section](other-changes-and-fixes.md) · [Release/subject declaration](the-future-for-python-2-x.md)
