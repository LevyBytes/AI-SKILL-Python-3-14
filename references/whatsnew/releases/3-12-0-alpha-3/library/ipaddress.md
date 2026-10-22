# Python 3.12.0 alpha 3 / library / ipaddress

[gh-82836](https://github.com/python/cpython/issues/82836): Correct the [`is_private`](https://docs.python.org/3.14/library/ipaddress.html#ipaddress.IPv4Address.is_private) properties in the [`ipaddress`](https://docs.python.org/3.14/library/ipaddress.html#module-ipaddress) module. Formerly non-private networks (0.0.0.0/0) reported `True` from this method; they now correctly report `False`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
