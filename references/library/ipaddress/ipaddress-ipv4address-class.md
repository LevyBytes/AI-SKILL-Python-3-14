# ipaddress: `ipaddress.IPv4Address`

### IP Addresses

### Address objects

`IPv4Address` and `IPv6Address` objects hold many attributes in common. A handful of attributes that only matter for IPv6 addresses are nonetheless provided on `IPv4Address` objects too, so that writing code which correctly serves both IP versions becomes simpler. Because address objects are [hashable](https://docs.python.org/3.14/glossary.html#term-hashable), you can employ them as dictionary keys.

 *class *ipaddress.IPv4Address(*address*)

Builds an IPv4 address. Should *address* not be a legitimate IPv4 address, an `AddressValueError` is raised.

Any of the following counts as a legitimate IPv4 address:

1.

A string written in decimal-dot notation — four decimal integers within the inclusive 0–255 range, joined by dots (for instance `192.168.0.1`). Every integer stands for one octet (byte) of the address. To avoid being mistaken for octal notation, leading zeroes are rejected.

2.

An integer that fits into 32 bits.

3.

An integer that has been packed, most significant octet leading, into a length-4 [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) object.

```python
>>> ipaddress.IPv4Address('192.168.0.1')
IPv4Address('192.168.0.1')
>>> ipaddress.IPv4Address(3232235521)
IPv4Address('192.168.0.1')
>>> ipaddress.IPv4Address(b'\xC0\xA8\x00\x01')
IPv4Address('192.168.0.1')

```

Changed in version 3.8: Leading zeros become permissible, including the ambiguous cases that resemble octal notation.

Changed in version 3.9.5: Leading zeros stop being permissible and now trigger an error; the parsing of IPv4 address strings became as strict as glibc [`inet_pton()`](https://docs.python.org/3.14/library/socket.html#socket.inet_pton).

[Subject index](INDEX.md) · [Continue](address-objects.md)
