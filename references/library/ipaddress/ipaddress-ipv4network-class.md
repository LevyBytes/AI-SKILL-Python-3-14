# ipaddress: `ipaddress.IPv4Network`

### Network objects

Every attribute that address objects provide is provided by network objects too. Beyond those, network objects add further attributes. Since all of these are shared between `IPv4Network` and `IPv6Network`, they are documented only against `IPv4Network` to avoid repeating things. Because network objects are [hashable](https://docs.python.org/3.14/glossary.html#term-hashable), you can employ them as dictionary keys.

 *class *ipaddress.IPv4Network(*address*, *strict=True*)

Builds an IPv4 network definition. *address* may take any of these forms:

1.

A string holding an IP address plus an optional mask, the two divided by a slash (`/`). The IP address serves as the network address, and the mask is either a lone number — meaning a *prefix*?or the string form of an IPv4 address. In the latter case, the mask reads as a *net mask* when it opens with a non-zero field, or as a *host mask* when it opens with a zero field, with the lone exception of an all-zero mask, which is handled as a *net mask*. Absent any mask, `/32` is assumed.

To illustrate, these *address* specifications all mean the same thing: `192.168.1.0/24`, `192.168.1.0/255.255.255.0` and `192.168.1.0/0.0.0.255`.

2.

An integer that fits into 32 bits. This matches a single-address network, where *address* is the network address and the mask is `/32`.

3.

An integer packed into a [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) object of length 4, big-endian. It is read much like an integer *address*.

4.

A two-tuple combining an address description with a netmask. For the address description, the permitted forms are a string, a 32-bits integer, a 4-bytes packed integer, and also an `IPv4Address` object that already exists. The netmask, meanwhile, is either an integer giving the prefix length (such as `24`) or a string giving the prefix mask (such as `255.255.255.0`).

When *address* is not a legitimate IPv4 address, an `AddressValueError` is raised. When the mask is not valid for an IPv4 address, a `NetmaskValueError` is raised.

When *strict* is `True` and the supplied address has host bits set, [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) is raised. Otherwise those host bits are cleared to work out the right network address.

Except where noted, every network method that takes other network or address objects raises [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) when the argument's IP version does not match `self`.

Changed in version 3.5: The *address* constructor parameter gained its two-tuple form.

[Subject index](INDEX.md) · [Previous](prefix-net-mask-and-host-mask.md) · [Continue](ipaddress-ipv4network-hosts-to-ipaddress-ipv4network-overlaps.md)
