# Python 3.13.0 beta 1 / library / ipaddress

[gh-117566](https://github.com/python/cpython/issues/117566): [`ipaddress.IPv6Address.is_loopback()`](https://docs.python.org/3.14/library/ipaddress.html#ipaddress.IPv6Address.is_loopback) now yields `True` for IPv4-mapped loopback addresses, meaning those inside the `::ffff:127.0.0.0/104` address space.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
