# Python 3.10.0 beta 1 / security / ipaddress

[bpo-36384](https://bugs.python.org/issue?@action=redirect&bpo=36384): The [`ipaddress`](https://docs.python.org/3.14/library/ipaddress.html#module-ipaddress) module will no longer take any leading zeros within IPv4 address strings. Because leading zeros are ambiguous, certain libraries read them as octal notation. As one example, the legacy [`socket.inet_aton()`](https://docs.python.org/3.14/library/socket.html#socket.inet_aton) function reads leading zeros as octal. The glibc build of the modern [`inet_pton()`](https://docs.python.org/3.14/library/socket.html#socket.inet_pton) refuses every leading zero. For some time the `ipaddress` module had been tolerating these ambiguous leading zeros.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
