# What's New In Python 3.13 / ipaddress - ipaddress

### ipaddress

- A new [`IPv4Address.ipv6_mapped`](https://docs.python.org/3.14/library/ipaddress.html#ipaddress.IPv4Address.ipv6_mapped) property has been added; it yields the IPv4-mapped IPv6 address. (Contributed by Charles Machalow in [gh-109466](https://github.com/python/cpython/issues/109466).)

- Corrected how `is_global` and `is_private` behave across [`IPv4Address`](https://docs.python.org/3.14/library/ipaddress.html#ipaddress.IPv4Address), [`IPv6Address`](https://docs.python.org/3.14/library/ipaddress.html#ipaddress.IPv6Address), [`IPv4Network`](https://docs.python.org/3.14/library/ipaddress.html#ipaddress.IPv4Network), and [`IPv6Network`](https://docs.python.org/3.14/library/ipaddress.html#ipaddress.IPv6Network). (Contributed by Jakub Stasiak in [gh-113171](https://github.com/python/cpython/issues/113171).)

[Subject index](INDEX.md) · [Previous source section](io.md) · [Next source section](itertools.md) · [Release/subject declaration](summary-release-highlights.md)
