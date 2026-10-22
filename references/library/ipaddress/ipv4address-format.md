# ipaddress: `IPv4Address.__format__()`

is_global

`True` when the address is marked as globally reachable by [iana-ipv4-special-registry](https://www.iana.org/assignments/iana-ipv4-special-registry/iana-ipv4-special-registry.xhtml) (for IPv4) or [iana-ipv6-special-registry](https://www.iana.org/assignments/iana-ipv6-special-registry/iana-ipv6-special-registry.xhtml) (for IPv6), subject to this exception:

For IPv4-mapped IPv6-addresses, the embedded IPv4 address's semantics govern the `is_private` value, and the relationship below applies (see `IPv6Address.ipv4_mapped`):

```python
address.is_global == address.ipv4_mapped.is_global

```

The value of `is_global` is the inverse of `is_private`, save for the shared address space (`100.64.0.0/10` range), where both come out `False`.

Added in version 3.4.

Changed in version 3.13: Corrected several false positives along with false negatives; consult `is_private` for the particulars.

 is_unspecified

`True` when the address is unspecified. Consult [**RFC 5735**](https://datatracker.ietf.org/doc/html/rfc5735.html) (for IPv4) or [**RFC 2373**](https://datatracker.ietf.org/doc/html/rfc2373.html) (for IPv6).

 is_reserved

`True` when the IETF marks the address as reserved. With IPv4 that covers only `240.0.0.0/4`, the `Reserved` address block. With IPv6 it spans every address [allocated](https://www.iana.org/assignments/ipv6-address-space/ipv6-address-space.xhtml) as `Reserved by IETF` for later use.

Note

With IPv4, `is_reserved` bears no relation to the address-block value found in the `Reserved-by-Protocol` column of [iana-ipv4-special-registry](https://www.iana.org/assignments/iana-ipv4-special-registry/iana-ipv4-special-registry.xhtml).

Caution

With IPv6, `fec0::/10`?a former Site-Local scoped address prefix — is at present left off that list (see `is_site_local` & [**RFC 3879**](https://datatracker.ietf.org/doc/html/rfc3879.html)).

 is_loopback

`True` when this is a loopback address. Consult [**RFC 3330**](https://datatracker.ietf.org/doc/html/rfc3330.html) (for IPv4) or [**RFC 2373**](https://datatracker.ietf.org/doc/html/rfc2373.html) (for IPv6).

 is_link_local

`True` when the address is set aside for link-local use. Consult [**RFC 3927**](https://datatracker.ietf.org/doc/html/rfc3927.html).

 ipv6_mapped

`IPv4Address` object standing for the IPv4-mapped IPv6 address. Consult [**RFC 4291**](https://datatracker.ietf.org/doc/html/rfc4291.html).

Added in version 3.13.

 IPv4Address.__format__(*fmt*)

Hands back a string form of the IP address as dictated by an explicit format string. *fmt* may be any of these: `'s'`, the default, behaving like [`str()`](https://docs.python.org/3.14/library/stdtypes.html#str); `'b'` to get a zero-padded binary string; `'X'` or `'x'` to get an uppercase or, respectively, lowercase hexadecimal form; or `'n'`, which acts as `'b'` for IPv4 addresses and `'x'` for IPv6. With the binary and hexadecimal forms, the form specifier `'#'` and the grouping option `'_'` may be used. `format`, `str.format`, and f-strings all call `__format__`.

```python
>>> format(ipaddress.IPv4Address('192.168.0.1'))
'192.168.0.1'
>>> '{:#b}'.format(ipaddress.IPv4Address('192.168.0.1'))
'0b11000000101010000000000000000001'
>>> f'{ipaddress.IPv6Address("2001:db8::1000"):s}'
'2001:db8::1000'
>>> format(ipaddress.IPv6Address('2001:db8::1000'), '_X')
'2001_0DB8_0000_0000_0000_0000_0000_1000'
>>> '{:#_n}'.format(ipaddress.IPv6Address('2001:db8::1000'))
'0x2001_0db8_0000_0000_0000_0000_0000_1000'

```

Added in version 3.9.

[Subject index](INDEX.md) · [Previous](address-objects.md) · [Continue](ipaddress-ipv6address-class.md) · [Owning module, declaration or section: ipaddress.IPv4Address](ipaddress-ipv4address-class.md) · [Owning module, declaration or section: Address objects](ipaddress-ipv4address-class.md)
