# ipaddress: `ipaddress.IPv6Address`

*class *ipaddress.IPv6Address(*address*)

Builds an IPv6 address. Should *address* not be a legitimate IPv6 address, an `AddressValueError` is raised.

Any of the following counts as a legitimate IPv6 address:

1.

A string made of eight groups of four hexadecimal digits, with each group covering 16 bits. Colons separate the groups. That describes the *exploded* (longhand) notation. The string can additionally be *compressed* (shorthand notation) through several means. Consult [**RFC 4291**](https://datatracker.ietf.org/doc/html/rfc4291.html) for the specifics. As an illustration, `"0000:0000:0000:0000:0000:0abc:0007:0def"` may be compressed down to `"::abc:7:def"`.

The string may optionally carry a scope zone ID too, given as a `%scope_id` suffix. When present, that scope ID has to be non-empty and cannot include `%`. Consult [**RFC 4007**](https://datatracker.ietf.org/doc/html/rfc4007.html) for the specifics. As an illustration, `fe80::1234%1` could pick out address `fe80::1234` on the node's first link.

2.

An integer that fits into 128 bits.

3.

An integer packed into a [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) object of length 16, big-endian.

```python
>>> ipaddress.IPv6Address('2001:db8::1000')
IPv6Address('2001:db8::1000')
>>> ipaddress.IPv6Address('ff02::5678%1')
IPv6Address('ff02::5678%1')

```

 compressed

The condensed form of the address, with leading zeroes inside groups dropped and the longest run of all-zero groups folded down to one empty group.

For IPv6 addresses, this is likewise what `str(addr)` returns.

 exploded

The expanded form of the address, keeping every leading zero and every all-zero group in place.

For the attributes and methods listed below, consult the matching documentation on the `IPv4Address` class:

 packed

 reverse_pointer

 version

 max_prefixlen

 is_multicast

 is_private

 is_global

Added in version 3.4.

 is_unspecified

 is_reserved

 is_loopback

 is_link_local

 is_site_local

`True` when the address is set aside for site-local use. Bear in mind that [**RFC 3879**](https://datatracker.ietf.org/doc/html/rfc3879.html) has deprecated the site-local address space. To check whether an address falls within the unique-local address space defined by [**RFC 4193**](https://datatracker.ietf.org/doc/html/rfc4193.html), use `is_private` instead.

 ipv4_mapped

When an address looks like an IPv4 mapped address inside the `::FFFF:0:0/96` range described by [**RFC 4291**](https://datatracker.ietf.org/doc/html/rfc4291.html), this property surfaces the embedded IPv4 address. Otherwise, this property comes back `None`.

 scope_id

For scoped addresses as described by [**RFC 4007**](https://datatracker.ietf.org/doc/html/rfc4007.html), this property names, as a string, the specific zone of the address's scope to which the address belongs. With no scope zone given, this property comes back `None`.

 sixtofour

When an address looks like a 6to4 address (beginning with `2002::/16`) as described by [**RFC 3056**](https://datatracker.ietf.org/doc/html/rfc3056.html), this property surfaces the embedded IPv4 address. Otherwise, this property comes back `None`.

 teredo

When an address looks like a Teredo address (beginning with `2001::/32`) as described by [**RFC 4380**](https://datatracker.ietf.org/doc/html/rfc4380.html), this property surfaces the embedded `(server, client)` IP address pair. Otherwise, this property comes back `None`.

[Subject index](INDEX.md) · [Previous](ipv4address-format.md) · [Continue](ipv6address-format.md) · [Owning module, declaration or section: Address objects](ipaddress-ipv4address-class.md)
