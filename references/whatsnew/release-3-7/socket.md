# What's New In Python 3.7 / socket — os, socket

### socket

A new [`socket.getblocking()`](https://docs.python.org/3.14/library/socket.html#socket.socket.getblocking) method gives back `True` when the socket sits in blocking mode and `False` if not. (Contributed by Yury Selivanov in [bpo-32373](https://bugs.python.org/issue?@action=redirect&bpo=32373).)

A new [`socket.close()`](https://docs.python.org/3.14/library/socket.html#socket.close) function shuts the socket file descriptor passed to it. Reach for this rather than [`os.close()`](https://docs.python.org/3.14/library/os.html#os.close), since it behaves more consistently from one platform to the next. (Contributed by Christian Heimes in [bpo-32454](https://bugs.python.org/issue?@action=redirect&bpo=32454).)

The [`socket`](https://docs.python.org/3.14/library/socket.html#module-socket) module now surfaces the [socket.TCP_CONGESTION](https://docs.python.org/3.14/library/socket.html#socket-unix-constants) (Linux 2.6.13), [socket.TCP_USER_TIMEOUT](https://docs.python.org/3.14/library/socket.html#socket-unix-constants) (Linux 2.6.37), and [socket.TCP_NOTSENT_LOWAT](https://docs.python.org/3.14/library/socket.html#socket-unix-constants) (Linux 3.12) constants. (Contributed by Omar Sandoval in [bpo-26273](https://bugs.python.org/issue?@action=redirect&bpo=26273) and Nathaniel J. Smith in [bpo-29728](https://bugs.python.org/issue?@action=redirect&bpo=29728).)

[`socket.AF_VSOCK`](https://docs.python.org/3.14/library/socket.html#socket.AF_VSOCK) sockets are now supported, enabling traffic to pass between virtual machines and the hosts they run on. (Contributed by Cathy Avery in [bpo-27584](https://bugs.python.org/issue?@action=redirect&bpo=27584).)

By default, sockets now figure out the family, type and protocol straight from the file descriptor. (Contributed by Christian Heimes in [bpo-28134](https://bugs.python.org/issue?@action=redirect&bpo=28134).)

### socket

Quietly truncating the argument value inside [`socket.htons()`](https://docs.python.org/3.14/library/socket.html#socket.htons) and [`socket.ntohs()`](https://docs.python.org/3.14/library/socket.html#socket.ntohs) is now deprecated. From later Python versions onward, supplying an argument wider than 16 bits will raise an exception. (Contributed by Oren Milman in [bpo-28332](https://bugs.python.org/issue?@action=redirect&bpo=28332).)

[Subject index](INDEX.md) · [Previous source section](signal.md) · [Next source section](socketserver.md) · [Release/subject declaration](summary-release-highlights.md) · [Previous source section](threading.md) · [Next source section](ssl.md)
