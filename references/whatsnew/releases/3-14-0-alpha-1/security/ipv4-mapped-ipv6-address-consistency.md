# Python 3.14.0 alpha 1 / security / made ipv4 mapped ipaddress ipv6address rely uniformly mapped ipv4 address value

[gh-122792](https://github.com/python/cpython/issues/122792): Made IPv4-mapped `ipaddress.IPv6Address` rely uniformly on the mapped IPv4 address value when determining properties. The properties whose behavior is now corrected are `is_multicast`, `is_reserved`, `is_link_local`, `is_global`, and `is_unspecified`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
