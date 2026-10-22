# Python 3.14.0 alpha 1 / library / ipaddress

[gh-124217](https://github.com/python/cpython/issues/124217): Brings the RFC 9637 reserved IPv6 block `3fff::/20` into the [`ipaddress`](https://docs.python.org/3.14/library/ipaddress.html#module-ipaddress) module.

[gh-123409](https://github.com/python/cpython/issues/123409): Repairs the [`ipaddress.IPv6Address.reverse_pointer`](https://docs.python.org/3.14/library/ipaddress.html#ipaddress.IPv6Address.reverse_pointer) output to match [**RFC 3596, ??2.5**](https://datatracker.ietf.org/doc/html/rfc3596.html#section-2.5). Bénédikt Tran wrote the patch.

[gh-118710](https://github.com/python/cpython/issues/118710): The `version` and `max_prefixlen` attributes of [`ipaddress.IPv4Address`](https://docs.python.org/3.14/library/ipaddress.html#ipaddress.IPv4Address) and [`ipaddress.IPv6Address`](https://docs.python.org/3.14/library/ipaddress.html#ipaddress.IPv6Address) can now be reached directly on the class.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
