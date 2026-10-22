# Python 3.13.0 alpha 6 / library / ipaddress

[gh-113171](https://github.com/python/cpython/issues/113171): Repaired a range of false positives plus false negatives across

  - [`ipaddress.IPv4Address.is_private`](https://docs.python.org/3.14/library/ipaddress.html#ipaddress.IPv4Address.is_private) (consult these docs for specifics)

  - [`ipaddress.IPv4Address.is_global`](https://docs.python.org/3.14/library/ipaddress.html#ipaddress.IPv4Address.is_global)

  - [`ipaddress.IPv6Address.is_private`](https://docs.python.org/3.14/library/ipaddress.html#ipaddress.IPv6Address.is_private)

  - [`ipaddress.IPv6Address.is_global`](https://docs.python.org/3.14/library/ipaddress.html#ipaddress.IPv6Address.is_global)

The matching [`ipaddress.IPv4Network`](https://docs.python.org/3.14/library/ipaddress.html#ipaddress.IPv4Network) and [`ipaddress.IPv6Network`](https://docs.python.org/3.14/library/ipaddress.html#ipaddress.IPv6Network) attributes are covered too.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
