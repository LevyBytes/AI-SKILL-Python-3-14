# What's New In Python 3.6 / socket - socket

### socket

The [`SIO_LOOPBACK_FAST_PATH`](https://docs.python.org/3.14/library/socket.html#socket.SIO_LOOPBACK_FAST_PATH) control code is now handled by the [`ioctl()`](https://docs.python.org/3.14/library/socket.html#socket.socket.ioctl) function. (Contributed by Daniel Stokes in [bpo-26536](https://bugs.python.org/issue?@action=redirect&bpo=26536).)

For [`getsockopt()`](https://docs.python.org/3.14/library/socket.html#socket.socket.getsockopt), the constants `SO_DOMAIN`, `SO_PROTOCOL`, `SO_PEERSEC`, and `SO_PASSSEC` now work. (Contributed by Christian Heimes in [bpo-26907](https://bugs.python.org/issue?@action=redirect&bpo=26907).)

The `setsockopt(level, optname, None, optlen: int)` form is now accepted by [`setsockopt()`](https://docs.python.org/3.14/library/socket.html#socket.socket.setsockopt). (Contributed by Christian Heimes in [bpo-27744](https://bugs.python.org/issue?@action=redirect&bpo=27744).)

So it can talk to the Linux Kernel crypto API, the socket module now offers the [`AF_ALG`](https://docs.python.org/3.14/library/socket.html#socket.AF_ALG) address family. Newly added were `ALG_*`, `SOL_ALG` and [`sendmsg_afalg()`](https://docs.python.org/3.14/library/socket.html#socket.socket.sendmsg_afalg). (Contributed by Christian Heimes in [bpo-27744](https://bugs.python.org/issue?@action=redirect&bpo=27744) with support from Victor Stinner.)

The Linux constants `TCP_USER_TIMEOUT` and `TCP_CONGESTION` are new additions. (Contributed by Omar Sandoval, [bpo-26273](https://bugs.python.org/issue?@action=redirect&bpo=26273)).

[Subject index](INDEX.md) · [Previous source section](sqlite3.md) · [Next source section](socketserver.md) · [Release/subject declaration](summary-release-highlights.md)
