# What’s New In Python 3.8 / socket — socket

### socket

A pair of convenience functions, [`create_server()`](https://docs.python.org/3.14/library/socket.html#socket.create_server) and [`has_dualstack_ipv6()`](https://docs.python.org/3.14/library/socket.html#socket.has_dualstack_ipv6), arrived to handle the chores that typically accompany building a server socket, among them taking both IPv4 and IPv6 connections over one socket. (Contributed by Giampaolo Rodolà in [bpo-17561](https://bugs.python.org/issue?@action=redirect&bpo=17561).)

The [`socket.if_nameindex()`](https://docs.python.org/3.14/library/socket.html#socket.if_nameindex), [`socket.if_nametoindex()`](https://docs.python.org/3.14/library/socket.html#socket.if_nametoindex), and [`socket.if_indextoname()`](https://docs.python.org/3.14/library/socket.html#socket.if_indextoname) functions are henceforth available on Windows. (Contributed by Zackery Spytz in [bpo-37007](https://bugs.python.org/issue?@action=redirect&bpo=37007).)

[Subject index](INDEX.md) · [Previous source section](shutil.md) · [Next source section](ssl.md) · [Release/subject declaration](assignment-expressions.md)
