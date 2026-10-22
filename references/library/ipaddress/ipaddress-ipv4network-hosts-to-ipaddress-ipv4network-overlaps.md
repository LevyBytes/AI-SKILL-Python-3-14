# ipaddress: `hosts()`, `overlaps()`

version

 max_prefixlen

Refer to the corresponding attribute documentation in `IPv4Address`.

 is_multicast

 is_private

 is_unspecified

 is_reserved

 is_loopback

 is_link_local

For the network overall, these attributes hold true only when they hold true for both the network address and the broadcast address.

 network_address

This network's network address. The network address paired with the prefix length pins down a network uniquely.

 broadcast_address

This network's broadcast address. Every host on the network should get packets sent to the broadcast address.

 hostmask

The host mask, given as an `IPv4Address` object.

 netmask

The net mask, given as an `IPv4Address` object.

 with_prefixlen

 compressed

 exploded

A string form of the network whose mask appears in prefix notation.

`with_prefixlen` and `compressed` always equal `str(network)`. `exploded` employs the exploded form the network address.

 with_netmask

A string form of the network whose mask appears in net mask notation.

 with_hostmask

A string form of the network whose mask appears in host mask notation.

 num_addresses

How many addresses the network holds in total.

 prefixlen

The network prefix length, measured in bits.

 hosts()

Hands back an iterator across the usable hosts of the network. Those usable hosts are every IP address within the network apart from the network address itself and the network broadcast address. Where the mask length comes out to 31, both the network address and the network broadcast address join the result as well. With a mask of 32, the call hands back a list holding the one host address.

```python
>>> list(ip_network('192.0.2.0/29').hosts())
[IPv4Address('192.0.2.1'), IPv4Address('192.0.2.2'),
 IPv4Address('192.0.2.3'), IPv4Address('192.0.2.4'),
 IPv4Address('192.0.2.5'), IPv4Address('192.0.2.6')]
>>> list(ip_network('192.0.2.0/31').hosts())
[IPv4Address('192.0.2.0'), IPv4Address('192.0.2.1')]
>>> list(ip_network('192.0.2.1/32').hosts())
[IPv4Address('192.0.2.1')]

```

 overlaps(*other*)

`True` when this network sits partly or fully inside *other*, or when *other* sits fully inside this network.

[Subject index](INDEX.md) · [Previous](ipaddress-ipv4network-class.md) · [Continue](ipv4-network-exclusion-subnets-and-supernets.md) · [Owning module, declaration or section: ipaddress.IPv4Network](ipaddress-ipv4network-class.md) · [Owning module, declaration or section: Network objects](ipaddress-ipv4network-class.md)
