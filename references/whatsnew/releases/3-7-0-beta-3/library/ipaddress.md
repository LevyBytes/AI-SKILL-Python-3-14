# Python 3.7.0 beta 3 / library / ipaddress

[bpo-27683](https://bugs.python.org/issue?@action=redirect&bpo=27683): Correct a regression within [`ipaddress`](https://docs.python.org/3.14/library/ipaddress.html#module-ipaddress) where the `hosts()` result came back empty once the network was built from a tuple holding an integer mask with just 1 bit remaining for addresses.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
