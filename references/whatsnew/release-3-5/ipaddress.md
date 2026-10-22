# What’s New In Python 3.5 / ipaddress — ipaddress

### ipaddress

So that network objects can be built easily from addresses you already have, both the [`IPv4Network`](https://docs.python.org/3.14/library/ipaddress.html#ipaddress.IPv4Network) and [`IPv6Network`](https://docs.python.org/3.14/library/ipaddress.html#ipaddress.IPv6Network) classes now take an `(address, netmask)` tuple argument:

```python
>>> import ipaddress
>>> ipaddress.IPv4Network(('127.0.0.0', 8))
IPv4Network('127.0.0.0/8')
>>> ipaddress.IPv4Network(('127.0.0.0', '255.0.0.0'))
IPv4Network('127.0.0.0/8')

```

(Contributed by Peter Moody and Antoine Pitrou in [bpo-16531](https://bugs.python.org/issue?@action=redirect&bpo=16531).)

For the [`IPv4Address`](https://docs.python.org/3.14/library/ipaddress.html#ipaddress.IPv4Address) and [`IPv6Address`](https://docs.python.org/3.14/library/ipaddress.html#ipaddress.IPv6Address) classes, a new [`reverse_pointer`](https://docs.python.org/3.14/library/ipaddress.html#ipaddress.IPv4Address.reverse_pointer) attribute hands back the name belonging to the reverse DNS PTR record:

```python
>>> import ipaddress
>>> addr = ipaddress.IPv4Address('127.0.0.1')
>>> addr.reverse_pointer
'1.0.0.127.in-addr.arpa'
>>> addr6 = ipaddress.IPv6Address('::1')
>>> addr6.reverse_pointer
'1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.ip6.arpa'

```

(Contributed by Leon Weber in [bpo-20480](https://bugs.python.org/issue?@action=redirect&bpo=20480).)

[Subject index](INDEX.md) · [Previous source section](io.md) · [Next source section](json.md) · [Release/subject declaration](summary-release-highlights.md)
