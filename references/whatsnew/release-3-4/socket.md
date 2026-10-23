# What's New In Python 3.4 / socket - enum, os, socket

### socket

The socket module has added support for the [`CAN_BCM`](https://docs.python.org/3.14/library/socket.html#socket.CAN_BCM) protocol wherever the platform offers it. (Contributed by Brian Thorne in [bpo-15359](https://bugs.python.org/issue?@action=redirect&bpo=15359).)

Socket objects expose new methods for reading or assigning their [inheritable flag](https://docs.python.org/3.14/library/os.html#fd-inheritance), namely [`get_inheritable()`](https://docs.python.org/3.14/library/socket.html#socket.socket.get_inheritable) and [`set_inheritable()`](https://docs.python.org/3.14/library/socket.html#socket.socket.set_inheritable).

The `socket.AF_*` and `socket.SOCK_*` constants have become enumeration members backed by the new [`enum`](https://docs.python.org/3.14/library/enum.html#module-enum) module. Thanks to this, readable names show up while debugging rather than bare integer "magic numbers".

The [`AF_LINK`](https://docs.python.org/3.14/library/socket.html#socket.AF_LINK) constant is now exposed on BSD and OSX.

[`inet_pton()`](https://docs.python.org/3.14/library/socket.html#socket.inet_pton) and [`inet_ntop()`](https://docs.python.org/3.14/library/socket.html#socket.inet_ntop) work on Windows as of this release. (Contributed by Atsuo Ishimoto in [bpo-7171](https://bugs.python.org/issue?@action=redirect&bpo=7171).)

[Subject index](INDEX.md) · [Previous source section](smtplib.md) · [Next source section](sqlite3.md) · [Release/subject declaration](release-highlights.md)
