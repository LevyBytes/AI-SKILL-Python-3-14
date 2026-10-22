# Python 3.8.0 alpha 1 / library / ipaddress

[bpo-32819](https://bugs.python.org/issue?@action=redirect&bpo=32819): ssl.match_hostname() was streamlined and no longer leans on the re and ipaddress module for wildcard and IP addresses. Error reporting around invalid wildcards has improved.

[bpo-27683](https://bugs.python.org/issue?@action=redirect&bpo=27683): Repair a regression within [`ipaddress`](https://docs.python.org/3.14/library/ipaddress.html#module-ipaddress) where `hosts()` returns empty when the network is built from a tuple holding an integer mask and only 1 bit free for addresses.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
