# What's New In Python 3.9 / socket - socket

### socket

On Linux 4.1 and newer, the [`socket`](https://docs.python.org/3.14/library/socket.html#module-socket) module now makes the [`CAN_RAW_JOIN_FILTERS`](https://docs.python.org/3.14/library/socket.html#socket.CAN_RAW_JOIN_FILTERS) constant available. (Contributed by Stefan Tatschner and Zackery Spytz in [bpo-25780](https://bugs.python.org/issue?@action=redirect&bpo=25780).)

Where the platform allows it, the socket module now handles the [`CAN_J1939`](https://docs.python.org/3.14/library/socket.html#socket.CAN_J1939) protocol. (Contributed by Karl Ding in [bpo-40291](https://bugs.python.org/issue?@action=redirect&bpo=40291).)

Two new functions, [`socket.send_fds()`](https://docs.python.org/3.14/library/socket.html#socket.send_fds) and [`socket.recv_fds()`](https://docs.python.org/3.14/library/socket.html#socket.recv_fds), were added to the socket module. (Contributed by Joannah Nanjekye, Shinya Okano and Victor Stinner in [bpo-28724](https://bugs.python.org/issue?@action=redirect&bpo=28724).)

[Subject index](INDEX.md) · [Previous source section](smtplib.md) · [Next source section](time.md) · [Release/subject declaration](summary-release-highlights.md)
