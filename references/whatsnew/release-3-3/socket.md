# What's New In Python 3.3 / socket — socket

### socket

- When the host platform allows it, the [`socket`](https://docs.python.org/3.14/library/socket.html#socket.socket) class now offers extra methods for handling ancillary data:

  - [`sendmsg()`](https://docs.python.org/3.14/library/socket.html#socket.socket.sendmsg)

  - [`recvmsg()`](https://docs.python.org/3.14/library/socket.html#socket.socket.recvmsg)

  - [`recvmsg_into()`](https://docs.python.org/3.14/library/socket.html#socket.socket.recvmsg_into)

(Contributed by David Watson in [bpo-6560](https://bugs.python.org/issue?@action=redirect&bpo=6560); it built upon a prior patch from Heiko Wundram)

- The [`socket`](https://docs.python.org/3.14/library/socket.html#socket.socket) class now handles the PF_CAN protocol family ([https://en.wikipedia.org/wiki/Socketcan](https://en.wikipedia.org/wiki/Socketcan)), on Linux ([https://lwn.net/Articles/253425](https://lwn.net/Articles/253425)).

(Contributed by Matthias Fuchs, updated by Tiago Gonçalves in [bpo-10141](https://bugs.python.org/issue?@action=redirect&bpo=10141).)

- The [`socket`](https://docs.python.org/3.14/library/socket.html#socket.socket) class now handles the PF_RDS protocol family ([https://en.wikipedia.org/wiki/Reliable_Datagram_Sockets](https://en.wikipedia.org/wiki/Reliable_Datagram_Sockets) and [https://oss.oracle.com/projects/rds](https://web.archive.org/web/20130115155505/https://oss.oracle.com/projects/rds/)).

- The [`socket`](https://docs.python.org/3.14/library/socket.html#socket.socket) class now handles the `PF_SYSTEM` protocol family under OS X. (Contributed by Michael Goderbauer in [bpo-13777](https://bugs.python.org/issue?@action=redirect&bpo=13777).)

- A new [`sethostname()`](https://docs.python.org/3.14/library/socket.html#socket.sethostname) function permits setting the hostname on Unix systems whenever the calling process holds adequate privileges. (Contributed by Ross Lagerwall in [bpo-10866](https://bugs.python.org/issue?@action=redirect&bpo=10866).)

### socketserver

[Subject index](INDEX.md) · [Previous source section](smtplib.md) · [Release/subject declaration](summary-release-highlights.md) · [Following release/subject continuation](socketserver.md)
