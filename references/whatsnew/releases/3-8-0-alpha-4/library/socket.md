# Python 3.8.0 alpha 4 / library / socket

[bpo-35934](https://bugs.python.org/issue?@action=redirect&bpo=35934): The convenience helpers [`create_server()`](https://docs.python.org/3.14/library/socket.html#socket.create_server) and [`has_dualstack_ipv6()`](https://docs.python.org/3.14/library/socket.html#socket.has_dualstack_ipv6) were added to handle the chores that normally accompany building a server socket, among them accepting IPv4 plus IPv6 connections over one socket. Giampaolo Rodola landed this in [bpo-17561](https://bugs.python.org/issue?@action=redirect&bpo=17561).

[bpo-34139](https://bugs.python.org/issue?@action=redirect&bpo=34139): Clear away any stale unix datagram socket prior to binding

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
