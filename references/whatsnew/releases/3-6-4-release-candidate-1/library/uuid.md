# Python 3.6.4 release candidate 1 / library / uuid

[bpo-9678](https://bugs.python.org/issue?@action=redirect&bpo=9678): Corrected how the uuid module resolves the MAC address: ifconfig is invoked on NetBSD and OpenBSD, while arp serves Linux, FreeBSD, NetBSD and OpenBSD. Takayuki Shimizukawa supplied the original patch this builds on.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
