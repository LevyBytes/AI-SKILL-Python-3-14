# Python 3.9.0 alpha 5 / library / uuid

[bpo-39991](https://bugs.python.org/issue?@action=redirect&bpo=39991): When an IPv6 address happens to share the 17-character string length of a MAC address, [`uuid.getnode()`](https://docs.python.org/3.14/library/uuid.html#uuid.getnode) now passes over it: only genuine MAC addresses are used.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
