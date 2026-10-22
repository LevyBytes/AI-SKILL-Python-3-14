# Python 3.10.0 alpha 1 / security / collections and iteration

[bpo-41004](https://bugs.python.org/issue?@action=redirect&bpo=41004): For ipaddress.IPv4Interface and ipaddress.IPv6Interface, the __hash__() methods were wrongly returning fixed hash values of 32 and 128 in turn. Because of that, hash collisions happened every time. The repair calls hash() on the tuple of (address, mask length, network address) to derive the value.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
