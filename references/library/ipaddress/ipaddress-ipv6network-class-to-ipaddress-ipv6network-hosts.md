# ipaddress: `ipaddress.IPv6Network`, `hosts()`

*class *ipaddress.IPv6Network(*address*, *strict=True*)

Build an IPv6 network definition. The value of *address* may take any of these forms:

1.

A string that pairs an IP address with an optional prefix length, the two parts divided by a slash (`/`). That IP address serves as the network address, while the prefix length is required to be one number, the *prefix*. When the prefix length is left off, it defaults to `/128`.

Be aware that expanded netmasks have no support at present. So `2001:db00::0/24` passes as a valid argument, whereas `2001:db00::0/ffff:ff00::` does not.

2.

An integer small enough to fit within 128 bits. That amounts to a single-address network whose network address is *address* and whose mask is `/128`.

3.

An integer packed big-endian into a 16-length [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) object. It is read much the same way as an integer *address*.

4.

A two-tuple pairing an address description with a netmask. For the address description, any of the following will do: a string, an integer of 128-bits width, a packed integer occupying 16-bytes, or an already-existing `IPv6Address` object; the netmask, for its part, is an integer that stands for the prefix length.

Should *address* fail to be a valid IPv6 address, an `AddressValueError` results. Should the mask be invalid for an IPv6 address, a `NetmaskValueError` results.

When *strict* equals `True` and the address you give has host bits turned on, a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) follows. Failing that, those host bits get masked away so the right network address can be worked out.

Changed in version 3.5: The two-tuple form became available for the *address* constructor parameter.

 version

 max_prefixlen

 is_multicast

 is_private

 is_unspecified

 is_reserved

 is_loopback

 is_link_local

 network_address

 broadcast_address

 hostmask

 netmask

 with_prefixlen

 compressed

 exploded

 with_netmask

 with_hostmask

 num_addresses

 prefixlen

 hosts()

Gives back an iterator across the network's usable hosts. Those usable hosts comprise every IP address belonging to the network apart from the Subnet-Router anycast address. Where a network has a mask length of 127, the Subnet-Router anycast address is folded into the result as well. A network whose mask is 128 yields a list holding just the single host address.

[Subject index](INDEX.md) · [Previous](ipv4-network-containment-and-comparison.md) · [Continue](ipv6-network-overlap-and-comparison.md) · [Owning module, declaration or section: Network objects](ipaddress-ipv4network-class.md)
