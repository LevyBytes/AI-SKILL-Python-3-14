# Python 3.6.6 release candidate 1 / library / ipaddress

[bpo-27683](https://bugs.python.org/issue?@action=redirect&bpo=27683): Corrected a regression in [`ipaddress`](https://docs.python.org/3.14/library/ipaddress.html#module-ipaddress) under which `hosts()` came back empty when the network was built from a tuple holding an integer mask and only a single bit remaining for addresses.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
