# Conversion to Strings and Integers

### Conversion to Strings and Integers

To work alongside networking interfaces like the socket module, addresses have to become strings or integers. The [`str()`](https://docs.python.org/3.14/library/stdtypes.html#str) and [`int()`](https://docs.python.org/3.14/library/functions.html#int) builtin functions take care of this:

```python
>>> str(ipaddress.IPv4Address('192.168.0.1'))
'192.168.0.1'
>>> int(ipaddress.IPv4Address('192.168.0.1'))
3232235521
>>> str(ipaddress.IPv6Address('::1'))
'::1'
>>> int(ipaddress.IPv6Address('::1'))
1

```

Keep in mind that scoped IPv6 addresses turn into integers without their scope zone ID.

[Subject index](INDEX.md) · [Previous](ipv6address-format.md) · [Continue](operators.md)
