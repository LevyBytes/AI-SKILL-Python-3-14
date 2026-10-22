# ipaddress: `subnet_of()`, `supernet_of()`, `compare_networks()`

Yields the supernet that encloses this network definition, with the result governed by the arguments you supply. *prefixlen_diff* gives the number of bits by which the prefix length is to shrink. *new_prefix* names the target prefix you want the supernet to have, and it has to be smaller than the current prefix. Exactly one of *prefixlen_diff* or *new_prefix* may be supplied. The call hands back a single network object.

```python
>>> ip_network('192.0.2.0/24').supernet()
IPv4Network('192.0.2.0/23')
>>> ip_network('192.0.2.0/24').supernet(prefixlen_diff=2)
IPv4Network('192.0.0.0/22')
>>> ip_network('192.0.2.0/24').supernet(new_prefix=20)
IPv4Network('192.0.0.0/20')

```

 subnet_of(*other*)

Hands back `True` whenever this network sits inside *other* as a subnet.

```python
>>> a = ip_network('192.168.1.0/24')
>>> b = ip_network('192.168.1.128/30')
>>> b.subnet_of(a)
True

```

Added in version 3.7.

 supernet_of(*other*)

Hands back `True` whenever this network encloses *other* as a supernet.

```python
>>> a = ip_network('192.168.1.0/24')
>>> b = ip_network('192.168.1.128/30')
>>> a.supernet_of(b)
True

```

Added in version 3.7.

 compare_networks(*other*)

Weigh this network against *other*. The comparison looks solely at the network addresses and leaves host bits out of it. The result is one of `-1`, `0` or `1`.

```python
>>> ip_network('192.0.2.1/32').compare_networks(ip_network('192.0.2.2/32'))
-1
>>> ip_network('192.0.2.1/32').compare_networks(ip_network('192.0.2.0/32'))
1
>>> ip_network('192.0.2.1/32').compare_networks(ip_network('192.0.2.1/32'))
0

```

Deprecated since version 3.7: The ordering and comparison logic it applies is identical to that of “<”, “==”, and “>”

[Subject index](INDEX.md) · [Continue](ipaddress-ipv6network-class-to-ipaddress-ipv6network-hosts.md) · [Owning module, declaration or section: ipaddress.IPv4Network](ipaddress-ipv4network-class.md) · [Owning module, declaration or section: Network objects](ipaddress-ipv4network-class.md) · [Owning module, declaration or section: supernet](ipv4-network-exclusion-subnets-and-supernets.md) · [Preceding source contract and version conditions](ipv4-network-exclusion-subnets-and-supernets.md)
