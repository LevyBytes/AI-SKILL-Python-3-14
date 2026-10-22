# Python 3.11.0 alpha 1 / library / ipaddress

[bpo-33433](https://bugs.python.org/issue?@action=redirect&bpo=33433): With IPv4 mapped IPv6 addresses ([**RFC 4291**](https://datatracker.ietf.org/doc/html/rfc4291.html) Section 2.5.5.2), the [`ipaddress.IPv6Address.is_private`](https://docs.python.org/3.14/library/ipaddress.html#ipaddress.IPv6Address.is_private) test now defers to the mapped IPv4 address. This fixes a defect whereby public mapped IPv4 addresses came out as private under the IPv6 test.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
