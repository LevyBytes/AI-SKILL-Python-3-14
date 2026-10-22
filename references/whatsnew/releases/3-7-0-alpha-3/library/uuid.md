# Python 3.7.0 alpha 3 / library / uuid

[bpo-9678](https://bugs.python.org/issue?@action=redirect&bpo=9678): Corrects how the MAC address gets determined in the uuid module: ifconfig is used on NetBSD and OpenBSD, while arp is used on Linux, FreeBSD, NetBSD and OpenBSD. Takayuki Shimizukawa's patch was the basis.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
