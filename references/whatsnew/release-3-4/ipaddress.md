# What's New In Python 3.4 / ipaddress - ipaddress

### ipaddress

[`ipaddress`](https://docs.python.org/3.14/library/ipaddress.html#module-ipaddress) entered the standard library back in Python 3.3 carrying a [provisional API](https://docs.python.org/3.14/glossary.html#term-provisional-API) label. Once Python 3.4 shipped, that label was dropped: `ipaddress` counts as a stable API, bound by the usual standard library duty to preserve backwards compatibility.

A fresh [`is_global`](https://docs.python.org/3.14/library/ipaddress.html#ipaddress.IPv4Address.is_global) property reads `True` whenever an address is routeable across the global internet. (Contributed by Peter Moody in [bpo-17400](https://bugs.python.org/issue?@action=redirect&bpo=17400).)

[Subject index](INDEX.md) · [Previous source section](inspect.md) · [Next source section](logging.md) · [Release/subject declaration](release-highlights.md)
