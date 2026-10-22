# Convenience factory functions

### Convenience factory functions

To make building IP addresses, networks, and interfaces painless, the `ipaddress` module ships these factory functions:

 ipaddress.ip_address(*address*)

Yields an `IPv4Address` or `IPv6Address` object according to whichever IP address was handed in as the argument. You can pass either an IPv4 or an IPv6 address; by default, any integer below `2**32` is treated as IPv4. When *address* fails to describe a legitimate IPv4 or IPv6 address, a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) results.

```python
>>> ipaddress.ip_address('192.168.0.1')
IPv4Address('192.168.0.1')
>>> ipaddress.ip_address('2001:db8::')
IPv6Address('2001:db8::')

```

 ipaddress.ip_network(*address*, *strict=True*)

Yields an `IPv4Network` or `IPv6Network` object according to whichever IP address was handed in as the argument. Here *address* is a string or integer that stands for the IP network. You may supply either IPv4 or IPv6 networks; by default, any integer below `2**32` is treated as IPv4. The *strict* argument is forwarded to the `IPv4Network` or `IPv6Network` constructor. When *address* fails to describe a legitimate IPv4 or IPv6 address, or when the network carries host bits, a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) results.

```python
>>> ipaddress.ip_network('192.168.0.0/28')
IPv4Network('192.168.0.0/28')

```

 ipaddress.ip_interface(*address*)

Yields an `IPv4Interface` or `IPv6Interface` object according to whichever IP address was handed in as the argument. Here *address* is a string or integer that stands for the IP address. You may supply either an IPv4 or an IPv6 address; by default, any integer below `2**32` is treated as IPv4. When *address* fails to describe a legitimate IPv4 or IPv6 address, a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) results.

A drawback of these convenience helpers is that, because they must accept both IPv4 and IPv6 formats, their error messages carry little detail about the exact problem — the helpers have no way to know which of the two formats you meant. To get richer error diagnostics, invoke the version-specific class constructors yourself.

[Subject index](INDEX.md) · [Previous](ipaddress-ipv4-ipv6-manipulation-library.md) · [Continue](ipaddress-ipv4address-class.md)
