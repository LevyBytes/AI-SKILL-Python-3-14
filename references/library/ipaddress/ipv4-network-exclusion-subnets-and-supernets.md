# ipaddress: `address_exclude()`, `subnets()`, `supernet()`

address_exclude(*network*)

Works out the network definitions left over once the given *network* is taken out of this one. Hands back an iterator of network objects. Raises [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) when *network* is not fully held within this network.

```python
>>> n1 = ip_network('192.0.2.0/28')
>>> n2 = ip_network('192.0.2.1/32')
>>> list(n1.address_exclude(n2))
[IPv4Network('192.0.2.8/29'), IPv4Network('192.0.2.4/30'),
 IPv4Network('192.0.2.2/31'), IPv4Network('192.0.2.0/32')]

```

 subnets(*prefixlen_diff=1*, *new_prefix=None*)

The subnets that combine into the present network definition, governed by the argument values. *prefixlen_diff* is how much to grow our prefix length. *new_prefix* is the wanted new prefix for the subnets; it has to exceed our prefix. Exactly one of *prefixlen_diff* and *new_prefix* may be set. Hands back an iterator of network objects.

```python
>>> list(ip_network('192.0.2.0/24').subnets())
[IPv4Network('192.0.2.0/25'), IPv4Network('192.0.2.128/25')]
>>> list(ip_network('192.0.2.0/24').subnets(prefixlen_diff=2))
[IPv4Network('192.0.2.0/26'), IPv4Network('192.0.2.64/26'),
 IPv4Network('192.0.2.128/26'), IPv4Network('192.0.2.192/26')]
>>> list(ip_network('192.0.2.0/24').subnets(new_prefix=26))
[IPv4Network('192.0.2.0/26'), IPv4Network('192.0.2.64/26'),
 IPv4Network('192.0.2.128/26'), IPv4Network('192.0.2.192/26')]
>>> list(ip_network('192.0.2.0/24').subnets(new_prefix=23))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    raise ValueError('new prefix must be longer')
ValueError: new prefix must be longer
>>> list(ip_network('192.0.2.0/24').subnets(new_prefix=25))
[IPv4Network('192.0.2.0/25'), IPv4Network('192.0.2.128/25')]

```

 supernet(*prefixlen_diff=1*, *new_prefix=None*)

[Subject index](INDEX.md) · [Previous](ipaddress-ipv4network-hosts-to-ipaddress-ipv4network-overlaps.md) · [Owning module, declaration or section: ipaddress.IPv4Network](ipaddress-ipv4network-class.md) · [Owning module, declaration or section: Network objects](ipaddress-ipv4network-class.md) · [Required continuation of the source contract](ipv4-network-containment-and-comparison.md)
