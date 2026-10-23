# ipaddress: IP address version and classification properties

version

The relevant version number: `4` for IPv4 and `6` for IPv6.

Changed in version 3.14: Made available on the class.

 max_prefixlen

How many bits the address occupies in this version overall: `32` for IPv4 and `128` for IPv6.

The prefix sets how many of an address's leading bits get compared when deciding whether that address belongs to a network.

Changed in version 3.14: Made available on the class.

 compressed

 exploded

The string form written in dotted decimal notation. Leading zeroes never appear in this form.

Since IPv4 offers no shorthand for addresses whose octets are zero, for IPv4 addresses these two attributes always match `str(addr)`. Surfacing them makes it simpler to author display logic that copes with both IPv4 and IPv6 addresses.

 packed

This address in binary form - a [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) object of the matching length (most significant octet first). For IPv4 that is 4 bytes, and for IPv6 it is 16 bytes.

 reverse_pointer

The reverse DNS PTR record name for the IP address, for example:

```python
>>> ipaddress.ip_address("127.0.0.1").reverse_pointer
'1.0.0.127.in-addr.arpa'
>>> ipaddress.ip_address("2001:db8::1").reverse_pointer
'1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.8.b.d.0.1.0.0.2.ip6.arpa'

```

This is the name you would query with a PTR lookup; it is not the resolved hostname.

Added in version 3.5.

 is_multicast

`True` when the address is set aside for multicast purposes. Consult [**RFC 3171**](https://datatracker.ietf.org/doc/html/rfc3171.html) (for IPv4) or [**RFC 2373**](https://datatracker.ietf.org/doc/html/rfc2373.html) (for IPv6).

 is_private

`True` when the address is marked as not globally reachable by [iana-ipv4-special-registry](https://www.iana.org/assignments/iana-ipv4-special-registry/iana-ipv4-special-registry.xhtml) (for IPv4) or [iana-ipv6-special-registry](https://www.iana.org/assignments/iana-ipv6-special-registry/iana-ipv6-special-registry.xhtml) (for IPv6), subject to these exceptions:

- `is_private` is `False` for the shared address space (`100.64.0.0/10`)

- With IPv4-mapped IPv6-addresses, the underlying IPv4 address's semantics drive the `is_private` value, so that this relationship is satisfied (see `IPv6Address.ipv4_mapped`):

```python
address.is_private == address.ipv4_mapped.is_private

```

The value of `is_private` is the inverse of `is_global`, save for the shared address space (`100.64.0.0/10` range), where both come out `False`.

Changed in version 3.13: Fixed some false positives and false negatives.

- `192.0.0.0/24` counts as private aside from `192.0.0.9/32` and `192.0.0.10/32` (formerly only the `192.0.0.0/29` sub-range counted as private).

- `64:ff9b:1::/48` counts as private.

- `2002::/16` counts as private.

- Within `2001::/23` (otherwise treated as private) some exceptions apply: `2001:1::1/128`, `2001:1::2/128`, `2001:3::/32`, `2001:4:112::/48`, `2001:20::/28`, `2001:30::/28`. Those exceptions do not count as private.

[Subject index](INDEX.md) · [Previous](ipaddress-ipv4address-class.md) · [Continue](ipv4address-format.md) · [Owning module, declaration or section: ipaddress.IPv4Address](ipaddress-ipv4address-class.md) · [Owning module, declaration or section: Address objects](ipaddress-ipv4address-class.md)
