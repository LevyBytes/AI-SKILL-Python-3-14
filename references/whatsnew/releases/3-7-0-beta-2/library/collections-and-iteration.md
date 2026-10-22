# Python 3.7.0 beta 2 / library / collections and iteration

[bpo-32852](https://bugs.python.org/issue?@action=redirect&bpo=32852): Guarantee that sys.argv stays a list throughout a trace run.

[bpo-32221](https://bugs.python.org/issue?@action=redirect&bpo=32221): Assorted functions that return a tuple holding IPv6 addresses now leave out the `%scope` portion given that the very same data already lives within the *scopeid* tuple item. This in particular makes `socket.recvfrom()` quicker whenever it gets a multicast packet, since the pointless resolving of the network interface name is skipped.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
