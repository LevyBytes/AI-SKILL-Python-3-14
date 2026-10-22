# Python 3.14.0 beta 2 / security / ipaddress

[gh-128840](https://github.com/python/cpython/issues/128840): Cut off the handling of lengthy IPv6 addresses up front in [`ipaddress`](https://docs.python.org/3.14/library/ipaddress.html#module-ipaddress) so that runaway memory use and a small denial-of-service are avoided.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
