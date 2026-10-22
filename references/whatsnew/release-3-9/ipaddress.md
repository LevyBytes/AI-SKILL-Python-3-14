# What's New In Python 3.9 / ipaddress — ipaddress

### ipaddress

Scoped IPv6 addresses (an IPv6 address carrying the suffix `%<scope_id>`) are now handled by [`ipaddress`](https://docs.python.org/3.14/library/ipaddress.html#module-ipaddress).

You can parse such scoped IPv6 addresses with [`ipaddress.IPv6Address`](https://docs.python.org/3.14/library/ipaddress.html#ipaddress.IPv6Address). When one is present, the scope zone identifier becomes reachable via the [`scope_id`](https://docs.python.org/3.14/library/ipaddress.html#ipaddress.IPv6Address.scope_id) attribute. (Contributed by Oleksandr Pavliuk in [bpo-34788](https://bugs.python.org/issue?@action=redirect&bpo=34788).)

As of Python 3.9.5, leading zeros in IPv4 address strings are rejected by the [`ipaddress`](https://docs.python.org/3.14/library/ipaddress.html#module-ipaddress) module. (Contributed by Christian Heimes in [bpo-36384](https://bugs.python.org/issue?@action=redirect&bpo=36384)).

[Subject index](INDEX.md) · [Previous source section](inspect.md) · [Next source section](math.md) · [Release/subject declaration](summary-release-highlights.md)
